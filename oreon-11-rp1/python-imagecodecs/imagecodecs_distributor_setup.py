import platform

def customize_build(EXTENSIONS, OPTIONS):
    """Customize build for Fedora"""

    del EXTENSIONS['apng']  # apng patch not commonly available
    del EXTENSIONS['bitshuffle']  # Uses 3rdparty source
    del EXTENSIONS['brunsli']  # not available on Fedora
    del EXTENSIONS['jetraw']  # commercial
    del EXTENSIONS['jpegls']  # Fedora's charls is too old at the moment
    del EXTENSIONS['jpegsof3']  # Uses 3rdparty source
    del EXTENSIONS['jpegxl']  # requires static linking?
    del EXTENSIONS['ljpeg']  # Uses 3rdparty source
    del EXTENSIONS['lz4f']  # requires static linking
    del EXTENSIONS['lzf']  # Uses 3rdparty source
    del EXTENSIONS['lzham']  # Uses 3rdparty source
    del EXTENSIONS['mozjpeg']  # Win32 only
    del EXTENSIONS['pglz']  # Uses 3rdparty source
    del EXTENSIONS['qoi']  # Uses 3rdparty source
    del EXTENSIONS['rgbe']  # Uses 3rdparty source
    del EXTENSIONS['spng']  # Uses 3rdparty source
    EXTENSIONS['jpeg2k']['include_dirs'].extend(
        (
            '/usr/include/openjpeg-2.4',
            '/usr/include/openjpeg-2.5',
        )
    )
    del EXTENSIONS['jpeg2k']  # Uses 3rdparty source to use private function - https://github.com/cgohlke/imagecodecs/issues/77
    EXTENSIONS['jpegxr']['include_dirs'].append('/usr/include/jxrlib')
    EXTENSIONS['zopfli']['include_dirs'].append('/usr/include/zopfli')

    if platform.machine() == 's390x':
        del EXTENSIONS['lzfse'] # Not supported on big-endian
    # New or changed in 2024.9.22
    del EXTENSIONS['bcn']  # not available in Fedora
    del EXTENSIONS['h5checksum']  # uses 3rdparty source
    EXTENSIONS['jpeg8']['sources'] = []  # requires libjpeg-turbo v3
    del EXTENSIONS['jpegxs']  # not available on Fedora
    del EXTENSIONS['lzo']  # Uses 3rdparty source
    del EXTENSIONS['pcodec']  # Uses 3rdparty source
    del EXTENSIONS['quantize']  # Uses 3rdparty source
    del EXTENSIONS['rcomp']  # Uses 3rdparty source
    del EXTENSIONS['sperr']  # Uses 3rdparty source
    del EXTENSIONS['sz3']  # Uses 3rdparty source
    del EXTENSIONS['ultrahdr']  # Uses 3rdparty source
