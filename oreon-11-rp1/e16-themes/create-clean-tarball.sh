#! /bin/bash
#
# Script to remove free to distribute, however not free to modify fonts
# in e16-themes.
#  

tar xvf e16-themes-1.0.1.tar.gz

pushd e16-themes-1.0.1

# fonts are inside etheme tarballs, need to unpack, remove and repack.

for theme in BlueSteel BrushedMetal-Tigert Ganymede ShinyMetal ; do
    pushd $theme
    mkdir staging
    pushd staging
    tar xvf ../$theme.etheme
    popd
    popd
done

for font in vixar aircut3 ganymede ganymede_italic rothwell zirkle ; do
    find -name $font.ttf -delete
done

for theme in BlueSteel BrushedMetal-Tigert Ganymede ShinyMetal ; do
    pushd $theme
    rm -f $theme.etheme
    pushd $theme/staging
    tar czvf ../$theme.etheme *
    popd
    rm -rf staging
    popd
done

popd

tar czvf e16-themes-cleaned-1.0.1.tar.gz e16-themes-1.0.1


