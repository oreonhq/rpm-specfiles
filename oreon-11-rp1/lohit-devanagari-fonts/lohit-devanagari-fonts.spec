%global source0_hash none

%global fontname lohit-devanagari

Version:        2.95.5
Release:        15%{?dist}
URL:            https://github.com/lohit-fonts/lohit-devanagari-fonts

%global foundry           Lohit
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt COPYRIGHT
%global fontdocs          AUTHORS README.md ChangeLog test-devanagari.txt

%global fontfamily        Lohit Devanagari
%global fontsummary       Free Devanagari Script Font
%global fonts             *.ttf
%global fontconfs         %{SOURCE10} %{SOURCE11}

%global fontdescription   %{expand:
This package provides a free Devanagari Script TrueType/OpenType font.
}

BuildRequires:  make
BuildRequires:  fontforge
BuildRequires:  ttfautohint
Source0:        https://github.com/lohit-fonts/%{name}/files/6454324/%{fontname}-%{version}.tar.gz
Source10:       59-%{fontpkgname}.conf
Source11:       66-%{fontpkgname}.conf

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{fontname}-%{version} 
%linuxtext OFL.txt AUTHORS README.md ChangeLog COPYRIGHT test-devanagari.txt

%build
make ttf %{?_smp_mflags}
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.95.5-15
- Prepare for Oreon 11 (RP1)
