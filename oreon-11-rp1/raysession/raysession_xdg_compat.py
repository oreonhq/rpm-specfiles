# raysession_xdg_compat.py: Patch system xdg to provide top-level helpers
from xdg import BaseDirectory
import sys
from pathlib import Path

def xdg_data_home():
    return Path(BaseDirectory.xdg_data_home)

def xdg_config_home():
    return Path(BaseDirectory.xdg_config_home)

def xdg_cache_home():
    return Path(BaseDirectory.xdg_cache_home)

def xdg_data_dirs():
    return [Path(p) for p in BaseDirectory.xdg_data_dirs]

def xdg_config_dirs():
    return [Path(p) for p in BaseDirectory.xdg_config_dirs]

import types
xdg_mod = sys.modules.get('xdg')
if xdg_mod:
    xdg_mod.xdg_data_home = xdg_data_home
    xdg_mod.xdg_config_home = xdg_config_home
    xdg_mod.xdg_cache_home = xdg_cache_home
    xdg_mod.xdg_data_dirs = xdg_data_dirs
    xdg_mod.xdg_config_dirs = xdg_config_dirs
