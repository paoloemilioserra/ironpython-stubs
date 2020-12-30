# encoding: utf-8
# module Autodesk.AutoCAD.Internal calls itself Internal
# from Acmgd, Version=24.0.0.0, Culture=neutral, PublicKeyToken=null, Acdbmgd, Version=24.0.0.0, Culture=neutral, PublicKeyToken=null, accoremgd, Version=24.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AcadTaskDialogs(object):
    """ AcadTaskDialogs() """
    @staticmethod
    def ShowCurrentLayerOff():
        """ ShowCurrentLayerOff() -> int """
        pass

    @staticmethod
    def ShowDuplicateNameCopyReplaceTD(objectname, duplicatename, copyname, pParentWnd):
        """ ShowDuplicateNameCopyReplaceTD(objectname: str, duplicatename: str, copyname: str, pParentWnd: IntPtr) -> int """
        pass

    @staticmethod
    def ShowDuplicateNameErrorTD(objectname, duplicatename, pParentWnd):
        """ ShowDuplicateNameErrorTD(objectname: str, duplicatename: str, pParentWnd: IntPtr) -> int """
        pass

    @staticmethod
    def ShowDuplicateNameReplaceCancelTD(objectname, duplicatename, pParentWnd):
        """ ShowDuplicateNameReplaceCancelTD(objectname: str, duplicatename: str, pParentWnd: IntPtr) -> int """
        pass

    @staticmethod
    def ShowFileConfirmationWithNoToAll(featureName, featureType, fullFileName, fileName, pParentWnd):
        """ ShowFileConfirmationWithNoToAll(featureName: str, featureType: str, fullFileName: str, fileName: str, pParentWnd: IntPtr) -> int """
        pass

    @staticmethod
    def ShowFileConfirmationWithoutNoToAll(featureName, featureType, fullFileName, fileName, pParentWnd):
        """ ShowFileConfirmationWithoutNoToAll(featureName: str, featureType: str, fullFileName: str, fileName: str, pParentWnd: IntPtr) -> int """
        pass

    @staticmethod
    def ShowInvalidNameEmptyNameTD(objectname, fieldname, pParentWnd):
        """ ShowInvalidNameEmptyNameTD(objectname: str, fieldname: str, pParentWnd: IntPtr) """
        pass

    @staticmethod
    def ShowInvalidNameTooLongTD(objectname, fieldname, pParentWnd):
        """ ShowInvalidNameTooLongTD(objectname: str, fieldname: str, pParentWnd: IntPtr) """
        pass

    @staticmethod
    def ShowInvalidNameUnsupportedCharactersTD(objectname, fieldname, pParentWnd):
        """ ShowInvalidNameUnsupportedCharactersTD(objectname: str, fieldname: str, pParentWnd: IntPtr) """
        pass

    @staticmethod
    def ShowLayerCannotFreeze():
        """ ShowLayerCannotFreeze() """
        pass

    @staticmethod
    def Source():
        """ Source() -> Uri """
        pass

    AcadAppNoAcVBA = 'AcadApp.NoAcVBA'
    AcadContainsLargeObjects = 'Acad.ContainsLargeObjects'
    AcadContainsLargeObjects_TurnOffSysvarButon = 1001
    AcadContainsLargeObjects_TurnOnSysvarButon = 1002
    AcadDigitallySignedDWFx = 'Acad.DigitallySignedDWFx'
    AcadExternalReferenceApplyPath = 'Acad.ExternalReferenceApplyPath'
    AcadLowMemoryAlert = 'Acad.LowMemoryAlert'
    AcadRenameSheetLayout = 'Acad.RenameSheetLayout'
    AcadRenameSheetLayout_DiscardNameChangeButon = 1003
    AcadRenameSheetLayout_RenameLayoutAndSheetButon = 1001
    AcadRenameSheetLayout_RenameLayoutOnlyButon = 1002
    AcadRenameSheetSetLocked = 'Acad.RenameSheetSetLocked'
    AcadRenameSheetSetLocked_CancelRenameButon = 1002
    AcadRenameSheetSetLocked_RenameOnlyLayoutButon = 1001
    AcadUnresolvedFontFiles = 'Acad.UnresolvedFontFiles'
    AcadUnresolvedFontFiles_IgnoreUnresolvedFontButon = 1002
    AcadUnresolvedFontFiles_UpdateFontButon = 1001
    AcadUnresolvedReferenceFiles = 'Acad.UnresolvedReferenceFiles'
    AcadUnresolvedReferenceFilesWithPathMap = 'Acad.UnresolvedReferenceFilesWithPathMap'
    AcadUnresolvedReferenceFilesWithPathMap_IgnoreUnresolvedRef2Buton = 1002
    AcadUnresolvedReferenceFilesWithPathMap_UpdateLocation2Buton = 1001
    AcadUnresolvedReferenceFilesWithPathMap_XrefPathMapping2Buton = 1003
    AcadUnresolvedReferenceFiles_IgnoreUnresolvedRefButon = 1002
    AcadUnresolvedReferenceFiles_UpdateLocationButon = 1001
    AcadUpdateXRefRelativePathOnSave = 'Acad.UpdateXRefRelativePathOnSave'
    AcadUpdateXRefRelativePathOnSave_IgnoreXRefPathUpdateButon = 1002
    AcadUpdateXRefRelativePathOnSave_UpdateXRefRelativePathButon = 1001
    AcArrayArrayClose = 'AcArray.ArrayClose'
    AcArrayArrayClose_CancelButon = 1003
    AcArrayArrayClose_NoButon = 1002
    AcArrayArrayClose_YesButon = 1001
    AcArrayCreateNonAssocArrayForCustomObj = 'AcArray.CreateNonAssocArrayForCustomObj'
    AcArrayCustomObjSelected = 'AcArray.CustomObjSelected'
    AcArrayCustomObjSelected_NonAssocButon = 1001
    AcArrayCustomObjSelected_RemoveCustomObjButon = 1002
    AcArrayEditSource = 'AcArray.EditSource'
    AcArrayMaxArrayObject = 'AcArray.MaxArrayObject'
    AcAuthEnvironBTableAuditCellEvalError = 'AcAuthEnviron.BTableAuditCellEvalError'
    AcAuthEnvironBTableAuditCellNotMatchConstant = 'AcAuthEnviron.BTableAuditCellNotMatchConstant'
    AcAuthEnvironBTableAuditDefinitionNotMatch = 'AcAuthEnviron.BTableAuditDefinitionNotMatch'
    AcAuthEnvironBTableAuditDefinitionNotMatch_AddRowButon = 1001
    AcAuthEnvironBTableAuditDunplicateRow = 'AcAuthEnviron.BTableAuditDunplicateRow'
    AcAuthEnvironBTableAuditDunplicateRow_DeleteRowButon = 1001
    AcAuthEnvironBTableAuditEmptyCell = 'AcAuthEnviron.BTableAuditEmptyCell'
    AcAuthEnvironBTableAuditNotInValueSet = 'AcAuthEnviron.BTableAuditNotInValueSet'
    AcAuthEnvironBTableAuditNotInValueSetAndReadOnly = 'AcAuthEnviron.BTableAuditNotInValueSetAndReadOnly'
    AcAuthEnvironBTableAuditNotInValueSet_UpdateValueButon = 1001
    AcAuthEnvironBTableAuditReferenceNotFound = 'AcAuthEnviron.BTableAuditReferenceNotFound'
    AcAuthEnvironBTableErrorClosing = 'AcAuthEnviron.BTableErrorClosing'
    AcAuthEnvironBTableErrorClosing_ReturnToBTableButon = 1002
    AcAuthEnvironBTableErrorClosing_SaveTheBTableButon = 1001
    AcAuthEnvironBTableInvalidCharacter = 'AcAuthEnviron.BTableInvalidCharacter'
    AcAuthEnvironBTableNoErrorsFound = 'AcAuthEnviron.BTableNoErrorsFound'
    AcAuthEnvironBTableOutofValueSet = 'AcAuthEnviron.BTableOutofValueSet'
    AcAuthEnvironBTablePasteError = 'AcAuthEnviron.BTablePasteError'
    AcAuthEnvironBTablePasteError_ContinuePasteButon = 1001
    AcAuthEnvironChangesNotSaved = 'AcAuthEnviron.ChangesNotSaved'
    AcAuthEnvironChangesNotSaved_DiscardChangesButon = 1002
    AcAuthEnvironChangesNotSaved_SaveTheBlockButon = 1001
    AcAuthEnvironLookupParameterNotDefined = 'AcAuthEnviron.LookupParameterNotDefined'
    AcAuthEnvironNoErrorsFound = 'AcAuthEnviron.NoErrorsFound'
    AcAuthEnvironNotShowBlockActionPanel = 'AcAuthEnviron.NotShowBlockActionPanel'
    AcAuthEnvironParameterChangesNotSaved = 'AcAuthEnviron.ParameterChangesNotSaved'
    AcAuthEnvironParameterChangesNotSavedUnderConstrained = 'AcAuthEnviron.ParameterChangesNotSavedUnderConstrained'
    AcAuthEnvironParameterChangesNotSavedUnderConstrainedClosingEditor = 'AcAuthEnviron.ParameterChangesNotSavedUnderConstrainedClosingEditor'
    AcAuthEnvironParameterChangesNotSavedUnderConstrainedClosingEditor_DiscardTheChangesButon = 1002
    AcAuthEnvironParameterChangesNotSavedUnderConstrainedClosingEditor_SaveTheParameterButon = 1001
    AcAuthEnvironParameterChangesNotSavedUnderConstrained_SaveItButon = 1001
    AcAuthEnvironParameterChangesNotSaved_DiscardTheChangesButon = 1002
    AcAuthEnvironParameterChangesNotSaved_SaveTheParameterButon = 1001
    AcAuthEnvironProxyObjectsFound = 'AcAuthEnviron.ProxyObjectsFound'
    AcAuthEnvironRedefineBlock = 'AcAuthEnviron.RedefineBlock'
    AcAuthEnvironRedefineBlock_RedefineBlockAndUpdateButon = 1001
    AcAuthEnvironRedefineBlock_UnRedefineBlockButon = 1002
    AcBattmanSynchronizeBlocks = 'AcBattman.SynchronizeBlocks'
    AcBattManValueChange = 'AcBattMan.ValueChange'
    AcBlockAnnotivePropertyChanged = 'AcBlock.AnnotivePropertyChanged'
    AcBlockAnnotivePropertyChanged_NotSaveChangesButon = 1002
    AcBlockAnnotivePropertyChanged_SaveChangesButon = 1001
    AcBlockBlockNameNotSpecified = 'AcBlock.BlockNameNotSpecified'
    AcBlockCannotInsertAnnotiveBlocks = 'AcBlock.CannotInsertAnnotiveBlocks'
    AcBlockCircularBlockReference = 'AcBlock.CircularBlockReference'
    AcBlockCustomPropMightLost = 'AcBlock.CustomPropMightLost'
    AcBlockCustomPropMightLost_RetainCurrentScaleButon = 1002
    AcBlockCustomPropMightLost_SetUniformScaleButon = 1001
    AcBlockEducationalPlotStampDetected = 'AcBlock.EducationalPlotStampDetected'
    AcBlockEducationalPlotStampDetected_CancelOperation_EMRButon = 1002
    AcBlockEducationalPlotStampDetected_ContinueOperationButon = 1001
    AcBlockFileNotFound = 'AcBlock.FileNotFound'
    AcBlockGeographicData = 'AcBlock.GeographicData'
    AcBlockGeographicData_Button_prompt_for_insertion_pointButon = 1002
    AcBlockGeographicData_Button_using_geographic_dataButon = 1001
    AcBlockInvalidBlockName = 'AcBlock.InvalidBlockName'
    AcBlockInvalidBlockName_Continue2Buton = 1001
    AcBlockInvalidCoordianteVaule = 'AcBlock.InvalidCoordianteVaule'
    AcBlockInvalidCoordianteVaule_Continue1Buton = 1001
    AcBlockLibraryInvalid = 'AcBlock.LibraryInvalid'
    AcBlockLibraryInvalid_KeepRecordButon = 1002
    AcBlockLibraryInvalid_RemoveRecordButon = 1001
    AcBlockMismatchGeoCS = 'AcBlock.MismatchGeoCS'
    AcBlockNoObjectsSelected = 'AcBlock.NoObjectsSelected'
    AcBlockNoObjectsSelected_ContinueDefineButon = 1002
    AcBlockNoObjectsSelected_SelObjectsButon = 1001
    AcBlockNotModified = 'AcBlock.NotModified'
    AcBlockObjectsOnLockedLayer = 'AcBlock.ObjectsOnLockedLayer'
    AcBlockRedefineBlock = 'AcBlock.RedefineBlock'
    AcBlockRedefineBlock_RedefineBlockButon = 1001
    AcBlockWriteBlockNoObjectsSelected = 'AcBlock.WriteBlockNoObjectsSelected'
    AcBlockWriteBlockNoObjectsSelected_SelectObjectsButon = 1001
    AcBlockXrefConflict = 'AcBlock.XrefConflict'
    AcCloudCreateFolderExists = 'AcCloud.CreateFolderExists'
    AcCloudCreateFolderInvalid = 'AcCloud.CreateFolderInvalid'
    AcCloudCreateFolderPathnameLength = 'AcCloud.CreateFolderPathnameLength'
    AcCmMgrAlreadyInGroup = 'AcCmMgr.AlreadyInGroup'
    AcCmMgrAutoconNoTypeSelected = 'AcCmMgr.AutoconNoTypeSelected'
    AcCmMgrConstrBarFilterZero = 'AcCmMgr.ConstrBarFilterZero'
    AcCmMgrCovertAssocDimTooMany = 'AcCmMgr.CovertAssocDimTooMany'
    AcCmMgrDeleteDimConstraint = 'AcCmMgr.DeleteDimConstraint'
    AcCmMgrDeleteDimParameter = 'AcCmMgr.DeleteDimParameter'
    AcCmMgrDeleteDimParameter_ConvertDimensionalConstraintButon = 1001
    AcCmMgrDeleteDimParameter_DeleteParameterNameButon = 1002
    AcCmMgrDeleteUserParameter = 'AcCmMgr.DeleteUserParameter'
    AcCmMgrDeleteUserParameter_DeleteUserParameterButon = 1001
    AcCmMgrDimOverConstrain = 'AcCmMgr.DimOverConstrain'
    AcCmMgrDimOverConstrain_CreateRefButon = 1001
    AcCmMgrDimOverConstrain_ReselectButon = 1002
    AcCmMgrEntityBlockSame = 'AcCmMgr.EntityBlockSame'
    AcCmMgrEvaluationFail = 'AcCmMgr.Evaluation.Fail'
    AcCmMgrRefeditWithConstraint = 'AcCmMgr.RefeditWithConstraint'
    AcCmMgrReferencedInEquation = 'AcCmMgr.ReferencedInEquation'
    AcCmMgrRelaxDragging = 'AcCmMgr.RelaxDragging'
    AcCmMgrToleranceTooLarge = 'AcCmMgr.ToleranceTooLarge'
    AcCmMgrToleranceTooLarge_ProceedAutoConstrainButon = 1001
    AcContentBlockImportMultiple = 'AcContent.BlockImportMultiple'
    AcContentBlockImportSingle = 'AcContent.BlockImportSingle'
    AcCoreBHCreatFailure = 'AcCore.BHCreatFailure'
    AcCoreCheckSpellBlock = 'AcCore.CheckSpellBlock'
    AcCoreCheckSpellXref = 'AcCore.CheckSpellXref'
    AcCoreDeleteKey = 'AcCore.DeleteKey'
    AcCoreIncompatibleArxApplication = 'AcCore.IncompatibleArxApplication'
    AcCoreIncompatibleArxApplication_LoadAllButon = 1002
    AcCoreIncompatibleArxApplication_LoadAppButon = 1001
    AcCoreIncompatibleArxApplication_SkipAllButon = 1004
    AcCoreIncompatibleArxApplication_SkipThisButon = 1003
    AcCoreMissingLanguagePack = 'AcCore.MissingLanguagePack'
    AcCoreMissingLanguagePack_CancelAndInstallButon = 1002
    AcCoreMissingLanguagePack_OpenDrawingButon = 1001
    AcCoreOpenACopy = 'AcCore.OpenACopy'
    AcCorePartialOpenDrawing = 'AcCore.PartialOpenDrawing'
    AcCorePartialOpenDrawing_PartialOpenButon = 1001
    AcCorePartialOpenDrawing_RestorePartialOpenStateButon = 1002
    AcCorePartialOpenEducationVersion = 'AcCore.PartialOpenEducationVersion'
    AcCorePartialOpenEducationVersion_CancelOperationButon = 1002
    AcCorePartialOpenEducationVersion_PartialOpenEducationContinueButon = 1001
    AcCorePartialOpenFileLocked = 'AcCore.PartialOpenFileLocked'
    AcCorePartialOpenLastSaved = 'AcCore.PartialOpenLastSaved'
    AcCorePartialOpenLastSaved_OpenButon = 1001
    AcCorePartialOpenLastSaved_RestoreButon = 1002
    AcCorePartialOpenLocked = 'AcCore.PartialOpenLocked'
    AcCorePointInBoundary = 'AcCore.PointInBoundary'
    AcCorePointOutsideBoundary = 'AcCore.PointOutsideBoundary'
    AcCoreRasteroutput = 'AcCore.Rasteroutput'
    AcCoreRasteroutput_IgnoreRasterButon = 1001
    AcCoreTrueConvert = 'AcCore.TrueConvert'
    AcCoreWelcomeScreenNotFound = 'AcCore.WelcomeScreenNotFound'
    AcDataLinkCannotUpdateData = 'AcDataLink.CannotUpdateData'
    AcDataLinkExcelNotFound = 'AcDataLink.ExcelNotFound'
    AcDataLinkExcelSheetNotFound = 'AcDataLink.ExcelSheetNotFound'
    AcDataLinkInvalidExcelFile = 'AcDataLink.InvalidExcelFile'
    AcDataLinkInvalidRange = 'AcDataLink.InvalidRange'
    AcDataLinkOverwrittenDatalinkCells = 'AcDataLink.OverwrittenDatalinkCells'
    AcDataLinkOverwrittenDatalinkCells_RetainCellsButon = 1002
    AcDataLinkOverwrittenDatalinkCells_UpdateCellsButon = 1001
    AcDimInvalidStyleName = 'AcDim.InvalidStyleName'
    AcDimRedefineDimStyle = 'AcDim.RedefineDimStyle'
    AcDwgFeedSaveFile = 'AcDwgFeed.SaveFile'
    AcDwgFeedSaveFile_SaveButon = 1001
    AcDwgFeedSaveFile_SyncToA360Buton = 1002
    AcDxFilesNotFound = 'AcDx.FilesNotFound'
    AcDxFilesNotFound_ContinueUpdateButon = 1001
    AcDxFilesNotFound_DoNotUpdateButon = 1002
    AcDxOutdatedTable = 'AcDx.OutdatedTable'
    AcDxOutdatedTable_SkipAllUpdatesButon = 1004
    AcDxOutdatedTable_SkipUpdateButon = 1003
    AcDxOutdatedTable_UpdateAllButon = 1002
    AcDxOutdatedTable_UpdateButon = 1001
    AcDxUpdateMCCells = 'AcDx.UpdateMCCells'
    AcDxUpdateMCCells_SkipManuallyChangedCellsButon = 1002
    AcDxUpdateMCCells_UpdateAllCellsButon = 1001
    AcDxWizardDataExtractionFilesNotFound = 'AcDxWizard.DataExtractionFilesNotFound'
    AcDxWizardQuitWizard = 'AcDxWizard.QuitWizard'
    AcDxWizardRemoveDrawing = 'AcDxWizard.RemoveDrawing'
    AcDxWizardRemoveDrawings = 'AcDxWizard.RemoveDrawings'
    AcDxWizardRemoveFolder = 'AcDxWizard.RemoveFolder'
    AcDxWizardUnsavedDrawing = 'AcDxWizard.UnsavedDrawing'
    AcDxWizardUnsavedDrawing_SaveDrawingButon = 1001
    AcGeoLocationUICoordSysAlreadyDefined = 'AcGeoLocationUI.CoordSysAlreadyDefined'
    AcGeoLocationUIDGLGEInstalled = 'AcGeoLocationUI.DGL.GEInstalled'
    AcGeoLocationUIDGLGENotInstalled = 'AcGeoLocationUI.DGL.GENotInstalled'
    AcGeoLocationUIGoogleEarthNotOpen = 'AcGeoLocationUI.GoogleEarthNotOpen'
    AcGeoLocationUIImportFromGoogleEarth = 'AcGeoLocationUI.ImportFromGoogleEarth'
    AcGeoLocationUIInitialNotification = 'AcGeoLocationUI.InitialNotification'
    AcGeoLocationUIInvalidKMLFile = 'AcGeoLocationUI.InvalidKMLFile'
    AcGeoLocationUIInvalidValue = 'AcGeoLocationUI.InvalidValue'
    AcGeoLocationUILocationAlreadyExists = 'AcGeoLocationUI.LocationAlreadyExists'
    AcGeoLocationUIMultipleLocationsFound = 'AcGeoLocationUI.MultipleLocationsFound'
    AcGeoLocationUIOptimizeGeomapImage = 'AcGeoLocationUI.OptimizeGeomapImage'
    AcGeoLocationUIOptimizeGeomapImage_OptimizeButon = 1001
    AcGeoLocationUIOptimizeGeomapImage_ReloadButon = 1002
    AcGeoLocationUIOxygenDisabled = 'AcGeoLocationUI.OxygenDisabled'
    AcGeoLocationUIOxygenUpdateAvailable = 'AcGeoLocationUI.OxygenUpdateAvailable'
    AcGeoLocationUIPlotLiveMapWarning = 'AcGeoLocationUI.PlotLiveMapWarning'
    AcGeoLocationUIRemove = 'AcGeoLocationUI.Remove'
    AcGeoLocationUIReorientMarker = 'AcGeoLocationUI.ReorientMarker'
    AcGeoLocationUITimeZoneChanged = 'AcGeoLocationUI.TimeZoneChanged'
    AcGeoLocationUITimeZoneUpdated = 'AcGeoLocationUI.TimeZoneUpdated'
    AcGeoLocationUIUnitMismatch = 'AcGeoLocationUI.UnitMismatch'
    AcGeoLocationUIUnitMismatch_ContinueButon = 1002
    AcGeoLocationUIUnitMismatch_ResetButon = 1001
    AcGuSMInvalidEntry = 'AcGuSM.InvalidEntry'
    AcGuSMReuildCurveDialogBoxInvalidEntry = 'AcGuSM.ReuildCurveDialogBoxInvalidEntry'
    AcGuSMReuildSurfaceDialogBoxInvalidEntry = 'AcGuSM.ReuildSurfaceDialogBoxInvalidEntry'
    AcLayerAppsCannotRestoreLayerState = 'AcLayerApps.CannotRestoreLayerState'
    AcLayerAppsDleteLayerState = 'AcLayerApps.DleteLayerState'
    AcLayerAppsLayerMergeVerify = 'AcLayerApps.LayerMergeVerify'
    AcLayerAppsLayerNotMerged = 'AcLayerApps.LayerNotMerged'
    AcLayerAppsLayerStateAddLayer = 'AcLayerApps.LayerStateAddLayer'
    AcLayerAppsLayerStateDuplicates = 'AcLayerApps.LayerStateDuplicates'
    AcLayerAppsLayerstateInvalidFile = 'AcLayerApps.LayerstateInvalidFile'
    AcLayerAppsLayerstateInvalidFile2 = 'AcLayerApps.LayerstateInvalidFile2'
    AcLayerAppsLayerStateNoneFound = 'AcLayerApps.LayerStateNoneFound'
    AcLayerAppsLayerStateNoneSelected = 'AcLayerApps.LayerStateNoneSelected'
    AcLayerAppsLayerStateSuccessfulImport = 'AcLayerApps.LayerStateSuccessfulImport'
    AcLayerAppsOverwriteLayerState = 'AcLayerApps.OverwriteLayerState'
    AcLaytransChangesNotSaved = 'AcLaytrans.ChangesNotSaved'
    AcLaytransChangesNotSaved_TranslateAndSaveButon = 1001
    AcLaytransChangesNotSaved_TranslateOnlyButon = 1002
    AcLayTransInvalidTransparencyValue = 'AcLayTrans.InvalidTransparencyValue'
    AcModelDocInventorImport = 'AcModelDoc.InventorImport'
    AcModelDocSketchModeEnteringViewSketch = 'AcModelDoc.SketchMode.EnteringViewSketch'
    AcOpmExtZeroValueParameter = 'AcOpmExt.ZeroValueParameter'
    AcParameterParameterFiltered = 'AcParameter.ParameterFiltered'
    AcPlotGuiPlotFileExists = 'AcPlotGui.PlotFileExists'
    AcPlotGuiPlotScaleConfirm = 'AcPlotGui.PlotScaleConfirm'
    AcPlotGuiUnsupportedPaperSize = 'AcPlotGui.UnsupportedPaperSize'
    AcPlotGuiUnsupportedPaperSize_UseDefaultPaperSizeButon = 1001
    AcPlotGuiUnsupportedPaperSize_UseOriginalPaperSizeButon = 1002
    AcPointCloudCompatibility = 'AcPointCloud.Compatibility'
    AcPointCloudGeoMismatch = 'AcPointCloud.GeoMismatch'
    AcPublish3DDWFCreated = 'AcPublish.3DDWFCreated'
    AcPublishDSDSettingConflict = 'AcPublish.DSDSettingConflict'
    AcPublishLoadSheetList = 'AcPublish.LoadSheetList'
    AcPublishNoPasswordSpecified = 'AcPublish.NoPasswordSpecified'
    AcPublishSaveSheetList = 'AcPublish.SaveSheetList'
    AcPurgeConfirmPurge = 'AcPurge.ConfirmPurge'
    AcPurgeConfirmSinglePurge = 'AcPurge.ConfirmSinglePurge'
    AcPurgeConfirmSinglePurge_PurgeThisItemButon = 1001
    AcPurgeConfirmSinglePurge_SkipThisItemButon = 1002
    AcPurgeSelectObjects_LayerNotVisible = 'AcPurge.SelectObjects_LayerNotVisible'
    AcPurgeSelectObjects_LayerNotVisible_Button_not_turn_on_layerButon = 1002
    AcPurgeSelectObjects_LayerNotVisible_Button_turn_on_layerButon = 1001
    AcPurgeSelectObjects_VPFrozen = 'AcPurge.SelectObjects_VPFrozen'
    AcPurgeSelectObjects_VPFrozen_Button_not_turn_on_VP_layerButon = 1002
    AcPurgeSelectObjects_VPFrozen_Button_turn_on_VP_layerButon = 1001
    AcSignAppDigitalIDNotAvailable = 'AcSignApp.DigitalIDNotAvailable'
    AcSignApplyDigitalSignaturePreviouslySignedFile = 'AcSignApply.DigitalSignaturePreviouslySignedFile'
    AcSignApplyDigitalSignatureReadOnlyFile = 'AcSignApply.DigitalSignatureReadOnlyFile'
    AcSMConersonToASpline = 'AcSM.ConersonToASpline'
    AcSmNavCalloutBlockImportMultiple = 'AcSmNav.CalloutBlock.ImportMultiple'
    AcSmNavCalloutBlockImportMultiple_MultipleFileMultipleBlockButon = 1001
    AcSmNavCalloutBlockImportMultiple_MultipleFileOneBlockButon = 1002
    AcSmNavCalloutBlockImportSingle = 'AcSmNav.CalloutBlock.ImportSingle'
    AcSmNavCalloutBlockImportSingle_SingleFileMultipleBlockButon = 1001
    AcSmNavCalloutBlockImportSingle_SingleFileOneBlockButon = 1002
    AcSMNavDrawingFileNotFound = 'AcSMNav.DrawingFileNotFound'
    AcSmNavInvalidNameTooLong = 'AcSmNav.InvalidName.TooLong'
    AcSmNavLayoutDrawingMissing = 'AcSmNav.Layout.DrawingMissing'
    AcSmNavLayoutDrawingMissing_AcSmNav_BrowseRemapLayoutButon = 1002
    AcSmNavLayoutDrawingMissing_AcSmNav_RemoveLayoutButon = 1001
    AcSmNavLayoutIssueWithDrawing = 'AcSmNav.Layout.IssueWithDrawing'
    AcSmNavLayoutIssueWithDrawing_DiscardDuplicateButon = 1003
    AcSmNavLayoutIssueWithDrawing_DuplicateButon = 1002
    AcSmNavLayoutMissing = 'AcSmNav.Layout.Missing'
    AcSmNavLayoutMissing_BrowseRemapLayoutButon = 1003
    AcSmNavLayoutMissing_RemapLayoutButon = 1002
    AcSmNavLayoutMissing_RemoveLayoutButon = 1001
    AcSmNavProjectManagerProjectsFolderCreation = 'AcSmNav.ProjectManager.ProjectsFolderCreation'
    AcSmNavProjectManagerProjectsFolderCreation_SELECTFOLDERButon = 1002
    AcSmNavProjectManagerProjectsFolderCreation_UseDocumentsFolderButon = 1001
    AcStdCheckComplete = 'AcStd.CheckComplete'
    AcStdStandardsViolationFound = 'AcStd.StandardsViolationFound'
    AcSubDCannotRefineAtMinLevel = 'AcSubD.CannotRefineAtMinLevel'
    AcSubDConvertToASM = 'AcSubD.ConvertToASM'
    AcSubDConvertToASMInvalidTopology = 'AcSubD.ConvertToASMInvalidTopology'
    AcSubDConvertToASM_ConvertToFacetedASMButon = 1003
    AcSubDConvertToASM_ConvertToSmoothASMButon = 1002
    AcSubDConvertToASM_FilterMeshObjectsButon = 1001
    AcSubDConvertToMesh = 'AcSubD.ConvertToMesh'
    AcSubDConvertToMesh_ConvertObjectsButon = 1002
    AcSubDConvertToMesh_FilterObjectsButon = 1001
    AcSubDMaxSmoothLevel = 'AcSubD.MaxSmoothLevel'
    AcSubDMeshPrimitiveDialogBoxInvalidEntry = 'AcSubD.MeshPrimitiveDialogBoxInvalidEntry'
    AcSubDMeshSmoothInvalidSelection = 'AcSubD.MeshSmoothInvalidSelection'
    AcSubDMeshSmoothNonPrimitiveObject = 'AcSubD.MeshSmoothNonPrimitiveObject'
    AcSubDMeshSmoothNonPrimitiveObject_CreateMeshButon = 1001
    AcSubDMeshSmoothNonPrimitiveObject_DoNotConvertToMeshButon = 1002
    AcSubDMeshSmoothTooManyFaces = 'AcSubD.MeshSmoothTooManyFaces'
    AcSubDMinSmoothLevel = 'AcSubD.MinSmoothLevel'
    AcSubDOptionsDialogBoxInvalidEntry = 'AcSubD.OptionsDialogBoxInvalidEntry'
    AcSubDTessellationDialogBoxInvalidEntry = 'AcSubD.TessellationDialogBoxInvalidEntry'
    AcSubDUnsupportedObject = 'AcSubD.UnsupportedObject'
    AcSubDUnsupportedSubObject = 'AcSubD.UnsupportedSubObject'
    AcSynergyDeferUpdatesQueuedChanges = 'AcSynergy.DeferUpdates.QueuedChanges'
    AcSynergyFinishSymbolSketchDeleteSymbol = 'AcSynergy.FinishSymbolSketch.DeleteSymbol'
    AcSynergyFinishSymbolSketchInvalidSymbol = 'AcSynergy.FinishSymbolSketch.InvalidSymbol'
    AcSynergyFinishSymbolSketchInvalidSymbol_DiscardInvalidChangesButon = 1001
    AcSynergyFinishSymbolSketchInvalidSymbol_RepairSymbolButon = 1002
    AcSynergyFinishSymbolSketchSaveExit = 'AcSynergy.FinishSymbolSketch.SaveExit'
    AcSynergyFinishSymbolSketchSaveExit_DiscardSymbolSketchChangesButon = 1002
    AcSynergyFinishSymbolSketchSaveExit_SaveSymbolSketchButon = 1001
    AcSynergyInventorReferencesOutOfDate = 'AcSynergy.InventorReferences.OutOfDate'
    AcSynergyLabelExcludeCharactersInvalid = 'AcSynergy.LabelExcludeCharacters.Invalid'
    AcSynergyLODUnresolved = 'AcSynergy.LOD.Unresolved'
    AcSynergyOpenDrawingLostFunctionality = 'AcSynergy.OpenDrawing.LostFunctionality'
    AcSynergyPublishNotification = 'AcSynergy.PublishNotification'
    AcSynergyUnresolvedBeingOpened = 'AcSynergy.UnresolvedBeingOpened'
    AcSynergyUnresolvedInventorFiles = 'AcSynergy.UnresolvedInventorFiles'
    AcSynergyUnresolvedInventorFiles_SelectProjectButon = 1001
    AcSynergyVIEWBASEUnresolved = 'AcSynergy.VIEWBASE.Unresolved'
    AcSynergyViewSTDHighResolution = 'AcSynergy.ViewSTD.HighResolution'
    AcSynergyViewStyleRestoreDefaults = 'AcSynergy.ViewStyle.RestoreDefaults'
    AcSynergyViewUpdateAssociativeAnnotations = 'AcSynergy.ViewUpdate.AssociativeAnnotations'
    AcSynergyViewUpdateAssociativeLossDetected = 'AcSynergy.ViewUpdate.AssociativeLossDetected'
    AcTableCanNotPasteIntoLockedCells = 'AcTable.CanNotPasteIntoLockedCells'
    AcTableConfirmDeleteTableStyle = 'AcTable.ConfirmDeleteTableStyle'
    AcTableConfirmDeleteTableStyle_DeleteTableStyleButon = 1001
    AcTableDetachDataLink = 'AcTable.DetachDataLink'
    AcTableInvalidTbCellValue = 'AcTable.InvalidTbCellValue'
    AcTableInvalidTbCellValue_ChangeDataTypeButon = 1001
    AcTableInvalidTbCellValue_ChangeDataValueButon = 1002
    AcTableLargeNBOfCells = 'AcTable.LargeNBOfCells'
    AcTableMergeCells = 'AcTable.MergeCells'
    AcTableOverwriteStartingTable = 'AcTable.OverwriteStartingTable'
    AcTableOverwriteStartingTable_OverwriteButon = 1001
    AcTableRangeMismatch = 'AcTable.RangeMismatch'
    AcTableRangeOverlap = 'AcTable.RangeOverlap'
    AcTableRedefineCellStyle = 'AcTable.RedefineCellStyle'
    AcTableRedefineTableStyle = 'AcTable.RedefineTableStyle'
    AcTableRemoveStartingTable = 'AcTable.RemoveStartingTable'
    ActionRecorderCommandNotRecordedOnDYNMODE = 'ActionRecorder.CommandNotRecordedOnDYNMODE'
    ActionRecorderConfirmDeletionOfActionMacro = 'ActionRecorder.ConfirmDeletionOfActionMacro'
    ActionRecorderConfirmDeletionOfItem = 'ActionRecorder.ConfirmDeletionOfItem'
    ActionRecorderConfirmMultipleDeletion = 'ActionRecorder.ConfirmMultipleDeletion'
    ActionRecorderConflictWithCommandName = 'ActionRecorder.ConflictWithCommandName'
    ActionRecorderConflictWithExistingMacroName = 'ActionRecorder.ConflictWithExistingMacroName'
    ActionRecorderError = 'ActionRecorder.Error'
    ActionRecorderFileNameAlreadyExists = 'ActionRecorder.FileNameAlreadyExists'
    ActionRecorderInconsistency = 'ActionRecorder.Inconsistency'
    ActionRecorderInvalidName = 'ActionRecorder.InvalidName'
    ActionRecorderNameAlreadyExists = 'ActionRecorder.NameAlreadyExists'
    ActionRecorderNoDirectorySpecified = 'ActionRecorder.NoDirectorySpecified'
    ActionRecorderNoObjectsSelected = 'ActionRecorder.NoObjectsSelected'
    ActionRecorderPlaybackComplete = 'ActionRecorder.PlaybackComplete'
    ActionRecorderPlaybackError = 'ActionRecorder.PlaybackError'
    ActionRecorderUnableToAccessDefaultFolder = 'ActionRecorder.UnableToAccessDefaultFolder'
    ActionRecorderUserMessage = 'ActionRecorder.UserMessage'
    ActionRecorderValueNotRecorded = 'ActionRecorder.ValueNotRecorded'
    ActionRecorderValueTypeMismatch = 'ActionRecorder.ValueTypeMismatch'
    AcTranslatorsExportTranslationProcessIsRunning = 'AcTranslators.ExportTranslationProcessIsRunning'
    AcTranslatorsRunExportTranslationInBackground = 'AcTranslators.RunExportTranslationInBackground'
    AcTranslatorsRunTranslationInBackground = 'AcTranslators.RunTranslationInBackground'
    AcTranslatorsTranslationProcessIsRunning = 'AcTranslators.TranslationProcessIsRunning'
    AcUnderlayInvalidFile = 'AcUnderlay.InvalidFile'
    AdRefManAddXRefs = 'AdRefMan.AddXRefs'
    AdRefManRemoveFolderPaths = 'AdRefMan.RemoveFolderPaths'
    AssocFilletExplodePolyline = 'AssocFillet.ExplodePolyline'
    AssocNetworkEvaluationFail = 'AssocNetwork.Evaluation.Fail'
    AssocSurfaceCreationFail = 'AssocSurface.Creation.Fail'
    AssocSurfaceModificationFail = 'AssocSurface.Modification.Fail'
    AssocVariableEvaluationFail = 'AssocVariable.Evaluation.Fail'
    AutoCADAcCloudConnectDocCloseBlocker = 'AutoCAD.AcCloudConnect.DocCloseBlocker'
    AutoCADAcCloudConnectSyncFileNotSaved = 'AutoCAD.AcCloudConnect.SyncFileNotSaved'
    AutoCADApplicationRestart = 'AutoCAD.ApplicationRestart'
    AutoCADAssociativePathArray = 'AutoCAD.AssociativePathArray'
    AutoCADAssociativePathArray_AssociativePathArray_CancelButon = 1002
    AutoCADAssociativePathArray_AssociativePathArray_ContinueButon = 1001
    AutoCADAutodeskMaterialLibNotFound = 'AutoCAD.AutodeskMaterialLibNotFound'
    AutoCADAutodeskMaterialLibNotInstalled = 'AutoCAD.AutodeskMaterialLibNotInstalled'
    AutoCADAutodeskMaterialTexNotFound = 'AutoCAD.AutodeskMaterialTexNotFound'
    AutoCADAutodeskMaterialTexNotInstalled = 'AutoCAD.AutodeskMaterialTexNotInstalled'
    AutoCADAutodeskMediumTexDownloadError = 'AutoCAD.AutodeskMediumTexDownloadError'
    AutoCADAutodeskMediumTexNotInstalled = 'AutoCAD.AutodeskMediumTexNotInstalled'
    AutoCADAutodeskMediumTexNotInstalledLight = 'AutoCAD.AutodeskMediumTexNotInstalledLight'
    AutoCADAutodeskMediumTexTobeInstalled = 'AutoCAD.AutodeskMediumTexTobeInstalled'
    AutoCADCannotGripEdit = 'AutoCAD.CannotGripEdit'
    AutoCADCannotGripEdit_CannotGripEdit_CancelButon = 1002
    AutoCADCannotGripEdit_CannotGripEdit_continueButon = 1001
    AutoCADCannotRelax = 'AutoCAD.CannotRelax'
    AutoCADCannotRotate = 'AutoCAD.CannotRotate'
    AutoCADCannotRotate_CannotRotate_MaintainButon = 1002
    AutoCADCannotRotate_CannotRotate_RelaxButon = 1001
    AutoCADChangesNotSaved = 'AutoCAD.ChangesNotSaved'
    AutoCADChangesNotSaved_DiscardAndCloseButon = 1002
    AutoCADChangesNotSaved_SaveAndCloseButon = 1001
    AutoCADCleanScreenOn = 'AutoCAD.CleanScreenOn'
    AutoCADDependencyOnTrimAction = 'AutoCAD.DependencyOnTrimAction'
    AutoCADDependencyOnTrimAction_DependencyOnTrimAction_CancelButon = 1002
    AutoCADDependencyOnTrimAction_DependencyOnTrimAction_continueButon = 1001
    AutoCADDWGAssociation = 'AutoCAD.DWGAssociation'
    AutoCADExceededSizeLimit = 'AutoCAD.ExceededSizeLimit'
    AutoCADExceededSizeLimit_SaveDWGXButon = 1002
    AutoCADExceededSizeLimit_ShowDetailsButon = 1001
    AutoCADHelpFileNotFound = 'AutoCAD.HelpFileNotFound'
    AutoCADHelpFileNotFound_NotLaunchHelpButon = 2
    AutoCADHelpFileNotFound_UpdateHelpFileLocationButon = 1
    AutoCADMissingDWFViewer = 'AutoCAD.MissingDWFViewer'
    AutoCADMissingOrCorruptDisplayDriver = 'AutoCAD.MissingOrCorruptDisplayDriver'
    AutoCADMissingOrCorruptDisplayDriverMac = 'AutoCAD.MissingOrCorruptDisplayDriverMac'
    AutoCADMissingPDFViewer = 'AutoCAD.MissingPDFViewer'
    AutoCADNearingSizeLimit = 'AutoCAD.NearingSizeLimit'
    AutoCADNearingSizeLimit_LargeObjectSupportOffButon = 1001
    AutoCADNearingSizeLimit_LargeObjectSupportOnButon = 1002
    AutoCADOfflineHelpNotInstalled = 'AutoCAD.OfflineHelpNotInstalled'
    AutoCADOfflineHelpNotInstalledMac = 'AutoCAD.OfflineHelpNotInstalledMac'
    AutoCADOfflineHelpNotInstalled_CopyToClipboardButon = 1003
    AutoCADOfflineHelpNotInstalled_DownloadOfflineHelpButon = 1001
    AutoCADOfflineHelpNotInstalled_UseOnlineHelpButon = 1002
    AutoCADOnlineHelpNotAccessible = 'AutoCAD.OnlineHelpNotAccessible'
    AutoCADOnlineHelpNotAccessible_TryConnectInternetButon = 1001
    AutoCADOnlineHelpNotAccessible_UseOfflineHelpButon = 1002
    AutoCADParametricExpression = 'AutoCAD.ParametricExpression'
    AutoCADParametricExpression_ParametricExpression_CancelButon = 1002
    AutoCADParametricExpression_ParametricExpression_ContinueButon = 1001
    AutoCADRelaxDragging = 'AutoCAD.RelaxDragging'
    AutoCADRelaxDragging_DeleteButon = 1002
    AutoCADRelaxDragging_RelaxButon = 1001
    AutoCADRenderScaleSettings = 'AutoCAD.RenderScaleSettings'
    AutoCADRenderScaleSettings_CancelRenderButon = 1002
    AutoCADRenderScaleSettings_ConvertToMetersButon = 1001
    AutoCADSubtractSurface = 'AutoCAD.SubtractSurface'
    AutoCADSubtractSurface_SubtractSurface_CancelButon = 1002
    AutoCADSubtractSurface_SubtractSurface_ContinueButon = 1001
    AutoCADTooManyControlVertices = 'AutoCAD.TooManyControlVertices'
    AutoCADTooManyControlVertices_TooManyControlVertices_CancelButon = 1002
    AutoCADTooManyControlVertices_TooManyControlVertices_ContinueButon = 1001
    AutoCADUnionSurface = 'AutoCAD.UnionSurface'
    AutoCADUnionSurface_UnionSurface_CancelButon = 1002
    AutoCADUnionSurface_UnionSurface_ContinueButon = 1001
    AutoCADUnsupportedObjects = 'AutoCAD.UnsupportedObjects'
    AutoCADUnsupportedObjects_DoNotShowUnsupportedObjects_ButtonButon = 1003
    AutoCADUnsupportedObjects_ShowBoundingBox_ButtonButon = 1002
    AutoCADUnsupportedObjects_ShowObjectsIfAvailable_ButtonButon = 1001
    AutoCADXrefLockFail = 'AutoCAD.XrefLockFail'
    AutodeskInitDisplayDriverError = 'Autodesk.InitDisplayDriverError'
    AutodeskMismatchGeoCS = 'Autodesk.MismatchGeoCS'
    AutodeskRemoveSectionJogs = 'Autodesk.RemoveSectionJogs'
    AutodeskReqVersionNoOpen = 'Autodesk.ReqVersionNoOpen'
    AutodeskReqVersionOpenForWrite = 'Autodesk.ReqVersionOpenForWrite'
    AutodeskReqVersionReadOnly = 'Autodesk.ReqVersionReadOnly'
    AutodeskSharedCloudFile = 'Autodesk.SharedCloudFile'
    AutoLISPLoadSettings = 'AutoLISP.LoadSettings'
    AutoLISPPromptRestartAcad = 'AutoLISP.PromptRestartAcad'
    AutoLISPSelectAutoLISPExtension = 'AutoLISP.SelectAutoLISPExtension'
    AutoLISPSelectAutoLISPExtension_SelectVisualLISPButon = 1002
    AutoLISPSelectAutoLISPExtension_SelectVSCodeExtensionButon = 1001
    BatchStandardsCheckerReportFile = 'BatchStandardsChecker.ReportFile'
    BEDITConstraintsFound = 'BEDIT.ConstraintsFound'
    BlockCircularReference = 'Block.CircularReference'
    BlockCircularReferenceToTable = 'Block.CircularReferenceToTable'
    BoundaryBoundaryDefinitionError = 'Boundary.BoundaryDefinitionError'
    ColorDlgMissingColorBook = 'ColorDlg.MissingColorBook'
    CommadNotAllowedInCompare = 'Commad.NotAllowedInCompare'
    CommadNotAllowedInXCompare = 'Commad.NotAllowedInXCompare'
    CompareExportProcessingContinueorStop = 'CompareExport.ProcessingContinueorStop'
    CompareExportProcessingInProgress = 'CompareExport.ProcessingInProgress'
    CompareExportProcessingStarted = 'CompareExport.ProcessingStarted'
    ConstraintDynamicBlockGripsWillBeHidden = 'Constraint.DynamicBlockGripsWillBeHidden'
    ConstraintNonAssociativeSelection = 'Constraint.NonAssociativeSelection'
    ConstraintNonDimConstraintSelection = 'Constraint.NonDimConstraintSelection'
    ConstraintOverConstraint = 'Constraint.OverConstraint'
    ConstraintWouldOverContrain = 'Constraint.WouldOverContrain'
    ConvertHatchObjectsWarning = 'Convert.HatchObjectsWarning'
    CUICannotCopyNestedToolbarFlyouts = 'CUI.CannotCopyNestedToolbarFlyouts'
    CUIDeleteReferencedImage = 'CUI.DeleteReferencedImage'
    CUIDeleteUnreferencedImage = 'CUI.DeleteUnreferencedImage'
    CUIFoldPanelContents = 'CUI.FoldPanelContents'
    CUIImageNameAlreadyExist = 'CUI.ImageNameAlreadyExist'
    CUIImageNameInvalid = 'CUI.ImageNameInvalid'
    CUIReset = 'CUI.Reset'
    CUIReset_CUIResetCancelButon = 1002
    CUIReset_CUIResetContinueButon = 1001
    CUIRestoreBackup = 'CUI.RestoreBackup'
    CUIRestoreBackup_CUIRestoreBackupCancelButon = 1002
    CUIRestoreBackup_CUIRestoreBackupContinueButon = 1001
    CustomizationComfirmCopytoRibbonPanels = 'Customization.ComfirmCopytoRibbonPanels'
    CustomizationSaveChanges = 'Customization.SaveChanges'
    CustomizationUndefinedObjectType = 'Customization.UndefinedObjectType'
    CustomizationUnsavedCUIChanges = 'Customization.UnsavedCUIChanges'
    DGN3DSeedFileRequired = 'DGN.3DSeedFileRequired'
    DGNIncompatibleSeedFile = 'DGN.IncompatibleSeedFile'
    DGNIncompatibleSeedFile_SelectAnotherDGNExportButon = 1002
    DGNIncompatibleSeedFile_SelectAnotherSeedButon = 1001
    DGNInvalidDGNFile = 'DGN.InvalidDGNFile'
    DGNNoDesignModelsFound = 'DGN.NoDesignModelsFound'
    DGNUIConfirmMappingRemoval = 'DGNUI.ConfirmMappingRemoval'
    DgnUIDGNImportUnsupportObjects = 'DgnUI.DGNImportUnsupportObjects'
    DGNUIIncompatibleSeedFileSettings = 'DGNUI.IncompatibleSeedFileSettings'
    DGNUIIncompatibleSeedFileSettings_ContinueExportButon = 1001
    DGNUIInvalidPropertyName = 'DGNUI.InvalidPropertyName'
    DGNUIInvalidSeedFile = 'DGNUI.InvalidSeedFile'
    DGNUINumberOfElementsExceededLimit = 'DGNUI.NumberOfElementsExceededLimit'
    DgnUIUnsupportDGNExportObjects = 'DgnUI.UnsupportDGNExportObjects'
    DigitalSignaturesUnsupportedDrawingFormat = 'DigitalSignatures.UnsupportedDrawingFormat'
    DimensionFrozenLayer = 'Dimension.FrozenLayer'
    DimensionNoDimensionsSelected = 'Dimension.NoDimensionsSelected'
    DimMLeaderStyleRedefineStyle = 'Dim.MLeaderStyle.RedefineStyle'
    DimMLeaderStyleRedefineStyle_DoNotRedefineStyleButon = 1002
    DimMLeaderStyleRedefineStyle_RedefineStyleButon = 1001
    DrawingOpenForeignDWGFile = 'DrawingOpen.ForeignDWGFile'
    DrawingSaveAsAcModelDoc = 'DrawingSaveAs.AcModelDoc'
    DwgAidsRestoreAllContexts = 'DwgAids.RestoreAllContexts'
    DwgAidsRestoreClassicColors = 'DwgAids.RestoreClassicColors'
    DwgAidsRestoreCurrentContext = 'DwgAids.RestoreCurrentContext'
    DwgAidsRestoreCurrentContext_RestoreCurrentContextButon = 1001
    DWGCompareCompletelyDifferent = 'DWGCompare.CompletelyDifferent'
    DWGCompareCompletelyIdentical = 'DWGCompare.CompletelyIdentical'
    DWGCompareExport = 'DWGCompare.Export'
    DWGCompareIsResultDrawing = 'DWGCompare.IsResultDrawing'
    DWGCompareReCompare = 'DWGCompare.ReCompare'
    DWGCompareUncomparableObjects = 'DWGCompare.UncomparableObjects'
    DWGRecoveryDamagedFile = 'DWGRecovery.DamagedFile'
    DWGRecoveryDrawingRecovery = 'DWGRecovery.DrawingRecovery'
    DWGRecoveryErrorsFound = 'DWGRecovery.ErrorsFound'
    DWGRecoveryRecoverSummary = 'DWGRecovery.RecoverSummary'
    EnterpriseWorkspaceCannotSaveChanges = 'EnterpriseWorkspace.CannotSaveChanges'
    ExportLayoutFileCreated = 'ExportLayout.FileCreated'
    ExportLayoutFileCreatedSDI = 'ExportLayout.FileCreatedSDI'
    ExportSelectWindow = 'Export.SelectWindow'
    ExportSelectWindowSuccessful = 'Export.SelectWindowSuccessful'
    HatchBoundaryDefinitionErrorNRC = 'Hatch.BoundaryDefinitionErrorNRC'
    HatchBoundaryDefinitionErrorRC = 'Hatch.BoundaryDefinitionErrorRC'
    HatchDenseHatchCreation = 'Hatch.DenseHatchCreation'
    HatchDrawingHasLargeHatches = 'Hatch.DrawingHasLargeHatches'
    HatchDuplicatePatternSelected = 'Hatch.DuplicatePatternSelected'
    HatchDuplicatePatternSelected_OverwriteButon = 1002
    HatchDuplicatePatternSelected_SkipButon = 1003
    HatchFrozenLayer = 'Hatch.FrozenLayer'
    HatchInvalidPatternSelected = 'Hatch.InvalidPatternSelected'
    HatchInvalidPatternSelectedSandboxed = 'Hatch.InvalidPatternSelected.Sandboxed'
    HatchInvalidPatternSelectedSandboxed_RemoveButon = 1001
    HatchInvalidPatternSelected_CancelButon = 1002
    HatchInvalidPatternSelected_RevealInFinderButon = 1001
    HatchOpenBoundary = 'Hatch.OpenBoundary'
    LayerManagerCannotAdjustPlotSetting = 'LayerManager.CannotAdjustPlotSetting'
    LayerManagerCannotMakeCurrent = 'LayerManager.CannotMakeCurrent'
    LayerManagerCurrentLayerOff = 'LayerManager.CurrentLayerOff'
    LayerManagerCurrentLayerOffMac = 'LayerManager.CurrentLayerOffMac'
    LayerManagerDeletedBlockRefs = 'LayerManager.DeletedBlockRefs'
    LayerManagerDeleteGroupWarning = 'LayerManager.DeleteGroupWarning'
    LayerManagerDeleteGroupWarning_DeleteGroupAndLayersButon = 1002
    LayerManagerDeleteGroupWarning_DeleteGroupWithoutLayersButon = 1001
    LayerManagerExcessLayerFilters = 'LayerManager.ExcessLayerFilters'
    LayerManagerHideSystemGroup = 'LayerManager.HideSystemGroup'
    LayerManagerLayerCannotFreeze = 'LayerManager.LayerCannotFreeze'
    LayerManagerLayerCannotFreezeMac = 'LayerManager.LayerCannotFreezeMac'
    LayerManagerLayerDeleteMac = 'LayerManager.LayerDeleteMac'
    LayerManagerLayerDeleteMac_Calcel_DeleteButon = 1003
    LayerManagerLayerDeleteMac_DeleteLayerAndMoveObjectsButon = 1002
    LayerManagerLayerDeleteMac_DeleteLayerAndObjectsButon = 1001
    LayerManagerLayerRename = 'LayerManager.LayerRename'
    LayerManagerMultipleDeleteConfirmation = 'LayerManager.MultipleDeleteConfirmation'
    LayerManagerMutipleLayerNotDeleted = 'LayerManager.MutipleLayerNotDeleted'
    LayerManagerNewLayerFilteredWarning = 'LayerManager.NewLayerFilteredWarning'
    LayerManagerNoMatchingLayers = 'LayerManager.NoMatchingLayers'
    LayerManagerNoMatchingLayers_CreateGroupAnywayButon = 1002
    LayerManagerNoMatchingLayers_EditTheGroupButon = 1001
    LayerManagerShowMessageClose = 'LayerManager.ShowMessageClose'
    LayerManagerShowMessageYesNo = 'LayerManager.ShowMessageYesNo'
    LayerManagerSingleDeleteConfirmation = 'LayerManager.SingleDeleteConfirmation'
    LayerManagerSingleLayerNotDeleted = 'LayerManager.SingleLayerNotDeleted'
    LayerManagerUnableToModifyLayersWarning = 'LayerManager.UnableToModifyLayersWarning'
    LayerToolsIncompatibleVisualStyle = 'LayerTools.IncompatibleVisualStyle'
    LayerWalkLayerStatesChange = 'LayerWalk.LayerStatesChange'
    LicensingCHECKOUTTIMEDOUTSHUTDOWN = 'Licensing.CHECKOUTTIMEDOUTSHUTDOWN'
    LicensingGENRICSHUTDOWN = 'Licensing.GENRICSHUTDOWN'
    LicensingNetworkLicenseLost = 'Licensing.NetworkLicenseLost'
    LicensingNetworkLicenseLostAcadShutDown = 'Licensing.NetworkLicenseLostAcadShutDown'
    LicensingUserLicenseSignoutAndQuit = 'Licensing.UserLicenseSignoutAndQuit'
    LicensingUserLicenseSignoutAndQuitAcadShutDown = 'Licensing.UserLicenseSignoutAndQuitAcadShutDown'
    LinetypeReloadLinetype = 'Linetype.ReloadLinetype'
    MainFrameCommandLineHideWindow = 'MainFrame.CommandLineHideWindow'
    MaterialDeleteNestedMaps = 'Material.DeleteNestedMaps'
    MaterialsDesynchronizeMaps = 'Materials.DesynchronizeMaps'
    MaterialsLibraryInUse = 'Materials.LibraryInUse'
    MaterialsSynchronizeMaps = 'Materials.SynchronizeMaps'
    MaterialUIMaterialInUse = 'MaterialUI.MaterialInUse'
    MaterialUIMigrateMaterial = 'MaterialUI.MigrateMaterial'
    MTEUnknownTextFonts = 'MTE.UnknownTextFonts'
    MTEXTAutoStackProperties1 = 'MTEXT.AutoStackProperties1'
    MTEXTAutoStackProperties1WithoutDoNotShow = 'MTEXT.AutoStackProperties1.WithoutDoNotShow'
    MTEXTAutoStackProperties2 = 'MTEXT.AutoStackProperties2'
    MTextStyleChange = 'MText.StyleChange'
    MTextUnsavedChanges = 'MText.UnsavedChanges'
    MTextWarningAboutBullets = 'MText.WarningAboutBullets'
    MTextWarningAboutPasting = 'MText.WarningAboutPasting'
    NavToolsNeedGreaterEqualNumber = 'NavTools.NeedGreaterEqualNumber'
    NavToolsNeedGreaterNumber = 'NavTools.NeedGreaterNumber'
    NavToolsNeedNumInRange = 'NavTools.NeedNumInRange'
    ObjectNameNoFolderAccess = 'ObjectName.NoFolderAccess'
    OPMAcPEXCtlCannotModifyProperty = 'OPM.AcPEXCtl.CannotModifyProperty'
    OPMAcPEXCtlPatternNameNotFound = 'OPM.AcPEXCtl.PatternNameNotFound'
    OpmNoObjectsFound = 'Opm.NoObjectsFound'
    OptionOnlineTabDisableCloudDocuments = 'OptionOnlineTab.DisableCloudDocuments'
    PdfImportNoDataImported = 'PdfImport.NoDataImported'
    PdfImportNoRasterDataImported = 'PdfImport.NoRasterDataImported'
    PdfImportReadOnlyPDFImportImagePath = 'PdfImport.ReadOnlyPDFImportImagePath'
    PdfShxTextTextRecognitionFailed = 'PdfShxText.TextRecognitionFailed'
    PdfShxTextTextRecognitionSucceeded = 'PdfShxText.TextRecognitionSucceeded'
    PhotoViewerFileNotFound = 'PhotoViewer.FileNotFound'
    PhotoViewerFileOrFolderNotFound = 'PhotoViewer.FileOrFolderNotFound'
    PhotoViewerInvalidFileFormat = 'PhotoViewer.InvalidFileFormat'
    PhotoViewerRemoveImage = 'PhotoViewer.RemoveImage'
    PlotAndPublishCancelEntireJob = 'PlotAndPublish.CancelEntireJob'
    PlotAndPublishCancelEntireSheet = 'PlotAndPublish.CancelEntireSheet'
    PlotBatchPlotFromPlot = 'Plot.BatchPlotFromPlot'
    PlotBatchPlotFromPlot_BatchPlotFromPlot_CancelButon = 1002
    PlotBatchPlotFromPlot_BatchPlotFromPlot_ContinueButon = 1001
    PlotBatchPlotFromPlot_BatchPlotFromPlot_LearnMoreButon = 1003
    PlotGuiPlotModelSpaceAlert = 'PlotGui.PlotModelSpaceAlert'
    PlotGuiPlotModelSpaceAlert_TaskPlotDialogButton_181Buton = 1001
    PlotGuiPlotModelSpaceAlert_TaskPlotDialogButton_182Buton = 1002
    PlotPaperSizeNotFound = 'Plot.PaperSizeNotFound'
    PlotProcessingBackgroundJob = 'Plot.ProcessingBackgroundJob'
    PlotShadePlot = 'Plot.ShadePlot'
    Printing3DNoInternetConn = 'Printing3D.NoInternetConn'
    Printing3DObjectsOnLockedLayer = 'Printing3D.ObjectsOnLockedLayer'
    Printing3DPrepareModel = 'Printing3D.PrepareModel'
    Printing3DPrintStudioNotInstalled = 'Printing3D.PrintStudioNotInstalled'
    PropertiesObjectsMoveToFrozenOrOffLayers = 'Properties.ObjectsMoveToFrozenOrOffLayers'
    PropertiesObjectsOnLockedLayers = 'Properties.ObjectsOnLockedLayers'
    PulishNoPreset = 'Pulish.NoPreset'
    PulishPresetIllegalChar = 'Pulish.PresetIllegalChar'
    PulishPresetInvalidName = 'Pulish.PresetInvalidName'
    PulishPresetInvalidResolution = 'Pulish.PresetInvalidResolution'
    PulishPresetNameExist = 'Pulish.PresetNameExist'
    PulishSaveDSD = 'Pulish.SaveDSD'
    QPDockToRibbon = 'QP.DockToRibbon'
    QPOffPanelWarning = 'QP.OffPanelWarning'
    QPRemoveUndefObjType = 'QP.RemoveUndefObjType'
    QPRestoreDefault = 'QP.RestoreDefault'
    QPRestoreDefault_KeepQPCustomButon = 1002
    QPRestoreDefault_RestorQPeSettingsButon = 1001
    QPSwitchToFloatMode = 'QP.SwitchToFloatMode'
    QPSyncWithTooptip = 'QP.SyncWithTooptip'
    QVDrawingCloseAllOtherDrawings = 'QVDrawing.CloseAllOtherDrawings'
    QVDrawingCloseReadOnly = 'QVDrawing.CloseReadOnly'
    RecoverAllWarning = 'RecoverAll.Warning'
    RenderIBLWarnSetBackgroundWithDisplayImageOn = 'Render.IBL.WarnSetBackgroundWithDisplayImageOn'
    RenderNoFacesToRender = 'Render.NoFacesToRender'
    RenderOutOfMemory = 'Render.OutOfMemory'
    RenderSoftOutOfMemory = 'Render.SoftOutOfMemory'
    RibbonUnableToAddControlIntoQAT = 'Ribbon.UnableToAddControlIntoQAT'
    RibbonUnableToAddSeparatorIntoQAT = 'Ribbon.UnableToAddSeparatorIntoQAT'
    RibbonUnableToRemoveFromQAT = 'Ribbon.UnableToRemoveFromQAT'
    RollOverRestoreDefault = 'RollOver.RestoreDefault'
    RollOverRestoreDefault_KeepCustomButon = 1002
    RollOverRestoreDefault_RestoreSettingsButon = 1001
    SaveToWebMobileFailDownloadInstall = 'SaveToWebMobile.FailDownloadInstall'
    SaveToWebMobileFeatureNotAvailable = 'SaveToWebMobile.FeatureNotAvailable'
    SaveToWebMobileNoInternetConn = 'SaveToWebMobile.NoInternetConn'
    SaveToWebMobileUpdateAvailable = 'SaveToWebMobile.UpdateAvailable'
    ScaleListLargeScaleAlert = 'ScaleList.LargeScaleAlert'
    ScaleListResetScaleList = 'ScaleList.ResetScaleList'
    SceneUIPhotometricDistantLights = 'SceneUI.PhotometricDistantLights'
    SceneUISunlightAndExposure = 'SceneUI.SunlightAndExposure'
    SceneUIViewportLightingMode = 'SceneUI.ViewportLightingMode'
    SecurityInvalidCertificate = 'Security.InvalidCertificate'
    SecuritySignedFileNotinTrustedFolder = 'Security.SignedFileNotinTrustedFolder'
    SecurityStartAutoCADInAdminMode = 'Security.StartAutoCADInAdminMode'
    SecurityUnsignedExecutableFile = 'Security.UnsignedExecutableFile'
    SecurityWritablePathWarning = 'Security.WritablePathWarning'
    SecurityWritablePathWarning_ContinueButon = 1001
    SeekFileNameTooLong = 'Seek.FileName.TooLong'
    seekSaveChanges = 'seek.SaveChanges'
    seekSaveChanges_TranslateAndSave1Buton = 1001
    seekSaveChanges_TranslateAndSave2Buton = 1002
    seekSaveFile = 'seek.SaveFile'
    seekSaveFile_SaveFileButon = 1001
    seekWebsiteNotAvailable = 'seek.WebsiteNotAvailable'
    ShareViewProcessingContinueOrStop = 'ShareView.ProcessingContinueOrStop'
    ShareViewProcessingInProgress = 'ShareView.ProcessingInProgress'
    ShareViewProcessingStarted = 'ShareView.ProcessingStarted'
    ShareViewX86ProcessingStarted = 'ShareView.X86ProcessingStarted'
    SheetSetManagerConfirmChanges = 'SheetSetManager.ConfirmChanges'
    SheetSetManagerConfirmChangesForGroups = 'SheetSetManager.ConfirmChangesForGroups'
    SheetSetManagerDrawingFileNotFound = 'SheetSetManager.DrawingFileNotFound'
    SheetSetManagerLostSetAssociation = 'SheetSetManager.LostSetAssociation'
    ShowMotionDeleteAllView = 'ShowMotion.DeleteAllView'
    ShowMotionQuickViewDeleteCategoryViews = 'ShowMotionQuickView.DeleteCategoryViews'
    ShowMotionQuickViewRenameError = 'ShowMotionQuickView.RenameError'
    ShowMotionUpdateAll = 'ShowMotion.UpdateAll'
    SpellerCheckLayersLocked = 'SpellerCheck.LayersLocked'
    StandardCloseReadOnly = 'Standard.CloseReadOnly'
    StandardDeleteConfirmation = 'Standard.DeleteConfirmation'
    StandardDuplicateNameCopyOverwrite = 'Standard.DuplicateName.CopyOverwrite'
    StandardDuplicateNameError = 'Standard.DuplicateName.Error'
    StandardDuplicateNameReplaceCancel = 'Standard.DuplicateName.ReplaceCancel'
    StandardFileAlreadyExists = 'Standard.FileAlreadyExists'
    StandardFileAlreadyExists_RenameButon = 1002
    StandardFileAlreadyExists_ReplaceButon = 1001
    StandardFileConfirmationWithNoToAll = 'Standard.FileConfirmation.WithNoToAll'
    StandardFileConfirmationWithoutNoToAll = 'Standard.FileConfirmation.WithoutNoToAll'
    StandardFileInUse = 'Standard.FileInUse'
    StandardFileNotFound = 'Standard.FileNotFound'
    StandardFilePathTooLong = 'Standard.FilePathTooLong'
    StandardInvalidNameEmptyName = 'Standard.InvalidName.EmptyName'
    StandardInvalidNameTooLong = 'Standard.InvalidName.TooLong'
    StandardInvalidNameUnsupportedCharacters = 'Standard.InvalidName.UnsupportedCharacters'
    StandardInvalidNameValueTooLong = 'Standard.InvalidNameValue.TooLong'
    StandardInvalidNameValueUnsupportedCharacters = 'Standard.InvalidNameValue.UnsupportedCharacters'
    StandardInvalidPath = 'Standard.InvalidPath'
    StandardInValidPropertyName = 'Standard.InValidPropertyName'
    StandardObjectTypeCannotBeDeleted = 'Standard.ObjectTypeCannotBeDeleted'
    StandardObjectUnsupportCharacters = 'Standard.Object.UnsupportCharacters'
    StandardOffsetObjectIsNotPlanar = 'Standard.OffsetObjectIsNotPlanar'
    StandardPathOrFileNameNotSpecified = 'Standard.PathOrFileNameNotSpecified'
    StandardWriteProtectedFile = 'Standard.WriteProtectedFile'
    SurfaceCVEditing = 'Surface.CVEditing'
    TextFindBlockRef = 'TextFind.BlockRef'
    TextFindBlockRef_ReplaceAllButon = 1001
    TextFindBlockRef_ReplaceThisButon = 1002
    TextFindBlockRef_SkipButon = 1003
    UnitsInsertUnits = 'Units.InsertUnits'
    UnitsInsertUSSurveyFeetUnits = 'Units.InsertUSSurveyFeetUnits'
    UnitsRenderEngine = 'Units.RenderEngine'
    VMToolsUIOverwriteAnimationFrames = 'VMToolsUI.OverwriteAnimationFrames'
    VMToolsUIWalkFlyToPerspectiveView = 'VMToolsUI.WalkFlyToPerspectiveView'
    XrefCompareReload = 'XrefCompare.Reload'
    XrefCompareReloadInXCompare = 'XrefCompare.ReloadInXCompare'


