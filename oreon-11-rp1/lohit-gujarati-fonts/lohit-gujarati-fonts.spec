%global fontname lohit-gujarati

Version:       2.92.4
Release:       25%{?dist}
URL:           https://github.com/lohit-fonts/lohit-gujarati-fonts

%global foundry           Lohit
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt COPYRIGHT
%global fontdocs          AUTHORS README ChangeLog test-gujarati.txt

%global fontfamily        Lohit Gujarati
%global fontsummary       Free Gujarati font
%global fonts             *.ttf
%global fontconfs         %{SOURCE10}

%global fontdescription   %{expand:
This package provides a free Gujarati truetype/opentype font.
}

BuildRequires: make
BuildRequires: fontforge
Source0:        https://releases.pagure.org/lohit/%{fontname}-%{version}.tar.gz
Source10:       66-%{fontpkgname}.conf

%fontpkg

%prep
%setup -q -n %{fontname}-%{version} 
%linuxtext OFL.txt AUTHORS README ChangeLog COPYRIGHT test-gujarati.txt

%build
make ttf %{?_smp_mflags}
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.92.4-25
- Prepare for Oreon 11 (RP1)
