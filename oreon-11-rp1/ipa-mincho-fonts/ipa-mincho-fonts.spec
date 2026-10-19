%global source0_hash 448428496fe30c3c9b13f12c2258aee5b96e34ddc4b2b71b69c7157f159b2999
Version: 003.03
Release:        1%{?dist}
URL:     http://ossipedia.ipa.go.jp/ipafont/
%global foundry           IPA 
%global fontlicense       IPA
%global fontlicenses      IPA_Font_License_Agreement_v1.0.txt
%global fontdocs          Readme_ipam00303.txt
%global fontdocsex        %{fontlicenses}
%global fontfamily        IPAMincho
%global fontsummary       Japanese Mincho-typeface OpenType font by IPA
%global fonts             ipam.ttf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
IPA Font is a Japanese OpenType fonts that is JIS X 0213:2004
compliant, provided by Information-technology Promotion Agency, Japan.
This package contains Mincho style font.
}
Source0:        http://info.openlab.ipa.go.jp/ipafont/fontdata/ipam00303.zip
Source10: 69-ipa-mincho-fonts.conf
%fontpkg
# oreon:deps
BuildRequires:  fonts-rpm-macros
# /oreon:deps
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ipam00303

%build

%fontbuild
%install
%fontinstall
%oreon_autofiles main

%check

%fontcheck
%fontfiles
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
