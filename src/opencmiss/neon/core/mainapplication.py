'''
   Copyright 2015 University of Auckland

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''
import os

from PySide import QtCore

from opencmiss.neon.core.neondocument import NeonDocument
from opencmiss.neon.core.preferences import Preferences
from opencmiss.neon.core.misc.utils import getMatchingVisualisationClass, \
    importProblem
from opencmiss.neon.core.neonlogger import NeonLogger
from opencmiss.neon.core.projectmodel import ProjectModel
from opencmiss.neon.core.neonproject import NeonProject
from opencmiss.neon.core.misc.neonerror import NeonError


class MainApplication(QtCore.QObject):

    documentChanged = QtCore.Signal()

    def __init__(self):
        super(MainApplication, self).__init__()
        self._saveUndoRedoIndex = 0
        self._currentUntoRedoIndex = 0

        self._location = None
        self._recents = []

        self._document = None  # NeonDocument()

        self._project_model = ProjectModel()
        self._setupModel()

        self._preferences = Preferences(self._project_model)

    def _setupModel(self):
        from opencmiss.neon.settings.projects import active_project_names

        for name in active_project_names:
            row = self._project_model.rowCount()
            if self._project_model.insertRow(row):
                index = self._project_model.index(row)
                project = NeonProject()
                project.setProblem(importProblem(name))
                self._project_model.setData(index, project)

    def getZincContext(self):
        if self._document:
            return self._document.getZincContext()

        return None

    def isModified(self):
        return self._saveUndoRedoIndex != self._currentUntoRedoIndex

    def setCurrentUndoRedoIndex(self, index):
        self._currentUntoRedoIndex = index

    def setSaveUndoRedoIndex(self, index):
        self._saveUndoRedoIndex = index

    def setLocation(self, location):
        self._location = location

    def getLocation(self):
        return self._location

    def new(self, project=None):
        """
        Create a blank document with the supplied project, or default project if not supplied
        """
        if self._document is not None:
            self._document.freeVisualisationContents()
            self._document.freeProject()

        self._document = NeonDocument()
        if project:
            self._document.setProject(project)
        else:
            defaultProject = self._project_model.getDefaultProject()
            self._document.setProject(defaultProject)

        self._document.initialiseVisualisationContents()
        self.documentChanged.emit()

    def save(self):
        # make model sources relative to current location if possible
        # note that sources on different windows drives have absolute paths
        basePath = os.path.dirname(self._location)
        state = self._document.serialize(basePath)
        with open(self._location, 'w') as f:
            f.write(state)

    def load(self, filename):
        """
        Loads the named Neon file and on success sets filename as the current location.
        Emits documentChange separately if new document loaded, including if existing document cleared due to load failure.
        :return  True on success, otherwise False.
        """
        modelChanged = False
        try:
            with open(filename, 'r') as f:
                state = f.read()
                modelChanged = True
                self._location = None
                if self._document is not None:
                    self._document.freeVisualisationContents()
                    self._document.freeProject()
                self._document = NeonDocument()
                self._document.initialiseProject()
                self._document.initialiseVisualisationContents()
                # set current directory to path from file, to support scripts and fieldml with external resources
                path = os.path.dirname(filename)
                os.chdir(path)
                self._document.deserialize(state)
                self._location = filename
                self.documentChanged.emit()
                return True
        except (NeonError, IOError, ValueError) as e:
            NeonLogger.getLogger().error("Failed to load Neon model " + filename + ": " + str(e))
        except:
            NeonLogger.getLogger().error("Failed to load Neon model " + filename + ": Unknown error")
        if modelChanged:
            self.new()  # in case document half constructed; emits documentChanged
        return False

    def addRecent(self, recent):
        self.removeRecent(recent)
        self._recents.append(recent)

    def removeRecent(self, recent):
        if recent in self._recents:
            index = self._recents.index(recent)
            del self._recents[index]

    def getRecents(self):
        return self._recents

    def clearRecents(self):
        self._recents = []

    def getDocument(self):
        return self._document

    def getProjectModel(self):
        return self._project_model

    def getPreferences(self):
        return self._preferences

    def visualiseSimulation(self, simulation):
        self._document.freeVisualisationContents()
        self._document.initialiseVisualisationContents()
        visualisation = getMatchingVisualisationClass(simulation)
        visualisation.setSimulation(simulation)
        visualisation.visualise(self._document)

        self.documentChanged.emit()