class AcAeUtilities(object):
    """ AcAeUtilities() """
    @staticmethod
    def GetBeditConstraintColor(constraintType):
        """ GetBeditConstraintColor(constraintType: ConstraintType) -> Color """
        pass

    @staticmethod
    def GetBlockName():
        """ GetBlockName() -> str """
        pass

    @staticmethod
    def GetCurrentVisibilityStateName():
        """ GetCurrentVisibilityStateName() -> str """
        pass

    @staticmethod
    def GetVisibilitySets(visibilities):
        """ GetVisibilitySets(visibilities: List[str]) """
        pass

    @staticmethod
    def IsAuthorPaletteVisible():
        """ IsAuthorPaletteVisible() -> bool """
        pass

    @staticmethod
    def IsInBlockEditor():
        """ IsInBlockEditor() -> bool """
        pass

    @staticmethod
    def IsInBVMode():
        """ IsInBVMode() -> bool """
        pass

    @staticmethod
    def IsVisibilityParameterPresent():
        """ IsVisibilityParameterPresent() -> bool """
        pass

    @staticmethod
    def PickFirstBeforeInvokeBvHide():
        """ PickFirstBeforeInvokeBvHide() -> bool """
        pass

    @staticmethod
    def PickFirstBeforeInvokeBvShow():
        """ PickFirstBeforeInvokeBvShow() -> bool """
        pass

    @staticmethod
    def SetBeditConstraintColor(constraintType, color):
        """ SetBeditConstraintColor(constraintType: ConstraintType, color: Color) """
        pass

    @staticmethod
    def ShowAuthorPalette(bShow):
        """ ShowAuthorPalette(bShow: bool) """
        pass

    ConstraintType = None


