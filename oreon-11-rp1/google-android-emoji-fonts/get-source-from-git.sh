#!/bin/sh

set -e
set -u

package_name=google-android-emoji-fonts
checkout_date=$(date -u +%Y%m%d)git
output_filename=$package_name-${checkout_date}.tar.xz

repo_web_url=https://android.googlesource.com/platform/frameworks/base.git
branch=jb-release
path=data/fonts.tar.gz
tarball_url=$repo_web_url/+archive/$branch/$path

tarball_filename=$(mktemp -t get-source-from-git.XXXXXX)
curl $tarball_url -o $tarball_filename

working_dir=$(mktemp -d -t get-source-from-git.XXXXXX)
unpacked_dir=$package_name-$checkout_date
mkdir $working_dir/$package_name-$checkout_date

tar -xf $tarball_filename -C $working_dir/$unpacked_dir \
    README.txt NOTICE AndroidEmoji.ttf
tar -cJf $output_filename -C $working_dir $package_name-$checkout_date

rm -r $tarball_filename $working_dir
