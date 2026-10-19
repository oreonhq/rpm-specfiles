%global source0_hash b5e6f61de7465476f2f946dd83ee0961dc4d0ceea0833d253bb697297f232d97
Version: 003.03
Release:        1%{?dist}
URL:     http://ossipedia.ipa.go.jp/ipafont/
%global foundry           IPA 
%global fontlicense       IPA
%global fontlicenses      IPA_Font_License_Agreement_v1.0.txt
%global fontdocs          Readme_ipag00303.txt
%global fontdocsex        %{fontlicenses}
%global fontfamily        IPAGothic
%global fontsummary       Japanese Gothic-typeface OpenType font by IPA
%global fonts             ipag.ttf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
IPA Font is a Japanese OpenType fonts that is JIS X 0213:2004compliant, providedby Information-technology Promotion Agency, Japan.This package contains Gothic(sans-serif) style font.
}
Source0:        http://info.openlab.ipa.go.jp/ipafont/fontdata/ipag00303.zip
Source10: 69-ipa-gothic-fonts.conf
%fontpkg
# oreon:deps
BuildRequires:  fonts-rpm-macros
# /oreon:deps
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ipag00303

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
