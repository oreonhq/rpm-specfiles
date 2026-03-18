BuildRequires:  fontforge
BuildRequires:  make

Version:        1.3
Release:        21%{?dist}
URL:            https://github.com/aravindavk/Gubbi

%global fontlicense       GPL-3.0-or-later WITH Font-exception-2.0
%global fontlicenses      COPYING

%global fontdocs          ChangeLog README
%global fontdocsex        %{fontlicenses}

%global fontfamily        Gubbi
%global fontsummary       Free Kannada Opentype serif font
%global fonts             *.ttf
%global fontconfs         %{SOURCE1}
%global fontdescription   %{expand:
This package provides a free Kannada opentype serif font.}

Source0:        https://github.com/aravindavk/Gubbi/archive/v%{version}.tar.gz#/%{fontfamily}-%{version}.tar.gz
Source1:        65-0-%{fontpkgname}.conf

%fontpkg

%prep
%autosetup -n %{fontfamily}-%{version}

%build
%fontbuild
make

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3-21
- Prepare for Oreon 11 (RP1)