class AcDownloadCallback(MulticastDelegate):
    """ AcDownloadCallback(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, callback, obj):
        """ BeginInvoke(self: AcDownloadCallback, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: AcDownloadCallback, result: IAsyncResult) """
        pass

    def Invoke(self):
        """ Invoke(self: AcDownloadCallback) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class AcNavisworksProtocolAdapter(object):
    # no doc

class AcNavisworksService(object):
    """ AcNavisworksService() """
    def Dispose(self):
        """ Dispose(self: AcNavisworksService) """
        pass

    def RegisterFileProtocol(self, scheme, fileprotocol):
        """ RegisterFileProtocol(self: AcNavisworksService, scheme: str, fileprotocol: INavisworksFileProtocol) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass


class ActiveThemeColor(object):
    # no doc
    @staticmethod
    def Instance():
        """ Instance() -> ActiveThemeColor """
        pass

    ColorThemeChanged = None
    CurrentTheme = None
    InspectorBGHighlight = None
    InspectorItem = None
    PaletteBackground = None


class AppLoaderDownloadUtils(object):
    """ AppLoaderDownloadUtils() """
    @staticmethod
    def CancelDownloadJob(nToken):
        """ CancelDownloadJob(nToken: UInt32) """
        pass


class AppMenuUtil(object):
    """ AppMenuUtil() """
    @staticmethod
    def IsApplicationRegistered(appName):
        """ IsApplicationRegistered(appName: str) -> bool """
        pass

    @staticmethod
    def OpenDocument(fileName):
        """ OpenDocument(fileName: str) """
        pass


class AttachUtil(object):
    """ AttachUtil() """
    @staticmethod
    def CheckDwgFile(csDwgPath):
        """ CheckDwgFile(csDwgPath: str) -> bool """
        pass

    @staticmethod
    def CheckImageFile(csImagePath):
        """ CheckImageFile(csImagePath: str) -> bool """
        pass

    @staticmethod
    def CmdLineImageAttach(strImageFile):
        """ CmdLineImageAttach(strImageFile: str) """
        pass

    @staticmethod
    def CmdLineNavisworksAttach(strNavisworksFile):
        """ CmdLineNavisworksAttach(strNavisworksFile: str) """
        pass

    @staticmethod
    def CmdLinePointCloudAttach(strPointCloudFile):
        """ CmdLinePointCloudAttach(strPointCloudFile: str) """
        pass

    @staticmethod
    def CmdLineXAttach(strDWGFile):
        """ CmdLineXAttach(strDWGFile: str) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: AttachUtil) """
        pass

    @staticmethod
    def GetImageFileExtensions():
        """ GetImageFileExtensions() -> str """
        pass

    @staticmethod
    def GetImageFilterString():
        """ GetImageFilterString() -> str """
        pass

    @staticmethod
    def GetOpenFilesResult(opt, multiSelArray):
        """ GetOpenFilesResult(opt: PromptOpenFileOptions, multiSelArray: Array[str]) -> Array[str] """
        pass

    @staticmethod
    def ImageAdjust(objIds):
        """ ImageAdjust(objIds: Array[ObjectId]) """
        pass

    @staticmethod
    def ImageAttach(strImageFile):
        """ ImageAttach(strImageFile: str) """
        pass

    @staticmethod
    def ImageClip(objId):
        """ ImageClip(objId: ObjectId) """
        pass

    @staticmethod
    def isDialogShow():
        """ isDialogShow() -> bool """
        pass

    @staticmethod
    def IsPCAttachAllowed():
        """ IsPCAttachAllowed() -> bool """
        pass

    @staticmethod
    def LoadBIMUnderlayArx():
        """ LoadBIMUnderlayArx() """
        pass

    @staticmethod
    def LoadBIMUnderlayCrx():
        """ LoadBIMUnderlayCrx() """
        pass

    @staticmethod
    def LoadISM():
        """ LoadISM() """
        pass

    @staticmethod
    def LoadPointCloudArx():
        """ LoadPointCloudArx() """
        pass

    @staticmethod
    def LoadPointCloudCrx():
        """ LoadPointCloudCrx() """
        pass

    @staticmethod
    def NavisworksAttach(strNavisworksFile):
        """ NavisworksAttach(strNavisworksFile: str) """
        pass

    @staticmethod
    def PointCloudAttach(strPointCloudFile):
        """ PointCloudAttach(strPointCloudFile: str) """
        pass

    @staticmethod
    def PointCloudClip(objId):
        """ PointCloudClip(objId: ObjectId) """
        pass

    @staticmethod
    def VPClip():
        """ VPClip() """
        pass

    @staticmethod
    def XAttach(strDWGFileArray):
        """ XAttach(strDWGFileArray: Array[str]) """
        pass

    @staticmethod
    def XClip():
        """ XClip() """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass


class BlockDisplayItem(DependencyObject):
    """
    BlockDisplayItem(hostPath: str, blockName: str, modifiedTime: Int64, lastAccessTime: Int64)
    BlockDisplayItem(recentBlockNameStr: str, viewMode: BlockViewMode)
    BlockDisplayItem(btrId: ValueType, viewMode: BlockViewMode, asCurrentDwgBlock: bool)
    BlockDisplayItem(btrId: ValueType, viewMode: BlockViewMode)
    BlockDisplayItem(fullPathName: str, blockName: str, viewMode: BlockViewMode)
    BlockDisplayItem(fullPathName: AcString*, blockName: AcString*, viewMode: BlockViewMode, modifyTime: Int64, isAnnotative: bool, isDynamic: bool, drawingThumbnail: HBITMAP__*)
    BlockDisplayItem(fullPathName: AcString*, blockName: AcString*, bitmap: HBITMAP__*, viewMode: BlockViewMode)
    BlockDisplayItem(block: AcContentRecentBlock*, viewMode: BlockViewMode)
    BlockDisplayItem(block: AcContentBlock*, viewMode: BlockViewMode)
    """
    def computeKey(self, *args): #cannot find CLR method
        """ computeKey(self: BlockDisplayItem, block: AcContentBlock*)computeKey(self: BlockDisplayItem, fullPathName: AcString*, blockName: AcString*) """
        pass

    def copyFrom(self, other):
        """ copyFrom(self: BlockDisplayItem, other: BlockDisplayItem) """
        pass

    @staticmethod
    def createDrawingDisplayItem(fullPathName, viewMode):
        """ createDrawingDisplayItem(fullPathName: str, viewMode: BlockViewMode) -> BlockDisplayItem """
        pass

    @staticmethod
    def generateKey(*__args):
        """
        generateKey(btrId: ValueType, asCurrentDwgBlock: bool) -> str
        generateKey(recentBlockPropStr: str) -> str
        """
        pass

    def generateThumbnail(self):
        """ generateThumbnail(self: BlockDisplayItem) """
        pass

    def generateToolTipThumbnail(self, size):
        """ generateToolTipThumbnail(self: BlockDisplayItem, size: int) """
        pass

    def hasThumbnailCreated(self):
        """ hasThumbnailCreated(self: BlockDisplayItem) -> bool """
        pass

    def hasToolTipImageCreated(self):
        """ hasToolTipImageCreated(self: BlockDisplayItem) -> bool """
        pass

    def isEqualTo(self, other):
        """ isEqualTo(self: BlockDisplayItem, other: BlockDisplayItem) -> bool """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: BlockDisplayItem, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def refreshBlockStandardIcon(self):
        """ refreshBlockStandardIcon(self: BlockDisplayItem) """
        pass

    def resetThumbnail(self):
        """ resetThumbnail(self: BlockDisplayItem) """
        pass

    def resetToolTipThumbnail(self):
        """ resetToolTipThumbnail(self: BlockDisplayItem) """
        pass

    def setDrawingAsBlockForEmptyBlockName(self, *args): #cannot find CLR method
        """ setDrawingAsBlockForEmptyBlockName(self: BlockDisplayItem, fullPathName: AcString*, blockName: AcString*) """
        pass

    def setPinned(self, *args): #cannot find CLR method
        """ setPinned(self: BlockDisplayItem, val: bool) """
        pass

    def setThumbnailToDefault(self):
        """ setThumbnailToDefault(self: BlockDisplayItem) """
        pass

    def setTooltipThumbnailToDefault(self):
        """ setTooltipThumbnailToDefault(self: BlockDisplayItem) """
        pass

    def ToBlockSelectedItemData(self):
        """ ToBlockSelectedItemData(self: BlockDisplayItem) -> str """
        pass

    def ToString(self):
        """ ToString(self: BlockDisplayItem) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, hostPath: str, blockName: str, modifiedTime: Int64, lastAccessTime: Int64)
        __new__(cls: type, recentBlockNameStr: str, viewMode: BlockViewMode)
        __new__(cls: type, btrId: ValueType, viewMode: BlockViewMode, asCurrentDwgBlock: bool)
        __new__(cls: type, btrId: ValueType, viewMode: BlockViewMode)
        __new__(cls: type, fullPathName: str, blockName: str, viewMode: BlockViewMode)
        __new__(cls: type, fullPathName: AcString*, blockName: AcString*, viewMode: BlockViewMode, modifyTime: Int64, isAnnotative: bool, isDynamic: bool, drawingThumbnail: HBITMAP__*)
        __new__(cls: type, fullPathName: AcString*, blockName: AcString*, bitmap: HBITMAP__*, viewMode: BlockViewMode)
        __new__(cls: type, block: AcContentRecentBlock*, viewMode: BlockViewMode)
        __new__(cls: type, block: AcContentBlock*, viewMode: BlockViewMode)
        """
        pass

    AllowExplode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowExplode(self: BlockDisplayItem) -> bool

Set: AllowExplode(self: BlockDisplayItem) = value
"""

    Explodable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Explodable(self: BlockDisplayItem) -> bool

Set: Explodable(self: BlockDisplayItem) = value
"""

    GeoCoordSystemId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeoCoordSystemId(self: BlockDisplayItem) -> str

Set: GeoCoordSystemId(self: BlockDisplayItem) = value
"""

    HasGeoData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasGeoData(self: BlockDisplayItem) -> bool

Set: HasGeoData(self: BlockDisplayItem) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: BlockDisplayItem) -> ObjectId

"""

    InsertTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InsertTime(self: BlockDisplayItem) -> Int64

Set: InsertTime(self: BlockDisplayItem) = value
"""

    InsUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InsUnit(self: BlockDisplayItem) -> UnitsValue

Set: InsUnit(self: BlockDisplayItem) = value
"""

    IsAnnotative = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAnnotative(self: BlockDisplayItem) -> bool

Set: IsAnnotative(self: BlockDisplayItem) = value
"""

    IsBlockOriented = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBlockOriented(self: BlockDisplayItem) -> bool

Set: IsBlockOriented(self: BlockDisplayItem) = value
"""

    IsDynamic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDynamic(self: BlockDisplayItem) -> bool

Set: IsDynamic(self: BlockDisplayItem) = value
"""

    IsPinned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPinned(self: BlockDisplayItem) -> bool

Set: IsPinned(self: BlockDisplayItem) = value
"""

    IsThumbnailGenerated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsThumbnailGenerated(self: BlockDisplayItem) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: BlockDisplayItem) -> bool

Set: IsValid(self: BlockDisplayItem) = value
"""

    IsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVisible(self: BlockDisplayItem) -> bool

Set: IsVisible(self: BlockDisplayItem) = value
"""

    ItemType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemType(self: BlockDisplayItem) -> ItemTypeEnum

"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Key(self: BlockDisplayItem) -> str

Set: Key(self: BlockDisplayItem) = value
"""

    ModifyTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModifyTime(self: BlockDisplayItem) -> Int64

Set: ModifyTime(self: BlockDisplayItem) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: BlockDisplayItem) -> str

Set: Name(self: BlockDisplayItem) = value
"""

    PreviewImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreviewImage(self: BlockDisplayItem) -> str

Set: PreviewImage(self: BlockDisplayItem) = value
"""

    ScaleUniformly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScaleUniformly(self: BlockDisplayItem) -> bool

Set: ScaleUniformly(self: BlockDisplayItem) = value
"""

    SerializeState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SerializeState(self: BlockDisplayItem) -> RecentBlockSerializeState

Set: SerializeState(self: BlockDisplayItem) = value
"""

    SnapshotInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SnapshotInfo(self: BlockDisplayItem) -> BlockSnapshotInfo

Set: SnapshotInfo(self: BlockDisplayItem) = value
"""

    Thumbnail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Thumbnail(self: BlockDisplayItem) -> ImageSource

"""

    ThumbnailLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThumbnailLabel(self: BlockDisplayItem) -> str

"""

    ThumbnailSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThumbnailSize(self: BlockDisplayItem) -> int

"""

    ThumbnailState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThumbnailState(self: BlockDisplayItem) -> ThumbnailGenerateState

Set: ThumbnailState(self: BlockDisplayItem) = value
"""

    ToolTipImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToolTipImage(self: BlockDisplayItem) -> ImageSource

"""

    ToolTipImageSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToolTipImageSize(self: BlockDisplayItem) -> int

Set: ToolTipImageSize(self: BlockDisplayItem) = value
"""

    ToolTipImageState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToolTipImageState(self: BlockDisplayItem) -> ThumbnailGenerateState

Set: ToolTipImageState(self: BlockDisplayItem) = value
"""

    TranslatedURL = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TranslatedURL(self: BlockDisplayItem) -> str

Set: TranslatedURL(self: BlockDisplayItem) = value
"""

    URL = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: URL(self: BlockDisplayItem) -> str

Set: URL(self: BlockDisplayItem) = value
"""

    ViewMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewMode(self: BlockDisplayItem) -> BlockViewMode

Set: ViewMode(self: BlockDisplayItem) = value
"""


    PropertyChanged = None


class BlockLibraryPathChangedEventArgs(EventArgs):
    """ BlockLibraryPathChangedEventArgs(strPath: str) """
    @staticmethod # known case of __new__
    def __new__(self, strPath):
        """ __new__(cls: type, strPath: str) """
        pass

    BlockLibraryPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BlockLibraryPath(self: BlockLibraryPathChangedEventArgs) -> str

"""



class BlockSnapshotInfo(object):
    """ BlockSnapshotInfo(snapshotUrl: str, targetBlockName: str) """
    @staticmethod # known case of __new__
    def __new__(self, snapshotUrl, targetBlockName):
        """ __new__(cls: type, snapshotUrl: str, targetBlockName: str) """
        pass

    snapshotUrl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: snapshotUrl(self: BlockSnapshotInfo) -> str

"""

    targetBlockName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: targetBlockName(self: BlockSnapshotInfo) -> str

"""



class BlockStreamCIPLog(object):
    """ BlockStreamCIPLog() """
    @staticmethod
    def logBlockPaletteClosed():
        """ logBlockPaletteClosed() """
        pass

    @staticmethod
    def logBlockPaletteOpened():
        """ logBlockPaletteOpened() """
        pass

    @staticmethod
    def logBlockrecentfolderSysvarInfo(valueType):
        """ logBlockrecentfolderSysvarInfo(valueType: str) """
        pass

    @staticmethod
    def logCountOfCurrentTabSwitchedTo():
        """ logCountOfCurrentTabSwitchedTo() """
        pass

    @staticmethod
    def logCountOfCurrentTabUsed():
        """ logCountOfCurrentTabUsed() """
        pass

    @staticmethod
    def logCountOfExplodeChecked():
        """ logCountOfExplodeChecked() """
        pass

    @staticmethod
    def logCountOfExternalTabSwitchedTo():
        """ logCountOfExternalTabSwitchedTo() """
        pass

    @staticmethod
    def logCountOfExternalTabUsed():
        """ logCountOfExternalTabUsed() """
        pass

    @staticmethod
    def logCountOfInsertPointChecked():
        """ logCountOfInsertPointChecked() """
        pass

    @staticmethod
    def logCountOfRecentTabSwitchedTo():
        """ logCountOfRecentTabSwitchedTo() """
        pass

    @staticmethod
    def logCountOfRecentTabUsed():
        """ logCountOfRecentTabUsed() """
        pass

    @staticmethod
    def logCountOfRepeatChecked():
        """ logCountOfRepeatChecked() """
        pass

    @staticmethod
    def logCountOfRotationChecked():
        """ logCountOfRotationChecked() """
        pass

    @staticmethod
    def logCountOfScaleChecked():
        """ logCountOfScaleChecked() """
        pass

    @staticmethod
    def logCountOfScaleUniformUsed():
        """ logCountOfScaleUniformUsed() """
        pass

    @staticmethod
    def logCurrentTabUsedMetaData(bMetaDataUsedInCurrentDrawingTab):
        """ logCurrentTabUsedMetaData(bMetaDataUsedInCurrentDrawingTab: bool) """
        pass

    @staticmethod
    def logDwgInsertedAsABlock():
        """ logDwgInsertedAsABlock() """
        pass

    @staticmethod
    def logFileSelectedAsLibrary():
        """ logFileSelectedAsLibrary() """
        pass

    @staticmethod
    def logFolderSelectedAsLibrary(countOfFilesInFolder):
        """ logFolderSelectedAsLibrary(countOfFilesInFolder: int) """
        pass

    @staticmethod
    def logLibraryInfo(libraryOperation, libraryType):
        """ logLibraryInfo(libraryOperation: str, libraryType: str) """
        pass

    @staticmethod
    def logLocalServerActivityInfo(activityType, runTime, status):
        """ logLocalServerActivityInfo(activityType: str, runTime: int, status: str) """
        pass

    @staticmethod
    def logNonDwgBlockInserted():
        """ logNonDwgBlockInserted() """
        pass

    @staticmethod
    def logNumberOfBlocksInCurrentTab(count):
        """ logNumberOfBlocksInCurrentTab(count: int) """
        pass

    @staticmethod
    def logNumberOfBlocksInExternalTab(count):
        """ logNumberOfBlocksInExternalTab(count: int) """
        pass

    @staticmethod
    def logNumberOfBlocksInRecentTab(count):
        """ logNumberOfBlocksInRecentTab(count: int) """
        pass

    @staticmethod
    def logSearchUsed():
        """ logSearchUsed() """
        pass

    @staticmethod
    def logWayToInsertBlockByContextMenu():
        """ logWayToInsertBlockByContextMenu() """
        pass

    @staticmethod
    def logWayToInsertBlockByDoubleClick():
        """ logWayToInsertBlockByDoubleClick() """
        pass

    @staticmethod
    def logWayToInsertBlockByDragDrop():
        """ logWayToInsertBlockByDragDrop() """
        pass

    @staticmethod
    def logWayToInsertBlockBySinglelick():
        """ logWayToInsertBlockBySinglelick() """
        pass


class BlockStreamLocalServer(object):
    """ BlockStreamLocalServer() """
    @staticmethod
    def displayItemToBlockPreviewInfo(displayItem, bForToolTip):
        """ displayItemToBlockPreviewInfo(displayItem: BlockDisplayItem, bForToolTip: bool) -> mgBlockPreviewInfo """
        pass

    @staticmethod
    def getBlockNameListResultJsonUrlName():
        """ getBlockNameListResultJsonUrlName() -> str """
        pass

    @staticmethod
    def getBlockNameListResultReadyStr():
        """ getBlockNameListResultReadyStr() -> str """
        pass

    @staticmethod
    def getBlockPreviewpartialResultName():
        """ getBlockPreviewpartialResultName() -> str """
        pass

    @staticmethod
    def getFileModifyTime(filePath):
        """ getFileModifyTime(filePath: str) -> Int64 """
        pass

    @staticmethod
    def getRequestDict():
        """ getRequestDict() -> Dictionary[str, List[Tuple[BlockDisplayItem, bool]]] """
        pass

    @staticmethod
    def getRequstBlocksStr(*__args):
        """
        getRequstBlocksStr(infoList: List[mgBlockPreviewInfo]) -> str
        getRequstBlocksStr(displayList: List[Tuple[BlockDisplayItem, bool]]) -> str
        """
        pass

    @staticmethod
    def pushBlockPreviewGenerationRequest(displayItem, bForToolTip):
        """ pushBlockPreviewGenerationRequest(displayItem: BlockDisplayItem, bForToolTip: bool) -> bool """
        pass

    @staticmethod
    def useLocalServerForBlock(blockDisplayItem):
        """ useLocalServerForBlock(blockDisplayItem: BlockDisplayItem) -> bool """
        pass


