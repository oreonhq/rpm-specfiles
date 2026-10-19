%global source0_hash 85e7d4aafa3ba613586ec96bbe696113c6c0a64d0dbbc37a8988d96dd65a59b2
%global fontname lohit-kannada
Version:       2.5.4
Release:        23%{?dist}
URL:           https://github.com/lohit-fonts/lohit-kannada-fonts
%global foundry           Lohit
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt COPYRIGHT
%global fontdocs          AUTHORS README ChangeLog
%global fontfamily        Lohit Kannada
%global fontsummary       Free Kannada font
%global fonts             *.ttf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
This package provides a free Kannada truetype/opentype font.
}
Source0:        https://github.com/lohit-fonts/lohit-kannada-fonts/archive/refs/heads/main.tar.gz#/lohit-kannada-fonts-main.tar.gz
Source10:       66-%{fontpkgname}.conf
%fontpkg
# oreon:deps
BuildRequires:  fontforge
BuildRequires:  fonts-rpm-macros
BuildRequires:  make
# /oreon:deps
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n lohit-kannada-fonts-main
%linuxtext OFL.txt AUTHORS README ChangeLog COPYRIGHT

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

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5.4-23
- Prepare for Oreon 11 (RP1)
