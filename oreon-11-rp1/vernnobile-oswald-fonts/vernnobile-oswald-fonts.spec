%global source0_hash e6138d3982041ff3429e26e1814229826ad882b78cbb244a504ba19066c25b45

# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/googlefonts/OswaldFont
%global commit      5a5fff234687674f8531a8537455e626b08b3321
%forgemeta

Version: 4.101
Release: 22%{?dist}
URL:     %{forgeurl}

%global foundry           vernnobile
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *txt *html *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Oswald
%global fontsummary       Oswald, a reworked Gothic style font family
%global fonts             fonts/otf/*otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Oswald is a reworking of the classic Gothic typeface style historically
represented by designs such as “Alternate Gothic”. The characters of Oswald
have been re-drawn and reformed to better fit the pixel grid of standard
digital screens. Oswald is designed to be used freely across the internet by
web browsers on desktop computers, laptops and mobile devices.}

Source0:  %{forgesource}
Source10: 60-%{fontpkgname}.xml

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup
%linuxtext %{fontlicenses}
chmod 644 %{fontdocs} %{fontlicenses}

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
