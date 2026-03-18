%global fontname lohit-telugu

Version:       2.5.5
Release:       23%{?dist}
URL:           https://github.com/lohit-fonts/lohit-odia-fonts

%global foundry           Lohit
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt COPYRIGHT
%global fontdocs          AUTHORS README ChangeLog

%global fontfamily        Lohit Telugu 
%global fontsummary       Free Telugu font
%global fonts             *.ttf
%global fontconfs         %{SOURCE10}

%global fontdescription   %{expand:
This package provides a free Telugu truetype/opentype font.
}

BuildRequires: make
BuildRequires: fontforge
BuildRequires: ttfautohint
Source0:        https://releases.pagure.org/lohit/%{fontname}-%{version}.tar.gz
Source10:       66-%{fontpkgname}.conf

%fontpkg

%prep
%setup -q -n %{fontname}-%{version}
%linuxtext OFL.txt AUTHORS README ChangeLog COPYRIGHT

%build
make ttf %{?_smp_mflags}
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5.5-23
- Prepare for Oreon 11 (RP1)
