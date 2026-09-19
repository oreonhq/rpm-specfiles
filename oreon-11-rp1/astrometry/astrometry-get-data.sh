#!/bin/sh

set -e

# 41xx series - 2000 to 22 arcmin
mkdir -p astrometry-data-4107-4119
cd astrometry-data-4107-4119
for ((i=7; i<=19; i++)); do
        I=$(printf %02i $i)
        wget -c http://data.astrometry.net/4100/index-41$I.fits
done
cd ..
tar -I 'zstd -9' -cf astrometry-data-4107-4119.tar.zst astrometry-data-4107-4119

# 5206 series - 16 to 22 arcmin
mkdir -p astrometry-data-5206
cd astrometry-data-5206
for ((i=0; i<=47; i++)); do
        I=$(printf %02i $i)
        wget -c https://portal.nersc.gov/project/cosmo/temp/dstn/index-5200/LITE/index-5206-$I.fits
done
cd ..
tar -I 'zstd -9' -cf astrometry-data-5206.tar.zst astrometry-data-5206

# 5205 series - 11 to 16 arcmin
mkdir -p astrometry-data-5205
cd astrometry-data-5205
for ((i=0; i<=47; i++)); do
        I=$(printf %02i $i)
        wget -c https://portal.nersc.gov/project/cosmo/temp/dstn/index-5200/LITE/index-5205-$I.fits
done
cd ..
tar -I 'zstd -9' -cf astrometry-data-5205.tar.zst astrometry-data-5205


#Clean up
rm -rf astrometry-data-4107-4119
rm -rf astrometry-data-5206
rm -rf astrometry-data-5205
