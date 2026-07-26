#!/bin/bash -e

CMSIS_VERSION=9fe411cef1cef5de58e5957b89760759de44e393
CMSIS_SVD_DATA_VERSION=05a9562ec59b87945a8d7177a4b08b7aa2f2fd58

if [ -e "cmsis-${CMSIS_VERSION}-clean.tar.xz" ]; then
echo "Not downloading cmsis-${CMSIS_VERSION}-clean.tar.xz again!"
else
# The license for this tarball is complicated, but the headers are under the
# BSD-3-Clause license, so we only package them.
wget -nc https://github.com/ARM-software/CMSIS/archive/${CMSIS_VERSION}/cmsis-${CMSIS_VERSION}.tar.gz
tar xf cmsis-${CMSIS_VERSION}.tar.gz
tar cJf cmsis-${CMSIS_VERSION}-clean.tar.xz \
    CMSIS-${CMSIS_VERSION}/README.md \
    CMSIS-${CMSIS_VERSION}/CMSIS/Include/
rm -r CMSIS-${CMSIS_VERSION}/
fi

if [ -e "cmsis_svd_data-${CMSIS_SVD_DATA_VERSION}-clean.tar.xz" ]; then
echo "Not downloading cmsis_svd_data-${CMSIS_SVD_DATA_VERSION}-clean.tar.xz again!"
else
# This is basically a "collection of random stuff" from various vendors, under
# various licenses. Some licenses are non-free and some are actively hostile,
# but we only need a rather small portion under a good license:
# - Atmel: Apache-2.0 AND BSD-Source-Code
# - Espressif: Apache-2.0
# - Espressif-Community: Apache-2.0 OR MIT
# - Kendryte-Community: ISC
# - Nordic: BSD-3-Clause
# - NXP/L*: Proprietary, so not included.
# - NXP/Q*: Unknown, so not included.
# - NXP/M*: BSD-3-Clause
# - RaspberryPi: BSD-3-Clause
# - Renesas: Proprietary
# - SiFive-Community: ISC AND (Apache-2.0 OR MIT)
# - STMicro: Apache-2.0 AND Proprietary, so only a subset included.
# These directories are not used by TinyGo, so are not kept:
# - ARM_SAMPLE: BSD-3-Clause
# - Allwinner-Community: Apache-2.0 OR MIT
# - ArteryTek: BSD-3-Clause
# - Cypress: Apache-2.0
# - Freescale: Proprietary
# - Fujitsu: Proprietary
# - GigaDevice: Apache-2.0
# - Holtek: Proprietary
# - Infineon: Proprietary
# - Nuvoton: Unknown
# - SiliconLabs: Zlib
# - Spansion: Proprietary
# - TexasInstruments: Proprietary
# - Toshiba: Unknown
wget -nc https://github.com/cmsis-svd/cmsis-svd-data/archive/${CMSIS_SVD_DATA_VERSION}/cmsis_svd_data-${CMSIS_SVD_DATA_VERSION}.tar.gz
tar xf cmsis_svd_data-${CMSIS_SVD_DATA_VERSION}.tar.gz
mapfile -t clean_stmicro < <(grep -Rl '^ *SPDX-License-Identifier: Apache-2.0$' \
                             cmsis-svd-data-${CMSIS_SVD_DATA_VERSION}/data/STMicro/*.svd)
tar cJf cmsis_svd_data-${CMSIS_SVD_DATA_VERSION}-clean.tar.xz \
    cmsis-svd-data-${CMSIS_SVD_DATA_VERSION}/data/Atmel/ \
    cmsis-svd-data-${CMSIS_SVD_DATA_VERSION}/data/Espressif/ \
    cmsis-svd-data-${CMSIS_SVD_DATA_VERSION}/data/Espressif-Community/ \
    cmsis-svd-data-${CMSIS_SVD_DATA_VERSION}/data/Kendryte-Community/ \
    cmsis-svd-data-${CMSIS_SVD_DATA_VERSION}/data/Nordic/ \
    cmsis-svd-data-${CMSIS_SVD_DATA_VERSION}/data/NXP/M* \
    cmsis-svd-data-${CMSIS_SVD_DATA_VERSION}/data/RaspberryPi/ \
    cmsis-svd-data-${CMSIS_SVD_DATA_VERSION}/data/SiFive-Community/ \
    "${clean_stmicro[@]}"
rm -r cmsis-svd-data-${CMSIS_SVD_DATA_VERSION}/
fi
