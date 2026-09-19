#!/bin/sh

[ $# -lt 2 ] && {
    echo "Usage: $0  binary  nm_file" >&2
    exit 2
}

sum=`sha1sum $1`
sum=${sum%% *}

sed -i "/^SHA1: / {
	    s/^SHA1: .*/SHA1: $sum/
	    n
	}" $2

