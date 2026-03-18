BuildRequires:  fontforge
BuildRequires: make

Version:        1.2
Release:        29%{?dist}
URL:            https://github.com/aravindavk/Navilu

%global fontlicense       OFL-1.1
%global fontlicenses      COPYING

%global fontdocs          ChangeLog README
%global fontdocsex        %{fontlicenses}

%global fontfamily        Navilu
%global fontsummary       Free Kannada opentype sans-serif font
%global fonts             *.ttf
%global fontconfs         %{SOURCE1}
%global fontdescription   %{expand:
This package provides a free Kannada opentype sans-serif font.}

Source0:        https://github.com/aravindavk/Navilu/archive/v%{version}.tar.gz#/%{fontfamily}-%{version}.tar.gz
Source1:        67-%{fontpkgname}.conf

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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2-29
- Prepare for Oreon 11 (RP1)
