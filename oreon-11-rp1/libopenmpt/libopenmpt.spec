# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 976d259288c40cd285771f77d09eff3d02514511d5677ecfcfb53be5013317e2
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: libopenmpt
Version: 0.8.10
Release: 1%{?dist}

%global tar_root %{name}-%{version}+release.autotools

License: BSD-3-Clause
Summary: C/C++ library to decode tracker music module (MOD) files

URL: https://lib.openmpt.org/libopenmpt/

Source0: https://lib.openmpt.org/files/libopenmpt/src/%{tar_root}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: chrpath
BuildRequires: pkgconfig(libmpg123)
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(flac)
BuildRequires: pkgconfig(zlib)

BuildRequires: pulseaudio-libs-devel

%if 0%{?rhel} && 0%{?rhel} < 11
Requires: libmpg123%{?_isa} >= 1.32.0
%endif

%description
libopenmpt is a cross-platform C++ and C library to decode tracked music
files (modules) into a raw PCM audio stream.

libopenmpt is based on the player code of the OpenMPT project (Open
ModPlug Tracker). In order to avoid code base fragmentation, libopenmpt is
developed in the same source code repository as OpenMPT.

%package -n openmpt123
Summary: Command-line tracker music player based on libopenmpt
Group: Applications/Multimedia
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n openmpt123
Openmpt123 is a cross-platform command-line or terminal based player
for tracker music (MOD) module files.

%package devel
Summary: Development files for the libopenmpt library
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files needed when building software which uses libopenmpt.

%prep
%oreon_sha256
%autosetup -p1 -n %{tar_root}
sed -i 's/\r$//' LICENSE

%build
%configure  \
  --disable-static  \
  --without-sdl --without-sdl2 \
  --without-portaudio --without-portaudiocpp
make %{?_smp_mflags}

%install
%make_install
find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'
chrpath --delete ${RPM_BUILD_ROOT}%{_bindir}/openmpt123

%files -n openmpt123
%{_bindir}/openmpt123
%{_mandir}/man1/*

%files
%license LICENSE
%{_libdir}/*.so.0*
%{_docdir}/%{name}/
%exclude %{_docdir}/%{name}/examples

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_docdir}/%{name}/examples/

%changelog
%autochangelog
