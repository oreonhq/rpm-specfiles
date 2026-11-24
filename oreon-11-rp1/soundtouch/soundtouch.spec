# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 3dda3c9ab1e287f15028c010a66ab7145fa855dfa62763538f341e70b4d10abd
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           soundtouch
Version:        2.4.0
Release:        1%{?dist}
Summary:        Audio Processing library for changing Tempo, Pitch and Playback Rates
License:        LGPL-2.1-or-later
URL:            http://www.surina.net/soundtouch/

Source0:        https://codeberg.org/soundtouch/soundtouch/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  cmake

%description
SoundTouch is a LGPL-licensed open-source audio processing library for
changing the Tempo, Pitch and Playback Rates of audio streams or
files. The SoundTouch library is suited for application developers
writing sound processing tools that require tempo/pitch control
functionality, or just for playing around with the sound effects.

The SoundTouch library source kit includes an example utility
SoundStretch which allows processing .wav audio files from a
command-line interface.

%package devel
Summary:  Libraries, includes, etc to develop soundtouch applications
Requires: soundtouch = %{version}-%{release}
Requires: pkgconfig

%description devel
Libraries, include files, etc you can use to develop soundtouch applications.

%prep
%oreon_sha256
%autosetup -p1 -n %{name}

%build
%cmake
%cmake_build

%install
%cmake_install

ln -s soundtouch.pc %{buildroot}%{_libdir}/pkgconfig/libSoundTouch.pc
ln -s soundtouch.pc %{buildroot}%{_libdir}/pkgconfig/soundtouch-1.0.pc

%files
%doc README.html
%license COPYING.TXT
%{_bindir}/soundstretch
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}
%{_libdir}/cmake/SoundTouch

%changelog
%autochangelog
