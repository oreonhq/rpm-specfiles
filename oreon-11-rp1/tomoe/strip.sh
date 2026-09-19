#!/bin/sh -x

pkgname=tomoe
litepkgname=tomoe-stripped

if test "x$1" = x; then
    echo "help: $0 <tomoe tar ball>"
    exit 1
fi

#compute file/path name
tarfile=$1
expandpath=${tarfile%.tar.gz}
newtarfile="$litepkgname${tarfile#$pkgname}"

#prepare tmp directory
rm -f $newtarfile
mkdir ./tmp

pushd "./tmp"
	tar xf ../$tarfile

	pushd "$expandpath/data"
                # remove the skip code from kanjidic2-original.xml
		sed -i s/\<q_code\ qc_type=\"skip\"\>[0-9]*-[0-9]*-[0-9]*\<\\/q_code\>//g  kanjidic2-original.xml
                mv kanjidic2.xml kanjidic2.xml.orig
                xsltproc kanjidic2-original.xsl kanjidic2-original.xml > kanjidic2.xml
                # check the changes in kanjidic2.xml
                diff kanjidic2.xml.orig kanjidic2.xml
                mv kanjidic2.xml.orig kanjidic2.xml
	popd

	tar zcf ${newtarfile} $expandpath
	rm -r $expandpath
popd

mv ./tmp/$newtarfile .
rmdir ./tmp
