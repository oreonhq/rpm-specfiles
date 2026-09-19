%global source0_hash none

Name:           torcs-data
Version:        1.3.8
Release:        1%{?dist}
Summary:        The Open Racing Car Simulator data files

# Automatically converted from old format: GPLv2+ and Free Art - review is highly recommended.
License:        GPL-2.0-or-later AND LAL-1.3
URL:            http://torcs.org/
Source0:        http://downloads.sf.net/torcs/torcs-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  freealut-devel
BuildRequires:  freeglut-devel
BuildRequires:  libGL-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXt-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  openal-soft-devel
BuildRequires:  plib-devel
BuildRequires:  zlib-devel

Requires:       torcs = %{version}

# Subpackages dropped in F23
Obsoletes:      torcs-data-cars-extra < 1.3.6
Obsoletes:      torcs-data-tracks-dirt < 1.3.6
Obsoletes:      torcs-data-tracks-oval < 1.3.6
Obsoletes:      torcs-data-tracks-road < 1.3.6

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

%files
# Directory default mode of 0755 is MANDATORY, since installed dirs are 0777
%defattr(-,root,root,0755)
%license COPYING
%{_datadir}/games/torcs/

%changelog
%autochangelog
