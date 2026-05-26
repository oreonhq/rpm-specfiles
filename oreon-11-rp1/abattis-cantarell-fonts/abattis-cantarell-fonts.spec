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
# oreon url source checksums begin
%global source0_sha256 3d35db0ac03f9e6b0d5a53577591b714238985f4cfc31a0aa17f26cd74675e83
%global source0_file cantarell-fonts-0.301.tar.xz
# oreon url source checksums end

BuildRequires: gettext
BuildRequires: meson

%fontpkg -a

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/cantarell-fonts-0.301.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3d35db0ac03f9e6b0d5a53577591b714238985f4cfc31a0aa17f26cd74675e83" || { echo "oreon: Source0 SHA256 mismatch for cantarell-fonts-0.301.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
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