class BlockStreamLog(object):
    # no doc
    @staticmethod
    def debug(message):
        """ debug(message: str)debug(message: AcString*) """
        pass

    def Dispose(self):
        """ Dispose(self: BlockStreamLog) """
        pass

    @staticmethod
    def error(message):
        """ error(message: str)error(message: AcString*) """
        pass

    @staticmethod
    def inform(message):
        """ inform(message: str)inform(message: AcString*) """
        pass

    @staticmethod
    def isLogEnabled():
        """ isLogEnabled() -> bool """
        pass

    @staticmethod
    def warning(message):
        """ warning(message: str)warning(message: AcString*) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    LogLevel = None


class BlockStreamUtils(object):
    """ BlockStreamUtils() """
    @staticmethod
    def cleanupSnapshotFromRecentBlockList(snapshotInfo):
        """ cleanupSnapshotFromRecentBlockList(snapshotInfo: BlockSnapshotInfo) """
        pass

    @staticmethod
    def clearBlockRecentSignInFromPage():
        """ clearBlockRecentSignInFromPage() """
        pass

    @staticmethod
    def clearBlockRecentStorageSetFromPage():
        """ clearBlockRecentStorageSetFromPage() """
        pass

    @staticmethod
    def closeInSideDbPool(key):
        """ closeInSideDbPool(key: str) """
        pass

    @staticmethod
    def combineRecentBlocksPath(recent_item):
        """ combineRecentBlocksPath(recent_item: Dictionary[str, str]) -> str """
        pass

    @staticmethod
    def convertProviderDetailToProvider(inputTechnology, inputSubscription, outputProvider):
        """ convertProviderDetailToProvider(inputTechnology: AcString*, inputSubscription: AcString*, outputProvider: AcString*) -> bool """
        pass

    @staticmethod
    def convertProviderToProviderDetail(inputProvider, outputTechnology, outputSubscription):
        """ convertProviderToProviderDetail(inputProvider: AcString*, outputTechnology: AcString*, outputSubscription: AcString*) -> bool """
        pass

    @staticmethod
    def doDragDrop(item):
        """ doDragDrop(item: BlockDisplayItem) -> UInt32 """
        pass

    @staticmethod
    def FindFile(FullPathName):
        """ FindFile(FullPathName: str) -> bool """
        pass

    @staticmethod
    def getAbsolutePath(provider, accountEmail, relativePath):
        """ getAbsolutePath(provider: str, accountEmail: str, relativePath: str) -> str """
        pass

    @staticmethod
    def getBlockNavigateFile():
        """ getBlockNavigateFile() -> str """
        pass

    @staticmethod
    def getBlockRecentIsSignInFromPage():
        """ getBlockRecentIsSignInFromPage() -> bool """
        pass

    @staticmethod
    def getBlockRecentIsStorageSetFromPage():
        """ getBlockRecentIsStorageSetFromPage() -> bool """
        pass

    @staticmethod
    def getBlockRecentOnboardingFolder():
        """ getBlockRecentOnboardingFolder() -> str """
        pass

    @staticmethod
    def getBlocksFromExternalFile(FullPathName, *__args):
        """
        getBlocksFromExternalFile(FullPathName: str, bNeedEntireDrawing: bool, viewMode: BlockViewMode) -> ObservableCollection[BlockDisplayItem]
        getBlocksFromExternalFile(FullPathName: str, metadataRoot: str, bNeedEntireDrawing: bool, viewMode: BlockViewMode, bDarkTheme: bool) -> ObservableCollection[BlockDisplayItem]
        """
        pass

    @staticmethod
    def getBlocksFromPartialResults(FullPathName, partialResultsJsonFilePath, bNeedEntireDrawing, viewMode):
        """ getBlocksFromPartialResults(FullPathName: str, partialResultsJsonFilePath: str, bNeedEntireDrawing: bool, viewMode: BlockViewMode) -> ObservableCollection[BlockDisplayItem] """
        pass

    @staticmethod
    def GetClientId():
        """ GetClientId() -> str """
        pass

    @staticmethod
    def getCurrentDrawingBlocks(viewMode):
        """ getCurrentDrawingBlocks(viewMode: BlockViewMode) -> ObservableCollection[BlockDisplayItem] """
        pass

    @staticmethod
    def getDwgDisplayItem(FullPathName, viewMode):
        """ getDwgDisplayItem(FullPathName: str, viewMode: BlockViewMode) -> BlockDisplayItem """
        pass

    @staticmethod
    def getFilePathType(path):
        """ getFilePathType(path: str) -> str """
        pass

    @staticmethod
    def getLastAccessedLibrary():
        """ getLastAccessedLibrary() -> str """
        pass

    @staticmethod
    def getLastAccessedLibraryNode():
        """ getLastAccessedLibraryNode() -> str """
        pass

    @staticmethod
    def GetLocalServerUage():
        """ GetLocalServerUage() -> int """
        pass

    @staticmethod
    def GetPreviewGenerateMethod():
        """ GetPreviewGenerateMethod() -> int """
        pass

    @staticmethod
    def GetPreviewParameter(viewMode):
        """ GetPreviewParameter(viewMode: BlockViewMode) -> str """
        pass

    @staticmethod
    def GetPreviewParameterAsJsonString(viewMode, bForFileSnapshot):
        """ GetPreviewParameterAsJsonString(viewMode: BlockViewMode, bForFileSnapshot: bool) -> str """
        pass

    @staticmethod
    def getRealPath(path):
        """ getRealPath(path: str) -> str """
        pass

    @staticmethod
    def getRecentBlocks(viewMode):
        """ getRecentBlocks(viewMode: BlockViewMode) -> ObservableCollection[BlockDisplayItem] """
        pass

    @staticmethod
    def getSerializedBlocks(viewMode):
        """ getSerializedBlocks(viewMode: BlockViewMode) -> List[BlockDisplayItem] """
        pass

    @staticmethod
    def getThumbnailSize(viewMode):
        """ getThumbnailSize(viewMode: BlockViewMode) -> int """
        pass

    @staticmethod
    def isBlocksRecentFolderSetToCloudStorage():
        """ isBlocksRecentFolderSetToCloudStorage() -> bool """
        pass

    @staticmethod
    def IsCloudDriveSyncFolder(dir):
        """ IsCloudDriveSyncFolder(dir: str) -> bool """
        pass

    @staticmethod
    def isLocalPath(filePath):
        """ isLocalPath(filePath: str) -> bool """
        pass

    @staticmethod
    def IsMetadataValid(dwgFileUrl, metadataRootDir, viewMode, bDarakTheme, bForFileSnapShot, bMiniValidation):
        """ IsMetadataValid(dwgFileUrl: str, metadataRootDir: str, viewMode: BlockViewMode, bDarakTheme: bool, bForFileSnapShot: bool, bMiniValidation: bool) -> bool """
        pass

    @staticmethod
    def isPaletteVisible():
        """ isPaletteVisible() -> bool """
        pass

    @staticmethod
    def isReadyToLoadSideDb():
        """ isReadyToLoadSideDb() -> bool """
        pass

    @staticmethod
    def isSystemBlock(blockId):
        """ isSystemBlock(blockId: ValueType) -> bool """
        pass

    @staticmethod
    def isUnsavedBlock(block):
        """ isUnsavedBlock(block: BlockDisplayItem) -> bool """
        pass

    @staticmethod
    def Log(msg):
        """ Log(msg: str) """
        pass

    @staticmethod
    def notifyBlockLibraryPathChanged(strPath):
        """ notifyBlockLibraryPathChanged(strPath: str) """
        pass

    @staticmethod
    def OnBlockThumbnailGenerated(fileName, blockName, width, height, bkColorRed, bkColorGreen, bkColorBlue, bUseBlackForWhite, bForTooltip, pngFilePath, itemToUpdate):
        """ OnBlockThumbnailGenerated(fileName: str, blockName: str, width: int, height: int, bkColorRed: int, bkColorGreen: int, bkColorBlue: int, bUseBlackForWhite: bool, bForTooltip: bool, pngFilePath: str, itemToUpdate: BlockDisplayItem) """
        pass

    @staticmethod
    def openInSideDbPool(key):
        """ openInSideDbPool(key: str) """
        pass

    @staticmethod
    def parseConentKey(contentKey):
        """ parseConentKey(contentKey: str) -> Tuple[str, str] """
        pass

    @staticmethod
    def parseJsonBlockPreview(resultJsonStr, itemsToUpdate):
        """ parseJsonBlockPreview(resultJsonStr: str, itemsToUpdate: List[Tuple[BlockDisplayItem, bool]]) """
        pass

    @staticmethod
    def parseRecentBlocksPath(path):
        """ parseRecentBlocksPath(path: str) -> Dictionary[str, str] """
        pass

    @staticmethod
    def readRegistryInt(keyName, defValue):
        """ readRegistryInt(keyName: str, defValue: int) -> int """
        pass

    @staticmethod
    def readRegistryString(keyName, defValue):
        """ readRegistryString(keyName: str, defValue: str) -> str """
        pass

    @staticmethod
    def refreshCurrentDwgBlocks(oldCurrentDwgBlocks, viewMode):
        """ refreshCurrentDwgBlocks(oldCurrentDwgBlocks: ObservableCollection[BlockDisplayItem], viewMode: BlockViewMode) """
        pass

    @staticmethod
    def refreshRecentBlocks(oldRecentBlocks, viewMode):
        """ refreshRecentBlocks(oldRecentBlocks: ObservableCollection[BlockDisplayItem], viewMode: BlockViewMode) """
        pass

    @staticmethod
    def removeFromRecentBlocks(itemToBeRemoved):
        """ removeFromRecentBlocks(itemToBeRemoved: BlockDisplayItem) """
        pass

    @staticmethod
    def saveSerializedBlocks(blocksToSerialize):
        """ saveSerializedBlocks(blocksToSerialize: List[BlockDisplayItem]) """
        pass

    @staticmethod
    def setLastAccessedLibrary(value):
        """ setLastAccessedLibrary(value: str) """
        pass

    @staticmethod
    def setLastAccessedLibraryNode(value):
        """ setLastAccessedLibraryNode(value: str) """
        pass

    @staticmethod
    def setRecentBlockPinned(key, val):
        """ setRecentBlockPinned(key: str, val: bool) """
        pass

    @staticmethod
    def UpdateDisplayItemFromPartialResults(resultsFile, dataSources):
        """ UpdateDisplayItemFromPartialResults(resultsFile: str, dataSources: ObservableCollection[BlockDisplayItem]) -> bool """
        pass

    @staticmethod
    def UseLocalServerForActivities():
        """ UseLocalServerForActivities() -> bool """
        pass

    @staticmethod
    def UseLocalServerForMetadata():
        """ UseLocalServerForMetadata() -> bool """
        pass

    @staticmethod
    def UseWhipToGeneratePreview():
        """ UseWhipToGeneratePreview() -> bool """
        pass

    @staticmethod
    def writeRegistryInt(keyName, value):
        """ writeRegistryInt(keyName: str, value: int) """
        pass

    @staticmethod
    def writeRegistryString(keyName, value):
        """ writeRegistryString(keyName: str, value: str) """
        pass

    BlockLibraryPathChanged = None


class BlockViewMode(Enum):
    """ enum BlockViewMode, values: kDetails (4), kExtraLargeIcon (0), kLargeIcon (1), kList (5), kMediumIcon (2), kSmallIcon (3) """
    kDetails = None
    kExtraLargeIcon = None
    kLargeIcon = None
    kList = None
    kMediumIcon = None
    kSmallIcon = None
    value__ = None


class BlockViewModeEnum(Enum):
    """ enum BlockViewModeEnum, values: """
    value__ = None


class CipUtils(object):
    # no doc
    def getMacroString(self, macro):
        """ getMacroString(self: CipUtils, macro: str) -> str """
        pass

    def getSessionId(self):
        """ getSessionId(self: CipUtils) -> str """
        pass

    @staticmethod
    def Instance():
        """ Instance() -> CipUtils """
        pass

    def IsOperational(self):
        """ IsOperational(self: CipUtils) -> bool """
        pass

    def LogApplicationMenuCommandExecute(self, id, sCmd):
        """ LogApplicationMenuCommandExecute(self: CipUtils, id: str, sCmd: str) """
        pass

    def LogIcLaunch(self, icType, group, category, title, url):
        """ LogIcLaunch(self: CipUtils, icType: int, group: str, category: str, title: str, url: str) """
        pass

    def LogIcQuery(self, queryString, buttonIndex):
        """ LogIcQuery(self: CipUtils, queryString: str, buttonIndex: int) """
        pass

    def LogModelessLayerItem(self, cmdStr, bInRibbon):
        """ LogModelessLayerItem(self: CipUtils, cmdStr: str, bInRibbon: bool) """
        pass

    def LogQuickAccessToolbarCommandExecute(self, id, sCmd):
        """ LogQuickAccessToolbarCommandExecute(self: CipUtils, id: str, sCmd: str) """
        pass

    def LogRibbonItemCommandExecute(self, sCmd, sTabName, sPanelName, bMenuMacro, dockSide):
        """ LogRibbonItemCommandExecute(self: CipUtils, sCmd: str, sTabName: str, sPanelName: str, bMenuMacro: bool, dockSide: int) """
        pass

    def LogStatusBarElementVisibility(self, elementName, isVisible):
        """ LogStatusBarElementVisibility(self: CipUtils, elementName: str, isVisible: bool) """
        pass

    def SetUaLaunchType(self, uaLaunchType):
        """ SetUaLaunchType(self: CipUtils, uaLaunchType: str) """
        pass

    def WaypointReachedWithAttributes(self, waypoint, state, attrs):
        """ WaypointReachedWithAttributes(self: CipUtils, waypoint: str, state: str, attrs: Dictionary[str, str]) """
        pass

    def WaypointReachedWithNoState(self, waypoint):
        """ WaypointReachedWithNoState(self: CipUtils, waypoint: str) """
        pass

    def WaypointReachedWithStringAtt(self, waypoint, state, att, strAttValue):
        """ WaypointReachedWithStringAtt(self: CipUtils, waypoint: str, state: str, att: str, strAttValue: str) """
        pass


class CloudPrintingServiceManager(object):
    """ CloudPrintingServiceManager() """
    Host = None


class ColorThemeChangedEventHandler(MulticastDelegate):
    """ ColorThemeChangedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: ColorThemeChangedEventHandler, sender: object, e: EventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ColorThemeChangedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ColorThemeChangedEventHandler, sender: object, e: EventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class ColorThemeEnum(Enum):
    """ enum ColorThemeEnum, values: Dark (0), Light (1), User (2) """
    Dark = None
    Light = None
    User = None
    value__ = None


class ComboBoxWrapper(ControlWrapper):
    # no doc
    def Dispose(self):
        """ Dispose(self: ControlWrapper, A_0: bool) """
        pass

    def raise_SelectionChanged(self, *args): #cannot find CLR method
        """ raise_SelectionChanged(self: ComboBoxWrapper, value0: object, value1: EventArgs) """
        pass

    def Select(self):
        """ Select(self: Control, directed: bool, forward: bool) """
        pass

    CanEnableIme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CreateParams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultCursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultImeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMargin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMaximumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMinimumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultPadding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DoubleBuffered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    FontHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ImeModeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    RenderRightToLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ResizeRedraw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ScaleChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShowFocusCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShowKeyboardCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    SelectionChanged = None


class CommandCallback(MulticastDelegate):
    """ CommandCallback(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, callback, obj):
        """ BeginInvoke(self: CommandCallback, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: CommandCallback, result: IAsyncResult) """
        pass

    def Invoke(self):
        """ Invoke(self: CommandCallback) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class CommandPiper(object):
    """
    CommandPiper(layerMgrCtrlId: int, bInRibbon: bool)
    CommandPiper()
    """
    @staticmethod
    def CommandsSentButNotStartedClear():
        """ CommandsSentButNotStartedClear() """
        pass

    @staticmethod
    def CommandWillStart(layerMgrCtrlId):
        """ CommandWillStart(layerMgrCtrlId: int) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: CommandPiper) """
        pass

    @staticmethod
    def GetRegenLayers(layerIds):
        """ GetRegenLayers(layerIds: ObjectIdCollection) -> int """
        pass

    @staticmethod
    def IsBlockingCommand(cmdName):
        """ IsBlockingCommand(cmdName: str) -> bool """
        pass

    def LayerClose(self):
        """ LayerClose(self: CommandPiper) """
        pass

    def LayerColor(self, value, *__args):
        """
        LayerColor(self: CommandPiper, value: Color, layerNames: ArrayList) -> bool
        LayerColor(self: CommandPiper, value: Color, layerName: str) -> bool
        """
        pass

    def LayerCurrent(self, layerName):
        """ LayerCurrent(self: CommandPiper, layerName: str) """
        pass

    def LayerDelete(self, *__args):
        """ LayerDelete(self: CommandPiper, layerNames: ArrayList)LayerDelete(self: CommandPiper, layerName: str) """
        pass

    def LayerDescription(self, value, existingValueEmpty, *__args):
        """ LayerDescription(self: CommandPiper, value: str, existingValueEmpty: bool, layerNames: ArrayList)LayerDescription(self: CommandPiper, value: str, existingValueEmpty: bool, layerName: str) """
        pass

    def LayerFilterDelete(self, filtersNames):
        """ LayerFilterDelete(self: CommandPiper, filtersNames: ArrayList) """
        pass

    def LayerFilterEditGroup(self, add, filterName, *__args):
        """ LayerFilterEditGroup(self: CommandPiper, add: bool, filterName: str, layerNames: ArrayList)LayerFilterEditGroup(self: CommandPiper, add: bool, filterName: str, layerName: str) """
        pass

    def LayerFilterEditGroupReplace(self, filterName, parentName, layerNames):
        """ LayerFilterEditGroupReplace(self: CommandPiper, filterName: str, parentName: str, layerNames: ArrayList) """
        pass

    def LayerFilterEditPropertyConvert(self, filterName):
        """ LayerFilterEditPropertyConvert(self: CommandPiper, filterName: str) """
        pass

    def LayerFilterEditPropertyDef(self, filterName, filterExpression):
        """ LayerFilterEditPropertyDef(self: CommandPiper, filterName: str, filterExpression: str) """
        pass

    def LayerFilterNewGroup(self, filterName, parentName):
        """ LayerFilterNewGroup(self: CommandPiper, filterName: str, parentName: str) """
        pass

    def LayerFilterNewProperty(self, filterName, filterExpression, parentName):
        """ LayerFilterNewProperty(self: CommandPiper, filterName: str, filterExpression: str, parentName: str) """
        pass

    def LayerFilterRename(self, value, filterName):
        """ LayerFilterRename(self: CommandPiper, value: str, filterName: str) """
        pass

    def LayerFilterSet(self, filterName):
        """ LayerFilterSet(self: CommandPiper, filterName: str) """
        pass

    def LayerFrozen(self, value, *__args):
        """ LayerFrozen(self: CommandPiper, value: bool, layerNames: ArrayList, layerIds: ObjectIdCollection)LayerFrozen(self: CommandPiper, value: bool, layerName: str, layerId: ObjectId) """
        pass

    def LayerLinetype(self, value, *__args):
        """ LayerLinetype(self: CommandPiper, value: str, layerNames: ArrayList)LayerLinetype(self: CommandPiper, value: str, layerName: str) """
        pass

    def LayerLineWeight(self, value, *__args):
        """ LayerLineWeight(self: CommandPiper, value: LineWeight, layerNames: ArrayList)LayerLineWeight(self: CommandPiper, value: LineWeight, layerName: str) """
        pass

    def LayerLocked(self, value, *__args):
        """ LayerLocked(self: CommandPiper, value: bool, layerNames: ArrayList)LayerLocked(self: CommandPiper, value: bool, layerName: str) """
        pass

    def LayerNew(self, layerName):
        """ LayerNew(self: CommandPiper, layerName: str) """
        pass

    def LayerOffCurrent(self, layerName):
        """ LayerOffCurrent(self: CommandPiper, layerName: str) """
        pass

    def LayerOn(self, value, *__args):
        """ LayerOn(self: CommandPiper, value: bool, layerNames: ArrayList)LayerOn(self: CommandPiper, value: bool, layerName: str) """
        pass

    def LayerPlot(self, value, *__args):
        """ LayerPlot(self: CommandPiper, value: bool, layerNames: ArrayList)LayerPlot(self: CommandPiper, value: bool, layerName: str) """
        pass

    def LayerPlotStyle(self, value, *__args):
        """ LayerPlotStyle(self: CommandPiper, value: str, layerNames: ArrayList)LayerPlotStyle(self: CommandPiper, value: str, layerName: str) """
        pass

    def LayerReconcile(self, *__args):
        """ LayerReconcile(self: CommandPiper, layerNames: ArrayList)LayerReconcile(self: CommandPiper, layerName: str) """
        pass

    def LayerRename(self, value, layerName):
        """ LayerRename(self: CommandPiper, value: str, layerName: str) """
        pass

    def LayerTemplate(self, protoName, layerName, showUsed, freezeInAllVPs):
        """ LayerTemplate(self: CommandPiper, protoName: str, layerName: str, showUsed: bool, freezeInAllVPs: bool) """
        pass

    def LayerTransparency(self, value, *__args):
        """ LayerTransparency(self: CommandPiper, value: str, layerNames: ArrayList)LayerTransparency(self: CommandPiper, value: str, layerName: str) """
        pass

    @staticmethod
    def OnCommandEnded():
        """ OnCommandEnded() -> bool """
        pass

    @staticmethod
    def QueueClear():
        """ QueueClear() """
        pass

    @staticmethod
    def QueueSend():
        """ QueueSend() """
        pass

    def Send(self):
        """ Send(self: CommandPiper) """
        pass

    @staticmethod
    def SkipUpdate():
        """ SkipUpdate() -> bool """
        pass

    def VplayerColor(self, value, all, *__args):
        """
        VplayerColor(self: CommandPiper, value: Color, all: bool, layerNames: ArrayList) -> bool
        VplayerColor(self: CommandPiper, value: Color, all: bool, layerName: str) -> bool
        """
        pass

    def VplayerFrozen(self, value, flag, *__args):
        """ VplayerFrozen(self: CommandPiper, value: bool, flag: VPType, layerNames: ArrayList, layerIds: ObjectIdCollection)VplayerFrozen(self: CommandPiper, value: bool, flag: VPType, layerName: str, layerId: ObjectId) """
        pass

    def VplayerLinetype(self, value, all, *__args):
        """ VplayerLinetype(self: CommandPiper, value: str, all: bool, layerNames: ArrayList)VplayerLinetype(self: CommandPiper, value: str, all: bool, layerName: str) """
        pass

    def VplayerLineWeight(self, value, all, *__args):
        """ VplayerLineWeight(self: CommandPiper, value: LineWeight, all: bool, layerNames: ArrayList)VplayerLineWeight(self: CommandPiper, value: LineWeight, all: bool, layerName: str) """
        pass

    def VplayerPlotStyle(self, value, all, *__args):
        """ VplayerPlotStyle(self: CommandPiper, value: str, all: bool, layerNames: ArrayList)VplayerPlotStyle(self: CommandPiper, value: str, all: bool, layerName: str) """
        pass

    def VplayerRemoveOverrides(self, theProperty, all, *__args):
        """ VplayerRemoveOverrides(self: CommandPiper, theProperty: str, all: bool, layerNames: ArrayList)VplayerRemoveOverrides(self: CommandPiper, theProperty: str, all: bool, layerName: str) """
        pass

    def VplayerReset(self, all, *__args):
        """ VplayerReset(self: CommandPiper, all: bool, layerNames: ArrayList)VplayerReset(self: CommandPiper, all: bool, layerName: str) """
        pass

    def VplayerTransparency(self, value, all, *__args):
        """ VplayerTransparency(self: CommandPiper, value: str, all: bool, layerNames: ArrayList)VplayerTransparency(self: CommandPiper, value: str, all: bool, layerName: str) """
        pass

    def VplayerViewportVisibilityDefault(self, bFrozen, all, *__args):
        """ VplayerViewportVisibilityDefault(self: CommandPiper, bFrozen: bool, all: bool, layerNames: ArrayList)VplayerViewportVisibilityDefault(self: CommandPiper, bFrozen: bool, all: bool, layerName: str) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, layerMgrCtrlId=None, bInRibbon=None):
        """
        __new__(cls: type, layerMgrCtrlId: int, bInRibbon: bool)
        __new__(cls: type)
        """
        pass

    BlockingCommands = 0
    LayerCount = 0
    QueueCount = 0
    VPType = None


class CommandTypeFlags(Enum):
    """ enum (flags) CommandTypeFlags, values: ActionMacroCmd (4), ARXCmd (2), CoreCmd (1), LispCmd (3), NoneCmd (0), SetvarCmd (5) """
    ActionMacroCmd = None
    ARXCmd = None
    CoreCmd = None
    LispCmd = None
    NoneCmd = None
    SetvarCmd = None
    value__ = None


class CoreLayerUtilities(object):
    # no doc
    @staticmethod
    def LayerNameCompareNatural(str1, str2):
        """ LayerNameCompareNatural(str1: str, str2: str) -> int """
        pass

    @staticmethod
    def RegenLayers(layers, regenPending, regenRequired=None):
        """ RegenLayers(layers: Array[ObjectId], regenPending: int, regenRequired: int)RegenLayers(layers: Array[ObjectId], regenPending: int) """
        pass

    RegenPending = 0


class CoreUtils(object):
    """ CoreUtils() """
    @staticmethod
    def AreFilesSame(file1, file2):
        """ AreFilesSame(file1: str, file2: str) -> bool """
        pass

    @staticmethod
    def GraphScr():
        """ GraphScr() """
        pass

    @staticmethod
    def SetUndoRequiresRegen(db):
        """ SetUndoRequiresRegen(db: Database) -> bool """
        pass

    @staticmethod
    def TextScr():
        """ TextScr() """
        pass

    @staticmethod
    def WcMatch(str, pattern):
        """ WcMatch(str: str, pattern: str) -> bool """
        pass


class CoreXRefUtils(object):
    """ CoreXRefUtils() """
    @staticmethod
    def getDelayResolveXRefRelativePaths():
        """ getDelayResolveXRefRelativePaths() -> Array[ObjectId] """
        pass

    @staticmethod
    def isMarkedForDelayXRefRelativePathResolve(defId):
        """ isMarkedForDelayXRefRelativePathResolve(defId: ObjectId) -> bool """
        pass

    @staticmethod
    def markForDelayXRefRelativePathResolve(defId):
        """ markForDelayXRefRelativePathResolve(defId: ObjectId) """
        pass

    @staticmethod
    def unmarkForDelayXRefRelativePathResolve(defId):
        """ unmarkForDelayXRefRelativePathResolve(defId: ObjectId) """
        pass


class COwnerDrawComboBoxWrapper(ComboBox):
    # no doc
    def Dispose(self):
        """ Dispose(self: COwnerDrawComboBoxWrapper, A_0: bool) """
        pass

    def raise_DrawItem(self, *args): #cannot find CLR method
        """ raise_DrawItem(self: COwnerDrawComboBoxWrapper, value0: object, value1: DrawItemEventArgs) """
        pass

    def raise_MeasureItem(self, *args): #cannot find CLR method
        """ raise_MeasureItem(self: COwnerDrawComboBoxWrapper, value0: object, value1: MeasureItemEventArgs) """
        pass

    def Select(self, start=None, length=None):
        """ Select(self: Control, directed: bool, forward: bool) """
        pass

    AllowSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CanEnableIme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CreateParams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DataManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultCursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultImeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMargin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMaximumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMinimumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultPadding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DoubleBuffered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    FontHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ImeModeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    RenderRightToLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ResizeRedraw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ScaleChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShowFocusCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShowKeyboardCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DrawItem = None
    MeasureItem = None


class CustomizationUtilities(object):
    # no doc
    @staticmethod
    def SetCustomizationInterface(customization):
        """ SetCustomizationInterface(customization: object) """
        pass


class DebugUtil(object):
    """ DebugUtil() """
    @staticmethod
    def Assert(condition, message=None, detailMessage=None):
        """ Assert(condition: bool)Assert(condition: bool, message: str)Assert(condition: bool, message: str, detailMessage: str) """
        pass

    @staticmethod
    def Verify(b, t=None):
        """
        Verify(b: bool) -> bool
        Verify(b: bool, t: str) -> bool
        """
        pass


class DocumentWindowUtil(object):
    """ DocumentWindowUtil() """
    @staticmethod
    def CanClose(docWindow):
        """ CanClose(docWindow: DocumentWindow) -> bool """
        pass

    @staticmethod
    def SetNextActiveWindow(docWindow):
        """ SetNextActiveWindow(docWindow: DocumentWindow) """
        pass


class DxLegacyBinaryTemplate(object):
    """ DxLegacyBinaryTemplate() """
    def LoadFromFile(self, filename):
        """ LoadFromFile(self: DxLegacyBinaryTemplate, filename: str) """
        pass

    AttributeList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AttributeList(self: DxLegacyBinaryTemplate) -> ArrayList

"""

    BlockList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BlockList(self: DxLegacyBinaryTemplate) -> ArrayList

"""



class ExternalBlockListResultHost(object):
    """ ExternalBlockListResultHost() """
    def getBlockDataSource(self):
        """ getBlockDataSource(self: ExternalBlockListResultHost) -> ObservableCollection[BlockDisplayItem] """
        pass

    def getBlockListRequestFileInfo(self):
        """ getBlockListRequestFileInfo(self: ExternalBlockListResultHost) -> str """
        pass

    def getBlocksFromExternalFile(self, fullPathName):
        """ getBlocksFromExternalFile(self: ExternalBlockListResultHost, fullPathName: str) -> ObservableCollection[BlockDisplayItem] """
        pass

    def parseJsonBlockList(self, resultJsonStr, viewMode):
        """ parseJsonBlockList(self: ExternalBlockListResultHost, resultJsonStr: str, viewMode: BlockViewMode) -> bool """
        pass

    def setBlockDataSource(self, dataSource):
        """ setBlockDataSource(self: ExternalBlockListResultHost, dataSource: ObservableCollection[BlockDisplayItem]) """
        pass


class FocusChangedEventHandler(MulticastDelegate):
    """ FocusChangedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, callback, obj):
        """ BeginInvoke(self: FocusChangedEventHandler, sender: GroupControl, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FocusChangedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender):
        """ Invoke(self: FocusChangedEventHandler, sender: GroupControl) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class GetSharedRecentFilesCallback(MulticastDelegate):
    """ GetSharedRecentFilesCallback(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, data, nItems, callback, obj):
        """ BeginInvoke(self: GetSharedRecentFilesCallback, data: List[SharedRecentFileData], nItems: int, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: GetSharedRecentFilesCallback, result: IAsyncResult) """
        pass

    def Invoke(self, data, nItems):
        """ Invoke(self: GetSharedRecentFilesCallback, data: List[SharedRecentFileData], nItems: int) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class GetTheAnswerDelegate(MulticastDelegate):
    """ GetTheAnswerDelegate(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, pngFilePath, previewTaskInfo, callback, obj):
        """ BeginInvoke(self: GetTheAnswerDelegate, pngFilePath: AcString*, previewTaskInfo: AcBlockPreviewInfo*, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: GetTheAnswerDelegate, result: IAsyncResult) """
        pass

    def Invoke(self, pngFilePath, previewTaskInfo):
        """ Invoke(self: GetTheAnswerDelegate, pngFilePath: AcString*, previewTaskInfo: AcBlockPreviewInfo*) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class GroupControl(Control):
    """ GroupControl() """
    def AddStyle(self, styleAdd):
        """ AddStyle(self: GroupControl, styleAdd: GroupControlStyles) """
        pass

    def AddTitleButton(self, button):
        """ AddTitleButton(self: GroupControl, button: GroupControlHeaderButton) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: GroupControl, A_0: bool) """
        pass

    def OnUpdateTitleBar(self, *args): #cannot find CLR method
        """ OnUpdateTitleBar(self: GroupControl) """
        pass

    def RemoveBitmap(self, button):
        """ RemoveBitmap(self: GroupControl, button: GroupControlHeaderButton) -> bool """
        pass

    def RemoveStyle(self, styleRemove):
        """ RemoveStyle(self: GroupControl, styleRemove: GroupControlStyles) """
        pass

    def Select(self):
        """ Select(self: Control, directed: bool, forward: bool) """
        pass

    def SetActive(self, bActive):
        """ SetActive(self: GroupControl, bActive: bool) """
        pass

    def SetHeight(self):
        """ SetHeight(self: GroupControl) """
        pass

    CanEnableIme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CreateParams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultCursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultImeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMargin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMaximumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMinimumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultPadding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DoubleBuffered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    FontHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    HeaderHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeaderHeight(self: GroupControl) -> int

Set: HeaderHeight(self: GroupControl) = value
"""

    Hidden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Hidden(self: GroupControl) -> bool

Set: Hidden(self: GroupControl) = value
"""

    ImeModeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Minimized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Minimized(self: GroupControl) -> bool

Set: Minimized(self: GroupControl) = value
"""

    RenderRightToLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ResizeRedraw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    RestoredHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RestoredHeight(self: GroupControl) -> int

Set: RestoredHeight(self: GroupControl) = value
"""

    ScaleChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShowFocusCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShowKeyboardCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Title(self: GroupControl) -> str

Set: Title(self: GroupControl) = value
"""

    UseDialogTheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseDialogTheme(self: GroupControl) -> bool

Set: UseDialogTheme(self: GroupControl) = value
"""


    FocusChanged = None
    HiddenChanged = None
    Resize = None


class GroupControlEventHandler(MulticastDelegate):
    """ GroupControlEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: GroupControlEventHandler, sender: object, e: EventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: GroupControlEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: GroupControlEventHandler, sender: object, e: EventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class GroupControlEventIndex(Enum):
    """ enum (flags) GroupControlEventIndex, values: ChevronClick (2), FocusChange (4), Hide (1), Resize (5), Show (0), TitleButtonClick (3) """
    ChevronClick = None
    FocusChange = None
    Hide = None
    Resize = None
    Show = None
    TitleButtonClick = None
    value__ = None


class GroupControlHeaderButton(object):
    """
    GroupControlHeaderButton(bmp: Bitmap, tooltip: str)
    GroupControlHeaderButton()
    """
    def Dispose(self):
        """ Dispose(self: GroupControlHeaderButton) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, bmp=None, tooltip=None):
        """
        __new__(cls: type, bmp: Bitmap, tooltip: str)
        __new__(cls: type)
        """
        pass

    Bitmap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bitmap(self: GroupControlHeaderButton) -> Bitmap

Set: Bitmap(self: GroupControlHeaderButton) = value
"""

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Enabled(self: GroupControlHeaderButton) -> bool

Set: Enabled(self: GroupControlHeaderButton) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: GroupControlHeaderButton) -> GroupControl

"""

    ToolTip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToolTip(self: GroupControlHeaderButton) -> str

