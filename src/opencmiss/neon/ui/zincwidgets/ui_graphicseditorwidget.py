# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res\designer\graphicseditorwidget.ui'
#
# Created: Fri Jul 29 13:31:58 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_GraphicsEditorWidget(object):
    def setupUi(self, GraphicsEditorWidget):
        GraphicsEditorWidget.setObjectName("GraphicsEditorWidget")
        GraphicsEditorWidget.setEnabled(True)
        GraphicsEditorWidget.resize(298, 964)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GraphicsEditorWidget.sizePolicy().hasHeightForWidth())
        GraphicsEditorWidget.setSizePolicy(sizePolicy)
        GraphicsEditorWidget.setMinimumSize(QtCore.QSize(180, 0))
        self.verticalLayout = QtGui.QVBoxLayout(GraphicsEditorWidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(2, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.general_groupbox = QtGui.QGroupBox(GraphicsEditorWidget)
        self.general_groupbox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.general_groupbox.setTitle("")
        self.general_groupbox.setCheckable(False)
        self.general_groupbox.setObjectName("general_groupbox")
        self.formLayout_3 = QtGui.QFormLayout(self.general_groupbox)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setContentsMargins(7, 7, 7, 7)
        self.formLayout_3.setObjectName("formLayout_3")
        self.coordinate_field_label = QtGui.QLabel(self.general_groupbox)
        self.coordinate_field_label.setObjectName("coordinate_field_label")
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.coordinate_field_label)
        self.coordinate_field_chooser = FieldChooserWidget(self.general_groupbox)
        self.coordinate_field_chooser.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.coordinate_field_chooser.setObjectName("coordinate_field_chooser")
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.coordinate_field_chooser)
        self.scenecoordinatesystem_label = QtGui.QLabel(self.general_groupbox)
        self.scenecoordinatesystem_label.setObjectName("scenecoordinatesystem_label")
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.LabelRole, self.scenecoordinatesystem_label)
        self.scenecoordinatesystem_combobox = QtGui.QComboBox(self.general_groupbox)
        self.scenecoordinatesystem_combobox.setObjectName("scenecoordinatesystem_combobox")
        self.scenecoordinatesystem_combobox.addItem("")
        self.scenecoordinatesystem_combobox.addItem("")
        self.scenecoordinatesystem_combobox.addItem("")
        self.scenecoordinatesystem_combobox.addItem("")
        self.scenecoordinatesystem_combobox.addItem("")
        self.scenecoordinatesystem_combobox.addItem("")
        self.scenecoordinatesystem_combobox.addItem("")
        self.scenecoordinatesystem_combobox.addItem("")
        self.scenecoordinatesystem_combobox.addItem("")
        self.scenecoordinatesystem_combobox.addItem("")
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.scenecoordinatesystem_combobox)
        self.exterior_checkbox = QtGui.QCheckBox(self.general_groupbox)
        self.exterior_checkbox.setObjectName("exterior_checkbox")
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.LabelRole, self.exterior_checkbox)
        self.face_label = QtGui.QLabel(self.general_groupbox)
        self.face_label.setObjectName("face_label")
        self.formLayout_3.setWidget(6, QtGui.QFormLayout.LabelRole, self.face_label)
        self.face_combobox = QtGui.QComboBox(self.general_groupbox)
        self.face_combobox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.face_combobox.setObjectName("face_combobox")
        self.face_combobox.addItem("")
        self.face_combobox.addItem("")
        self.face_combobox.addItem("")
        self.face_combobox.addItem("")
        self.face_combobox.addItem("")
        self.face_combobox.addItem("")
        self.face_combobox.addItem("")
        self.face_combobox.addItem("")
        self.face_combobox.addItem("")
        self.formLayout_3.setWidget(6, QtGui.QFormLayout.FieldRole, self.face_combobox)
        self.material_label = QtGui.QLabel(self.general_groupbox)
        self.material_label.setObjectName("material_label")
        self.formLayout_3.setWidget(8, QtGui.QFormLayout.LabelRole, self.material_label)
        self.material_chooser = MaterialChooserWidget(self.general_groupbox)
        self.material_chooser.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.material_chooser.setObjectName("material_chooser")
        self.formLayout_3.setWidget(8, QtGui.QFormLayout.FieldRole, self.material_chooser)
        self.data_field_label = QtGui.QLabel(self.general_groupbox)
        self.data_field_label.setObjectName("data_field_label")
        self.formLayout_3.setWidget(11, QtGui.QFormLayout.LabelRole, self.data_field_label)
        self.data_field_chooser = FieldChooserWidget(self.general_groupbox)
        self.data_field_chooser.setEditable(False)
        self.data_field_chooser.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.data_field_chooser.setObjectName("data_field_chooser")
        self.formLayout_3.setWidget(11, QtGui.QFormLayout.FieldRole, self.data_field_chooser)
        self.spectrum_label = QtGui.QLabel(self.general_groupbox)
        self.spectrum_label.setObjectName("spectrum_label")
        self.formLayout_3.setWidget(12, QtGui.QFormLayout.LabelRole, self.spectrum_label)
        self.spectrum_chooser = SpectrumChooserWidget(self.general_groupbox)
        self.spectrum_chooser.setObjectName("spectrum_chooser")
        self.formLayout_3.setWidget(12, QtGui.QFormLayout.FieldRole, self.spectrum_chooser)
        self.wireframe_checkbox = QtGui.QCheckBox(self.general_groupbox)
        self.wireframe_checkbox.setObjectName("wireframe_checkbox")
        self.formLayout_3.setWidget(7, QtGui.QFormLayout.LabelRole, self.wireframe_checkbox)
        self.tessellation_chooser = TessellationChooserWidget(self.general_groupbox)
        self.tessellation_chooser.setObjectName("tessellation_chooser")
        self.formLayout_3.setWidget(13, QtGui.QFormLayout.FieldRole, self.tessellation_chooser)
        self.tessellation_label = QtGui.QLabel(self.general_groupbox)
        self.tessellation_label.setObjectName("tessellation_label")
        self.formLayout_3.setWidget(13, QtGui.QFormLayout.LabelRole, self.tessellation_label)
        self.subgroup_field_label = QtGui.QLabel(self.general_groupbox)
        self.subgroup_field_label.setObjectName("subgroup_field_label")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.subgroup_field_label)
        self.subgroup_field_chooser = FieldChooserWidget(self.general_groupbox)
        self.subgroup_field_chooser.setObjectName("subgroup_field_chooser")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.subgroup_field_chooser)
        self.verticalLayout.addWidget(self.general_groupbox)
        self.contours_groupbox = QtGui.QGroupBox(GraphicsEditorWidget)
        self.contours_groupbox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.contours_groupbox.setFlat(False)
        self.contours_groupbox.setObjectName("contours_groupbox")
        self.formLayout_2 = QtGui.QFormLayout(self.contours_groupbox)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setContentsMargins(7, 7, 7, 7)
        self.formLayout_2.setSpacing(7)
        self.formLayout_2.setObjectName("formLayout_2")
        self.isovalues_lineedit = QtGui.QLineEdit(self.contours_groupbox)
        self.isovalues_lineedit.setObjectName("isovalues_lineedit")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.isovalues_lineedit)
        self.isoscalar_field_label = QtGui.QLabel(self.contours_groupbox)
        self.isoscalar_field_label.setObjectName("isoscalar_field_label")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.isoscalar_field_label)
        self.isoscalar_field_chooser = FieldChooserWidget(self.contours_groupbox)
        self.isoscalar_field_chooser.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.isoscalar_field_chooser.setObjectName("isoscalar_field_chooser")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.isoscalar_field_chooser)
        self.isovalues_label = QtGui.QLabel(self.contours_groupbox)
        self.isovalues_label.setObjectName("isovalues_label")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.isovalues_label)
        self.verticalLayout.addWidget(self.contours_groupbox)
        self.streamlines_groupbox = QtGui.QGroupBox(GraphicsEditorWidget)
        self.streamlines_groupbox.setObjectName("streamlines_groupbox")
        self.formLayout_5 = QtGui.QFormLayout(self.streamlines_groupbox)
        self.formLayout_5.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_5.setContentsMargins(7, 7, 7, 7)
        self.formLayout_5.setObjectName("formLayout_5")
        self.stream_vector_field_label = QtGui.QLabel(self.streamlines_groupbox)
        self.stream_vector_field_label.setObjectName("stream_vector_field_label")
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.stream_vector_field_label)
        self.stream_vector_field_chooser = FieldChooserWidget(self.streamlines_groupbox)
        self.stream_vector_field_chooser.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.stream_vector_field_chooser.setObjectName("stream_vector_field_chooser")
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.FieldRole, self.stream_vector_field_chooser)
        self.streamlines_track_length_label = QtGui.QLabel(self.streamlines_groupbox)
        self.streamlines_track_length_label.setObjectName("streamlines_track_length_label")
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.LabelRole, self.streamlines_track_length_label)
        self.streamlines_track_length_lineedit = QtGui.QLineEdit(self.streamlines_groupbox)
        self.streamlines_track_length_lineedit.setObjectName("streamlines_track_length_lineedit")
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.FieldRole, self.streamlines_track_length_lineedit)
        self.streamline_track_direction_label = QtGui.QLabel(self.streamlines_groupbox)
        self.streamline_track_direction_label.setObjectName("streamline_track_direction_label")
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.LabelRole, self.streamline_track_direction_label)
        self.streamlines_track_direction_combobox = QtGui.QComboBox(self.streamlines_groupbox)
        self.streamlines_track_direction_combobox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.streamlines_track_direction_combobox.setObjectName("streamlines_track_direction_combobox")
        self.streamlines_track_direction_combobox.addItem("")
        self.streamlines_track_direction_combobox.addItem("")
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.FieldRole, self.streamlines_track_direction_combobox)
        self.streamlines_colour_data_type_label = QtGui.QLabel(self.streamlines_groupbox)
        self.streamlines_colour_data_type_label.setObjectName("streamlines_colour_data_type_label")
        self.formLayout_5.setWidget(3, QtGui.QFormLayout.LabelRole, self.streamlines_colour_data_type_label)
        self.streamlines_colour_data_type_combobox = QtGui.QComboBox(self.streamlines_groupbox)
        self.streamlines_colour_data_type_combobox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.streamlines_colour_data_type_combobox.setObjectName("streamlines_colour_data_type_combobox")
        self.streamlines_colour_data_type_combobox.addItem("")
        self.streamlines_colour_data_type_combobox.addItem("")
        self.streamlines_colour_data_type_combobox.addItem("")
        self.formLayout_5.setWidget(3, QtGui.QFormLayout.FieldRole, self.streamlines_colour_data_type_combobox)
        self.verticalLayout.addWidget(self.streamlines_groupbox)
        self.lines_groupbox = QtGui.QGroupBox(GraphicsEditorWidget)
        self.lines_groupbox.setObjectName("lines_groupbox")
        self.formLayout_4 = QtGui.QFormLayout(self.lines_groupbox)
        self.formLayout_4.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setContentsMargins(7, 7, 7, 7)
        self.formLayout_4.setObjectName("formLayout_4")
        self.line_shape_label = QtGui.QLabel(self.lines_groupbox)
        self.line_shape_label.setObjectName("line_shape_label")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.line_shape_label)
        self.line_shape_combobox = QtGui.QComboBox(self.lines_groupbox)
        self.line_shape_combobox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.line_shape_combobox.setObjectName("line_shape_combobox")
        self.line_shape_combobox.addItem("")
        self.line_shape_combobox.addItem("")
        self.line_shape_combobox.addItem("")
        self.line_shape_combobox.addItem("")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.line_shape_combobox)
        self.line_base_size_label = QtGui.QLabel(self.lines_groupbox)
        self.line_base_size_label.setObjectName("line_base_size_label")
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.line_base_size_label)
        self.line_base_size_lineedit = QtGui.QLineEdit(self.lines_groupbox)
        self.line_base_size_lineedit.setObjectName("line_base_size_lineedit")
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.line_base_size_lineedit)
        self.line_orientation_scale_field_label = QtGui.QLabel(self.lines_groupbox)
        self.line_orientation_scale_field_label.setObjectName("line_orientation_scale_field_label")
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.line_orientation_scale_field_label)
        self.line_orientation_scale_field_chooser = FieldChooserWidget(self.lines_groupbox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_orientation_scale_field_chooser.sizePolicy().hasHeightForWidth())
        self.line_orientation_scale_field_chooser.setSizePolicy(sizePolicy)
        self.line_orientation_scale_field_chooser.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.line_orientation_scale_field_chooser.setObjectName("line_orientation_scale_field_chooser")
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.FieldRole, self.line_orientation_scale_field_chooser)
        self.line_scale_factors_label = QtGui.QLabel(self.lines_groupbox)
        self.line_scale_factors_label.setObjectName("line_scale_factors_label")
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.LabelRole, self.line_scale_factors_label)
        self.line_scale_factors_lineedit = QtGui.QLineEdit(self.lines_groupbox)
        self.line_scale_factors_lineedit.setObjectName("line_scale_factors_lineedit")
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.FieldRole, self.line_scale_factors_lineedit)
        self.verticalLayout.addWidget(self.lines_groupbox)
        self.points_groupbox = QtGui.QGroupBox(GraphicsEditorWidget)
        self.points_groupbox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.points_groupbox.setObjectName("points_groupbox")
        self.formLayout = QtGui.QFormLayout(self.points_groupbox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(7, 7, 7, 7)
        self.formLayout.setObjectName("formLayout")
        self.glyph_label = QtGui.QLabel(self.points_groupbox)
        self.glyph_label.setObjectName("glyph_label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.glyph_label)
        self.glyph_chooser = GlyphChooserWidget(self.points_groupbox)
        self.glyph_chooser.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.glyph_chooser.setObjectName("glyph_chooser")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.glyph_chooser)
        self.point_base_size_label = QtGui.QLabel(self.points_groupbox)
        self.point_base_size_label.setObjectName("point_base_size_label")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.point_base_size_label)
        self.point_base_size_lineedit = QtGui.QLineEdit(self.points_groupbox)
        self.point_base_size_lineedit.setObjectName("point_base_size_lineedit")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.point_base_size_lineedit)
        self.point_orientation_scale_field_label = QtGui.QLabel(self.points_groupbox)
        self.point_orientation_scale_field_label.setObjectName("point_orientation_scale_field_label")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.point_orientation_scale_field_label)
        self.point_orientation_scale_field_chooser = FieldChooserWidget(self.points_groupbox)
        self.point_orientation_scale_field_chooser.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.point_orientation_scale_field_chooser.setObjectName("point_orientation_scale_field_chooser")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.point_orientation_scale_field_chooser)
        self.point_scale_factors_label = QtGui.QLabel(self.points_groupbox)
        self.point_scale_factors_label.setObjectName("point_scale_factors_label")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.point_scale_factors_label)
        self.label_field_label = QtGui.QLabel(self.points_groupbox)
        self.label_field_label.setObjectName("label_field_label")
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_field_label)
        self.label_field_chooser = FieldChooserWidget(self.points_groupbox)
        self.label_field_chooser.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.label_field_chooser.setObjectName("label_field_chooser")
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.label_field_chooser)
        self.point_scale_factors_lineedit = QtGui.QLineEdit(self.points_groupbox)
        self.point_scale_factors_lineedit.setObjectName("point_scale_factors_lineedit")
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.point_scale_factors_lineedit)
        self.verticalLayout.addWidget(self.points_groupbox)
        self.sampling_groupbox = QtGui.QGroupBox(GraphicsEditorWidget)
        self.sampling_groupbox.setObjectName("sampling_groupbox")
        self.formLayout_6 = QtGui.QFormLayout(self.sampling_groupbox)
        self.formLayout_6.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_6.setObjectName("formLayout_6")
        self.sampling_mode_label = QtGui.QLabel(self.sampling_groupbox)
        self.sampling_mode_label.setObjectName("sampling_mode_label")
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.LabelRole, self.sampling_mode_label)
        self.sampling_mode_combobox = QtGui.QComboBox(self.sampling_groupbox)
        self.sampling_mode_combobox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.sampling_mode_combobox.setObjectName("sampling_mode_combobox")
        self.sampling_mode_combobox.addItem("")
        self.sampling_mode_combobox.addItem("")
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.FieldRole, self.sampling_mode_combobox)
        self.verticalLayout.addWidget(self.sampling_groupbox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(GraphicsEditorWidget)
        QtCore.QObject.connect(self.data_field_chooser, QtCore.SIGNAL("currentIndexChanged(int)"), GraphicsEditorWidget.dataFieldChanged)
        QtCore.QObject.connect(self.material_chooser, QtCore.SIGNAL("currentIndexChanged(int)"), GraphicsEditorWidget.materialChanged)
        QtCore.QObject.connect(self.glyph_chooser, QtCore.SIGNAL("currentIndexChanged(int)"), GraphicsEditorWidget.glyphChanged)
        QtCore.QObject.connect(self.point_base_size_lineedit, QtCore.SIGNAL("editingFinished()"), GraphicsEditorWidget.pointBaseSizeEntered)
        QtCore.QObject.connect(self.point_scale_factors_lineedit, QtCore.SIGNAL("editingFinished()"), GraphicsEditorWidget.pointScaleFactorsEntered)
        QtCore.QObject.connect(self.point_orientation_scale_field_chooser, QtCore.SIGNAL("currentIndexChanged(int)"), GraphicsEditorWidget.pointOrientationScaleFieldChanged)
        QtCore.QObject.connect(self.label_field_chooser, QtCore.SIGNAL("currentIndexChanged(int)"), GraphicsEditorWidget.labelFieldChanged)
        QtCore.QObject.connect(self.exterior_checkbox, QtCore.SIGNAL("clicked(bool)"), GraphicsEditorWidget.exteriorClicked)
        QtCore.QObject.connect(self.isoscalar_field_chooser, QtCore.SIGNAL("currentIndexChanged(int)"), GraphicsEditorWidget.isoscalarFieldChanged)
        QtCore.QObject.connect(self.face_combobox, QtCore.SIGNAL("currentIndexChanged(int)"), GraphicsEditorWidget.faceChanged)
        QtCore.QObject.connect(self.wireframe_checkbox, QtCore.SIGNAL("clicked(bool)"), GraphicsEditorWidget.wireframeClicked)
        QtCore.QObject.connect(self.isovalues_lineedit, QtCore.SIGNAL("editingFinished()"), GraphicsEditorWidget.isovaluesEntered)
        QtCore.QObject.connect(self.line_base_size_lineedit, QtCore.SIGNAL("editingFinished()"), GraphicsEditorWidget.lineBaseSizeEntered)
        QtCore.QObject.connect(self.line_orientation_scale_field_chooser, QtCore.SIGNAL("currentIndexChanged(int)"), GraphicsEditorWidget.lineOrientationScaleFieldChanged)
        QtCore.QObject.connect(self.line_scale_factors_lineedit, QtCore.SIGNAL("editingFinished()"), GraphicsEditorWidget.lineScaleFactorsEntered)
        QtCore.QObject.connect(self.line_shape_combobox, QtCore.SIGNAL("currentIndexChanged(int)"), GraphicsEditorWidget.lineShapeChanged)
        QtCore.QObject.connect(self.stream_vector_field_chooser, QtCore.SIGNAL("currentIndexChanged(int)"), GraphicsEditorWidget.streamVectorFieldChanged)
        QtCore.QObject.connect(self.streamlines_track_length_lineedit, QtCore.SIGNAL("editingFinished()"), GraphicsEditorWidget.streamlinesTrackLengthEntered)
        QtCore.QObject.connect(self.streamlines_track_direction_combobox, QtCore.SIGNAL("currentIndexChanged(int)"), GraphicsEditorWidget.streamlinesTrackDirectionChanged)
        QtCore.QObject.connect(self.coordinate_field_chooser, QtCore.SIGNAL("currentIndexChanged(int)"), GraphicsEditorWidget.coordinateFieldChanged)
        QtCore.QObject.connect(self.sampling_mode_combobox, QtCore.SIGNAL("currentIndexChanged(int)"), GraphicsEditorWidget.samplingModeChanged)
        QtCore.QObject.connect(self.streamlines_colour_data_type_combobox, QtCore.SIGNAL("currentIndexChanged(int)"), GraphicsEditorWidget.streamlinesColourDataTypeChanged)
        QtCore.QObject.connect(self.spectrum_chooser, QtCore.SIGNAL("currentIndexChanged(int)"), GraphicsEditorWidget.spectrumChanged)
        QtCore.QObject.connect(self.scenecoordinatesystem_combobox, QtCore.SIGNAL("currentIndexChanged(int)"), GraphicsEditorWidget.scenecoordinatesystemChanged)
        QtCore.QObject.connect(self.tessellation_chooser, QtCore.SIGNAL("currentIndexChanged(int)"), GraphicsEditorWidget.tessellationChanged)
        QtCore.QObject.connect(self.subgroup_field_chooser, QtCore.SIGNAL("currentIndexChanged(int)"), GraphicsEditorWidget.subgroupFieldChanged)
        QtCore.QMetaObject.connectSlotsByName(GraphicsEditorWidget)

    def retranslateUi(self, GraphicsEditorWidget):
        GraphicsEditorWidget.setWindowTitle(QtGui.QApplication.translate("GraphicsEditorWidget", "Graphics Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.coordinate_field_label.setText(QtGui.QApplication.translate("GraphicsEditorWidget", "Coordinates:", None, QtGui.QApplication.UnicodeUTF8))
        self.scenecoordinatesystem_label.setText(QtGui.QApplication.translate("GraphicsEditorWidget", "Coord System:", None, QtGui.QApplication.UnicodeUTF8))
        self.scenecoordinatesystem_combobox.setItemText(0, QtGui.QApplication.translate("GraphicsEditorWidget", "LOCAL", None, QtGui.QApplication.UnicodeUTF8))
        self.scenecoordinatesystem_combobox.setItemText(1, QtGui.QApplication.translate("GraphicsEditorWidget", "WORLD", None, QtGui.QApplication.UnicodeUTF8))
        self.scenecoordinatesystem_combobox.setItemText(2, QtGui.QApplication.translate("GraphicsEditorWidget", "NORMALISED_WINDOW_FILL", None, QtGui.QApplication.UnicodeUTF8))
        self.scenecoordinatesystem_combobox.setItemText(3, QtGui.QApplication.translate("GraphicsEditorWidget", "NORMALISED_WINDOW_FIT_CENTRE", None, QtGui.QApplication.UnicodeUTF8))
        self.scenecoordinatesystem_combobox.setItemText(4, QtGui.QApplication.translate("GraphicsEditorWidget", "NORMALISED_WINDOW_FIT_LEFT", None, QtGui.QApplication.UnicodeUTF8))
        self.scenecoordinatesystem_combobox.setItemText(5, QtGui.QApplication.translate("GraphicsEditorWidget", "NORMALISED_WINDOW_FIT_RIGHT", None, QtGui.QApplication.UnicodeUTF8))
        self.scenecoordinatesystem_combobox.setItemText(6, QtGui.QApplication.translate("GraphicsEditorWidget", "NORMALISED_WINDOW_FIT_BOTTOM", None, QtGui.QApplication.UnicodeUTF8))
        self.scenecoordinatesystem_combobox.setItemText(7, QtGui.QApplication.translate("GraphicsEditorWidget", "NORMALISED_WINDOW_FIT_TOP", None, QtGui.QApplication.UnicodeUTF8))
        self.scenecoordinatesystem_combobox.setItemText(8, QtGui.QApplication.translate("GraphicsEditorWidget", "WINDOW_PIXEL_BOTTOM_LEFT", None, QtGui.QApplication.UnicodeUTF8))
        self.scenecoordinatesystem_combobox.setItemText(9, QtGui.QApplication.translate("GraphicsEditorWidget", "WINDOW_PIXEL_TOP_LEFT", None, QtGui.QApplication.UnicodeUTF8))
        self.exterior_checkbox.setText(QtGui.QApplication.translate("GraphicsEditorWidget", "Exterior", None, QtGui.QApplication.UnicodeUTF8))
        self.face_label.setText(QtGui.QApplication.translate("GraphicsEditorWidget", "Face:", None, QtGui.QApplication.UnicodeUTF8))
        self.face_combobox.setItemText(0, QtGui.QApplication.translate("GraphicsEditorWidget", "all", None, QtGui.QApplication.UnicodeUTF8))
        self.face_combobox.setItemText(1, QtGui.QApplication.translate("GraphicsEditorWidget", "any face", None, QtGui.QApplication.UnicodeUTF8))
        self.face_combobox.setItemText(2, QtGui.QApplication.translate("GraphicsEditorWidget", "no face", None, QtGui.QApplication.UnicodeUTF8))
        self.face_combobox.setItemText(3, QtGui.QApplication.translate("GraphicsEditorWidget", "xi1 = 0", None, QtGui.QApplication.UnicodeUTF8))
        self.face_combobox.setItemText(4, QtGui.QApplication.translate("GraphicsEditorWidget", "xi1 = 1", None, QtGui.QApplication.UnicodeUTF8))
        self.face_combobox.setItemText(5, QtGui.QApplication.translate("GraphicsEditorWidget", "xi2 = 0", None, QtGui.QApplication.UnicodeUTF8))
        self.face_combobox.setItemText(6, QtGui.QApplication.translate("GraphicsEditorWidget", "xi2 = 1", None, QtGui.QApplication.UnicodeUTF8))
        self.face_combobox.setItemText(7, QtGui.QApplication.translate("GraphicsEditorWidget", "xi3 = 0", None, QtGui.QApplication.UnicodeUTF8))
        self.face_combobox.setItemText(8, QtGui.QApplication.translate("GraphicsEditorWidget", "xi3 = 1", None, QtGui.QApplication.UnicodeUTF8))
        self.material_label.setText(QtGui.QApplication.translate("GraphicsEditorWidget", "Material:", None, QtGui.QApplication.UnicodeUTF8))
        self.data_field_label.setText(QtGui.QApplication.translate("GraphicsEditorWidget", "Data field:", None, QtGui.QApplication.UnicodeUTF8))
        self.spectrum_label.setText(QtGui.QApplication.translate("GraphicsEditorWidget", "Spectrum:", None, QtGui.QApplication.UnicodeUTF8))
        self.wireframe_checkbox.setText(QtGui.QApplication.translate("GraphicsEditorWidget", "Wireframe", None, QtGui.QApplication.UnicodeUTF8))
        self.tessellation_label.setText(QtGui.QApplication.translate("GraphicsEditorWidget", "Tessellation:", None, QtGui.QApplication.UnicodeUTF8))
        self.subgroup_field_label.setText(QtGui.QApplication.translate("GraphicsEditorWidget", "Subgroup:", None, QtGui.QApplication.UnicodeUTF8))
        self.contours_groupbox.setTitle(QtGui.QApplication.translate("GraphicsEditorWidget", "Contours:", None, QtGui.QApplication.UnicodeUTF8))
        self.isoscalar_field_label.setText(QtGui.QApplication.translate("GraphicsEditorWidget", "Scalar field:", None, QtGui.QApplication.UnicodeUTF8))
        self.isovalues_label.setText(QtGui.QApplication.translate("GraphicsEditorWidget", "Isovalues:", None, QtGui.QApplication.UnicodeUTF8))
        self.streamlines_groupbox.setTitle(QtGui.QApplication.translate("GraphicsEditorWidget", "Streamlines:", None, QtGui.QApplication.UnicodeUTF8))
        self.stream_vector_field_label.setText(QtGui.QApplication.translate("GraphicsEditorWidget", "Vector field:", None, QtGui.QApplication.UnicodeUTF8))
        self.streamlines_track_length_label.setText(QtGui.QApplication.translate("GraphicsEditorWidget", "Time length:", None, QtGui.QApplication.UnicodeUTF8))
        self.streamline_track_direction_label.setText(QtGui.QApplication.translate("GraphicsEditorWidget", "Direction:", None, QtGui.QApplication.UnicodeUTF8))
        self.streamlines_track_direction_combobox.setItemText(0, QtGui.QApplication.translate("GraphicsEditorWidget", "forward", None, QtGui.QApplication.UnicodeUTF8))
        self.streamlines_track_direction_combobox.setItemText(1, QtGui.QApplication.translate("GraphicsEditorWidget", "reverse", None, QtGui.QApplication.UnicodeUTF8))
        self.streamlines_colour_data_type_label.setText(QtGui.QApplication.translate("GraphicsEditorWidget", "Colour data:", None, QtGui.QApplication.UnicodeUTF8))
        self.streamlines_colour_data_type_combobox.setItemText(0, QtGui.QApplication.translate("GraphicsEditorWidget", "field", None, QtGui.QApplication.UnicodeUTF8))
        self.streamlines_colour_data_type_combobox.setItemText(1, QtGui.QApplication.translate("GraphicsEditorWidget", "magnitude", None, QtGui.QApplication.UnicodeUTF8))
        self.streamlines_colour_data_type_combobox.setItemText(2, QtGui.QApplication.translate("GraphicsEditorWidget", "travel time", None, QtGui.QApplication.UnicodeUTF8))
        self.lines_groupbox.setTitle(QtGui.QApplication.translate("GraphicsEditorWidget", "Lines:", None, QtGui.QApplication.UnicodeUTF8))
        self.line_shape_label.setText(QtGui.QApplication.translate("GraphicsEditorWidget", "Shape:", None, QtGui.QApplication.UnicodeUTF8))
        self.line_shape_combobox.setItemText(0, QtGui.QApplication.translate("GraphicsEditorWidget", "line", None, QtGui.QApplication.UnicodeUTF8))
        self.line_shape_combobox.setItemText(1, QtGui.QApplication.translate("GraphicsEditorWidget", "ribbon", None, QtGui.QApplication.UnicodeUTF8))
        self.line_shape_combobox.setItemText(2, QtGui.QApplication.translate("GraphicsEditorWidget", "circle extrusion", None, QtGui.QApplication.UnicodeUTF8))
        self.line_shape_combobox.setItemText(3, QtGui.QApplication.translate("GraphicsEditorWidget", "square extrusion", None, QtGui.QApplication.UnicodeUTF8))
        self.line_base_size_label.setText(QtGui.QApplication.translate("GraphicsEditorWidget", "Base size:", None, QtGui.QApplication.UnicodeUTF8))
        self.line_orientation_scale_field_label.setText(QtGui.QApplication.translate("GraphicsEditorWidget", "Scale field:", None, QtGui.QApplication.UnicodeUTF8))
        self.line_scale_factors_label.setText(QtGui.QApplication.translate("GraphicsEditorWidget", "Scaling:", None, QtGui.QApplication.UnicodeUTF8))
        self.points_groupbox.setTitle(QtGui.QApplication.translate("GraphicsEditorWidget", "Points:", None, QtGui.QApplication.UnicodeUTF8))
        self.glyph_label.setText(QtGui.QApplication.translate("GraphicsEditorWidget", "Glyph:", None, QtGui.QApplication.UnicodeUTF8))
        self.point_base_size_label.setText(QtGui.QApplication.translate("GraphicsEditorWidget", "Base size:", None, QtGui.QApplication.UnicodeUTF8))
        self.point_orientation_scale_field_label.setText(QtGui.QApplication.translate("GraphicsEditorWidget", "Scale field:", None, QtGui.QApplication.UnicodeUTF8))
        self.point_scale_factors_label.setText(QtGui.QApplication.translate("GraphicsEditorWidget", "Scaling:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_field_label.setText(QtGui.QApplication.translate("GraphicsEditorWidget", "Label field:", None, QtGui.QApplication.UnicodeUTF8))
        self.sampling_groupbox.setTitle(QtGui.QApplication.translate("GraphicsEditorWidget", "Sampling:", None, QtGui.QApplication.UnicodeUTF8))
        self.sampling_mode_label.setText(QtGui.QApplication.translate("GraphicsEditorWidget", "Mode:", None, QtGui.QApplication.UnicodeUTF8))
        self.sampling_mode_combobox.setItemText(0, QtGui.QApplication.translate("GraphicsEditorWidget", "cell centres", None, QtGui.QApplication.UnicodeUTF8))
        self.sampling_mode_combobox.setItemText(1, QtGui.QApplication.translate("GraphicsEditorWidget", "cell corners", None, QtGui.QApplication.UnicodeUTF8))

from opencmiss.neon.ui.zincwidgets.fieldchooserwidget import FieldChooserWidget
from opencmiss.neon.ui.zincwidgets.glyphchooserwidget import GlyphChooserWidget
from opencmiss.neon.ui.zincwidgets.spectrumchooserwidget import SpectrumChooserWidget
from opencmiss.neon.ui.zincwidgets.materialchooserwidget import MaterialChooserWidget
from opencmiss.neon.ui.zincwidgets.tessellationchooserwidget import TessellationChooserWidget
