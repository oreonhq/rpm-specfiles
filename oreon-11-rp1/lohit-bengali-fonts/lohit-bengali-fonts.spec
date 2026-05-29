%global source0_hash 0df174f0819f4bed88573ad9773bfe6c7bec97883ff8eca4391a35487b1d1159

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
Source0:        https://releases.pagure.org/lohit/lohit-bengali-2.91.5.tar.gz
Source10:       66-%{fontpkgname}.conf


%fontpkg


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.91.5-25
- Import
