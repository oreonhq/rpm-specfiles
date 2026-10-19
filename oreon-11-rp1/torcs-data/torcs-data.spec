%global source0_hash 4b96773545fb36411982a6f3897205eb8fd572279d4ce569f2ce07b08e89a7af
Name:           torcs-data
Version:        1.3.8
Release:        1%{?dist}
Summary:        The Open Racing Car Simulator data files
License:        GPL-2.0-or-later AND LAL-1.3
URL:            http://torcs.org/
Source0:        http://downloads.sf.net/torcs/torcs-%{version}.tar.bz2
BuildArch:      noarch
Requires:       torcs = %{version}
Obsoletes:      torcs-data-cars-extra < 1.3.6
Obsoletes:      torcs-data-tracks-dirt < 1.3.6
Obsoletes:      torcs-data-tracks-oval < 1.3.6
Obsoletes:      torcs-data-tracks-road < 1.3.6
# oreon:deps
BuildRequires:  freealut-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libGL-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXt-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  openal-soft-devel
BuildRequires:  plib-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
TORCS is a 3D racing cars simulator using OpenGL.  The goal is to have
programmed robots drivers racing against each others.  You can also drive
yourself with either a wheel, keyboard or mouse.

This package contains the data files needed to run the game.

%prep

%setup -q -n torcs-%{version}

%build

%configure
%install
make datainstall DESTDIR=%{buildroot}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