Set: ToolTip(self: GroupControlHeaderButton) = value
"""


    Click = None


class GroupControlStyles(Enum):
    """ enum (flags) GroupControlStyles, values: ShowButtonBorder (32), ShowButtonForce (2), ShowChevron (1), ShowNoBorder (8), ShowNonActive (4), ShowOpaqueImage (128), ShowTransparentButton (16) """
    ShowButtonBorder = None
    ShowButtonForce = None
    ShowChevron = None
    ShowNoBorder = None
    ShowNonActive = None
    ShowOpaqueImage = None
    ShowTransparentButton = None
    value__ = None


class GroupResizedEventHandler(MulticastDelegate):
    """ GroupResizedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, callback, obj):
        """ BeginInvoke(self: GroupResizedEventHandler, sender: GroupControl, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: GroupResizedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender):
        """ Invoke(self: GroupResizedEventHandler, sender: GroupControl) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class HiddenChangedEventHandler(MulticastDelegate):
    """ HiddenChangedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, bHidden, callback, obj):
        """ BeginInvoke(self: HiddenChangedEventHandler, sender: GroupControl, bHidden: bool, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: HiddenChangedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, bHidden):
        """ Invoke(self: HiddenChangedEventHandler, sender: GroupControl, bHidden: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class HPPrinter(object):
    """ HPPrinter() """
    HPUserId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HPUserId(self: HPPrinter) -> str

Set: HPUserId(self: HPPrinter) = value
"""

    PrinterId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrinterId(self: HPPrinter) -> str

Set: PrinterId(self: HPPrinter) = value
"""

    PrinterName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrinterName(self: HPPrinter) -> str

Set: PrinterName(self: HPPrinter) = value
"""

    WSUserId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WSUserId(self: HPPrinter) -> str

Set: WSUserId(self: HPPrinter) = value
"""



class HPPrinterPlotOption(object):
    """ HPPrinterPlotOption() """
    Copies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Copies(self: HPPrinterPlotOption) -> int

Set: Copies(self: HPPrinterPlotOption) = value
"""

    Quality = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Quality(self: HPPrinterPlotOption) -> HPPrinterPlotQuality

Set: Quality(self: HPPrinterPlotOption) = value
"""



class HPPrinterPlotQuality(Enum):
    """ enum HPPrinterPlotQuality, values: Best (2), Fast (1), Normal (0) """
    Best = None
    Fast = None
    Normal = None
    value__ = None


class HPPrinterPlotResult(object):
    """ HPPrinterPlotResult() """
    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: HPPrinterPlotResult) -> str

Set: Code(self: HPPrinterPlotResult) = value
"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: HPPrinterPlotResult) -> str

Set: Message(self: HPPrinterPlotResult) = value
"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: HPPrinterPlotResult) -> int

Set: Status(self: HPPrinterPlotResult) = value
"""



class HttpMethod(Enum):
    """ enum HttpMethod, values: Delete (4), Get (0), Head (2), Post (1), Put (3) """
    Delete = None
    Get = None
    Head = None
    Post = None
    Put = None
    value__ = None


class ICloudPrintingService:
    # no doc
    def ListHPPrinters(self):
        """ ListHPPrinters(self: ICloudPrintingService) -> Array[HPPrinter] """
        pass

    def PlotHPPrinter(self, pdfFilePath, printer, option):
        """ PlotHPPrinter(self: ICloudPrintingService, pdfFilePath: str, printer: HPPrinter, option: HPPrinterPlotOption) -> HPPrinterPlotResult """
        pass

    def ShowHPUserLoginDialog(self):
        """ ShowHPUserLoginDialog(self: ICloudPrintingService) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IPreviewContext:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: IPreviewContext) -> str

Set: Description(self: IPreviewContext) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: IPreviewContext) -> str

Set: Name(self: IPreviewContext) = value
"""



class ILivePreviewControl(IPreviewContext):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ControlType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ControlType(self: ILivePreviewControl) -> PreviewControlType

Set: ControlType(self: ILivePreviewControl) = value
"""

    PreviewDelay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreviewDelay(self: ILivePreviewControl) -> Int16

Set: PreviewDelay(self: ILivePreviewControl) = value
"""

    Rule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rule(self: ILivePreviewControl) -> str

Set: Rule(self: ILivePreviewControl) = value
"""



class ILivePreviewRule:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsPreviewAble = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPreviewAble(self: ILivePreviewRule) -> bool

"""



class INavisworksFileProtocol:
    # no doc
    def CloseFile(self, filehandle):
        """ CloseFile(self: INavisworksFileProtocol, filehandle: IntPtr) """
        pass

    def GetAggregateInfo(self, filename, aggregateJson):
        """ GetAggregateInfo(self: INavisworksFileProtocol, filename: str, aggregateJson: str) -> (NavisworksFileType, str) """
        pass

    def GetFileInfo(self, filename):
        """ GetFileInfo(self: INavisworksFileProtocol, filename: str) -> NavisworksFileInfo """
        pass

    def OpenFile(self, filename):
        """ OpenFile(self: INavisworksFileProtocol, filename: str) -> IntPtr """
        pass

    def ReadFile(self, filehandle, offset, numbytes, bytes):
        """ ReadFile(self: INavisworksFileProtocol, filehandle: IntPtr, offset: UInt64, numbytes: UInt64, bytes: Array[Byte]) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class INavisworksService:
    # no doc
    def RegisterFileProtocol(self, scheme, fileprotocol):
        """ RegisterFileProtocol(self: INavisworksService, scheme: str, fileprotocol: INavisworksFileProtocol) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IPECallbackType(Enum):
    """ enum IPECallbackType, values: IPECallbackCreateToolbar (4), IPECallbackCreateUI (2), IPECallbackEnableUI (1), IPECallbackRemoveToolbar (5), IPECallbackRemoveUI (3), IPECallbackUpdateUI (0) """
    IPECallbackCreateToolbar = None
    IPECallbackCreateUI = None
    IPECallbackEnableUI = None
    IPECallbackRemoveToolbar = None
    IPECallbackRemoveUI = None
    IPECallbackUpdateUI = None
    value__ = None


class IPECharFlags(Enum):
    """ enum IPECharFlags, values: BoldFlag (1), ColorFlag (64), FlowAlignFlag (2048), FontFlag (16), HeightFlag (32), ItalicFlag (2), LanguageFlag (128), ObliqueAngleFlag (256), OverlineFlag (8), TrackingFactorFlag (1024), UnderlineFlag (4), WidthScaleFlag (512) """
    BoldFlag = None
    ColorFlag = None
    FlowAlignFlag = None
    FontFlag = None
    HeightFlag = None
    ItalicFlag = None
    LanguageFlag = None
    ObliqueAngleFlag = None
    OverlineFlag = None
    TrackingFactorFlag = None
    UnderlineFlag = None
    value__ = None
    WidthScaleFlag = None


class IPECharFlowType(Enum):
    """ enum IPECharFlowType, values: FlowBase (0), FlowCenter (1), FlowTop (2) """
    FlowBase = None
    FlowCenter = None
    FlowTop = None
    value__ = None


class IPECharStateWrapper(DisposableWrapper):
    """ IPECharStateWrapper() """
    def Clone(self):
        """ Clone(self: IPECharStateWrapper) -> object """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    Bold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bold(self: IPECharStateWrapper) -> bool

Set: Bold(self: IPECharStateWrapper) = value
"""

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: IPECharStateWrapper) -> Color

Set: Color(self: IPECharStateWrapper) = value
"""

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Flags(self: IPECharStateWrapper) -> IPECharFlags

Set: Flags(self: IPECharStateWrapper) = value
"""

    FlowAlign = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlowAlign(self: IPECharStateWrapper) -> IPECharFlowType

Set: FlowAlign(self: IPECharStateWrapper) = value
"""

    FontName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FontName(self: IPECharStateWrapper) -> str

Set: FontName(self: IPECharStateWrapper) = value
"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: IPECharStateWrapper) -> float

Set: Height(self: IPECharStateWrapper) = value
"""

    Italic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Italic(self: IPECharStateWrapper) -> bool

Set: Italic(self: IPECharStateWrapper) = value
"""

    Language = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Language(self: IPECharStateWrapper) -> int

Set: Language(self: IPECharStateWrapper) = value
"""

    ObliqueAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObliqueAngle(self: IPECharStateWrapper) -> float

Set: ObliqueAngle(self: IPECharStateWrapper) = value
"""

    Overline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Overline(self: IPECharStateWrapper) -> bool

Set: Overline(self: IPECharStateWrapper) = value
"""

    TrackingFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TrackingFactor(self: IPECharStateWrapper) -> float

Set: TrackingFactor(self: IPECharStateWrapper) = value
"""

    TrueType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TrueType(self: IPECharStateWrapper) -> bool

Set: TrueType(self: IPECharStateWrapper) = value
"""

    Underline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Underline(self: IPECharStateWrapper) -> bool

Set: Underline(self: IPECharStateWrapper) = value
"""

    WidthScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WidthScale(self: IPECharStateWrapper) -> float

Set: WidthScale(self: IPECharStateWrapper) = value
"""



class IPEColumnCommandType(Enum):
    """ enum IPEColumnCommandType, values: IPEColumnSettingsCommand (5), IPEDynamicColumnsCommand (2), IPEInsertColumnBreakCommand (4), IPEMoreStaticColumnsCommand (3), IPENoColumnsCommand (0), IPEStaticColumnsCommand (1) """
    IPEColumnSettingsCommand = None
    IPEDynamicColumnsCommand = None
    IPEInsertColumnBreakCommand = None
    IPEMoreStaticColumnsCommand = None
    IPENoColumnsCommand = None
    IPEStaticColumnsCommand = None
    value__ = None


class IPECommands(Enum):
    """ enum IPECommands, values: IPEAttachmentMenuCmd (22), IPEChangeCaseCmd (29), IPECloseCmd (6), IPEColumnsMenuCmd (21), IPEContextMenuCmd (8), IPEFieldDialogCmd (27), IPEHandleColumnsCmd (40), IPEHandleJustificationCmd (41), IPEHandleLineSpacingCmd (42), IPEHandleNumberingCmd (44), IPEHandleOptionsCmd (45), IPEHandleSymbolCmd (43), IPEInsertCustomStringCmd (38), IPEInsertMTextCmd (31), IPELineSpacingMenuCmd (23), IPENumberingMenuCmd (24), IPEParagraphDialogCmd (26), IPERedoCmd (4), IPEReinstateEditorCmd (2), IPERemoveCustomStringCmd (39), IPEReplaceContentsCmd (30), IPESetColorCmd (13), IPESetCustomStringCmd (37), IPESetFontCmd (10), IPESetLayerCmd (46), IPESetObliqueAngleCmd (18), IPESetParagraphAlignmentCmd (28), IPESetStyleCmd (9), IPESetTextHeightCmd (12), IPESetTrackingFactorCmd (19), IPESetWidthScaleCmd (20), IPEStackCmd (5), IPESuspendEditorCmd (1), IPESymbolMenuCmd (25), IPEToggleAnnotativeCmd (11), IPEToggleBoldCmd (14), IPEToggleDimAlternateCmd (33), IPEToggleDimParenthesesCmd (35), IPEToggleDimPrimaryCmd (32), IPEToggleDimUnderlineCmd (34), IPEToggleItalicCmd (15), IPEToggleOverlineCmd (17), IPEToggleRulerCmd (7), IPEToggleUnderlineCmd (16), IPETweakDimensionCmd (36), IPEUndoCmd (3), IPEUnknownCmd (0) """
    IPEAttachmentMenuCmd = None
    IPEChangeCaseCmd = None
    IPECloseCmd = None
    IPEColumnsMenuCmd = None
    IPEContextMenuCmd = None
    IPEFieldDialogCmd = None
    IPEHandleColumnsCmd = None
    IPEHandleJustificationCmd = None
    IPEHandleLineSpacingCmd = None
    IPEHandleNumberingCmd = None
    IPEHandleOptionsCmd = None
    IPEHandleSymbolCmd = None
    IPEInsertCustomStringCmd = None
    IPEInsertMTextCmd = None
    IPELineSpacingMenuCmd = None
    IPENumberingMenuCmd = None
    IPEParagraphDialogCmd = None
    IPERedoCmd = None
    IPEReinstateEditorCmd = None
    IPERemoveCustomStringCmd = None
    IPEReplaceContentsCmd = None
    IPESetColorCmd = None
    IPESetCustomStringCmd = None
    IPESetFontCmd = None
    IPESetLayerCmd = None
    IPESetObliqueAngleCmd = None
    IPESetParagraphAlignmentCmd = None
    IPESetStyleCmd = None
    IPESetTextHeightCmd = None
    IPESetTrackingFactorCmd = None
    IPESetWidthScaleCmd = None
    IPEStackCmd = None
    IPESuspendEditorCmd = None
    IPESymbolMenuCmd = None
    IPEToggleAnnotativeCmd = None
    IPEToggleBoldCmd = None
    IPEToggleDimAlternateCmd = None
    IPEToggleDimParenthesesCmd = None
    IPEToggleDimPrimaryCmd = None
    IPEToggleDimUnderlineCmd = None
    IPEToggleItalicCmd = None
    IPEToggleOverlineCmd = None
    IPEToggleRulerCmd = None
    IPEToggleUnderlineCmd = None
    IPETweakDimensionCmd = None
    IPEUndoCmd = None
    IPEUnknownCmd = None
    value__ = None


class IPEConstants(object):
    """ IPEConstants() """
    IPEAcctachmentInfo = None
    IPECharsetInfo = None
    IPEColumnAutoHeightInfo = None
    IPEColumnCounts = None
    IPEColumnTypeInfo = None
    IPELineSpacingMultiples = None
    IPEParaAlignmentInfo = None
    IPESymbolInfo = None


class IPEControlIconType(Enum):
    """ enum IPEControlIconType, values: IPEBoldButtonIcon (0), IPEItalicButtonIcon (1), IPEObliqueAngleSpinnerIcon (4), IPEOverlineButtonIcon (2), IPEUnderlineButtonIcon (3) """
    IPEBoldButtonIcon = None
    IPEItalicButtonIcon = None
    IPEObliqueAngleSpinnerIcon = None
    IPEOverlineButtonIcon = None
    IPEUnderlineButtonIcon = None
    value__ = None


class IPEDimensionStateWrapper(DisposableWrapper):
    """ IPEDimensionStateWrapper() """
    def Clone(self):
        """ Clone(self: IPEDimensionStateWrapper) -> object """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    AlternateFound = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlternateFound(self: IPEDimensionStateWrapper) -> bool

Set: AlternateFound(self: IPEDimensionStateWrapper) = value
"""

    Dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dimension(self: IPEDimensionStateWrapper) -> Dimension

Set: Dimension(self: IPEDimensionStateWrapper) = value
"""

    EnclosedWithParentheses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnclosedWithParentheses(self: IPEDimensionStateWrapper) -> bool

Set: EnclosedWithParentheses(self: IPEDimensionStateWrapper) = value
"""

    EverythingUnderlined = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EverythingUnderlined(self: IPEDimensionStateWrapper) -> bool

Set: EverythingUnderlined(self: IPEDimensionStateWrapper) = value
"""

    PrimaryFound = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrimaryFound(self: IPEDimensionStateWrapper) -> bool

Set: PrimaryFound(self: IPEDimensionStateWrapper) = value
"""



class IPEExitType(Enum):
    """ enum IPEExitType, values: ExitQuit (0), ExitSave (1), ExitSaveAndGoAbove (5), ExitSaveAndGoBelow (4), ExitSaveAndGoLeft (3), ExitSaveAndGoRight (2) """
    ExitQuit = None
    ExitSave = None
    ExitSaveAndGoAbove = None
    ExitSaveAndGoBelow = None
    ExitSaveAndGoLeft = None
    ExitSaveAndGoRight = None
    value__ = None


class IPELineSpacingCommandType(Enum):
    """ enum IPELineSpacingCommandType, values: IPEClearLineSpaceCommand (2), IPEMoreLineSpaceCommand (1), IPEMultiLineSpaceCommand (0) """
    IPEClearLineSpaceCommand = None
    IPEMoreLineSpaceCommand = None
    IPEMultiLineSpaceCommand = None
    value__ = None


class IPELineSpacingStyle(Enum):
    """ enum IPELineSpacingStyle, values: LineSpacingAtLeast (2), LineSpacingDefault (0), LineSpacingExactly (1), LineSpacingMultiple (3), NumLineSpacingStyles (4) """
    LineSpacingAtLeast = None
    LineSpacingDefault = None
    LineSpacingExactly = None
    LineSpacingMultiple = None
    NumLineSpacingStyles = None
    value__ = None


class IPENumberingCommandType(Enum):
    """ enum IPENumberingCommandType, values: IPENumberingAutoListCommand (7), IPENumberingBulletCommand (1), IPENumberingContinueCommand (6), IPENumberingEnabledCommand (9), IPENumberingLetterLowCaseCommand (2), IPENumberingLetterUpperCaseCommand (3), IPENumberingNumberedCommand (4), IPENumberingOffCommand (0), IPENumberingRestartCommand (5), IPENumberingTabOnlyDelimiterCommand (8) """
    IPENumberingAutoListCommand = None
    IPENumberingBulletCommand = None
    IPENumberingContinueCommand = None
    IPENumberingEnabledCommand = None
    IPENumberingLetterLowCaseCommand = None
    IPENumberingLetterUpperCaseCommand = None
    IPENumberingNumberedCommand = None
    IPENumberingOffCommand = None
    IPENumberingRestartCommand = None
    IPENumberingTabOnlyDelimiterCommand = None
    value__ = None


class IPENumberingType(Enum):
    """ enum IPENumberingType, values: NumberingBullet (1), NumberingLetterLower (3), NumberingLetterUpper (4), NumberingNumber (2), NumberingNumTypes (5), NumberingOff (0) """
    NumberingBullet = None
    NumberingLetterLower = None
    NumberingLetterUpper = None
    NumberingNumber = None
    NumberingNumTypes = None
    NumberingOff = None
    value__ = None


class IPEOptionsCommandType(Enum):
    """ enum IPEOptionsCommandType, values: IPEAutoCAPSCommand (14), IPEBackgroundMaskCommand (19), IPECharaterSetCommand (32), IPECheckSpellingCommand (25), IPECheckSpellingSettingsCommand (26), IPECombineParagraphsCommand (15), IPEConvertCustomCommand (5), IPEConvertFieldCommand (3), IPEDictionariesCommand (27), IPEEditFieldCommand (1), IPEFindReplaceCommand (11), IPEHelpCommand (30), IPEImportTextCommand (4), IPEInsertFieldCommand (0), IPELowerCaseCommand (13), IPENewFeaturesCommand (29), IPEOpaqueBackgroundCommand (9), IPEParagraphAlignCommand (31), IPEParagraphCommand (10), IPERemoveAllFormattingCommand (18), IPERemoveCharaterFormattingCommand (16), IPERemoveParagraphFormattingCommand (17), IPEShowOptionsCommand (22), IPEShowRibbonCommand (24), IPEShowRulerCommand (23), IPEShowToolbarCommand (21), IPEStackCommand (6), IPEStackPropertyCommand (8), IPETextHeightlightColorCommand (28), IPEUnstackCommand (7), IPEUpdateFieldCommand (2), IPEUpperCaseCommand (12), IPEWYSIWYGCommand (20) """
    IPEAutoCAPSCommand = None
    IPEBackgroundMaskCommand = None
    IPECharaterSetCommand = None
    IPECheckSpellingCommand = None
    IPECheckSpellingSettingsCommand = None
    IPECombineParagraphsCommand = None
    IPEConvertCustomCommand = None
    IPEConvertFieldCommand = None
    IPEDictionariesCommand = None
    IPEEditFieldCommand = None
    IPEFindReplaceCommand = None
    IPEHelpCommand = None
    IPEImportTextCommand = None
    IPEInsertFieldCommand = None
    IPELowerCaseCommand = None
    IPENewFeaturesCommand = None
    IPEOpaqueBackgroundCommand = None
    IPEParagraphAlignCommand = None
    IPEParagraphCommand = None
    IPERemoveAllFormattingCommand = None
    IPERemoveCharaterFormattingCommand = None
    IPERemoveParagraphFormattingCommand = None
    IPEShowOptionsCommand = None
    IPEShowRibbonCommand = None
    IPEShowRulerCommand = None
    IPEShowToolbarCommand = None
    IPEStackCommand = None
    IPEStackPropertyCommand = None
    IPETextHeightlightColorCommand = None
    IPEUnstackCommand = None
    IPEUpdateFieldCommand = None
    IPEUpperCaseCommand = None
    IPEWYSIWYGCommand = None
    value__ = None


class IPEParagraphAlignmentType(Enum):
    """ enum IPEParagraphAlignmentType, values: AlignmentCenter (2), AlignmentDefault (0), AlignmentDistribute (5), AlignmentJustify (4), AlignmentLeft (1), AlignmentRight (3), NumAlignmentTypes (6) """
    AlignmentCenter = None
    AlignmentDefault = None
    AlignmentDistribute = None
    AlignmentJustify = None
    AlignmentLeft = None
    AlignmentRight = None
    NumAlignmentTypes = None
    value__ = None


class IPEParagraphFlags(Enum):
    """ enum IPEParagraphFlags, values: AlignmentFlag (64), FirstIndentFlag (1), LeftIndentFlag (2), LineSpacingFlag (32), NumberingFlag (128), RightIndentFlag (4), SpaceAfterFlag (16), SpaceBeforeFlag (8) """
    AlignmentFlag = None
    FirstIndentFlag = None
    LeftIndentFlag = None
    LineSpacingFlag = None
    NumberingFlag = None
    RightIndentFlag = None
    SpaceAfterFlag = None
    SpaceBeforeFlag = None
    value__ = None


class IPEParagraphStateWrapper(DisposableWrapper):
    """ IPEParagraphStateWrapper() """
    def Clone(self):
        """ Clone(self: IPEParagraphStateWrapper) -> object """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    Alignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Alignment(self: IPEParagraphStateWrapper) -> IPEParagraphAlignmentType

Set: Alignment(self: IPEParagraphStateWrapper) = value
"""

    AutoListEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoListEnabled(self: IPEParagraphStateWrapper) -> bool

"""

    FirstIndent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FirstIndent(self: IPEParagraphStateWrapper) -> float

Set: FirstIndent(self: IPEParagraphStateWrapper) = value
"""

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Flags(self: IPEParagraphStateWrapper) -> IPEParagraphFlags

Set: Flags(self: IPEParagraphStateWrapper) = value
"""

    LeftIndent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeftIndent(self: IPEParagraphStateWrapper) -> float

Set: LeftIndent(self: IPEParagraphStateWrapper) = value
"""

    LineSpacingFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineSpacingFactor(self: IPEParagraphStateWrapper) -> float

Set: LineSpacingFactor(self: IPEParagraphStateWrapper) = value
"""

    LineSpacingStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineSpacingStyle(self: IPEParagraphStateWrapper) -> IPELineSpacingStyle

Set: LineSpacingStyle(self: IPEParagraphStateWrapper) = value
"""

    NumberingType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberingType(self: IPEParagraphStateWrapper) -> IPENumberingType

Set: NumberingType(self: IPEParagraphStateWrapper) = value
"""

    RightIndent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RightIndent(self: IPEParagraphStateWrapper) -> float

Set: RightIndent(self: IPEParagraphStateWrapper) = value
"""

    SpaceAfter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpaceAfter(self: IPEParagraphStateWrapper) -> float

Set: SpaceAfter(self: IPEParagraphStateWrapper) = value
"""

    SpaceBefore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpaceBefore(self: IPEParagraphStateWrapper) -> float

Set: SpaceBefore(self: IPEParagraphStateWrapper) = value
"""

    TabOnlyDelimitedEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TabOnlyDelimitedEnabled(self: IPEParagraphStateWrapper) -> bool

"""



class IPESettingsWrapper(DisposableWrapper):
    """ IPESettingsWrapper() """
    def Clone(self):
        """ Clone(self: IPESettingsWrapper) -> object """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    AllowTabs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowTabs(self: IPESettingsWrapper) -> bool

Set: AllowTabs(self: IPESettingsWrapper) = value
"""

    AuthoringEntity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AuthoringEntity(self: IPESettingsWrapper) -> bool

Set: AuthoringEntity(self: IPESettingsWrapper) = value
"""

    DefinedHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefinedHeight(self: IPESettingsWrapper) -> float

Set: DefinedHeight(self: IPESettingsWrapper) = value
"""

    Dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dimension(self: IPESettingsWrapper) -> bool

Set: Dimension(self: IPESettingsWrapper) = value
"""

    DimensionObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DimensionObject(self: IPESettingsWrapper) -> Dimension

Set: DimensionObject(self: IPESettingsWrapper) = value
"""

    DimensionScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DimensionScale(self: IPESettingsWrapper) -> float

Set: DimensionScale(self: IPESettingsWrapper) = value
"""

    EditFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EditFlags(self: IPESettingsWrapper) -> int

Set: EditFlags(self: IPESettingsWrapper) = value
"""

    HorizontalMargin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HorizontalMargin(self: IPESettingsWrapper) -> float

Set: HorizontalMargin(self: IPESettingsWrapper) = value
"""

    InputString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InputString(self: IPESettingsWrapper) -> str

Set: InputString(self: IPESettingsWrapper) = value
"""

    MultilineAttribute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MultilineAttribute(self: IPESettingsWrapper) -> bool

Set: MultilineAttribute(self: IPESettingsWrapper) = value
"""

    RotateForFont = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RotateForFont(self: IPESettingsWrapper) -> bool

Set: RotateForFont(self: IPESettingsWrapper) = value
"""

    SimpleMText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SimpleMText(self: IPESettingsWrapper) -> bool

Set: SimpleMText(self: IPESettingsWrapper) = value
"""

    TableCell = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TableCell(self: IPESettingsWrapper) -> bool

Set: TableCell(self: IPESettingsWrapper) = value
"""

    TableId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TableId(self: IPESettingsWrapper) -> ObjectId

Set: TableId(self: IPESettingsWrapper) = value
"""

    ToolbarRectangle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToolbarRectangle(self: IPESettingsWrapper) -> ValueType

Set: ToolbarRectangle(self: IPESettingsWrapper) = value
"""

    VerticalMargin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VerticalMargin(self: IPESettingsWrapper) -> float

Set: VerticalMargin(self: IPESettingsWrapper) = value
"""



class IPEStateWrapper(DisposableWrapper):
    """ IPEStateWrapper() """
    def Clone(self):
        """ Clone(self: IPEStateWrapper) -> object """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    Annotative = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Annotative(self: IPEStateWrapper) -> bool

Set: Annotative(self: IPEStateWrapper) = value
"""

    AnnotativeAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnnotativeAvailable(self: IPEStateWrapper) -> bool

Set: AnnotativeAvailable(self: IPEStateWrapper) = value
"""

    AutoCapsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCapsEnabled(self: IPEStateWrapper) -> bool

"""

    AutoHeightColumns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoHeightColumns(self: IPEStateWrapper) -> bool

"""

    ChangeCaseAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChangeCaseAvailable(self: IPEStateWrapper) -> bool

Set: ChangeCaseAvailable(self: IPEStateWrapper) = value
"""

    CharState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CharState(self: IPEStateWrapper) -> IPECharStateWrapper

Set: CharState(self: IPEStateWrapper) = value
"""

    ColumnsAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColumnsAvailable(self: IPEStateWrapper) -> bool

Set: ColumnsAvailable(self: IPEStateWrapper) = value
"""

    CopyAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CopyAvailable(self: IPEStateWrapper) -> bool

Set: CopyAvailable(self: IPEStateWrapper) = value
"""

    DefinedWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefinedWidth(self: IPEStateWrapper) -> float

"""

    Dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dimension(self: IPEStateWrapper) -> bool

"""

    DimensionState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DimensionState(self: IPEStateWrapper) -> IPEDimensionStateWrapper

Set: DimensionState(self: IPEStateWrapper) = value
"""

    EmptySelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EmptySelection(self: IPEStateWrapper) -> bool

"""

    FieldsAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FieldsAvailable(self: IPEStateWrapper) -> bool

Set: FieldsAvailable(self: IPEStateWrapper) = value
"""

    ForceOpaqueBackground = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ForceOpaqueBackground(self: IPEStateWrapper) -> bool

"""

    HideOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HideOptions(self: IPEStateWrapper) -> bool

"""

    HideToolbar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HideToolbar(self: IPEStateWrapper) -> bool

"""

    IPEColumnType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IPEColumnType(self: IPEStateWrapper) -> ColumnType

"""

    IsAuthoringEntity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAuthoringEntity(self: IPEStateWrapper) -> bool

"""

    IsDText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDText(self: IPEStateWrapper) -> bool

"""

    IsSimpleMText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSimpleMText(self: IPEStateWrapper) -> bool

"""

    Justification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Justification(self: IPEStateWrapper) -> AttachmentPoint

"""

    LanguageIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LanguageIndex(self: IPEStateWrapper) -> int

"""

    LayerColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayerColor(self: IPEStateWrapper) -> Color

"""

    MLeader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MLeader(self: IPEStateWrapper) -> bool

"""

    MTextFixed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MTextFixed(self: IPEStateWrapper) -> int

"""

    NumberingAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberingAvailable(self: IPEStateWrapper) -> bool

Set: NumberingAvailable(self: IPEStateWrapper) = value
"""

    OpaqueBackground = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OpaqueBackground(self: IPEStateWrapper) -> bool

"""

    ParaAttsAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParaAttsAvailable(self: IPEStateWrapper) -> bool

Set: ParaAttsAvailable(self: IPEStateWrapper) = value
"""

    ParagraphState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParagraphState(self: IPEStateWrapper) -> IPEParagraphStateWrapper

Set: ParagraphState(self: IPEStateWrapper) = value
"""

    PasteAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PasteAvailable(self: IPEStateWrapper) -> bool

Set: PasteAvailable(self: IPEStateWrapper) = value
"""

    QuickStartLinkAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuickStartLinkAvailable(self: IPEStateWrapper) -> bool

"""

    RedoAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RedoAvailable(self: IPEStateWrapper) -> bool

Set: RedoAvailable(self: IPEStateWrapper) = value
"""

    RibbonOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RibbonOn(self: IPEStateWrapper) -> bool

"""

    RulerAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RulerAvailable(self: IPEStateWrapper) -> bool

Set: RulerAvailable(self: IPEStateWrapper) = value
"""

    RulerVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RulerVisible(self: IPEStateWrapper) -> bool

Set: RulerVisible(self: IPEStateWrapper) = value
"""

    SingleCustom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SingleCustom(self: IPEStateWrapper) -> bool

"""

    SingleField = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SingleField(self: IPEStateWrapper) -> bool

"""

    SpellingEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpellingEnabled(self: IPEStateWrapper) -> bool

"""

    StackAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StackAvailable(self: IPEStateWrapper) -> bool

Set: StackAvailable(self: IPEStateWrapper) = value
"""

    StaticColumnsCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaticColumnsCount(self: IPEStateWrapper) -> int

"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleId(self: IPEStateWrapper) -> ObjectId

Set: StyleId(self: IPEStateWrapper) = value
"""

    StyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleName(self: IPEStateWrapper) -> str

Set: StyleName(self: IPEStateWrapper) = value
"""

    TableCell = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TableCell(self: IPEStateWrapper) -> bool

"""

    UndoAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UndoAvailable(self: IPEStateWrapper) -> bool

Set: UndoAvailable(self: IPEStateWrapper) = value
"""

    UnstackAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnstackAvailable(self: IPEStateWrapper) -> bool

Set: UnstackAvailable(self: IPEStateWrapper) = value
"""

    VerticalSHX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VerticalSHX(self: IPEStateWrapper) -> bool

