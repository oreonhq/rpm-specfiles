%global source0_hash 0ee6593bee405e93e3f7e63ffe42600a9c3b3b0ab2a8306aa246f7f83b4cf8a5

# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/SorkinType/Merriweather-Sans
%global commit      f36d6e1eb17fd4eead50c320fc8313f5353c9f5f
%forgemeta

Version: 1.008
Release: 14%{?dist}
URL:     %{forgeurl}

%global foundry           SorkinType
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Merriweather Sans
%global fontsummary       Merriweather Sans, a low-contrast semi-condensed sans-serif font family
%global fonts             fonts/ttfs/*ttf fonts/variable/*.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Merriweather Sans is a low-contrast semi-condensed sans-serif font family
designed to be readable at very small sizes. Merriweather Sans is traditional
in feeling despite the modern shapes it has adopted for screens. It is a
companion to the serif font family Merriweather.}

Source0:  %{forgesource}
Source10: 57-%{fontpkgname}.xml

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
