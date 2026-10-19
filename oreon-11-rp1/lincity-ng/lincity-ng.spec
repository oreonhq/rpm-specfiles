%global source0_hash bc1eba0af24dd451ddf3e5ac8c335b48dcb29033ada424a3f5a798c3b1d91999
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global fonts font(dejavusans)
%global baserelease 2
Name:		lincity-ng
Version:	2.15.0
Release:        1%{?dist}
License:	GPL-2.0-or-later
Summary:        City Simulation Game
URL:		http://lincity-ng.berlios.de/
Source0:        https://github.com/lincity-ng/lincity-ng/releases/download/lincity-ng-%{version}/lincity-ng-%{version}-Source.tar.xz
Patch0:		lincity-ng-2.14.2-manfix.patch
Requires:	%{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_gfx-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  cmake
BuildRequires:  dejavu-sans-fonts
BuildRequires:  desktop-file-utils
BuildRequires:  fmt-devel
BuildRequires:  font(dejavusans)
BuildRequires:  fontconfig
BuildRequires:  gcc-c++
BuildRequires:  libX11-devel
BuildRequires:  libxml++50-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  physfs-devel
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  zlib-static
# /oreon:deps
%description
LinCity-NG is a City Simulation Game. It is a polished and improved version
of the classic LinCity (http://www.floot.demon.co.uk/lincity.html) game with
a new iso-3D graphics engine and a completely redone and modern GUI.

%package data
Summary:	Data files needed to run lincity-ng
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
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/sans.ttf
pushd $RPM_BUILD_ROOT
ln -f -s $(fc-match -f "%{file}" "sans") $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/sans.ttf
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lincity-ng-data -f %{oreon_filedir}/lincity-ng-data.list

%changelog

%autochangelog
