%global source0_hash 920dbba4a3e1624b07aa813c8b8dc9339aeb10e0676958d250f5bedc8a22db31
%global commit 48689ae7a73caeb747953f9ed664dc71d2f918d8
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20230517
%global fgittag %{gitdate}.git%{shortcommit}
Name:           cubeb
Version:        0.2
Release:        1%{?dist}
Summary:        A cross platform audio library
License:        ISC AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL:            https://github.com/mozilla/cubeb
Source0:        https://github.com/mozilla/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  pulseaudio-libs-devel
# /oreon:deps
%description
Cubeb is a cross-platform library, written in C/C++, that was created and has
been maintained by the Firefox Media Team.
The role of the library is to communicate with audio devices and to provide
audio input and/or output.

%package devel
Summary:        A cross platform audio library
Provides:       %{name}-static = %{version}-%{release}
%description devel
Cubeb is a cross-platform library, written in C/C++, that was created and has
been maintained by the Firefox Media Team.
The role of the library is to communicate with audio devices and to provide
audio input and/or output.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit}
#Clean up Android files
rm -rf src/android

#Clean up the README.md, we don't need building information:
sed -i -e "/^\[!/d" -e "/INSTALL.md/d" README.md

%build

%cmake . -DBUILD_SHARED_LIBS=OFF -DBUILD_TESTS=ON -DUSE_SANITIZERS=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles cubeb-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest -R "(record|resampler|duplex|triple_buffer|ring_array|utils|ring_buffer|device_changed_callback)"
%files -f %{oreon_filedir}/main.list
%files -n cubeb-devel -f %{oreon_filedir}/cubeb-devel.list

%changelog

%autochangelog
