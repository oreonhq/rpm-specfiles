%global source0_hash 6fb5ab4f7d529127419dd08b39f0254da4fc7c6ada002d58561bfb16a742b3ce
%global fontname lohit-marathi
Version:       2.94.2
Release:        1%{?dist}
URL:           https://github.com/lohit-fonts/lohit-marathi-fonts 
%global foundry           Lohit
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt COPYRIGHT
%global fontdocs          AUTHORS README ChangeLog test-marathi.txt
%global fontfamily        Lohit Marathi
%global fontsummary       Free truetype font for Marathi language
%global fonts             *.ttf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
This package provides a free Marathi truetype/opentype font.
}
Source0:        https://github.com/lohit-fonts/lohit-marathi-fonts/archive/refs/heads/main.tar.gz#/lohit-marathi-fonts-main.tar.gz
Source10:       66-%{fontpkgname}.conf
%fontpkg
# oreon:deps
BuildRequires:  fontforge
BuildRequires:  fonts-rpm-macros
BuildRequires:  make
# /oreon:deps
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n lohit-marathi-fonts-main
%linuxtext OFL.txt AUTHORS README ChangeLog COPYRIGHT test-marathi.txt

%build

make ttf %{?_smp_mflags}
%fontbuild
%install
%fontinstall
%oreon_autofiles main

%check

%fontcheck
%fontfiles
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.94.2-25
- Prepare for Oreon 11 (RP1)
