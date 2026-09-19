%global source0_hash 000299ba5990dad9362a8256a2d322e95e80da21dedf54834acb7253a840bbd0

# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/googlefonts/nunito
%global commit      6d8a4e1c00df8b361e59656eee7c2b458d663191
%forgemeta

Version: 3.504
Release: 20%{?dist}
URL:     %{forgeurl}

%global foundry           vernnobile
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *txt *html *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Nunito
%global fontsummary       Nunito, a sans serif font family with rounded terminals
%global fonts             fonts/TTF-unhinted/*otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Nunito is a well balanced sans serif with rounded terminals. Nunito has been
designed mainly to be used as a display font but is usable as a text font too.
Nunito has been designed to be used freely across the internet by web browsers
on desktop computers, laptops and mobile devices.}

Source0:  %{forgesource}
Source10: 58-%{fontpkgname}.xml

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
