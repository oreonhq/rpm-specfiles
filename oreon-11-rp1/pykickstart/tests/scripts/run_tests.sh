#!/bin/sh

echo "Running pykickstart tests"
cd ./tests/

# Run ksvalidator on good kickstart examples
for f in ./good-ks/*.ks; do
    echo "Checking $f"
    ksvalidator $f || exit 1
done

# Run ksvalidator on bad kickstart examples
for f in ./bad-ks/*.ks; do
    echo "Checking $f"
    ksvalidator $f && exit 1
done


# Run ksflatten on a set of kickstarts
echo "Testing ksflatten with included kickstarts"
ksflatten -c ./include-ks/fedora-live-xfce.ks -o flat.ks || exit 1
ksvalidator flat.ks || exit 1

exit 0
