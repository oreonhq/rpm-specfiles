%global source0_hash a518c7d6e6b3f81d1a738befeb617abba59f93bd6b1e626da079a1003e9db52b
%global ext_id uBlock0@raymondhill.net
%global firefox_app_id \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%global firefox_inst_dir %{_datadir}/mozilla/extensions/%{firefox_app_id}
Name:           mozilla-ublock-origin
Version:        1.75.0
Release:        1%{?dist}
Summary:        An efficient blocker for Firefox
License:        BSD-2-Clause AND GPL-3.0-only AND LGPL-3.0-or-later AND LicenseRef-Fedora-UltraPermissive AND MIT AND MPL-2.0 AND OFL-1.1 AND Unlicense
URL:            https://github.com/gorhill/uBlock
Source0:        https://github.com/gorhill/uBlock/archive/%{version}/uBlock-%{version}.tar.gz
Source1:        mozilla-ublock-origin.metainfo.xml
Source2:        uAssets-%{version}.tar.gz
Source10:       uAssets-mktarball.sh
Patch0:         %{name}-nonfree.patch
Requires:       mozilla-filesystem
BuildArch:      noarch
ExcludeArch:    ppc64 s390x
Provides:       bundled(npm-css-tree) = 2.2.1
Provides:       bundled(fontawesome-fonts) = 4.7.0
Provides:       bundled(inter-fonts)
Provides:       bundled(metropolis-fonts)
Provides:       bundled(js-beautify) = 1.14.7
Provides:       bundled(js-punycode) = 1.3.2
Provides:       bundled(js-github-swatinem-diff)
Provides:       bundled(js-codemirror) = 5.59.2
Provides:       bundled(lz4-wasm)
Provides:       bundled(js-regexanalyzer) = 1.2.0
Provides:       bundled(js-hsluv) = 0.1.0
Provides:       bundled(publicsuffix-list) = 20240504
# oreon:deps
BuildRequires:  binaryen
BuildRequires:  libappstream-glib
BuildRequires:  nodejs
BuildRequires:  python3
BuildRequires:  wabt
# /oreon:deps
%description
An efficient blocker: easy on memory and CPU footprint, and yet can load and
enforce thousands more filters than other popular blockers out there.

Flexible, it's more than an "ad blocker": it can also read and create filters
from hosts files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# https://github.com/gorhill/uBlock/tree/master/dist#build-instructions-for-developers
%setup -q -n uBlock-%{version}
mkdir -p dist/build/uAssets
tar -xz -C dist/build/uAssets -f %{SOURCE2}
pushd dist/build/uAssets/main
tools/make-ublock.sh
popd
%patch 0 -p1
rm src/{js/wasm,lib/{lz4,publicsuffixlist/wasm}}/*.wasm
mv src/css/fonts/Inter/LICENSE.txt LICENSE.Inter.txt
mv src/img/fontawesome/LICENSE.txt LICENSE.fontawesome.txt
mv src/lib/js-beautify/LICENSE LICENSE.js-beautify.txt
mv src/lib/codemirror/LICENSE LICENSE.codemirror.txt

%build

for d in src/{js/wasm,lib/{lz4,publicsuffixlist/wasm}} ; do
    pushd $d
        for f in *.wat ; do
            wat2wasm $f
        done
    popd
done
pushd src/lib/lz4
wasm-opt ./lz4-block-codec.wasm -O4 -o ./lz4-block-codec.wasm
popd
./tools/make-firefox.sh all
%install
install -Dpm644 dist/build/uBlock0.firefox.xpi %{buildroot}%{firefox_inst_dir}/%{ext_id}.xpi
install -Dpm644 %{SOURCE1} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
