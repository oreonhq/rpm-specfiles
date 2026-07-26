%global source0_hash none

# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/productiontype/Spectral
%global commit      748733e3761fc7985ca9c473996ed121954debf8
%forgemeta

Version: 2.003
Release: 16%{?dist}
URL:     %{forgeurl}

%global foundry           Production Type
%global fontlicense       OFL-1.1
%global fontlicenses      ofl.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Spectral
%global fontsummary       Spectral, an efficient and versatile serif font family
%global fonts             fonts/desktop_otf/*otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Spectral is a versatile serif font family available in seven weights of roman
and italic, with small caps. Spectral offers an efficient, beautiful design
that’s intended primarily for text-rich, screen-first environments and
long-form reading.}

Source0:  %{forgesource}
Source10: 57-%{fontpkgname}.xml

%fontpkg

%prep
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
