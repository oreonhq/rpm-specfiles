#!/bin/bash

# SWORD's gSOAP bindings contain a file at bindings/gsoap/include/stdsoap.h
# that is labeled "All rights reserved." We therefore have to repack the
# tarball to eliminate this file. Doing so most likely ruins the gSOAP
# bindings, so we just remove the gSOAP bindings altogether.
#
# The Objective C bindings have the same problem as the gSOAP bindings.
#
# There's some win32-related code that has a similar problem too.
#
# Also some sort of PalmOS application binary needs removed.
#
# We also remove the Android bindings since they contain a prebuilt .jar file.
# This could be handled in %prep but it's just as easy and probably a bit
# faster to do it here.

set -e

wget http://www.crosswire.org/ftpmirror/pub/sword/source/v1.9/sword-1.9.0.tar.gz
test "$(sha512sum sword-1.9.0.tar.gz | cut -d' ' -f1)" = "9ed3fbb5024af1f93b1473bae0d95534d02a5b00b3c9d41a0f855cee8106dc4e330844080adbee7c3f74c0e5ce1480bf16c87c842421337a341f641bae11137f"
tar -xf sword-1.9.0.tar.gz
rm sword-1.9.0.tar.gz
rm -r sword-1.9.0/bindings/gsoap
rm -r sword-1.9.0/bindings/Android
rm -r sword-1.9.0/bindings/objc
rm -r sword-1.9.0/src/utilfuns/win32
rm sword-1.9.0/utilities/diatheke/pqa/Diatheke.pqa
tar -czf sword-1.9.0.tar.gz sword-1.9.0
rm -r sword-1.9.0
