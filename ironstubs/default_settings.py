import os

PATHS = [
    # | Local Binaries
    # | AutoCAD
    # 'D:\\Python\\ironpython-stubs\\bin'
    'C:\\Program Files\\Autodesk\\AutoCAD 2021',
    # 'C:\\Program Files\\Autodesk\\AutoCAD 2021\\en-US',
    # | AutoCAD Architecture
    # 'C:\\Program Files\\Autodesk\\AutoCAD 2021\\ACA',
    # | Civil 3D
    # 'C:\\Program Files\\Autodesk\\AutoCAD 2021\\C3D',
    # 'C:\\Program Files\\Autodesk\\AutoCAD 2021\\C3D\\Dynamo',
    # | Map 3D
    # 'C:\\Program Files\\Autodesk\\AutoCAD 2021\\Map',
    # 'C:\\Program Files\\Autodesk\\AutoCAD 2021\\Map\\bin\\GisPlatform',
    # | Revit
    # 'C:\\Program Files\\Autodesk\\Revit 2021',
    # 'C:\\Program Files\\Autodesk\\Revit 2021\\en-US',
    # | Tekla Structures
    # 'C:\\Program Files\\Tekla Structures\\2017\\nt\\bin\\plugins',
    # | Dynamo
    # 'C:\\Program Files\\Dynamo\\Dynamo Core\\2.5',
    # 'C:\\Program Files\\Dynamo\Dynamo Core\\1.3',
    # 'C:\\Program Files\\Autodesk\\Revit 2021\\AddIns\\DynamoForRevit',
    # 'C:\\Program Files\\Dynamo\Dynamo Revit\\1.3\\Revit_2017',
    # | Rhino
    # 'C:\\Program Files\\Rhinoceros 5 (64-bit)\\System',
    # Grasshopper
    # 'C:\\Users\\gtalarico\\AppData\\Roaming\\McNeel\\Rhinoceros\\5.0\\Plug-ins\\Grasshopper (b45a29b1-4343-4035-989e-044e8580d9cf)\\0.9.76.0'
    ]

ASSEMBLIES = [
    # | Ironpython
    'IronPython.Wpf',
    # | Windows
    'PresentationCore',
    'PresentationFramework',
    'WindowsBase',
    # | System
    'System',
    'System.Drawing',
    'System.Windows.Forms',
    'System.Core',
    'System.Data',
    'System.Data.DataSetExtensions',
    'System.Net.Http',
    'System.Xml',
    # | Dynamo
    'ProtoGeometry',
    'DSCoreNodes',
    'DSOffice',
    'Tessellation',
    'GeometryColor',
    # | Rhino
    # 'Rhino3dmIO',
    # 'RhinoCommon',
    # | Grasshopper
    # 'Grasshopper',
    # 'GH_IO',
    # 'GH_Util',
    # | Tekla Structures
    # 'Tekla.Structures',
    # 'Tekla.Structures.Drawing',
    # 'Tekla.Structures.Model',
    # 'Tekla.Structures.Plugins',
    # | Dynamo for Civil 3D
    'AutoCADNodes',
    'AutoCADNodesUI',
    'Civil3DNodes',
    'AcDynamoServices',
    # | Civil 3D
    'AeccDbMgd',
    'AeccPressurePipesMgd',
    # | Map 3D
    'Autodesk.Map.Platform',
    'Autodesk.Map.Platform.Utils',
    'OSGeo.MapGuide.Foundation',
    'OSGeo.MapGuide.Geometry',
    'OSGeo.MapGuide.PlatformBase',
    # | AutoCAD Architecture
    'AecBaseMgd',
    'AecPropDataMgd',
    # | AutoCAD
    'accoremgd',
    'acdbmgd',
    'acdbmgdbrep',
    'Autodesk.AutoCAD.Interop',
    'Autodesk.AutoCAD.Interop.Common'
]

BUILTINS = [
    'clr',
    'wpf'
    ]

ASSEMBLIES.extend(BUILTINS)
ASSEMBLIES.sort()

REVIT_ASSEMBLIES = [
    # | Revit
    'RevitAPI',
    'RevitAPIUI',
    'RevitServices',
    'RevitNodes',
    ]

CIVIL3D_ASSEMBLIES = [
    # | Dynamo for Civil 3D
    'AutoCADNodes',
    'AutoCADNodesUI',
    'Civil3DNodes',
    'AcDynamoServices',
    # | Civil 3D
    'AeccDbMgd',
    'AeccPressurePipesMgd',
    # | Map 3D
    'Autodesk.Map.Platform',
    'Autodesk.Map.Platform.Utils',
    'OSGeo.MapGuide.Foundation',
    'OSGeo.MapGuide.Geometry',
    'OSGeo.MapGuide.PlatformBase',
    # | AutoCAD Architecture
    'AecBaseMgd',
    'AecPropDataMgd',
    # | AutoCAD
    'acmgd',
    'acdbmgd',
    'accoremgd',
    'acdbmgdbrep',
    'Autodesk.AutoCAD.Interop',
    'Autodesk.AutoCAD.Interop.Common'
]

AUTOCAD_ASSEMBLIES = [
    # 'acmgd',
    'acdbmgd',
    # 'accoremgd'
]

AUTOCAD_NAMESPACES = [
    'Autodesk.AutoCAD',
    'Autodesk.AutoCAD.Colors',
    'Autodesk.AutoCAD.ComponentModel',
    'Autodesk.AutoCAD.DatabaseServices',
    'Autodesk.AutoCAD.DatabaseServices.Filters',
    'Autodesk.AutoCAD.DatabaseServices.Internal',
    'Autodesk.AutoCAD.Geometry',
    'Autodesk.AutoCAD.GraphicsInterface',
    'Autodesk.AutoCAD.GraphicsSystem',
    'Autodesk.AutoCAD.Internal',
    'Autodesk.AutoCAD.LayerManager',
    'Autodesk.AutoCAD.Runtime'
]


# | If running inside Revit, Process Revit Assemblies Only
try:
    __revit__
except NameError:
    pass
else:
    ASSEMBLIES = CIVIL3D_ASSEMBLIES