Set: VerticalSHX(self: IPEStateWrapper) = value
"""



class IPESymbolCommandType(Enum):
    """ enum IPESymbolCommandType, values: IPECustomSymbolCommand (1), IPEStandardSymbolCommand (0) """
    IPECustomSymbolCommand = None
    IPEStandardSymbolCommand = None
    value__ = None


class IPETableFlags(Enum):
    """ enum IPETableFlags, values: CursorAtEndFlag (2048), DisableAutoStackFlag (512), kForceNoUIWhenScript (4096), SelectAllFlag (1024), StartInOpaqueBackground (2), TableFlipFlag (256), TableGoAboveFlag (32), TableGoBelowFlag (16), TableGoLeftFlag (8), TableGoRightFlag (4), TableSubsequentCellFlag (1) """
    CursorAtEndFlag = None
    DisableAutoStackFlag = None
    kForceNoUIWhenScript = None
    SelectAllFlag = None
    StartInOpaqueBackground = None
    TableFlipFlag = None
    TableGoAboveFlag = None
    TableGoBelowFlag = None
    TableGoLeftFlag = None
    TableGoRightFlag = None
    TableSubsequentCellFlag = None
    value__ = None


class IPETestingEventArgs(EventArgs):
    """ IPETestingEventArgs(data: object) """
    @staticmethod # known case of __new__
    def __new__(self, data):
        """ __new__(cls: type, data: object) """
        pass

    Data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Data(self: IPETestingEventArgs) -> object

"""



class IPETestingHandler(MulticastDelegate):
    """ IPETestingHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: IPETestingHandler, sender: object, e: IPETestingEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: IPETestingHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: IPETestingHandler, sender: object, e: IPETestingEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class IPETestingWrapper(object):
    # no doc
    def FireIPETestingHandler(self):
        """ FireIPETestingHandler(self: IPETestingWrapper) """
        pass

    Data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: Data(self: IPETestingWrapper) = value
"""


    IPETest = None
    IPETestingManager = None


class IPEUpdateUIEventArgs(EventArgs):
    """ IPEUpdateUIEventArgs(forceUpdate: bool) """
    @staticmethod # known case of __new__
    def __new__(self, forceUpdate):
        """ __new__(cls: type, forceUpdate: bool) """
        pass

    ForceUpdate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ForceUpdate(self: IPEUpdateUIEventArgs) -> bool

"""



class IPEWrapper(object):
    # no doc
    def FireUpdateUIEvent(self, forceUpdate):
        """ FireUpdateUIEvent(self: IPEWrapper, forceUpdate: bool) """
        pass

    IPEEventManager = None
    UpdateUI = None


class IPreviewContextProvider:
    # no doc
    def GetPreviewControl(self, name):
        """ GetPreviewControl(self: IPreviewContextProvider, name: str) -> ILivePreviewControl """
        pass

    def GetPreviewRule(self, name):
        """ GetPreviewRule(self: IPreviewContextProvider, name: str) -> ILivePreviewRule """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ItemTypeEnum(Enum):
    """ enum ItemTypeEnum, values: kBlock (0), kDrawing (2), kDrawingAsBlock (1), kFolder (3) """
    kBlock = None
    kDrawing = None
    kDrawingAsBlock = None
    kFolder = None
    value__ = None


class LayerUtilities(object):
    # no doc
    @staticmethod
    def addXRefLayerOverride(layerId, prop):
        """ addXRefLayerOverride(layerId: ValueType, prop: int) -> bool """
        pass

    @staticmethod
    def disableXRefLayerPropertyOverrideRecording():
        """ disableXRefLayerPropertyOverrideRecording() """
        pass

    @staticmethod
    def enableXRefLayerPropertyOverrideRecording():
        """ enableXRefLayerPropertyOverrideRecording() """
        pass

    @staticmethod
    def FocusMainFrameIfPossible():
        """ FocusMainFrameIfPossible() """
        pass

# Error generating skeleton for function getAllLayersWithXRefOveride: sequence item 0: expected string, NoneType found

    @staticmethod
    def GetCurViewportObjectId():
        """ GetCurViewportObjectId() -> ObjectId """
        pass

    @staticmethod
    def GetRestoreFlags():
        """ GetRestoreFlags() -> int """
        pass

    @staticmethod
    def hasAnyXRefLayerOverrides(*__args):
        """
        hasAnyXRefLayerOverrides(dbHost: Database) -> bool
        hasAnyXRefLayerOverrides(layerId: ValueType) -> bool
        """
        pass

    @staticmethod
    def IsXrefLayerPropertyOverridden(layerId, prop):
        """ IsXrefLayerPropertyOverridden(layerId: ValueType, prop: int) -> bool """
        pass

    @staticmethod
    def isXRefLayerPropertyOverrideRecordingEnabled():
        """ isXRefLayerPropertyOverrideRecordingEnabled() -> bool """
        pass

    @staticmethod
    def LineWeightToPixel(lineWeight):
        """ LineWeightToPixel(lineWeight: LineWeight) -> int """
        pass

    @staticmethod
    def removeXRefLayerOverride(layerId, prop):
        """ removeXRefLayerOverride(layerId: ValueType, prop: int) -> bool """
        pass

    @staticmethod
    def removeXRefLayerOverrides(*__args):
        """
        removeXRefLayerOverrides(layerId: ValueType) -> bool
        removeXRefLayerOverrides(dbHost: Database) -> bool
        """
        pass

    @staticmethod
    def SetAllLayersUsed(layerTable):
        """ SetAllLayersUsed(layerTable: LayerTable) """
        pass

    @staticmethod
    def SetLayerUsed(layerTableRecord):
        """ SetLayerUsed(layerTableRecord: LayerTableRecord) """
        pass

    @staticmethod
    def SetNotDefaultCommand(bNotDefaultCommand):
        """ SetNotDefaultCommand(bNotDefaultCommand: bool) """
        pass

    @staticmethod
    def ShowLayerMergeDialog(layers):
        """ ShowLayerMergeDialog(layers: Array[ObjectId]) """
        pass

    @staticmethod
    def ShowLayerStateManagerDialog():
        """ ShowLayerStateManagerDialog() """
        pass

    @staticmethod
    def ShowLayerStateSaveDialog():
        """ ShowLayerStateSaveDialog() """
        pass

    ApplyLayerFilterToToolbar = True
    InvertLayerFilter = False
    IsMultiDocumentActivationEnabled = True
    UseCurrentLayerFilter = False
    VpOverrideBackgroundColor = None
    WillHighlightLayerPropOverrides = False
    XrefOverrideBackgroundColor = None


class LayoutContextMenu(object):
    """
    LayoutContextMenu(handler: CommandHandler, removeFlag: UInt32, enableFlag: UInt32, disableFlag: UInt32)
    LayoutContextMenu(handler: CommandHandler)
    """
    def Invoke(self, doc, nTabIndex, hWndOwner):
        """ Invoke(self: LayoutContextMenu, doc: Document, nTabIndex: int, hWndOwner: IntPtr) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self, handler, removeFlag=None, enableFlag=None, disableFlag=None):
        """
        __new__(cls: type, handler: CommandHandler, removeFlag: UInt32, enableFlag: UInt32, disableFlag: UInt32)
        __new__(cls: type, handler: CommandHandler)
        """
        pass

    Command = None
    CommandHandler = None


class LayoutThumbnailEnumerator(DisposableWrapper):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod
    def EnumerateLayoutThumbnails(doc, nFlag):
        """ EnumerateLayoutThumbnails(doc: Document, nFlag: ThumbnailCaptureFlags) -> LayoutThumbnailEnumerator """
        pass

    def Locate(self, layoutName):
        """ Locate(self: LayoutThumbnailEnumerator, layoutName: str) -> bool """
        pass

    def MoveNext(self):
        """ MoveNext(self: LayoutThumbnailEnumerator) -> bool """
        pass

    def Reset(self):
        """ Reset(self: LayoutThumbnailEnumerator) -> bool """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: LayoutThumbnailEnumerator) -> UInt32

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: LayoutThumbnailEnumerator) -> int

"""

    IsLayoutEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLayoutEmpty(self: LayoutThumbnailEnumerator) -> bool

"""

    LayoutName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutName(self: LayoutThumbnailEnumerator) -> str

"""

    Thumbnail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Thumbnail(self: LayoutThumbnailEnumerator) -> Bitmap

"""


    ThumbnailCaptureFlags = None


class LightUtil(object):
    """ LightUtil() """
    @staticmethod
    def GetBackgroundType(type):
        """ GetBackgroundType() -> (bool, DrawableType) """
        pass

    @staticmethod
    def GetSkyStatus():
        """ GetSkyStatus() -> bool """
        pass

    @staticmethod
    def RegSceneUI():
        """ RegSceneUI() -> bool """
        pass

    @staticmethod
    def SetSunAngle(db, sunId, dateTime):
        """ SetSunAngle(db: Database, sunId: ValueType, dateTime: DateTime) """
        pass


class LineWeightPicker(ComboBoxWrapper):
    """ LineWeightPicker() """
    def Dispose(self):
        """ Dispose(self: ControlWrapper, A_0: bool) """
        pass

    def Select(self):
        """ Select(self: Control, directed: bool, forward: bool) """
        pass

    CanEnableIme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CreateParams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultCursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultImeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMargin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMaximumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMinimumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultPadding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DoubleBuffered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    FontHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ImeModeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    RenderRightToLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ResizeRedraw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ScaleChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShowFocusCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShowKeyboardCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class LivePreviewUtil(object):
    """ LivePreviewUtil() """
    @staticmethod
    def IsControlLivePreviewAble(element):
        """ IsControlLivePreviewAble(element: FrameworkElement) -> bool """
        pass

    @staticmethod
    def SetPreviewContextProvider(provider):
        """ SetPreviewContextProvider(provider: IPreviewContextProvider) -> IPreviewContextProvider """
        pass

    PreviewContextProvider = None


class LocalServerUsage(Enum):
    """ enum LocalServerUsage, values: kDisabled (0), kForActivity (1), kForBothActivityAndMetadata (3), kForMetaData (2) """
    kDisabled = None
    kForActivity = None
    kForBothActivityAndMetadata = None
    kForMetaData = None
    value__ = None


class mgBlockPreviewInfo(object):
    """ mgBlockPreviewInfo() """
    def getBlockPreviewInfoJsonStr(self):
        """ getBlockPreviewInfoJsonStr(self: mgBlockPreviewInfo) -> str """
        pass

    def isOutDated(self):
        """ isOutDated(self: mgBlockPreviewInfo) -> bool """
        pass

    bForTooltip = None
    bkColorBlue = None
    bkColorGreen = None
    bkColorRed = None
    blockName = None
    bUseBlackForWhite = None
    displayItem = None
    fileName = None
    height = None
    width = None


class MgdAcViewTransitions(object):
    # no doc
    @staticmethod
    def GetSettings(enable2d, enable3d, enableDuringScripts, timeMs, fps):
        """ GetSettings() -> (bool, bool, bool, UInt32, float) """
        pass

    @staticmethod
    def SetSettings(enable2d, enable3d, enableDuringScripts, timeMs, fps):
        """ SetSettings(enable2d: bool, enable3d: bool, enableDuringScripts: bool, timeMs: UInt32, fps: float) """
        pass


class MLibDownloadUtils(object):
    """ MLibDownloadUtils() """
    @staticmethod
    def BeginToExtract():
        """ BeginToExtract() """
        pass

    @staticmethod
    def CancelDownloadJob():
        """ CancelDownloadJob() """
        pass

    @staticmethod
    def DownloadCurrentSize():
        """ DownloadCurrentSize() -> UInt64 """
        pass

    @staticmethod
    def DownloadServicEndUp():
        """ DownloadServicEndUp() """
        pass

    @staticmethod
    def DownloadServiceStartUp():
        """ DownloadServiceStartUp() """
        pass

    @staticmethod
    def DownloadTotalSize():
        """ DownloadTotalSize() -> UInt64 """
        pass

    @staticmethod
    def IsMLibCancelled():
        """ IsMLibCancelled() -> bool """
        pass

    @staticmethod
    def IsMLibDownloadComplete():
        """ IsMLibDownloadComplete() -> bool """
        pass

    @staticmethod
    def IsMLibDownloading():
        """ IsMLibDownloading() -> bool """
        pass

    @staticmethod
    def IsMLibError():
        """ IsMLibError() -> bool """
        pass

    @staticmethod
    def IsMLibExtracting():
        """ IsMLibExtracting() -> bool """
        pass

    @staticmethod
    def IsMLibReadyToInstall():
        """ IsMLibReadyToInstall() -> bool """
        pass

    @staticmethod
    def RegisterTimerCallback(fp):
        """ RegisterTimerCallback(fp: AcDownloadCallback) """
        pass

    @staticmethod
    def ShowErrorTaskDialog():
        """ ShowErrorTaskDialog() """
        pass


class MlinesMgdServices(object):
    # no doc
    @staticmethod
    def AdjustColorToBackground(mgForeground, mgBackground):
        """ AdjustColorToBackground(mgForeground: Color, mgBackground: Color) -> Color """
        pass

    @staticmethod
    def CloseCachedMLStyle():
        """ CloseCachedMLStyle() """
        pass

    @staticmethod
    def GetDefaultMlnFilename():
        """ GetDefaultMlnFilename() -> str """
        pass

    @staticmethod
    def GetDisplayBGColor(mgColor):
        """ GetDisplayBGColor(mgColor: Color) """
        pass

    @staticmethod
    def GetLinetypeNameForDisplay(linetypeId):
        """ GetLinetypeNameForDisplay(linetypeId: ObjectId) -> str """
        pass

    @staticmethod
    def IsStyleAlterable(mgName):
        """ IsStyleAlterable(mgName: str) -> bool """
        pass

    @staticmethod
    def IsValidStyleName(mgName):
        """ IsValidStyleName(mgName: str) -> bool """
        pass

    @staticmethod
    def LoadAndUpdateMlnStyle(mlnFile, fileOffset):
        """ LoadAndUpdateMlnStyle(mlnFile: str, fileOffset: int) -> MLError """
        pass

    @staticmethod
    def MlnFileReadStyles(filename, nameList, positionList):
        """ MlnFileReadStyles(filename: str, nameList: ArrayList, positionList: ArrayList) -> MLError """
        pass

    @staticmethod
    def ProcessMlEditCommand(commandCode):
        """ ProcessMlEditCommand(commandCode: CommandCode) """
        pass

    @staticmethod
    def ShowOpenMlnFileDialog(currentMlnFile):
        """ ShowOpenMlnFileDialog(currentMlnFile: str) -> str """
        pass

    @staticmethod
    def ShowSaveDialog(styleId, mlnFilename):
        """ ShowSaveDialog(styleId: ObjectId, mlnFilename: str) -> (MLError, str) """
        pass

    CommandCode = None
    MLError = None


class MonitoredSysvarValueWrapper(DisposableWrapper):
    """
    MonitoredSysvarValueWrapper(p: IntPtr, _auto_delete: bool)
    MonitoredSysvarValueWrapper(p: IntPtr)
    """
    def clone(self):
        """ clone(self: MonitoredSysvarValueWrapper) -> MonitoredSysvarValueWrapper """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def isEqualTo(self, sysvar_value):
        """ isEqualTo(self: MonitoredSysvarValueWrapper, sysvar_value: MonitoredSysvarValueWrapper) -> bool """
        pass

    def setFromString(self, value):
        """ setFromString(self: MonitoredSysvarValueWrapper, value: str) -> bool """
        pass

    def toString(self, unit=None, prec=None):
        """
        toString(self: MonitoredSysvarValueWrapper) -> str
        toString(self: MonitoredSysvarValueWrapper, unit: int, prec: int) -> str
        """
        pass

    def type(self):
        """ type(self: MonitoredSysvarValueWrapper) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, p, _auto_delete=None):
        """
        __new__(cls: type, p: IntPtr, _auto_delete: bool)
        __new__(cls: type, p: IntPtr)
        """
        pass


class MonitoredSysvarWrapper(DisposableWrapper):
    """ MonitoredSysvarWrapper(p: IntPtr) """
    def currentValue(self):
        """ currentValue(self: MonitoredSysvarWrapper) -> MonitoredSysvarValueWrapper """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def isValidValue(self, value):
        """ isValidValue(self: MonitoredSysvarWrapper, value: MonitoredSysvarValueWrapper) -> bool """
        pass

    def name(self):
        """ name(self: MonitoredSysvarWrapper) -> str """
        pass

    def perferedValue(self):
        """ perferedValue(self: MonitoredSysvarWrapper) -> MonitoredSysvarValueWrapper """
        pass

    def resetToPreferedValue(self):
        """ resetToPreferedValue(self: MonitoredSysvarWrapper) """
        pass

    def setPreferedValue(self, *__args):
        """ setPreferedValue(self: MonitoredSysvarWrapper, prefered_value: MonitoredSysvarValueWrapper)setPreferedValue(self: MonitoredSysvarWrapper, value: str) -> int """
        pass

    def syncCurrentValue(self):
        """ syncCurrentValue(self: MonitoredSysvarWrapper) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, p):
        """ __new__(cls: type, p: IntPtr) """
        pass


class NamedViewUtilities(object):
    """ NamedViewUtilities() """
    @staticmethod
    def GetNamedViewImage(objectId, imageWidth, imageHeight, backgroundColor):
        """ GetNamedViewImage(objectId: ObjectId, imageWidth: int, imageHeight: int, backgroundColor: Color) -> IntPtr """
        pass


class NavigationUtils(object):
    """ NavigationUtils() """
    @staticmethod
    def GetNavStatus():
        """ GetNavStatus() -> int """
        pass

    @staticmethod
    def IsNavActive():
        """ IsNavActive() -> bool """
        pass

    @staticmethod
    def NavPauseRecording():
        """ NavPauseRecording() """
        pass

    @staticmethod
    def NavPlayAnimation():
        """ NavPlayAnimation() """
        pass

    @staticmethod
    def NavRecordAnimation():
        """ NavRecordAnimation() """
        pass

    @staticmethod
    def NavSaveAnimation():
        """ NavSaveAnimation() """
        pass

    @staticmethod
    def NavShowAnimationSetting():
        """ NavShowAnimationSetting() """
        pass


class NavisworksFileInfo(object):
    """
    NavisworksFileInfo(obj: NavisworksFileInfo)
    NavisworksFileInfo()
    """
    @staticmethod # known case of __new__
    def __new__(self, obj=None):
        """
        __new__(cls: type, obj: NavisworksFileInfo)
        __new__(cls: type)
        """
        pass

    fileSize = None
    hasModificationTime = None
    modificationTime = None
    revisionId = None


class NavisworksFileType(Enum):
    """ enum NavisworksFileType, values: Aggregate (0), Error (2), Model (1) """
    Aggregate = None
    Error = None
    Model = None
    value__ = None


class NavisworksServiceManager(object):
    """ NavisworksServiceManager() """
    Host = None


class NewTabPageUtil(object):
    """ NewTabPageUtil() """
    @staticmethod
    def SwitchToStartPage():
        """ SwitchToStartPage() -> bool """
        pass


class NonMonitoredSysvarEnumerator(DisposableWrapper):
    """ NonMonitoredSysvarEnumerator(p: IntPtr) """
    def Current(self):
        """ Current(self: NonMonitoredSysvarEnumerator) -> MonitoredSysvarWrapper """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Done(self):
        """ Done(self: NonMonitoredSysvarEnumerator) -> bool """
        pass

    def MoveNext(self):
        """ MoveNext(self: NonMonitoredSysvarEnumerator) """
        pass

    def Reset(self):
        """ Reset(self: NonMonitoredSysvarEnumerator) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, p):
        """ __new__(cls: type, p: IntPtr) """
        pass


class ObjectContexts(object):
    """ ObjectContexts() """
    @staticmethod
    def AddContext(obj, ctxt):
        """ AddContext(obj: DBObject, ctxt: ObjectContext) """
        pass

    @staticmethod
    def GetContexts(obj, collectionName):
        """ GetContexts(obj: DBObject, collectionName: str) -> List[ObjectContext] """
        pass

    @staticmethod
    def HasContext(obj, ctxt):
        """ HasContext(obj: DBObject, ctxt: ObjectContext) -> bool """
        pass

    @staticmethod
    def RemoveContext(obj, ctxt):
        """ RemoveContext(obj: DBObject, ctxt: ObjectContext) """
        pass


class OPMModeFlags(Enum):
    """ enum (flags) OPMModeFlags, values: FromCommand (4), HatchPattern (16), InvokeDialog (8), InvokeHatchDialog (24), Selection (1), ZeroSelection (2) """
    FromCommand = None
    HatchPattern = None
    InvokeDialog = None
    InvokeHatchDialog = None
    Selection = None
    value__ = None
    ZeroSelection = None


class OPMStatus(Enum):
    """ enum OPMStatus, values: Failed (5), InvalidProperty (1), InvalidPropertyCategory (4), InvalidPropertyType (3), InvalidPropertyValue (2), OK (0) """
    Failed = None
    InvalidProperty = None
    InvalidPropertyCategory = None
    InvalidPropertyType = None
    InvalidPropertyValue = None
    OK = None
    value__ = None


class OwnerDrawComboBox(COwnerDrawComboBoxWrapper):
    """ OwnerDrawComboBox() """
    def Dispose(self):
        """ Dispose(self: COwnerDrawComboBoxWrapper, A_0: bool) """
        pass

    def IsInEdit(self, state):
        """ IsInEdit(self: OwnerDrawComboBox, state: DrawItemState) -> bool """
        pass

    def Select(self, start=None, length=None):
        """ Select(self: Control, directed: bool, forward: bool) """
        pass

    AllowSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CanEnableIme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CreateParams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DataManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultCursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultImeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMargin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMaximumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMinimumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultPadding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DoubleBuffered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    FontHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ImeModeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    RenderRightToLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ResizeRedraw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ScaleChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShowFocusCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShowKeyboardCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    VistaTheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VistaTheme(self: OwnerDrawComboBox) -> bool

"""



class PreviewControl(ControlWrapper):
    """ PreviewControl() """
    def ClearAll(self):
        """ ClearAll(self: PreviewControl) """
        pass

    def CreateModel(self):
        """ CreateModel(self: PreviewControl) -> ErrorStatus """
        pass

    def Dispose(self):
        """ Dispose(self: ControlWrapper, A_0: bool) """
        pass

    def ErasePreview(self):
        """ ErasePreview(self: PreviewControl) """
        pass

    def GetImpObj(self, *args): #cannot find CLR method
        """ GetImpObj(self: PreviewControl) -> CPreviewStatic* """
        pass

    def Init(self):
        """ Init(self: PreviewControl) """
        pass

    def RefreshPreview(self):
        """ RefreshPreview(self: PreviewControl) -> ErrorStatus """
        pass

    def Select(self):
        """ Select(self: Control, directed: bool, forward: bool) """
        pass

    def ShowEntity(self, fieldWidth, fieldHeight, entity, added=None):
        """ ShowEntity(self: PreviewControl, fieldWidth: float, fieldHeight: float, entity: Entity)ShowEntity(self: PreviewControl, fieldWidth: float, fieldHeight: float, entity: Entity, added: bool) """
        pass

    CanEnableIme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CreateParams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultCursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultImeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMargin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMaximumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMinimumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultPadding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DoubleBuffered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    FontHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ImeModeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    RenderRightToLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ResizeRedraw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ScaleChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShowFocusCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShowKeyboardCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class PreviewControlType(Enum):
    """ enum PreviewControlType, values: PropertyPaletteControl (2), RibbonItemControl (1) """
    PropertyPaletteControl = None
    RibbonItemControl = None
    value__ = None


class ProductInfo(object):
    """ ProductInfo(product: AcProductInfo) -> AcProductInfo """
    @staticmethod # known case of __new__
    def __new__(self, product):
        """ __new__(cls: type, product: AcProductInfo) -> AcProductInfo """
        pass

    highlightsFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: highlightsFile(self: ProductInfo) -> str

Set: highlightsFile(self: ProductInfo) = value
"""

    info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: info(self: ProductInfo) -> str

Set: info(self: ProductInfo) = value
"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: name(self: ProductInfo) -> str

Set: name(self: ProductInfo) = value
"""

    productRootKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: productRootKey(self: ProductInfo) -> str

Set: productRootKey(self: ProductInfo) = value
"""

    update = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: update(self: ProductInfo) -> ValueType

Set: update(self: ProductInfo) = value
"""

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: version(self: ProductInfo) -> str

Set: version(self: ProductInfo) = value
"""



class QuickStartLink(ControlWrapper):
    """ QuickStartLink() """
    def Dispose(self):
        """ Dispose(self: ControlWrapper, A_0: bool) """
        pass

    def GetImpObj(self, *args): #cannot find CLR method
        """ GetImpObj(self: QuickStartLink) -> CAdUiQuickStartLink* """
        pass

    def Select(self):
        """ Select(self: Control, directed: bool, forward: bool) """
        pass

    def SetHelpTopic(self, helpTopic):
        """ SetHelpTopic(self: QuickStartLink, helpTopic: str) """
        pass

    CanEnableIme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CreateParams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultCursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultImeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMargin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMaximumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMinimumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultPadding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DoubleBuffered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    FontHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ImeModeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    RenderRightToLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ResizeRedraw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ScaleChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShowFocusCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShowKeyboardCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class RecentBlockSerializeState(Enum):
    """ enum RecentBlockSerializeState, values: kDeleted (4), kInMemory (0), kSerializable (1), kSerialized (3), kSerializing (2) """
    kDeleted = None
    kInMemory = None
    kSerializable = None
    kSerialized = None
    kSerializing = None
    value__ = None


class ResourceUtil(object):
    """ ResourceUtil() """
    @staticmethod
    def FormatByLocale(*__args):
        """
        FormatByLocale(formatString: str, *paramlist: Array[object]) -> str
        FormatByLocale(type: Type, formatId: str, *paramlist: Array[object]) -> str
        """
        pass

    @staticmethod
    def FormatInvariant(format, paramlist):
        """ FormatInvariant(format: str, *paramlist: Array[object]) -> str """
        pass

    @staticmethod
    def GetCultureInfo():
        """ GetCultureInfo() -> CultureInfo """
        pass

    @staticmethod
    def GetString(type, id):
        """ GetString(type: Type, id: str) -> str """
        pass

    @staticmethod
    def StringToDouble(text):
        """ StringToDouble(text: str) -> float """
        pass


class ThumbnailGenerateTask(object):
    """ ThumbnailGenerateTask(taskDesc: TaskDescriber) """
    def generateBitmap(self, *args): #cannot find CLR method
        """ generateBitmap(self: ThumbnailGenerateTask, fileName: AcString*, blockName: AcString*, size: int, gsBkColor: AcGsColor*, toBeResumed: Boolean*) -> HBITMAP__* """
        pass

    def generateBitmapWithState(self, *args): #cannot find CLR method
        """ generateBitmapWithState(self: ThumbnailGenerateTask, fileName: AcString*, blockName: AcString*, size: int, gsBkColor: AcGsColor*, toBeResumed: Boolean*, resumePreviewState: AcBlockPreviewGenerationlState*) -> HBITMAP__* """
        pass

    def onTaskDiscarded(self):
        """ onTaskDiscarded(self: ThumbnailGenerateTask) """
        pass

    def run(self):
        """ run(self: ThumbnailGenerateTask) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, taskDesc):
        """ __new__(cls: type, taskDesc: TaskDescriber) """
        pass

    DataHost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataHost(self: ThumbnailGenerateTask) -> BlockDisplayItem

"""

    Executed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Executed(self: ThumbnailGenerateTask) -> bool

Set: Executed(self: ThumbnailGenerateTask) = value
"""

    TaskDesc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TaskDesc(self: ThumbnailGenerateTask) -> TaskDescriber

Set: TaskDesc(self: ThumbnailGenerateTask) = value
"""

    Valid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Valid(self: ThumbnailGenerateTask) -> bool

"""

    WaitTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WaitTime(self: ThumbnailGenerateTask) -> Int64

"""



class ResumedThumbnailGenerateTask(ThumbnailGenerateTask):
    """ ResumedThumbnailGenerateTask(taskDesc: TaskDescriber, resumePreviewState: AcBlockPreviewGenerationlState*) """
    def Dispose(self):
        """ Dispose(self: ResumedThumbnailGenerateTask) """
        pass

    def onTaskDiscarded(self):
        """ onTaskDiscarded(self: ResumedThumbnailGenerateTask) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, taskDesc, resumePreviewState):
        """ __new__(cls: type, taskDesc: TaskDescriber, resumePreviewState: AcBlockPreviewGenerationlState*) """
        pass


class ScaleListHelpers(object):
    """ ScaleListHelpers() """
    @staticmethod
    def getDefaultScaleList(returnPredefinedScales, measurement, scaleStr, scaleNum, scaleDenom, scaleCount):
        """ getDefaultScaleList(returnPredefinedScales: bool, measurement: int, scaleStr: List[str], scaleNum: List[float], scaleDenom: List[float], scaleCount: Array[int]) -> str """
        pass

    @staticmethod
    def GetReferencedScaleNames(db, scaleIds, scaleStr, scaleCount):
        """ GetReferencedScaleNames(db: Database, scaleIds: ObjectIdCollection, scaleStr: List[str], scaleCount: Array[int]) """
        pass

    @staticmethod
    def GetUnitScaleName(db):
        """ GetUnitScaleName(db: Database) -> str """
        pass

    @staticmethod
    def loadScaleList(referencedScaleIds, referencedScaleCount, scaleStr, scaleNum, scaleDenom, scaleCount):
        """ loadScaleList(referencedScaleIds: ObjectIdCollection, referencedScaleCount: Array[int], scaleStr: List[str], scaleNum: List[float], scaleDenom: List[float], scaleCount: Array[int]) """
        pass

    @staticmethod
    def loadScaleUnitStrings(unitStrings):
        """ loadScaleUnitStrings(unitStrings: Array[str]) """
        pass

    @staticmethod
    def resetScaleList(measurement, scaleStr, scaleNum, scaleDenom, scaleCount):
        """ resetScaleList(measurement: int, scaleStr: List[str], scaleNum: List[float], scaleDenom: List[float], scaleCount: Array[int]) """
        pass

    @staticmethod
    def saveScaleList(scaleStr, scaleNum, scaleDenom, scaleCount):
        """ saveScaleList(scaleStr: List[str], scaleNum: List[float], scaleDenom: List[float], scaleCount: int) """
        pass

    @staticmethod
    def setDefaultScaleList(newScaleStr, scaleNum, scaleDenom, scaleType, scaleCount):
        """ setDefaultScaleList(newScaleStr: List[str], scaleNum: List[float], scaleDenom: List[float], scaleType: List[int], scaleCount: int) """
        pass

    @staticmethod
    def updateScaleList(oldScaleStr, newScaleStr, scaleNum, scaleDenom, scaleCount):
        """ updateScaleList(oldScaleStr: List[str], newScaleStr: List[str], scaleNum: List[float], scaleDenom: List[float], scaleCount: int) """
        pass


class SearchBox(TextBox):
    """ SearchBox() """
    def ClearEditor(self):
        """ ClearEditor(self: SearchBox) """
        pass

    def Dispose(self):
        """ Dispose(self: SearchBox, A_0: bool) """
        pass

    def Select(self, start=None, length=None):
        """ Select(self: Control, directed: bool, forward: bool) """
        pass

    def SetButtonBackgroundColorForThemeChange(self, color, bThemeIsDark):
        """ SetButtonBackgroundColorForThemeChange(self: SearchBox, color: Color, bThemeIsDark: bool) """
        pass

    CanEnableIme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CreateParams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultCursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultImeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMargin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMaximumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMinimumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultPadding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: DefaultText(self: SearchBox) = value
"""

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DoubleBuffered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    FontHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ImeModeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsEditEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEditEmpty(self: SearchBox) -> bool

"""

    Notification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: Notification(self: SearchBox) = value
