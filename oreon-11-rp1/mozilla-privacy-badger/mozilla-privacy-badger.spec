%global source0_hash 49143a2090c7bbd2bb902f1c12a07f175402e4bb1ddbfa9de6cd84969b22e3e6
%global moz_extensions %{_datadir}/mozilla/extensions
%global ext_id jid1-MnnxcxisBPnSXQ@jetpack
%global firefox_app_id \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%global firefox_inst_dir %{moz_extensions}/%{firefox_app_id}
Name:           mozilla-privacy-badger
Version:        2026.9.15
Release:        1%{?dist}
Summary:        Protects your privacy by blocking spying ads and invisible trackers
License:        Apache-2.0 AND GPL-3.0-or-later AND (GPL-3.0-or-later OR MPL-2.0) AND MIT AND OFL-1.1 AND LicenseRef-Fedora-Public-Domain AND CC-BY-SA-3.0
URL:            https://www.eff.org/privacybadger
Source0:        https://github.com/EFForg/privacybadger/archive/release-%{version}/privacybadger-%{version}.tar.gz
Source1:        %{name}.metainfo.xml
Requires:       mozilla-filesystem
BuildArch:      noarch
Provides:       bundled(js-jquery) = 3.7.0
Provides:       bundled(js-jquery-smooth-scroll) = 2.2.0
Provides:       bundled(js-jquery-ui) = 1.13.2
Provides:       bundled(js-jquery-ui-iconfont) = 2.3.2
Provides:       bundled(fontsquirrel-chunk-five-fonts)
Provides:       bundled(open-sans-fonts)
Provides:       bundled(js-select2) = 4.0.11
Provides:       bundled(tooltipster) = 4.2.6
# oreon:deps
BuildRequires:  libappstream-glib
BuildRequires:  python3
BuildRequires:  zip
# /oreon:deps
%description
Privacy Badger is a browser add-on that stops advertisers and other third-party
trackers from secretly tracking where you go and what pages you look at on the
web. If an advertiser seems to be tracking you across multiple websites without
your permission, Privacy Badger automatically blocks that advertiser from
loading any more content in your browser. To the advertiser, it's like you
suddenly disappeared.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n privacybadger-release-%{version}

%build

rm -rv src/tests src/data/dnt-policy.txt
sed -i -e 's/\.DEBUG = true/.DEBUG = false/' src/js/bootstrap.js
scripts/min_locales.py
PATCHER=scripts/patch_manifest.py
mkdir pkg
$PATCHER src/manifest.json 'set' 'author' 'privacybadger-owner@eff.org'
$PATCHER src/manifest.json 'del' 'update_url'
rm -fv pkg/privacybadger-%{version}.zip
pushd src
zip -x pkg -v -r ../pkg/privacybadger-%{version}.zip ./*
popd
%install
install -Dpm644 pkg/privacybadger-%{version}.zip %{buildroot}%{firefox_inst_dir}/%{ext_id}.xpi
install -Dpm644 %{SOURCE1} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
