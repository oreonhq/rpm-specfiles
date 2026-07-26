%global source0_hash none

# Force out of source build
%undefine __cmake_in_source_build

Name:		lugaru
Version:	1.2
Release:	26%{?dist}
Summary:	Ninja rabbit fighting game
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://osslugaru.gitlab.io
Source0:	https://bitbucket.org/osslugaru/lugaru/downloads/%{name}-%{version}.tar.xz

# Patches backported from upstream
Patch0001:	0001-CMake-Define-build-type-before-configuring-version-h.patch
Patch0002:	0002-ImageIO-fix-invalid-conversion.patch
Patch0003:	0003-Dist-Linux-Add-content-ratings-to-AppStream-appdata-.patch

# Fedora-specific patch, do not have CMake install docs,
# we'll grab them ourselves.
Patch1000:	lugaru-1.1-CMake-Do-not-install-documentation.patch

# For autosetup
BuildRequires:	git-core

%if 0%{?rhel}
BuildRequires:	cmake3 >= 3.0
%else
BuildRequires:	cmake >= 3.0
%endif

BuildRequires:	gcc-c++
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(vorbisfile)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(zlib)

# pkgconfig(libjpeg) doesn't work on EL7
BuildRequires:	libjpeg-turbo-devel

# For deduplicating data files
BuildRequires:	fdupes

# For desktop file validation
BuildRequires:	desktop-file-utils
# For AppStream metainfo validation
BuildRequires:	libappstream-glib

# Ensure the hicolor icon theme dirs exist
Requires:	hicolor-icon-theme

# Ensure matching game data is pulled in
Requires:	lugaru-data = %{version}-%{release}

%description
Lugaru (pronounced Loo-GAH-roo) is a cross-platform third-person action game.
The main character, Turner, is an anthropomorphic rebel bunny rabbit with
impressive combat skills. In his quest to find those responsible for
slaughtering his village, he uncovers a far-reaching conspiracy involving the
corrupt leaders of the rabbit republic and the starving wolves from a nearby
den. Turner takes it upon himself to fight against their plot and save his
fellow rabbits from slavery.

%package data
Summary:	Architecture-independent game data files for Lugaru
License:	CC-BY-SA-3.0 AND (CC-BY-SA-3.0 OR CC-BY-3.0) AND CC-BY-SA-4.0
BuildArch:	noarch

%description data
This package contains the game data files that make up the Lugaru game.

%prep
%autosetup -S git

%build
%{?cmake3:%cmake3}%{!?cmake3:%cmake} -DCMAKE_BUILD_TYPE=RelWithDebInfo \
				     -DSYSTEM_INSTALL=ON \
				     -DLUGARU_VERSION_RELEASE="Fedora %{?epel:EPEL }%{version}-%{release}"
%cmake_build

%install
%cmake_install

%fdupes %{buildroot}%{_datadir}/%{name}

%check
# Validate desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# Validate AppStream metainfo data
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%files
%license COPYING.txt
%doc Docs/* AUTHORS README.md RELEASE-NOTES.md
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man6/%{name}.6*

%files data
%license CONTENT-LICENSE.txt
%{_datadir}/%{name}/

%changelog
%autochangelog