"""

    RenderRightToLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ResizeRedraw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ScaleChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShowFocusCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShowKeyboardCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class SecUtil(object):
    """ SecUtil() """
    @staticmethod
    def GetCertificateSubjectName(filePath):
        """ GetCertificateSubjectName(filePath: str) -> str """
        pass

    @staticmethod
    def IsSignatureValid(filePath):
        """ IsSignatureValid(filePath: str) -> int """
        pass


class ServicePackInfo(object):
    """ ServicePackInfo() """
    def getProductInfo(self):
        """ getProductInfo(self: ServicePackInfo) -> List[ProductInfo] """
        pass


class SetReadOnlySysvar(object):
    """ SetReadOnlySysvar() """
    @staticmethod
    def SetLayerManagerState(eState):
        """ SetLayerManagerState(eState: int) """
        pass


class SharedRecentFileData(object):
    """
    SharedRecentFileData(nAccessTime: int, strProvider: str, strFileName: str, strPath: str, strID: str, strPlatform: str)
    SharedRecentFileData()
    """
    @staticmethod # known case of __new__
    def __new__(self, nAccessTime=None, strProvider=None, strFileName=None, strPath=None, strID=None, strPlatform=None):
        """
        __new__(cls: type, nAccessTime: int, strProvider: str, strFileName: str, strPath: str, strID: str, strPlatform: str)
        __new__(cls: type)
        """
        pass

    mnAccessTime = None
    mstrFileName = None
    mstrID = None
    mstrPath = None
    mstrPlatform = None
    mstrProvider = None


class SharedRecentFiles(object):
    """ SharedRecentFiles() """
    def GetRecentFilesCallback(self, *args): #cannot find CLR method
        """ GetSharedRecentFilesCallback(A_0: object, A_1: IntPtr) """
        pass

    def RecentFileCallback(self, *args): #cannot find CLR method
        """ ShareRecentFileCallback(A_0: object, A_1: IntPtr) """
        pass


class ShareRecentFileCallback(MulticastDelegate):
    """ ShareRecentFileCallback(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, path, filename, provider, nAccessTime, bSuccessfullyAdded, callback, obj):
        """ BeginInvoke(self: ShareRecentFileCallback, path: str, filename: str, provider: str, nAccessTime: int, bSuccessfullyAdded: bool, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ShareRecentFileCallback, result: IAsyncResult) """
        pass

    def Invoke(self, path, filename, provider, nAccessTime, bSuccessfullyAdded):
        """ Invoke(self: ShareRecentFileCallback, path: str, filename: str, provider: str, nAccessTime: int, bSuccessfullyAdded: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class SMManager(object):
    """ SMManager() """
    @staticmethod
    def CIP_LogTargetShot(strShotName):
        """ CIP_LogTargetShot(strShotName: str) -> bool """
        pass

    @staticmethod
    def DeleteSequenceShot(bSequence, strName):
        """ DeleteSequenceShot(bSequence: bool, strName: str) """
        pass

    @staticmethod
    def EndPlay():
        """ EndPlay() """
        pass

    @staticmethod
    def GetPlayStatus(activeShotName, activeSeqName, playMode, playAction, bPause):
        """ GetPlayStatus() -> (bool, str, str, PlayMode, PlayAction, bool) """
        pass

    @staticmethod
    def GetSequenceIds():
        """ GetSequenceIds() -> Array[ValueType] """
        pass

    @staticmethod
    def GetShotIds(strName):
        """ GetShotIds(strName: str) -> Array[ValueType] """
        pass

    @staticmethod
    def IsShotPlaying():
        """ IsShotPlaying() -> bool """
        pass

    @staticmethod
    def LoopStatusChanged(bLoop):
        """ LoopStatusChanged(bLoop: bool) """
        pass

    @staticmethod
    def MoveSequenceShot(bSequence, strName, bLeft):
        """ MoveSequenceShot(bSequence: bool, strName: str, bLeft: bool) """
        pass

    @staticmethod
    def PauseOrResumePlayBack(bPause):
        """ PauseOrResumePlayBack(bPause: bool) """
        pass

    @staticmethod
    def RenameSequenceShot(bSequence, oldName, newName):
        """ RenameSequenceShot(bSequence: bool, oldName: str, newName: str) -> bool """
        pass

    @staticmethod
    def UIToBeHidden():
        """ UIToBeHidden() """
        pass

    @staticmethod
    def UIToBeShown():
        """ UIToBeShown() """
        pass

    @staticmethod
    def UpdateCachedData():
        """ UpdateCachedData() """
        pass

    @staticmethod
    def UpdateThumbnailAll():
        """ UpdateThumbnailAll() -> bool """
        pass

    @staticmethod
    def UpdateThumbnailSequenceShot(bSequence, strName):
        """ UpdateThumbnailSequenceShot(bSequence: bool, strName: str) -> bool """
        pass

    PlayAction = None
    PlayMode = None


class SmManagerUtilities(object):
    # no doc
    @staticmethod
    def SetSmManagerInterface(mgr):
        """ SetSmManagerInterface(mgr: object) """
        pass


class StartupToolsEventArgs(EventArgs):
    """ StartupToolsEventArgs() """
    def Add(self, toolName, commandName):
        """ Add(self: StartupToolsEventArgs, toolName: str, commandName: str) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass


class SubSetting(object):
    """ SubSetting() """
    @staticmethod
    def IsCommandEnabled(command):
        """ IsCommandEnabled(command: str) -> bool """
        pass

    @staticmethod
    def IsSysVarEnabled(sysvar):
        """ IsSysVarEnabled(sysvar: str) -> bool """
        pass


class SysvarMonitorIteratorWrapper(DisposableWrapper):
    """ SysvarMonitorIteratorWrapper(p: IntPtr) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def isEqual(self, sysvarMonitorIter):
        """ isEqual(self: SysvarMonitorIteratorWrapper, sysvarMonitorIter: SysvarMonitorIteratorWrapper) -> bool """
        pass

    def isnotEqual(self, sysvarMonitorIter):
        """ isnotEqual(self: SysvarMonitorIteratorWrapper, sysvarMonitorIter: SysvarMonitorIteratorWrapper) -> bool """
        pass

    def next(self):
        """ next(self: SysvarMonitorIteratorWrapper) -> SysvarMonitorIteratorWrapper """
        pass

    def sysvar(self):
        """ sysvar(self: SysvarMonitorIteratorWrapper) -> MonitoredSysvarWrapper """
        pass

    @staticmethod # known case of __new__
    def __new__(self, p):
        """ __new__(cls: type, p: IntPtr) """
        pass


class SysvarMonitorWrapper(DisposableWrapper):
    # no doc
    def addMonitoredSysvar(self, sysvar):
        """ addMonitoredSysvar(self: SysvarMonitorWrapper, sysvar: MonitoredSysvarWrapper) -> MonitoredSysvarWrapper """
        pass

    def begin(self):
        """ begin(self: SysvarMonitorWrapper) -> SysvarMonitorIteratorWrapper """
        pass

    @staticmethod
    def createSysvarMonitorWrapper(p):
        """ createSysvarMonitorWrapper(p: IntPtr) -> SysvarMonitorWrapper """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def end(self):
        """ end(self: SysvarMonitorWrapper) -> SysvarMonitorIteratorWrapper """
        pass

    def getNonMonitoredSysvarEnumerator(self):
        """ getNonMonitoredSysvarEnumerator(self: SysvarMonitorWrapper) -> NonMonitoredSysvarEnumerator """
        pass

    def isDifferenceDetected(self):
        """ isDifferenceDetected(self: SysvarMonitorWrapper) -> bool """
        pass

    def isSysvarMonitored(self, sysvar_name):
        """ isSysvarMonitored(self: SysvarMonitorWrapper, sysvar_name: str) -> bool """
        pass

    def removeMonitoredSysvar(self, sysvar):
        """ removeMonitoredSysvar(self: SysvarMonitorWrapper, sysvar: MonitoredSysvarWrapper) """
        pass

    def resetMonitoredSysvar(self, sysvar):
        """ resetMonitoredSysvar(self: SysvarMonitorWrapper, sysvar: MonitoredSysvarWrapper) """
        pass

    BalloonAlertEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BalloonAlertEnabled(self: SysvarMonitorWrapper) -> bool

Set: BalloonAlertEnabled(self: SysvarMonitorWrapper) = value
"""

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Enabled(self: SysvarMonitorWrapper) -> bool

Set: Enabled(self: SysvarMonitorWrapper) = value
"""



class TableItem(Enum):
    """ enum TableItem, values: TableItemCell (1), TableItemColumn (3), TableItemInvalid (0), TableItemRow (2) """
    TableItemCell = None
    TableItemColumn = None
    TableItemInvalid = None
    TableItemRow = None
    value__ = None


class TableStylePreview(ControlWrapper):
    """ TableStylePreview() """
    def Dispose(self):
        """ Dispose(self: ControlWrapper, A_0: bool) """
        pass

    def EnablePreview(self, bEnable):
        """ EnablePreview(self: TableStylePreview, bEnable: bool) -> bool """
        pass

    def GetImpObj(self, *args): #cannot find CLR method
        """ GetImpObj(self: TableStylePreview) -> CAcTableStylePreviewStatic* """
        pass

    def InitializeTable(self):
        """ InitializeTable(self: TableStylePreview) -> bool """
        pass

    def Select(self):
        """ Select(self: Control, directed: bool, forward: bool) """
        pass

    def ShowTablePreview(self, bUpdateTable):
        """ ShowTablePreview(self: TableStylePreview, bUpdateTable: bool) -> bool """
        pass

    CanEnableIme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CreateParams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Database = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Database(self: TableStylePreview) -> Database

Set: Database(self: TableStylePreview) = value
"""

    DataText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: DataText(self: TableStylePreview) = value
"""

    DefaultCursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultImeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMargin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMaximumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMinimumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultPadding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DoubleBuffered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    FontHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    HeaderText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: HeaderText(self: TableStylePreview) = value
"""

    ImeModeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    NumColumns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: NumColumns(self: TableStylePreview) = value
"""

    NumRows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: NumRows(self: TableStylePreview) = value
"""

    RenderRightToLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ResizeRedraw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ScaleChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShowFocusCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShowKeyboardCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Table(self: TableStylePreview) -> Table

"""

    TableStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TableStyle(self: TableStylePreview) -> ObjectId

Set: TableStyle(self: TableStylePreview) = value
"""

    TitleText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: TitleText(self: TableStylePreview) = value
"""



class TableUtilities(object):
    """ TableUtilities() """
    @staticmethod
    def CanDelete(table, selRange, row):
        """ CanDelete(table: Table, selRange: CellRange, row: bool) -> bool """
        pass

    @staticmethod
    def CanInsert(table, selRange, row, rightOrBottom):
        """ CanInsert(table: Table, selRange: CellRange, row: bool, rightOrBottom: bool) -> bool """
        pass

    @staticmethod
    def CanMergeCells(table, selRange):
        """ CanMergeCells(table: Table, selRange: CellRange) -> bool """
        pass

    @staticmethod
    def CanUnMergeCells(table, selRange):
        """ CanUnMergeCells(table: Table, selRange: CellRange) -> bool """
        pass

    @staticmethod
    def GetBackgroundColor(table):
        """ GetBackgroundColor(table: Table) -> Color """
        pass

    @staticmethod
    def GetCellStyle(table, selRange, item, localized, varies):
        """ GetCellStyle(table: Table, selRange: CellRange, item: TableItem, localized: bool) -> (str, bool) """
        pass

    @staticmethod
    def GetCellStyles(tableStyle, count, localized=None, sort=None):
        """
        GetCellStyles(tableStyle: TableStyle, localized: bool, sort: bool) -> (Array[str], int)
        GetCellStyles(tableStyle: TableStyle) -> (Array[str], int)
        """
        pass

    @staticmethod
    def GetDataType(table, dateType, unitType):
        """ GetDataType(table: Table) -> (DataType, UnitType) """
        pass

    @staticmethod
    def GetPickFirstTable(tableId, selRange, tableIndex):
        """ GetPickFirstTable() -> (bool, ObjectId, CellRange, int) """
        pass

    @staticmethod
    def GetReadOnlyState(table, selRange, readOnlyContent, readOnlyFormat):
        """ GetReadOnlyState(table: Table, selRange: CellRange) -> (bool, bool) """
        pass

    @staticmethod
    def GetSelectionAlignment(tableId, alignment):
        """ GetSelectionAlignment(tableId: ValueType) -> (bool, CellAlignment) """
        pass

    @staticmethod
    def GetSelectionLock(table, cellState):
        """ GetSelectionLock(table: Table) -> (bool, CellStates) """
        pass

    @staticmethod
    def IsDataLinkCommandAllowed():
        """ IsDataLinkCommandAllowed() -> bool """
        pass

    @staticmethod
    def IsFieldCommandAllowed():
        """ IsFieldCommandAllowed() -> bool """
        pass

    @staticmethod
    def IsSingleCell(table, selRange):
        """ IsSingleCell(table: Table, selRange: CellRange) -> bool """
        pass

    @staticmethod
    def SetBackgroundColor(table, color):
        """ SetBackgroundColor(table: Table, color: Color) """
        pass


class TaskDescriber(object):
    """ TaskDescriber(displayItem: BlockDisplayItem) """
    def onTaskCompleted(self, imageSource):
        """ onTaskCompleted(self: TaskDescriber, imageSource: ImageSource) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, displayItem):
        """ __new__(cls: type, displayItem: BlockDisplayItem) """
        pass

    DisplayItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayItem(self: TaskDescriber) -> BlockDisplayItem

"""

    ThumbnailSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThumbnailSize(self: TaskDescriber) -> int

"""

    ThumbnailState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThumbnailState(self: TaskDescriber) -> ThumbnailGenerateState

Set: ThumbnailState(self: TaskDescriber) = value
"""

    UseLocalServer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseLocalServer(self: TaskDescriber) -> bool

Set: UseLocalServer(self: TaskDescriber) = value
"""


    mDisplayItem = None
    mUseLocalServer = None


class TextIPEUtils(object):
    # no doc
    @staticmethod
    def ContinueAutoNumbering():
        """ ContinueAutoNumbering() -> bool """
        pass

    @staticmethod
    def Diagonal():
        """ Diagonal() -> bool """
        pass

    @staticmethod
    def GetAllFontNames(trueTypeFonts, shxFonts, bigFonts):
        """ GetAllFontNames(trueTypeFonts: List[str], shxFonts: List[str], bigFonts: List[str]) """
        pass

    @staticmethod
    def GetCustomMacors(marcroList):
        """ GetCustomMacors(marcroList: List[str]) """
        pass

    @staticmethod
    def GetFontTypeImage(IsTrueType):
        """ GetFontTypeImage(IsTrueType: bool) -> IntPtr """
        pass

    @staticmethod
    def GetIconFromAcadResource(iconType, image, largeImage):
        """ GetIconFromAcadResource(iconType: IPEControlIconType) -> (bool, ImageSource, ImageSource) """
        pass

    @staticmethod
    def GetIPEState():
        """ GetIPEState() -> IPEStateWrapper """
        pass

    @staticmethod
    def Horizontal():
        """ Horizontal() -> bool """
        pass

    @staticmethod
    def MgdIPESendCommand(command, param1, param2):
        """ MgdIPESendCommand(command: IPECommands, param1: object, param2: object) -> bool """
        pass

    @staticmethod
    def NoUnitsNumberToString(dValue):
        """ NoUnitsNumberToString(dValue: float) -> str """
        pass

    @staticmethod
    def NumberToString(dValue):
        """ NumberToString(dValue: float) -> str """
        pass

    @staticmethod
    def RedoAutoNumbering():
        """ RedoAutoNumbering() -> bool """
        pass

    @staticmethod
    def RestartAutoNumbering():
        """ RestartAutoNumbering() -> bool """
        pass

    @staticmethod
    def StackProperties():
        """ StackProperties() -> bool """
        pass

    @staticmethod
    def StringToNoUnitsNumber(sText, dValue):
        """ StringToNoUnitsNumber(sText: str, dValue: float) -> (bool, float) """
        pass

    @staticmethod
    def StringToNumber(sText, dValue):
        """ StringToNumber(sText: str, dValue: float) -> (bool, float) """
        pass

    @staticmethod
    def UndoAutoNumbering():
        """ UndoAutoNumbering() -> bool """
        pass

    @staticmethod
    def Unstack():
        """ Unstack() -> bool """
        pass

    MaxmumObliqueAngle = 85.0
    MaxmumTrackingFactor = 4.0
    MaxmumWidthScale = 10.0
    MinimumObliqueAngle = -85.0
    MinimumTrackingFactor = 0.75
    MinimumWidthScale = 0.10000000000000001


class ThemeChangedEventHandler(MulticastDelegate):
    """ ThemeChangedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, callback, obj):
        """ BeginInvoke(self: ThemeChangedEventHandler, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ThemeChangedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self):
        """ Invoke(self: ThemeChangedEventHandler) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class ThumbnailGenerateState(Enum):
    """ enum ThumbnailGenerateState, values: kGenerated (3), kGenerating (2), kRaw (0), kRequired (1) """
    kGenerated = None
    kGenerating = None
    kRaw = None
    kRequired = None
    value__ = None


class ThumbnailGenerateTaskQueue(object):
    # no doc
    def clear(self):
        """ clear(self: ThumbnailGenerateTaskQueue) """
        pass

    def discard(self, data):
        """ discard(self: ThumbnailGenerateTaskQueue, data: BlockDisplayItem)discard(self: ThumbnailGenerateTaskQueue, data: HashSet[BlockDisplayItem]) """
        pass

    def Dispose(self):
        """ Dispose(self: ThumbnailGenerateTaskQueue) """
        pass

    def isEmpty(self):
        """ isEmpty(self: ThumbnailGenerateTaskQueue) -> bool """
        pass

    def pop(self):
        """ pop(self: ThumbnailGenerateTaskQueue) -> ThumbnailGenerateTask """
        pass

    def push(self, A_0):
        """ push(self: ThumbnailGenerateTaskQueue, A_0: ThumbnailGenerateTask) """
        pass

    @staticmethod
    def queue():
        """ queue() -> ThumbnailGenerateTaskQueue """
        pass

    def queueData(self):
        """ queueData(self: ThumbnailGenerateTaskQueue) -> Queue[ThumbnailGenerateTask] """
        pass

    def remove(self, task):
        """ remove(self: ThumbnailGenerateTaskQueue, task: ThumbnailGenerateTask) """
        pass

    def top(self):
        """ top(self: ThumbnailGenerateTaskQueue) -> ThumbnailGenerateTask """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass


class ThumbnailTaskDescriber(TaskDescriber):
    """ ThumbnailTaskDescriber(displayItem: BlockDisplayItem) """
    def onTaskCompleted(self, imageSource):
        """ onTaskCompleted(self: ThumbnailTaskDescriber, imageSource: ImageSource) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, displayItem):
        """ __new__(cls: type, displayItem: BlockDisplayItem) """
        pass

    ThumbnailSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThumbnailSize(self: ThumbnailTaskDescriber) -> int

"""

    ThumbnailState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThumbnailState(self: ThumbnailTaskDescriber) -> ThumbnailGenerateState

Set: ThumbnailState(self: ThumbnailTaskDescriber) = value
"""

    UseLocalServer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseLocalServer(self: ThumbnailTaskDescriber) -> bool

Set: UseLocalServer(self: ThumbnailTaskDescriber) = value
"""


    mDisplayItem = None
    mUseLocalServer = None


class TooltipTaskDescriber(TaskDescriber):
    """ TooltipTaskDescriber(displayItem: BlockDisplayItem) """
    def onTaskCompleted(self, imageSource):
        """ onTaskCompleted(self: TooltipTaskDescriber, imageSource: ImageSource) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, displayItem):
        """ __new__(cls: type, displayItem: BlockDisplayItem) """
        pass

    ThumbnailSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThumbnailSize(self: TooltipTaskDescriber) -> int

"""

    ThumbnailState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThumbnailState(self: TooltipTaskDescriber) -> ThumbnailGenerateState

Set: ThumbnailState(self: TooltipTaskDescriber) = value
"""

    UseLocalServer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseLocalServer(self: TooltipTaskDescriber) -> bool

Set: UseLocalServer(self: TooltipTaskDescriber) = value
"""


    mDisplayItem = None
    mUseLocalServer = None


class TrueColorPicker(ComboBoxWrapper):
    """ TrueColorPicker() """
    def AddOtherItemToList(self, name, cargo):
        """ AddOtherItemToList(self: TrueColorPicker, name: str, cargo: int) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: ControlWrapper, A_0: bool) """
        pass

    def GetCurrentItemColor(self):
        """ GetCurrentItemColor(self: TrueColorPicker) -> Color """
        pass

    def Select(self):
        """ Select(self: Control, directed: bool, forward: bool) """
        pass

    def SetCurrentByColor(self, mgColor):
        """ SetCurrentByColor(self: TrueColorPicker, mgColor: Color) """
        pass

    CanEnableIme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CreateParams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CurrentSelectionIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSelectionIndex(self: TrueColorPicker) -> int

Set: CurrentSelectionIndex(self: TrueColorPicker) = value
"""

    DefaultCursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultImeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMargin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMaximumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMinimumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultPadding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DoubleBuffered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    FontHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ImeModeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    RenderRightToLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ResizeRedraw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ScaleChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShowFocusCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShowKeyboardCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class UiCallback(MulticastDelegate):
    """ UiCallback(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, callback, obj):
        """ BeginInvoke(self: UiCallback, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: UiCallback, result: IAsyncResult) """
        pass

    def Invoke(self):
        """ Invoke(self: UiCallback) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class UndoBoundaryEnum(Enum):
    """ enum UndoBoundaryEnum, values: CommandBoundaryEnd (16), CommandBoundaryStart (8), SubCommandBoundary (4), SubCommandWall (2048) """
    CommandBoundaryEnd = None
    CommandBoundaryStart = None
    SubCommandBoundary = None
    SubCommandWall = None
    value__ = None


class UnmanagedResource(object):
    """ UnmanagedResource() """
    @staticmethod
    def GetResourceHandle(moduleName):
        """ GetResourceHandle(moduleName: str) -> IntPtr """
        pass

    @staticmethod
    def LoadString(resourceHandle, resourceId):
        """ LoadString(resourceHandle: IntPtr, resourceId: int) -> str """
        pass

    AcadResourceHandle = None


