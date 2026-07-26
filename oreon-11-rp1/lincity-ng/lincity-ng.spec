%global source0_hash none

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global fonts font(dejavusans)

# For rpmdev-bumpspec
%global baserelease 2

Name:		lincity-ng
Version:	2.14.2
Release:	1%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
Summary:	City Simulation Game
URL:		http://lincity-ng.berlios.de/
Source0:	https://github.com/lincity-ng/lincity-ng/releases/download/lincity-ng-%{version}/lincity-ng-%{version}-Source.tar.xz
Patch0:		lincity-ng-2.14.2-manfix.patch
BuildRequires:	gcc-c++
BuildRequires:	cmake, physfs-devel, zlib-devel, zlib-static, libxml2-devel, libxml++50-devel, xz-devel
BuildRequires:	libxslt-devel
BuildRequires:	SDL2-devel, SDL2_mixer-devel, SDL2_image-devel, SDL2_gfx-devel
BuildRequires:	SDL2_ttf-devel, desktop-file-utils
BuildRequires:	xorg-x11-proto-devel, libX11-devel, mesa-libGL-devel, mesa-libGLU-devel
BuildRequires:	fmt-devel
BuildRequires:	fontconfig %{fonts} dejavu-sans-fonts
Requires:	%{name}-data = %{version}-%{release}

%description
LinCity-NG is a City Simulation Game. It is a polished and improved version
of the classic LinCity (http://www.floot.demon.co.uk/lincity.html) game with
a new iso-3D graphics engine and a completely redone and modern GUI.

%package data
Summary:	Data files needed to run lincity-ng
# data bits are dual licensed GPL-2.0-or-later or CC-BY-SA-2.0
License:	GPL-2.0-or-later OR CC-BY-SA-2.0
Requires:	%{name} = %{version}-%{release}
Requires:	dejavu-sans-fonts
BuildArch: noarch

%description data
This package contains the data files (graphics, models, audio) necessary to
play Lincity-NG.

%prep
%setup -q -n %{name}-%{version}-Source
%patch -P0 -p1 -b .manfix

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

# Make a symlink to system font, rather than include a copy of DejaVu Sans
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/sans.ttf
pushd $RPM_BUILD_ROOT
ln -f -s $(fc-match -f "%{file}" "sans") $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/sans.ttf
popd

%files
%doc %{_pkgdocdir}
%{_bindir}/lincity-ng
%{_datadir}/metainfo/io.github.lincity_ng.lincity-ng.metainfo.xml
%{_datadir}/applications/*lincity-ng.desktop
%{_datadir}/icons/hicolor/*/apps/*lincity-ng.png
%{_mandir}/man6/lincity-ng.*

%files data
%{_datadir}/lincity-ng/

%changelog
%autochangelog
