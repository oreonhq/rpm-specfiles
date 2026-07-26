%global source0_hash 1d8a4ff03dce90f6002b008a5e37f890c409bc22e4e26561b67f3f3c40991b5c

# SPDX-License-Identifier: MIT
Version: 5.000
Release: 19%{?dist}

%global foundry           SIL
%global fontlicense       OFL-1.1-RFN
%global fontlicenses      OFL.txt
%global fontdocs          *.txt documentation/*.txt documentation/*.odt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Gentium Plus Compact
%global fontsummary       Gentium Plus Compact, a Latin/Greek/Cyrillic font family
%global projectname       gentium
%global archivename       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), "[%p%s]+", ""); print(t)}-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fontpkgheader     %{expand:
Suggests: font(gentium)
}
%global fonts             *.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Gentium is a font family designed to enable the diverse ethnic groups around
the world who use the Latin, Cyrillic and Greek scripts to produce readable,
high-quality publications.

Gentium was a winner of the TDC2003 Type Design Competition and was exhibited
as part of the bukva:raz! exhibit at the UN Headquarters Main Lobby, 17 Jan –
13 Feb, 2002.

The Gentium Plus Compact font family was derived from Gentium Plus using SIL
TypeTuner, by setting the “Line spacing” feature to “Tight”, and it cannot be
TypeTuned again. It may exhibit some diacritics clipping on screen (but should
print fine).}

Source0:  https://software.sil.org/downloads/r/%{projectname}/%{archivename}.zip
Source10: 61-%{fontpkgname}.xml

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{archivename}
%linuxtext *.txt documentation/*.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
