from pathlib import Path


def update_config(conf):
    # This works when installed and when in buildroot.
    conf['pre_existing_data_dir'] = str(
        Path(__file__).parents[4] / 'share/cartopy')
