#!/bin/sh

spec=linux-sgx.spec

dver=$(grep 'global dcap_version' ${spec} | awk '{print $3}')

function urls
{
    rpmspec -P ${spec} 2>/dev/null | grep Source | grep http | awk '{print $2}'

    grep "https.*prebuilt_dcap" ${spec} | awk '{print $2}' | sed -e "s/%{dcap_version}/$dver/g"
}

for url in $(urls)
do
    tarball=$(basename ${url})
    echo "Check $tarball"
    if ! test -f ${tarball}
    then
	echo "Downloading $url"
        curl --silent --fail -L --output "$tarball" "${url}"
	if test $? != 0
	then
	    echo "ERROR: download failed"
	    exit 1
	fi
    fi
done

./repack.sh $dver
