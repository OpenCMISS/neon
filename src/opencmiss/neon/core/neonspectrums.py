'''
   Copyright 2016 University of Auckland

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
import json

from opencmiss.zinc.spectrum import Spectrum
from opencmiss.zinc.status import OK as ZINC_OK

SPECTRUM_GLYPH_NAME_FORMAT = 'colour_bar_{0}'

class NeonSpectrums(object):
    """
    Manages and serialises Zinc Spectrums within Neon.
    Generates colour bar glyphs for spectrums, which is automatically done if if not found on loading.
    """

    def __init__(self, zincContext):
        self._zincContext = zincContext
        self._spectrummodule = zincContext.getSpectrummodule()
        self._findOrCreateAllSpectrumGlyphColourBars()

    def getZincContext(self):
        return self._zincContext

    def deserialize(self, dictInput):
        spectrumsDescription = json.dumps(dictInput)
        result = self._spectrummodule.readDescription(spectrumsDescription)
        if result != ZINC_OK:
            print("Failed to read spectrums")
        self._findOrCreateAllSpectrumGlyphColourBars()

    def serialize(self):
        spectrumsDescription = self._spectrummodule.writeDescription()
        dictOutput = json.loads(spectrumsDescription)
        return dictOutput

    def _findOrCreateAllSpectrumGlyphColourBars(self):
        """
        Ensures there exists a colour bar for each spectrum.
        """
        iter = self._spectrummodule.createSpectrumiterator()
        spectrum = iter.next()
        while spectrum.isValid():
            self.findOrCreateSpectrumGlyphColourBar(spectrum)
            spectrum = iter.next()

    def findOrCreateSpectrumGlyphColourBar(self, spectrum):
        """
        Find or create a GlyphColourBar for spectrum in the glyph module.
        Newly created colour bar is set up for display in the normalised window coordinates at left.
        """
        glyphmodule = self._zincContext.getGlyphmodule()
        glyphName = SPECTRUM_GLYPH_NAME_FORMAT.format(spectrum.getName())

        # try to find by name first
        glyph = glyphmodule.findGlyphByName(glyphName)
        colourBar = glyph.castColourBar()
        if colourBar.isValid() and (colourBar.getSpectrum() == spectrum):
            return colourBar

        # attempt to find by matching spectrum but do not rename it
        glyphiterator = glyphmodule.createGlyphiterator()
        glyph = glyphiterator.next()
        while glyph.isValid():
            colourBar = glyph.castColourBar()
            if colourBar.isValid() and (colourBar.getSpectrum() == spectrum):
                return colourBar
            glyph = glyphiterator.next()

        # create a new colour bar, matching Cmgui's defaults:
        glyphmodule.beginChange()
        colourBar = glyphmodule.createGlyphColourBar(spectrum)
        tmpName = glyphName
        i = 1
        while (colourBar.setName(tmpName) != ZINC_OK):
            tmpName = glyphName + str(i)
            i += 1
        colourBar.setManaged(True)
        colourBar.setCentre([-0.9, 0.0, 0.5])
        colourBar.setAxis([0.0, 1.6, 0.0])  # includes length
        colourBar.setSideAxis([0.06, 0.0, 0.0])  # includes radius
        colourBar.setExtendLength(0.06)
        colourBar.setTickLength(0.04)
        colourBar.setLabelDivisions(10)
        colourBar.setNumberFormat('%+.4e')
        glyphmodule.endChange()
        return colourBar

    def renameSpectrum(self, spectrum, name):
        """
        Renames spectrum and its glyph
        """
        colourBar = self.findOrCreateSpectrumGlyphColourBar(spectrum)
        result = spectrum.setName(str(name))
        if result == ZINC_OK:
            glyphName = SPECTRUM_GLYPH_NAME_FORMAT.format(str(name))
            tmpName = glyphName
            i = 1
            while (colourBar.setName(tmpName) != ZINC_OK):
                tmpName = glyphName + str(i)
                i += 1

    def removeSpectrum(self, spectrum):
        """
        Unmanages spectrum and its colour bar. Note spectrum is only removed if neither are in use.
        """
        spectrum.setManaged(False)
        colourBar = self.findOrCreateSpectrumGlyphColourBar(spectrum)
        colourBar.setManaged(False)