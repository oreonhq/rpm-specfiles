%global source0_hash 35d404e6e8c2ebd12fb4000da6fadd75c99e37eed2126a04721828c11c0377ec
Name:           soundtouch
Version:        2.4.1
Release:        1%{?dist}
Summary:        Audio Processing library for changing Tempo, Pitch and Playback Rates
License:        LGPL-2.1-or-later
URL:            http://www.surina.net/soundtouch/
Source0:        https://codeberg.org/soundtouch/soundtouch/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
ln -s soundtouch.pc %{buildroot}%{_libdir}/pkgconfig/libSoundTouch.pc
ln -s soundtouch.pc %{buildroot}%{_libdir}/pkgconfig/soundtouch-1.0.pc
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n soundtouch-devel -f %{oreon_filedir}/soundtouch-devel.list

%changelog

%autochangelog
