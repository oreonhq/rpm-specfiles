Version: 0.301
Release: 17%{?dist}
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

Source0: http://download.gnome.org/sources/cantarell-fonts/0.301/cantarell-fonts-%{version}.tar.xz
Source1: 31-cantarell.conf
Source2: 31-cantarell-vf.conf

BuildRequires: gettext
BuildRequires: meson

%fontpkg -a

%prep
%autosetup -n cantarell-fonts-%{version}

%build
%meson
%meson_build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.301-17
- Prepare for Oreon 11 (RP1)
