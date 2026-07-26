#!/bin/bash

SAMPLES="qrvideo_hflip_90.mov \
        qrvideo_hflip_270.mov \
        qrvideo_vflip.mov \
        vp9_audfirst.webm"

mkdir -p test/samples
for s in $SAMPLES ; do
    curl -o test/samples/$s https://storage.googleapis.com/ffms2tests/$s
done
tar czf ffms2-samples.tar.gz test
rm -rv test
