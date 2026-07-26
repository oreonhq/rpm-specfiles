%global source0_hash 41809a296870dd7b4753d6532b4093821d61f9806281e6c053ccb11083ad1190

# SPDX-License-Identifier: MIT
Version: 1.00
Release: 21%{?dist}
%global  projectname clear-sans
URL:     https://01.org/%{projectname}

%global foundry           Intel
%global fontlicense       Apache-2.0
%global fontlicenses      LICENSE-2.0.txt

%global fontfamily        Clear Sans
%global fontsummary       Clear Sans, a versatile font family for screen, print, and Web
%global fonts             TTF/*.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription  %{expand:
Clear Sans has been recognized as a versatile font for screen, print, and Web.
Its minimized, unambiguous characters and slightly narrow proportions, make it
ideal for UI design.

Clear Sans was designed with on-screen legibility in mind. It strikes a balance
between contemporary, professional, and stylish expression and thoroughly
functional purpose. It has a sophisticated and elegant personality at all
sizes, and its thoughtful design becomes even more evident at the thin weight.}

Source0:  https://01.org/sites/default/files/downloads/%{projectname}/clearsans-%{version}.zip
Source10: 60-%{fontpkgname}.xml

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