class UpdateTitleBarEventHandler(MulticastDelegate):
    """ UpdateTitleBarEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, callback, obj):
        """ BeginInvoke(self: UpdateTitleBarEventHandler, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: UpdateTitleBarEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self):
        """ Invoke(self: UpdateTitleBarEventHandler) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class UpdateUIEventHandler(MulticastDelegate):
    """ UpdateUIEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: UpdateUIEventHandler, sender: object, e: IPEUpdateUIEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: UpdateUIEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: UpdateUIEventHandler, sender: object, e: IPEUpdateUIEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class Utils(object):
    """ Utils() """
    @staticmethod
    def ActivateDocument(hWndDoc):
        """ ActivateDocument(hWndDoc: IntPtr) """
        pass

    @staticmethod
    def ActivateLayout(doc, index):
        """ ActivateLayout(doc: Document, index: int) """
        pass

    @staticmethod
    def AddCommand(cmdGroupName, cmdGlobalName, cmdLocalName, cmdFlags, func):
        """ AddCommand(cmdGroupName: str, cmdGlobalName: str, cmdLocalName: str, cmdFlags: CommandFlags, func: CommandCallback) """
        pass

    @staticmethod
    def AngleToString(dValue):
        """ AngleToString(dValue: float) -> str """
        pass

    @staticmethod
    def ApplyAcValueFormat(objValue, formatString):
        """ ApplyAcValueFormat(objValue: object, formatString: str) -> str """
        pass

    @staticmethod
    def CallButtonEditor(resId, packageName):
        """ CallButtonEditor(resId: str, packageName: str) -> str """
        pass

    @staticmethod
    def CallButtonEditorWithBitmap(bitmap, resId, packageName):
        """ CallButtonEditorWithBitmap(bitmap: Bitmap, resId: str, packageName: str) -> str """
        pass

    @staticmethod
    def CancelAndRunCmds(pStrCmd):
        """ CancelAndRunCmds(pStrCmd: str) -> bool """
        pass

    @staticmethod
    def CloseCommandLine():
        """ CloseCommandLine() """
        pass

    @staticmethod
    def ConvertBitmapToAcGiImageBGRA32(bmp):
        """ ConvertBitmapToAcGiImageBGRA32(bmp: Bitmap) -> ImageBGRA32 """
        pass

    @staticmethod
    def ConvertBitmapToAcGiImageBGRA32Ex(bmp):
        """ ConvertBitmapToAcGiImageBGRA32Ex(bmp: Bitmap) -> ImageBGRA32 """
        pass

    @staticmethod
    def ConvertCMenuToMenuItem(pMenu, menuItem):
        """ ConvertCMenuToMenuItem(pMenu: CMenu*, menuItem: MenuItem) """
        pass

    @staticmethod
    def ConvertOSnapCMenuToMenuItem(pMenu, menuItem, b3DOsnap):
        """ ConvertOSnapCMenuToMenuItem(pMenu: CMenu*, menuItem: MenuItem, b3DOsnap: bool) """
        pass

    @staticmethod
    def CreateCommandToolTip(pTooltipInfo):
        """ CreateCommandToolTip(pTooltipInfo: ValueType) -> object """
        pass

    @staticmethod
    def CreateNativeTrayItemInstance():
        """ CreateNativeTrayItemInstance() -> IntPtr """
        pass

    @staticmethod
    def CUIBitmapAdd(group):
        """ CUIBitmapAdd(group: str) """
        pass

    @staticmethod
    def CUIBitmapGet(group, id, smallIcon):
        """ CUIBitmapGet(group: str, id: str, smallIcon: bool) -> Bitmap """
        pass

    @staticmethod
    def CUIBitmapRemove(group):
        """ CUIBitmapRemove(group: str) """
        pass

    @staticmethod
    def CUIIsUsingSmallIcon():
        """ CUIIsUsingSmallIcon() -> bool """
        pass

    @staticmethod
    def CUISaveMenuAndToolbarState():
        """ CUISaveMenuAndToolbarState() """
        pass

    @staticmethod
    def DeleteDimConstraints(db, bKeepAnnotativeDimensions):
        """ DeleteDimConstraints(db: Database, bKeepAnnotativeDimensions: bool) -> bool """
        pass

    @staticmethod
    def DisableUndoRecording(db, bDisable):
        """ DisableUndoRecording(db: Database, bDisable: bool) -> bool """
        pass

    @staticmethod
    def DoHelpForCommand(cmdName):
        """ DoHelpForCommand(cmdName: str) """
        pass

    @staticmethod
    def Do_Cmd(menuString, IsSSetNeedRestore, bMenuMacro, IsHiddenCmd, bSynchronous):
        """ Do_Cmd(menuString: str, IsSSetNeedRestore: bool, bMenuMacro: bool, IsHiddenCmd: bool, bSynchronous: bool) """
        pass

    @staticmethod
    def DragDropLayoutTab(doc, index, isMoveOrCopy):
        """ DragDropLayoutTab(doc: Document, index: int, isMoveOrCopy: bool) """
        pass

    @staticmethod
    def DrawLineType(type, width, height):
        """ DrawLineType(type: ObjectId, width: int, height: int) -> IntPtr """
        pass

    @staticmethod
    def DrawLineWeight(weight, width, height):
        """ DrawLineWeight(weight: LineWeight, width: int, height: int) -> IntPtr """
        pass

    @staticmethod
    def DrawLineWeightLine(lineWeight, left, top, right, bottom):
        """ DrawLineWeightLine(lineWeight: LineWeight, left: int, top: int, right: int, bottom: int) -> IntPtr """
        pass

    @staticmethod
    def DropOpenFile(file):
        """ DropOpenFile(file: str) """
        pass

    @staticmethod
    def EnableDockControlBars(bEnable):
        """ EnableDockControlBars(bEnable: bool) """
        pass

    @staticmethod
    def EnableDWGResize(flag):
        """ EnableDWGResize(flag: bool) """
        pass

    @staticmethod
    def EnableFloatingWindows(bEnable):
        """ EnableFloatingWindows(bEnable: bool) """
        pass

    @staticmethod
    def EnableSysButtons(bEnable):
        """ EnableSysButtons(bEnable: bool) """
        pass

    @staticmethod
    def EntFirst():
        """ EntFirst() -> ObjectId """
        pass

    @staticmethod
    def EntLast():
        """ EntLast() -> ObjectId """
        pass

    @staticmethod
    def EntNext(entId, skipSubEnt=None):
        """
        EntNext(entId: ObjectId) -> ObjectId
        EntNext(entId: ObjectId, skipSubEnt: bool) -> ObjectId
        """
        pass

    @staticmethod
    def EvaluateTopLevelNetwork(db, bRelaxEvaluate):
        """ EvaluateTopLevelNetwork(db: Database, bRelaxEvaluate: bool) -> bool """
        pass

    @staticmethod
    def ExecuteApplicationStatusBarMenu(nId):
        """ ExecuteApplicationStatusBarMenu(nId: int) """
        pass

    @staticmethod
    def FlushGraphics():
        """ FlushGraphics() """
        pass

    @staticmethod
    def GetAcadFrameHandle():
        """ GetAcadFrameHandle() -> IntPtr """
        pass

    @staticmethod
    def GetAcadResourceIcon(sResId):
        """ GetAcadResourceIcon(sResId: str) -> Icon """
        pass

    @staticmethod
    def GetActualIndex(index):
        """ GetActualIndex(index: int) -> int """
        pass

    @staticmethod
    def GetApplicationFrameHWnd():
        """ GetApplicationFrameHWnd() -> IntPtr """
        pass

    @staticmethod
    def GetBlockImage(objectId, nImgWidth, nImgHeight, backgroundColor):
        """ GetBlockImage(objectId: ObjectId, nImgWidth: int, nImgHeight: int, backgroundColor: Color) -> IntPtr """
        pass

    @staticmethod
    def GetCommandAtLevelForDocument(level):
        """ GetCommandAtLevelForDocument(level: int) -> str """
        pass

    @staticmethod
    def GetCommandPromptString():
        """ GetCommandPromptString() -> str """
        pass

    @staticmethod
    def GetCommandVersion():
        """ GetCommandVersion() -> int """
        pass

    @staticmethod
    def GetCurrentEditBlock():
        """ GetCurrentEditBlock() -> ObjectId """
        pass

    @staticmethod
    def GetCurrentFindingContent():
        """ GetCurrentFindingContent() -> str """
        pass

    @staticmethod
    def GetCurrentObjectColor():
        """ GetCurrentObjectColor() -> Color """
        pass

    @staticmethod
    def GetCurrentViewportVisualStyleId():
        """ GetCurrentViewportVisualStyleId() -> ObjectId """
        pass

    @staticmethod
    def GetCustomSwatchImage(name, nWidth, nHeight):
        """ GetCustomSwatchImage(name: str, nWidth: int, nHeight: int) -> IntPtr """
        pass

    @staticmethod
    def GetDieselEvalString(text, bGrayed=None, bChecked=None):
        """
        GetDieselEvalString(text: str) -> str
        GetDieselEvalString(text: str, bGrayed: bool, bChecked: bool) -> (str, bool, bool)
        """
        pass

    @staticmethod
    def GetDimStyleImage(objectId, nImgWidth, nImgHeight, backgroundColor):
        """ GetDimStyleImage(objectId: ObjectId, nImgWidth: int, nImgHeight: int, backgroundColor: Color) -> IntPtr """
        pass

    @staticmethod
    def GetDockClientRect(excludeLayoutBar=None):
        """
        GetDockClientRect() -> Rect
        GetDockClientRect(excludeLayoutBar: bool) -> Rect
        """
        pass

    @staticmethod
    def GetDwgFrameIcon(doc):
        """ GetDwgFrameIcon(doc: Document) -> Icon """
        pass

    @staticmethod
    def GetFontImage(fontID):
        """ GetFontImage(fontID: ObjectId) -> IntPtr """
        pass

    @staticmethod
    def GetGradientDisplayText(*__args):
        """
        GetGradientDisplayText(gradientName: str) -> str
        GetGradientDisplayText(nHatchGradientNameEnum: int) -> str
        """
        pass

    @staticmethod
    def GetGradientName(displayText):
        """ GetGradientName(displayText: str) -> str """
        pass

    @staticmethod
    def GetGradientSwatchImage(displayText, angle, bShifted, startColor, stopColor, nWidth, nHeight):
        """ GetGradientSwatchImage(displayText: str, angle: float, bShifted: bool, startColor: Color, stopColor: Color, nWidth: int, nHeight: int) -> IntPtr """
        pass

    @staticmethod
    def GetGradientValue(displayText):
        """ GetGradientValue(displayText: str) -> int """
        pass

    @staticmethod
    def GetHideWarningDialogs(nType):
        """ GetHideWarningDialogs(nType: UInt32) -> bool """
        pass

    @staticmethod
    def GetLastCommandLines(lastLines, ignoreNull):
        """ GetLastCommandLines(lastLines: int, ignoreNull: bool) -> List[str] """
        pass

    @staticmethod
    def GetLastInsertBlockData(specifyScaleOnScreen, specifyRotationOnScreen):
        """ GetLastInsertBlockData(specifyScaleOnScreen: bool, specifyRotationOnScreen: bool) -> (bool, bool) """
        pass

    @staticmethod
    def GetLayoutThumbnail(doc, layoutName):
        """ GetLayoutThumbnail(doc: Document, layoutName: str) -> Bitmap """
        pass

    @staticmethod
    def GetMLeaderStyleImage(objectId, nImgWidth, nImgHeight, backgroundColor):
        """ GetMLeaderStyleImage(objectId: ObjectId, nImgWidth: int, nImgHeight: int, backgroundColor: Color) -> IntPtr """
        pass

    @staticmethod
    def GetMoreHideWarningDialogs(nType):
        """ GetMoreHideWarningDialogs(nType: UInt32) -> bool """
        pass

    @staticmethod
    def GetOpmWindow():
        """ GetOpmWindow() -> IntPtr """
        pass

    @staticmethod
    def GetPatSwatchImage(name, patternColor, backgroundColor, nWidth, nHeight):
        """ GetPatSwatchImage(name: str, patternColor: Color, backgroundColor: Color, nWidth: int, nHeight: int) -> IntPtr """
        pass

    @staticmethod
    def GetPredefinedVisualStyleGlobalName(localName):
        """ GetPredefinedVisualStyleGlobalName(localName: str) -> str """
        pass

    @staticmethod
    def GetProductbrandingName():
        """ GetProductbrandingName() -> str """
        pass

    @staticmethod
    def GetQpWindow():
        """ GetQpWindow() -> IntPtr """
        pass

    @staticmethod
    def GetRealHatchPreviewImage(nWidth, nHeight):
        """ GetRealHatchPreviewImage(nWidth: int, nHeight: int) -> IntPtr """
        pass

    @staticmethod
    def GetRedoHistory():
        """ GetRedoHistory() -> ObservableCollection[str] """
        pass

    @staticmethod
    def GetRefEditName():
        """ GetRefEditName() -> str """
        pass

    @staticmethod
    def GetStatusBarOsnapMenu(b3DOsnap, isDarkTheme):
        """ GetStatusBarOsnapMenu(b3DOsnap: bool, isDarkTheme: bool) -> MenuItem """
        pass

    @staticmethod
    def GetTableCellStyleImage(cellStyleName, nImgWidth, nImgHeight, backgroundColor):
        """ GetTableCellStyleImage(cellStyleName: str, nImgWidth: int, nImgHeight: int, backgroundColor: Color) -> IntPtr """
        pass

    @staticmethod
    def GetTableStyleImage(objectId, nImgWidth, nImgHeight, backgroundColor):
        """ GetTableStyleImage(objectId: ObjectId, nImgWidth: int, nImgHeight: int, backgroundColor: Color) -> IntPtr """
        pass

    @staticmethod
    def GetTextExtents(styleId, text, dHeight):
        """ GetTextExtents(styleId: ObjectId, text: str, dHeight: float) -> Point2d """
        pass

    @staticmethod
    def GetToolPaletteGroups(schemeName, pGroups):
        """ GetToolPaletteGroups(schemeName: str) -> (bool, StringCollection) """
        pass

    @staticmethod
    def GetUndoHistory():
        """ GetUndoHistory() -> ObservableCollection[str] """
        pass

    @staticmethod
    def GetUnitsConversion(fromUnits, toUnits):
        """ GetUnitsConversion(fromUnits: UnitsValue, toUnits: UnitsValue) -> float """
        pass

    @staticmethod
    def GetUnknownPatternSwatchImage(nWidth, nHeight):
        """ GetUnknownPatternSwatchImage(nWidth: int, nHeight: int) -> IntPtr """
        pass

    @staticmethod
    def GetUserDefinedSwatchImage(bDouble, patternColor, backgroundColor, nWidth, nHeight):
        """ GetUserDefinedSwatchImage(bDouble: bool, patternColor: Color, backgroundColor: Color, nWidth: int, nHeight: int) -> IntPtr """
        pass

    @staticmethod
    def GetVisualStyleEdgeColor(visualStyleId):
        """ GetVisualStyleEdgeColor(visualStyleId: ValueType) -> Color """
        pass

    @staticmethod
    def GetVisualStyleImage(objectId, size):
        """ GetVisualStyleImage(objectId: ObjectId, size: Size) -> IntPtr """
        pass

    @staticmethod
    def GetVisualStyleIntersectionEdgeColor(visualStyleId):
        """ GetVisualStyleIntersectionEdgeColor(visualStyleId: ValueType) -> Color """
        pass

    @staticmethod
    def GetVisualStyleObscuredEdgeColor(visualStyleId):
        """ GetVisualStyleObscuredEdgeColor(visualStyleId: ValueType) -> Color """
        pass

    @staticmethod
    def GetVisualStyles(objectIds, imageList):
        """ GetVisualStyles(objectIds: ObjectIdCollection, imageList: List[ImageSource]) """
        pass

    @staticmethod
    def GetWSUID(sWSName):
        """ GetWSUID(sWSName: str) -> str """
        pass

    @staticmethod
    def HistoryStatus():
        """ HistoryStatus() -> bool """
        pass

    @staticmethod
    def IconFilePath():
        """ IconFilePath() -> str """
        pass

    @staticmethod
    def InitDialog(bUseDialog):
        """ InitDialog(bUseDialog: bool) -> bool """
        pass

    @staticmethod
    def InitializeCommandLineFont():
        """ InitializeCommandLineFont() """
        pass

    @staticmethod
    def InvokeDataLinkManagerDialog(database, dialogMode, parentForm, objectId):
        """ InvokeDataLinkManagerDialog(database: Database, dialogMode: int, parentForm: Form) -> (DialogResult, ObjectId) """
        pass

    @staticmethod
    def InvokeDataTypeDialog(inDataType, inUnitType, sFormatIn, objValue, dialogOptions, parentForm, sTitle, sHelp, outDataType, outUnitType, sFormatOut):
        """ InvokeDataTypeDialog(inDataType: DataType, inUnitType: UnitType, sFormatIn: str, objValue: object, dialogOptions: int, parentForm: Form, sTitle: str, sHelp: str) -> (DialogResult, DataType, UnitType, str) """
        pass

    @staticmethod
    def InvokeOpmSetPropertyValue(prop, val, objIds, guid, mode):
        """ InvokeOpmSetPropertyValue(prop: object, val: object, objIds: ObjectIdCollection, guid: Guid, mode: OPMModeFlags) -> OPMStatus """
        pass

    @staticmethod
    def InvokeOptionsDialog(strPos, bInvokedAsChildDlg, defaultLabelIdInFileTab, bExpanded):
        """ InvokeOptionsDialog(strPos: str, bInvokedAsChildDlg: bool, defaultLabelIdInFileTab: UInt32, bExpanded: bool) """
        pass

    @staticmethod
    def InvokeStatusBarItemDeleted(ptr):
        """ InvokeStatusBarItemDeleted(ptr: IntPtr) """
        pass

    @staticmethod
    def InvokeStatusBarItemMouseDown(ptr, type, flag, point):
        """ InvokeStatusBarItemMouseDown(ptr: IntPtr, type: int, flag: int, point: Point) """
        pass

    @staticmethod
    def InvokeTableStyleDialog():
        """ InvokeTableStyleDialog() """
        pass

    @staticmethod
    def InvokeTrayItemCloseBubbleWindow(trayItemPtr):
        """ InvokeTrayItemCloseBubbleWindow(trayItemPtr: IntPtr) """
        pass

    @staticmethod
    def InvokeTrayItemShowBubbleWindow(title, description, iconType, hyperlink, hypertext, text, trayItemPtr):
        """ InvokeTrayItemShowBubbleWindow(title: str, description: str, iconType: BubbleWindowIconType, hyperlink: str, hypertext: str, text: str, trayItemPtr: IntPtr) """
        pass

    @staticmethod
    def Is3dVisualStyle(styleName):
        """ Is3dVisualStyle(styleName: str) -> bool """
        pass

    @staticmethod
    def IsAssociativeArrayRibbonContextApplicable(type, dataItem):
        """ IsAssociativeArrayRibbonContextApplicable(type: str, dataItem: object) -> bool """
        pass

    @staticmethod
    def IsCommandActive(name):
        """ IsCommandActive(name: str) -> bool """
        pass

    @staticmethod
    def IsCommandDefined(cmdName):
        """ IsCommandDefined(cmdName: str) -> bool """
        pass

    @staticmethod
    def IsCommandNameInUse(name):
        """ IsCommandNameInUse(name: str) -> CommandTypeFlags """
        pass

    @staticmethod
    def IsCommandReEntered(name):
        """ IsCommandReEntered(name: str) -> bool """
        pass

    @staticmethod
    def IsCoreCommand(name):
        """ IsCoreCommand(name: str) -> bool """
        pass

    @staticmethod
    def IsDiesel(text):
        """ IsDiesel(text: str) -> bool """
        pass

    @staticmethod
    def IsDocumentInBlockEditor(doc):
        """ IsDocumentInBlockEditor(doc: Document) -> bool """
        pass

    @staticmethod
    def IsDroppableExtension(extension):
        """ IsDroppableExtension(extension: str) -> bool """
        pass

    @staticmethod
    def IsFlagOn(id, bDefault):
        """ IsFlagOn(id: UInt32, bDefault: bool) -> bool """
        pass

    @staticmethod
    def IsInBlockEditor():
        """ IsInBlockEditor() -> bool """
        pass

    @staticmethod
    def IsInCommandStack(flags):
        """ IsInCommandStack(flags: CommandFlags) -> bool """
        pass

    @staticmethod
    def IsInCustomizeMode():
        """ IsInCustomizeMode() -> bool """
        pass

    @staticmethod
    def IsInDragging():
        """ IsInDragging() -> bool """
        pass

    @staticmethod
    def IsInPaperSpace():
        """ IsInPaperSpace() -> bool """
        pass

    @staticmethod
    def IsInputPending():
        """ IsInputPending() -> bool """
        pass

    @staticmethod
    def IsInQuiescentState():
        """ IsInQuiescentState() -> bool """
        pass

    @staticmethod
    def IsInStartup():
        """ IsInStartup() -> bool """
        pass

    @staticmethod
    def IsInTilemode():
        """ IsInTilemode() -> bool """
        pass

    @staticmethod
    def IsLinkedObjectExist(doc):
        """ IsLinkedObjectExist(doc: Document) -> bool """
        pass

    @staticmethod
    def IsLispCommandDefined(name):
        """ IsLispCommandDefined(name: str) -> bool """
        pass

    @staticmethod
    def IsMultiRedoAvaliable():
        """ IsMultiRedoAvaliable() -> bool """
        pass

    @staticmethod
    def IsNewTabCommandAllowed():
        """ IsNewTabCommandAllowed() -> bool """
        pass

    @staticmethod
    def IsNonDrawingDocumentDisabled():
        """ IsNonDrawingDocumentDisabled() -> bool """
        pass

    @staticmethod
    def IsOEM():
        """ IsOEM() -> bool """
        pass

    @staticmethod
    def IsOverrideActive():
        """ IsOverrideActive() -> bool """
        pass

    @staticmethod
    def IsPasteClipCommandAllowed():
        """ IsPasteClipCommandAllowed() -> bool """
        pass

    @staticmethod
    def IsPointOverToolbar(x, y):
        """ IsPointOverToolbar(x: int, y: int) -> bool """
        pass

    @staticmethod
    def IsTextEditorActive():
        """ IsTextEditorActive() -> bool """
        pass

    @staticmethod
    def IsUndoAvailable():
        """ IsUndoAvailable() -> bool """
        pass

    @staticmethod
    def IsVisualStyleDefault(visualStyleId):
        """ IsVisualStyleDefault(visualStyleId: ValueType) -> bool """
        pass

    @staticmethod
    def NewDocument():
        """ NewDocument() """
        pass

    @staticmethod
    def NotifyStatusBarServiceReady():
        """ NotifyStatusBarServiceReady() -> bool """
        pass

    @staticmethod
    def NumberToUnitsString(dValue):
        """ NumberToUnitsString(dValue: float) -> str """
        pass

    @staticmethod
    def OpenDocument():
        """ OpenDocument() """
        pass

    @staticmethod
    def Orbit():
        """ Orbit() """
        pass

    @staticmethod
    def Pan():
        """ Pan() """
        pass

    @staticmethod
    def PointOnScreen(pt):
        """ PointOnScreen(pt: Point3d) -> bool """
        pass

    @staticmethod
    def PostCommandPrompt():
        """ PostCommandPrompt() """
        pass

    @staticmethod
    def PostRouteMessageToDwgView(handle, message, wParam, lParam):
        """ PostRouteMessageToDwgView(handle: IntPtr, message: int, wParam: IntPtr, lParam: IntPtr) -> bool """
        pass

    @staticmethod
    def PreRouteMessageToDwgView(handle, message, wParam, lParam):
        """ PreRouteMessageToDwgView(handle: IntPtr, message: int, wParam: IntPtr, lParam: IntPtr) -> bool """
        pass

    @staticmethod
    def RawAngleToString(dValue):
        """ RawAngleToString(dValue: float) -> str """
        pass

    @staticmethod
    def RedrawGrips():
        """ RedrawGrips() """
        pass

    @staticmethod
    def RefreshDragCursor(hasDrawArea, isCopy, point):
        """ RefreshDragCursor(hasDrawArea: bool, isCopy: bool, point: Point) """
        pass

    @staticmethod
    def RegenEntity(entId):
        """ RegenEntity(entId: ObjectId) """
        pass

    @staticmethod
    def RegisterCommandLineWindow(window):
        """ RegisterCommandLineWindow(window: IntPtr) """
        pass

    @staticmethod
    def RegisterLeaveStartupUiCallback(func):
        """ RegisterLeaveStartupUiCallback(func: UiCallback) -> bool """
        pass

    @staticmethod
    def RegisterLispCommand(cmdName, lispName):
        """ RegisterLispCommand(cmdName: str, lispName: str) """
        pass

    @staticmethod
    def RegisterStartupUiCallback(ordering, func, delayInMs):
        """ RegisterStartupUiCallback(ordering: float, func: UiCallback, delayInMs: int) -> bool """
        pass

    @staticmethod
    def ReloadMenus(wsCurrentStr, bResetWorkspace, bIncrementalReloading):
        """ ReloadMenus(wsCurrentStr: str, bResetWorkspace: bool, bIncrementalReloading: bool) """
        pass

    @staticmethod
    def RemoveCommand(cmdGroupName, cmdGlobalName):
        """ RemoveCommand(cmdGroupName: str, cmdGlobalName: str) """
        pass

    @staticmethod
    def RestoreApplicationStatusBar():
        """ RestoreApplicationStatusBar() """
        pass

    @staticmethod
    def RunFindText(pStrCmd):
        """ RunFindText(pStrCmd: str) """
        pass

    @staticmethod
    def SelectObjects(ids):
        """ SelectObjects(ids: Array[ObjectId]) -> bool """
        pass

    @staticmethod
    def SendMenuStringToExecute(doc, menuString, bEchoString):
        """ SendMenuStringToExecute(doc: Document, menuString: str, bEchoString: bool) """
        pass

    @staticmethod
    def SetApplicationStatusBarProgressMeter(*__args):
        """ SetApplicationStatusBarProgressMeter(str: str, minimum: int, maximum: int)SetApplicationStatusBarProgressMeter(nPos: int) """
        pass

    @staticmethod
    def SetCurrentViewportVisualStyle(visualStyleId):
        """ SetCurrentViewportVisualStyle(visualStyleId: ObjectId) """
        pass

    @staticmethod
    def SetCurrentWorkspace(wsCurrent, bRestoreUI, bAutoSaveWS):
        """ SetCurrentWorkspace(wsCurrent: str, bRestoreUI: bool, bAutoSaveWS: bool) -> bool """
        pass

    @staticmethod
    def SetFocusToDwgView():
        """ SetFocusToDwgView() """
        pass

    @staticmethod
    def SetHideWarningDialogs(nType, bValue):
        """ SetHideWarningDialogs(nType: UInt32, bValue: bool) """
        pass

    @staticmethod
    def SetIsDragLayout(isDragging):
        """ SetIsDragLayout(isDragging: bool) """
        pass

    @staticmethod
    def SetMoreHideWarningDialogs(nType, bValue):
        """ SetMoreHideWarningDialogs(nType: UInt32, bValue: bool) """
        pass

    @staticmethod
    def SetPropertiesInDatabaseForTPPlayback(itemId, bSet):
        """ SetPropertiesInDatabaseForTPPlayback(itemId: Guid, bSet: bool) """
        pass

    @staticmethod
    def SetQnewTemplateAfterInitialSetup():
        """ SetQnewTemplateAfterInitialSetup() """
        pass

    @staticmethod
    def SetQuickViewWindowHandle(hWnd):
        """ SetQuickViewWindowHandle(hWnd: IntPtr) """
        pass

    @staticmethod
    def SetRecoverAllMode(bOn):
        """ SetRecoverAllMode(bOn: bool) """
        pass

    @staticmethod
    def SetRecoverRequestedMode(bOn):
        """ SetRecoverRequestedMode(bOn: bool) """
        pass

    @staticmethod
    def SetStatusBarContainerHeight(height):
        """ SetStatusBarContainerHeight(height: int) """
        pass

    @staticmethod
    def SetStatusBarContent(rootVisual):
        """ SetStatusBarContent(rootVisual: UIElement) -> bool """
        pass

    @staticmethod
    def SetUndoMark(begin):
        """ SetUndoMark(begin: bool) -> bool """
        pass

    @staticmethod
    def ShowHideTextWindow(bShow):
        """ ShowHideTextWindow(bShow: bool) """
        pass

    @staticmethod
    def ShowLineTypeDialog():
        """ ShowLineTypeDialog() """
        pass

    @staticmethod
    def ShowMeshConversionTaskDialog():
        """ ShowMeshConversionTaskDialog() -> MeshConversionType """
        pass

    @staticmethod
    def ShowOldLayoutTab(bShowTab):
        """ ShowOldLayoutTab(bShowTab: bool) """
        pass

    @staticmethod
    def StartToolbarDragDrop(menuGroups, names, tags, commands, helpStrs, smallImages, largeImages, resourceFiles):
        """ StartToolbarDragDrop(menuGroups: StringCollection, names: StringCollection, tags: StringCollection, commands: StringCollection, helpStrs: StringCollection, smallImages: StringCollection, largeImages: StringCollection, resourceFiles: StringCollection) -> bool """
        pass

    @staticmethod
    def StrCompareNatural(str1, str2):
        """ StrCompareNatural(str1: str, str2: str) -> int """
        pass

    @staticmethod
    def StringToAngle(sText, dValue):
        """ StringToAngle(sText: str, dValue: float) -> (bool, float) """
        pass

    @staticmethod
    def StringToRawAngle(sText, dValue):
        """ StringToRawAngle(sText: str, dValue: float) -> (bool, float) """
        pass

    @staticmethod
    def TransferToolbarBitmaps():
        """ TransferToolbarBitmaps() """
        pass

    @staticmethod
    def UcsToDisplay(ucsPoint, bPaperSpace):
        """ UcsToDisplay(ucsPoint: Point3d, bPaperSpace: bool) -> Point3d """
        pass

    @staticmethod
    def UnitsStringToNumber(sText, dValue):
        """ UnitsStringToNumber(sText: str, dValue: float) -> (bool, float) """
        pass

    @staticmethod
    def UnregisterCommandLineWindow(window):
        """ UnregisterCommandLineWindow(window: IntPtr) """
        pass

    @staticmethod
    def UpdateLayoutSelection():
        """ UpdateLayoutSelection() """
        pass

    @staticmethod
    def ViewHasChanged():
        """ ViewHasChanged() -> bool """
        pass

    @staticmethod
    def ViewportChange(x, y):
        """ ViewportChange(x: int, y: int) """
        pass

    @staticmethod
    def ViewportCycle():
        """ ViewportCycle() """
        pass

    @staticmethod
    def ViewportResize(sx, sy, ex, ey, split):
        """ ViewportResize(sx: Single, sy: Single, ex: Single, ey: Single, split: bool) """
        pass

    @staticmethod
    def ViewportTypeChange(id):
        """ ViewportTypeChange(id: int) """
        pass

    @staticmethod
    def visualStyleId(visualStyleName):
        """ visualStyleId(visualStyleName: str) -> ObjectId """
        pass

    @staticmethod
    def visualStyleName(id):
        """ visualStyleName(id: ObjectId) -> str """
        pass

    @staticmethod
    def VpMaxCommand():
        """ VpMaxCommand() """
        pass

    @staticmethod
    def VpMinCommand():
        """ VpMinCommand() """
        pass

    @staticmethod
    def WcMatchEx(str, pattern, ignoreCase):
        """ WcMatchEx(str: str, pattern: str, ignoreCase: bool) -> bool """
        pass

    @staticmethod
    def WorkspaceVisible(strWS):
        """ WorkspaceVisible(strWS: str) -> bool """
        pass

    @staticmethod
    def WriteToCommandLine(message):
        """ WriteToCommandLine(message: str) """
        pass

    @staticmethod
    def WriteUndoBoundary(db, boundary, name):
        """ WriteUndoBoundary(db: Database, boundary: UndoBoundaryEnum, name: str) -> bool """
        pass

    @staticmethod
    def Zoom():
        """ Zoom() """
        pass

    @staticmethod
    def ZoomAuto(type, a1, a2, a3, a4):
        """ ZoomAuto(type: Int16, a1: float, a2: float, a3: float, a4: float) """
        pass

    @staticmethod
    def ZoomObjects(use3d):
        """ ZoomObjects(use3d: bool) """
        pass

    CaptureOnLayoutSwitch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: CaptureOnLayoutSwitch() = value
"""


    ApplicationStatusBarMenu = None
    ApplicationToolbarsMenu = None
    BubbleWindowIconType = None
    ImpliedSelectionIsActive = False
    IsCuiCommandEnabled = True
    IsEditorReady = True
    IsOsThemed = True
    IsScriptActive = False
    MenuBuilder = None
    MeshConversionType = None
    OSnapCommand = None
    SavingStartupTools = None
    SysVarInProgress = ''


class ViewUtil(object):
    """ ViewUtil() """
    @staticmethod
    def acquireView(nVPNum, pView, pGraphicsKernel):
        """ acquireView(nVPNum: int, pView: AcGsView**, pGraphicsKernel: AcGsGraphicsKernel**) """
        pass

    @staticmethod
    def GetCurrentViewportNumber():
        """ GetCurrentViewportNumber() -> int """
        pass

    @staticmethod
    def releaseView(pView, pGraphicsKernel):
        """ releaseView(pView: AcGsView**, pGraphicsKernel: AcGsGraphicsKernel**) """
        pass

    GsLensLength = 50.0


class VisualStyleSet(RXObject):
    """ VisualStyleSet() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Intialize(self, objIds, pRemoveFromSet, pOverrideColor):
        """ Intialize(self: VisualStyleSet, objIds: ObjectIdCollection, pRemoveFromSet: VisualStyleSet, pOverrideColor: Color) """
        pass

    def RemoveAll(self):
        """ RemoveAll(self: VisualStyleSet) """
        pass

    def Replace(self, objIds, pRemoveFromSet):
        """ Replace(self: VisualStyleSet, objIds: ObjectIdCollection, pRemoveFromSet: VisualStyleSet) """
        pass


class WebMobGlobals(object):
    """ WebMobGlobals() """
    _acwindows = None


class WebMobileRecentDocs(object):
    """ WebMobileRecentDocs() """
    @staticmethod
    def AddRecentDocument(filePath):
        """ AddRecentDocument(filePath: str) -> bool """
        pass

    def OpenCallback(self, *args): #cannot find CLR method
        """ WebMobileRecentDocsCallback(A_0: object, A_1: IntPtr) """
        pass

    @staticmethod
    def OpenDocument(filePath):
        """ OpenDocument(filePath: str) -> bool """
        pass

    @staticmethod
    def SupressRecentDocuments(val):
        """ SupressRecentDocuments(val: bool) """
        pass


class WebMobileRecentDocsCallback(MulticastDelegate):
    """ WebMobileRecentDocsCallback(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, filePath, callback, obj):
        """ BeginInvoke(self: WebMobileRecentDocsCallback, filePath: str, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: WebMobileRecentDocsCallback, result: IAsyncResult) """
        pass

    def Invoke(self, filePath):
        """ Invoke(self: WebMobileRecentDocsCallback, filePath: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class WebServiceMultipartRequest(object):
    """
    WebServiceMultipartRequest(request: HttpWebRequest, boundary: str)
    WebServiceMultipartRequest(request: HttpWebRequest)
    """
    def AddFileContentPart(self, fileStream, *__args):
        """ AddFileContentPart(self: WebServiceMultipartRequest, fileStream: Stream, name: str, fileName: str)AddFileContentPart(self: WebServiceMultipartRequest, fileStream: Stream, paramName: str, fileName: str, contentType: str) """
        pass

    def BeginMultipartContent(self):
        """ BeginMultipartContent(self: WebServiceMultipartRequest) """
        pass

    def EndMultipartContent(self):
        """ EndMultipartContent(self: WebServiceMultipartRequest) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, request, boundary=None):
        """
        __new__(cls: type, request: HttpWebRequest, boundary: str)
        __new__(cls: type, request: HttpWebRequest)
        """
        pass

    Parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parameters(self: WebServiceMultipartRequest) -> Dictionary[str, str]

"""

    Request = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Request(self: WebServiceMultipartRequest) -> HttpWebRequest

"""



class WebServicePostRequest(object):
    """
    WebServicePostRequest(request: HttpWebRequest)
    WebServicePostRequest(request: HttpWebRequest, skipParameterFormatting: bool)
    """
    def UpdateRequestContent(self):
        """ UpdateRequestContent(self: WebServicePostRequest) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, request, skipParameterFormatting=None):
        """
        __new__(cls: type, request: HttpWebRequest)
        __new__(cls: type, request: HttpWebRequest, skipParameterFormatting: bool)
        """
        pass

    Parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parameters(self: WebServicePostRequest) -> Dictionary[str, str]

"""

    Request = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Request(self: WebServicePostRequest) -> HttpWebRequest

"""



class WebServiceRequestParam(object):
    """
    WebServiceRequestParam(name: str, value: str)
    WebServiceRequestParam(name: Array[Byte], value: Array[Byte])
    """
    @staticmethod # known case of __new__
    def __new__(self, name, value):
        """
        __new__(cls: type, name: str, value: str)
        __new__(cls: type, name: Array[Byte], value: Array[Byte])
        """
        pass


class WebServiceRequestParsingMode(Enum):
    """ enum WebServiceRequestParsingMode, values: ParseForHeaderArguments (2), ParseForInlineQuery (1), ParseForRequestContent (0), ParseForSignatureBaseString (3) """
    ParseForHeaderArguments = None
    ParseForInlineQuery = None
    ParseForRequestContent = None
    ParseForSignatureBaseString = None
    value__ = None


class WebServicesRequestUrlCode(Enum):
    """ enum WebServicesRequestUrlCode, values: AccountServerUrl (0), ExchangeUrl (10), LoggedInUrlEndPoint (1), NitrogenStorageEndPoint (8), NitrousStorageEndPoint (9), RegisterEndPoint (2), ShareUrl (7), StorageApiUrl (5), StorageOnlineUrl (4), StorageRoot (6), UpdateProfileEndPoint (3) """
    AccountServerUrl = None
    ExchangeUrl = None
    LoggedInUrlEndPoint = None
    NitrogenStorageEndPoint = None
    NitrousStorageEndPoint = None
    RegisterEndPoint = None
    ShareUrl = None
    StorageApiUrl = None
    StorageOnlineUrl = None
    StorageRoot = None
    UpdateProfileEndPoint = None
    value__ = None


class WSUtils(object):
    """ WSUtils() """
    @staticmethod
    def GetLoginUserName():
        """ GetLoginUserName() -> str """
        pass

    @staticmethod
    def GetO2tk(scopes):
        """ GetO2tk(scopes: str) -> str """
        pass

    @staticmethod
    def GetServer():
        """ GetServer() -> Server """
        pass

    @staticmethod
    def GetUrl(urlCode):
        """ GetUrl(urlCode: WebServicesRequestUrlCode) -> str """
        pass

    @staticmethod
    def IsLoggedIn():
        """ IsLoggedIn() -> bool """
        pass

    @staticmethod
    def IsLoginValid():
        """ IsLoginValid() -> bool """
        pass

    @staticmethod
    def Login():
        """ Login() -> bool """
        pass

    @staticmethod
    def SignRequest(url, params, httpMethod, parsingMode, consumerKey, consumerSecret):
        """ SignRequest(url: str, params: Array[WebServiceRequestParam], httpMethod: HttpMethod, parsingMode: WebServiceRequestParsingMode, consumerKey: str, consumerSecret: str) -> str """
        pass

    @staticmethod
    def SignUrlForBrowser(url, isEncoded):
        """ SignUrlForBrowser(url: str, isEncoded: bool) -> str """
        pass

    Server = None


class ZipExtractor(object):
    """
    ZipExtractor(zipFile: str, password: str)
    ZipExtractor(zipFile: str)
    """
    def Dispose(self):
        """ Dispose(self: ZipExtractor) """
        pass

    def Extract(self, file, destination):
        """ Extract(self: ZipExtractor, file: ZipFileInfo, destination: str) """
        pass

    def ExtractAll(self, destination):
        """ ExtractAll(self: ZipExtractor, destination: str) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, zipFile, password=None):
        """
        __new__(cls: type, zipFile: str, password: str)
        __new__(cls: type, zipFile: str)
        """
        pass

    Files = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Files(self: ZipExtractor) -> IEnumerable[ZipFileInfo]

"""


    ZipFileInfo = None


# variables with complex values

