%global source0_hash 3d35db0ac03f9e6b0d5a53577591b714238985f4cfc31a0aa17f26cd74675e83
Version: 0.301
Release:        17%{?dist}
URL: https://gitlab.gnome.org/GNOME/cantarell-fonts/
%global	common_description	%{expand:
The Cantarell font family is a contemporary Humanist sans serif
designed for on-screen reading. The fonts were originally designed
by Dave Crossland.}
%global	foundry		abattis
%global	fontlicense	OFL-1.1
%global	fontlicenses	COPYING
%global	fontdocs	NEWS README.md
%global	fontdocsex	%{fontlicenses}
%global	fontfamily0	Cantarell
%global	fontsummary0	Humanist sans serif font
%global	fonts0		prebuilt/Cantarell-*.otf
%global	fontsex0	prebuilt/Cantarell-VF.otf
%global	fontconfs0	%{SOURCE1}
%global	fontdescription1	%{expand:
%{common_description}
This package contains the non-variable font version of the Cantarell font.}
%global	fontfamily1	Cantarell-VF
%global	fontsummary1	Humanist sans serif font (variable)
%global	fonts1		prebuilt/Cantarell-VF.otf
%global	fontconfs1	%{SOURCE2}
%global fontdescription1	%{expand:
%{common_description}
This package contains the variable font version of the Cantarell font.}
Source0:        http://download.gnome.org/sources/cantarell-fonts/0.301/cantarell-fonts-%{version}.tar.xz
Source1: 31-cantarell.conf
Source2: 31-cantarell-vf.conf
%fontpkg -a
# oreon:deps
BuildRequires:  fonts-rpm-macros
BuildRequires:  gettext
BuildRequires:  meson
# /oreon:deps
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir cantarell-fonts-%{version}
%oreon_prep
%build

%meson
%meson_build
%fontbuild -a
%install
%fontinstall -a
%oreon_autofiles abattis-cantarell-vf-fonts usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%fontcheck -a
%fontfiles -a
%files -f %{oreon_filedir}/main.list
%files -n abattis-cantarell-vf-fonts -f %{oreon_filedir}/abattis-cantarell-vf-fonts.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.301-17
- Prepare for Oreon 11 (RP1)
