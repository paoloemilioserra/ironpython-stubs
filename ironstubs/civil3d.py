"""
MIT LICENSE
https://github.com/gtalarico/ironpython-stubs
Gui Talarico

-----------------------------------------------------------------

This file is intended to be executed from within Civil 3D.
Takes about 3 min

"""

import clr
import sys
sys.path.append(r'C:\Program Files (x86)\IronPython 2.7\Lib')
import os
import json
from pprint import pprint

STUBS_FOLDER = 'stubs'
DUMP_JSON = True
OVERWRITE = True

# Setp Dir First
PKG_DIR = os.path.dirname(__file__)
PROJECT_DIR = os.path.dirname(PKG_DIR)
release_dir = os.path.join(PROJECT_DIR, 'release', STUBS_FOLDER)
os.chdir(PROJECT_DIR)
sys.path.append(PKG_DIR)

# from utils.logger import logger
from utils.helper import Timer
from default_settings import PATHS, CIVIL3D_ASSEMBLIES, AUTOCAD_ASSEMBLIES, AUTOCAD_NAMESPACES
from make_stubs import make, dump_json_log

# Add Paths
# PATHS.append(os.path.join(PROJECT_DIR, 'bin'))
[sys.path.append(p) for p in PATHS]


# clr.AddReference('acdbmgd')
clr.AddReferenceToFile('acdbmgd.dll')
if False:
    clr.AddReference('acmgd')
    clr.AddReference('accoremgd')
    clr.AddReference('AecBaseMgd')
    clr.AddReference('AecPropDataMgd')
    clr.AddReference('AeccDbMgd')
    clr.AddReference('AeccPressurePipesMgd')
    clr.AddReference('acdbmgdbrep')
    clr.AddReference('System.Windows.Forms')
    clr.AddReference('AutoCADNodes')
    clr.AddReference('Civil3DNodes')

timer = Timer()
for assembly_name in AUTOCAD_ASSEMBLIES:
    try:
        # if True:
        assembly_dict = make(release_dir, assembly_name,
                             overwrite=OVERWRITE,
                             quiet=True)
        if DUMP_JSON:
            dump_json_log(assembly_dict)
    except:
        pass


print('Done: {} seconds'.format(timer.stop()))
