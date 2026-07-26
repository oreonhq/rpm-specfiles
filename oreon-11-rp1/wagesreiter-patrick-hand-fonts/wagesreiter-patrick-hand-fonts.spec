%global source0_hash 244812fe6081525d8d8c202a92101f0bcee38f556fa4b5663ba26ab062418c7b

# SPDX-License-Identifier: MIT
Version: 20200215
Release: 18%{?dist}
URL:     https://fonts.google.com/specimen/Patrick+Hand

%global foundry           Wagesreiter
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.pb *.html

%global fontfamily        Patrick Hand
%global fontsummary       Patrick Hand, an handwriting font family
%global fonts             *ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Patrick Hand is a font family based on the designer’s own handwriting. It is
developed to bring an impressive and useful handwriting effect to your
texts.

It has all the basic Latin characters as well as most of the Latin extended
ones. It also includes some fancy glyphs like heavy quotation marks and the
floral heart! Ligatures, small caps and old style numbers are available as
OpenType features.}

Source0:  %{name}-%{version}.tar.xz
# Not available outside the huge Google fonts repository
Source1:  getfiles.sh
Source10: 60-%{fontpkgname}.xml

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
