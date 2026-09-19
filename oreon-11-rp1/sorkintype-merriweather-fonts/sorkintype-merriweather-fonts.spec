%global source0_hash none

# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/SorkinType/Merriweather
%global commit      fad21f97f3525af393d7a1d6c2995cbaf4b0cd7b
%forgemeta

Version: 2.008
Release: 14%{?dist}
URL:     %{forgeurl}

%global foundry           SorkinType
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Merriweather
%global fontsummary       Merriweather, a warm space-saving serif font family
%global fonts             fonts/ttfs/*ttf fonts/variable/*ttf
%global fontsex           fonts/variable/*WO7*ttf fonts/ttfs/Merriweather35*ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Merriweather offers a Renaissance warmth while using proportions which are
space-saving. It is suitable for editorial design, news and other kinds of
space sensitive typography.

Merriweather was designed to be a text face that is pleasant to read on
screens. It features a very large x height, slightly condensed letter-forms, a
mild diagonal stress, sturdy serifs and open forms}

Source0:  %{forgesource}
Source10: 57-%{fontpkgname}.xml

%fontpkg

%package   doc
Summary:   Optional documentation files of %{name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{name}.

%prep
%forgesetup

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%files doc
%defattr(644, root, root, 0755)
%license OFL.txt
%doc documents/*

%changelog
%autochangelog
