%global fontname lohit-tamil

Version:       2.91.3
Release:       26%{?dist}
URL:           https://github.com/lohit-fonts/lohit-tamil-fonts

%global foundry           Lohit
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt COPYRIGHT
%global fontdocs          AUTHORS README.md ChangeLog src/test-tamil.txt 

%global fontfamily        Lohit Tamil
%global fontsummary       Free truetype font for Tamil language
%global fonts             *.ttf
%global fontconfs         %{SOURCE10}

%global fontdescription   %{expand:
This package provides a free Tamil truetype/opentype font.
}

BuildRequires: make
BuildRequires: fontforge
Source0:        https://github.com/lohit-fonts/lohit-tamil-fonts/archive/refs/tags/%{version}.tar.gz#/%{fontname}-fonts-%{version}.tar.gz
Source10:       66-%{fontpkgname}.conf

%fontpkg

%prep
%setup -q -n %{fontname}-fonts-%{version}
%linuxtext OFL.txt AUTHORS README.md ChangeLog COPYRIGHT src/test-tamil.txt

%build
make ttf %{?_smp_mflags}
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.91.3-26
- Prepare for Oreon 11 (RP1)
