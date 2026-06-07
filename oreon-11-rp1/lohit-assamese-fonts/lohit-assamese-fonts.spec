%global source0_hash none

%global fontname lohit-assamese

Version:       2.91.5 
Release:       26%{?dist}
URL:           https://github.com/lohit-fonts/lohit-assamese-fonts
 
%global foundry           Lohit  
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt COPYRIGHT
%global fontdocs          AUTHORS README ChangeLog test-assamese.txt

%global fontfamily        Lohit Assamese 
%global fontsummary       Free Assamese font
%global fonts             *.ttf
%global fontconfs         %{SOURCE10}

%global fontdescription   %{expand:
This package provides a free Assamese TrueType/OpenType font.
}

BuildRequires: make
BuildRequires: fontforge
Source0:        https://github.com/lohit-fonts/lohit-assamese-fonts/archive/refs/heads/main.tar.gz#/lohit-assamese-fonts-main.tar.gz
Source10:       66-%{fontpkgname}.conf

%fontpkg


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n lohit-assamese-fonts-main
%linuxtext OFL.txt AUTHORS README ChangeLog COPYRIGHT test-assamese.txt

%build
make ttf %{?_smp_mflags}
%fontbuild

%install
%fontinstall

%check            
%fontcheck

%fontfiles


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.91.5-26
- Import
