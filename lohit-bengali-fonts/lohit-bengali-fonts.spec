%global fontname lohit-bengali

Version:        2.91.5
Release:        25%{?dist}
URL:            https://github.com/lohit-fonts/lohit-bengali-fonts

%global foundry           Lohit
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt COPYRIGHT
%global fontdocs          AUTHORS README ChangeLog test-bengali.txt

%global fontfamily        Lohit Bengali
%global fontsummary       Free Bengali script font
%global fonts             *.ttf
%global fontconfs         %{SOURCE10}

%global fontdescription   %{expand:
This package provides a free Bengali TrueType/OpenType font.
}

BuildRequires: make
BuildRequires: fontforge
Source0:        https://releases.pagure.org/lohit/%{fontname}-%{version}.tar.gz
Source10:       66-%{fontpkgname}.conf


%fontpkg


%prep
%setup -q -n %{fontname}-%{version} 
%linuxtext OFL.txt ChangeLog COPYRIGHT OFL.txt AUTHORS README test-bengali.txt

%build
make ttf %{?_smp_mflags}
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.91.5-25
- Prepare for Oreon 11 (RP1)
