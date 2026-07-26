#!/usr/bin/bash

export GOPROXY='https://proxy.golang.org,direct'

version=$1

if [[ -z ${version} ]]; then
    echo "This script requires the version as an argument."
    exit 1
fi

git clone --branch v${version} --depth 1 https://github.com/42wim/matterbridge.git matterbridge-${version}
pushd matterbridge-${version}
# go vendoring
go mod tidy
go mod vendor

# remove non-OSI code
rm -rf vendor/github.com/harmony-development
rm -rf vendor/github.com/mrexodia/wray
rm -rf vendor/github.com/nelsonken/gomf

# let's parse bundled deps and licenses
declare -A LICENSE_ASSOC_ARR
for dep in $(go mod edit -json | jq -r '.Require.[] | "\(.Path);\(.Version)"'); do
	GO_MOD_PATH=$(echo -n $dep | awk -F ';' '{ printf "%s", $1 }')
	GO_MOD_PATH_URLENCODE=$(echo -n $GO_MOD_PATH | jq -sRr @uri)
	VERSION=$(echo -n $dep | awk -F ';' '{ printf "%s", $2 }')
	VERSION_SPEC=$(echo $VERSION | sed 's/-/~/g')
	CURL_OUT=$(curl -s https://api.deps.dev/v3/systems/go/packages/$GO_MOD_PATH_URLENCODE/versions/$VERSION)
	LICENSES=$(echo -n $CURL_OUT | jq -r '.licenses | join(" OR ")')
	if [ ! -z "$LICENSES" ]; then
		if echo "$LICENSES" | grep -q " OR "; then
			LICENSE_ASSOC_ARR["($LICENSES)"]=1
		else
			LICENSE_ASSOC_ARR["$LICENSES"]=1
		fi
	fi
	echo "# $LICENSES"
	echo "Provides:       bundled(golang($GO_MOD_PATH)) = $VERSION_SPEC"
done

echo ""

# flip back to an indexed array so we can use the values
LICENSE_ARR=("${!LICENSE_ASSOC_ARR[@]}")
# merge array values into an SPDX string
LICENSE_STRING=$(printf "%s AND "  "${LICENSE_ARR[@]}")
# remove extra "AND".  there's probably a better way to do this
LICENSE_STRING=${LICENSE_STRING::-4}
echo "License string for spec.  Don't forget to include the base software's license if not included."
echo $LICENSE_STRING
echo ""

popd
XZ_OPT='-9' tar --exclude .git -cJf matterbridge-${version}-vendored.tar.xz matterbridge-${version}
rm -rf matterbridge-${version}
