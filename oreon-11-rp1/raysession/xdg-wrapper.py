# Minimal xdg compatibility wrapper for RaySession
# Provides xdg.xdg_data_home() etc. using system pyxdg
from xdg import BaseDirectory
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
