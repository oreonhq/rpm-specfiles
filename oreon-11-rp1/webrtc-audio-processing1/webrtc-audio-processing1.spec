# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2365e93e778d7b61b5d6e02d21c47d97222e9c7deff9e1d0838ad6ec2e86f1b9
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           webrtc-audio-processing1
Version:        1.3
Release:        1%{?dist}
Summary:        Library for echo cancellation

License:        BSD-3-Clause
URL:            http://www.freedesktop.org/software/pulseaudio/webrtc-audio-processing/
Source0:        http://freedesktop.org/software/pulseaudio/webrtc-audio-processing/webrtc-audio-processing-%{version}.tar.xz

Patch0:         arches.patch
Patch1:         65f002e.patch
Patch2:         webrtc-audio-processing-1.3-gcc15.patch

Patch3:         webrtc-audio-processing-1.3-add-loongarch64-support.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: abseil-cpp-devel

%description
webrtc-audio-processing is a library derived from Google WebRTC project that
provides echo cancellation functionality. This library is used by for example
PulseAudio to provide echo cancellation.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header
files for developing applications that use %{name}.

%prep
%oreon_sha256
%autosetup -n webrtc-audio-processing-%{version} -p1

%build
%meson
%meson_build \

%install
%meson_install

%ldconfig_scriptlets

%files
%doc NEWS AUTHORS README.md
%license COPYING
%{_libdir}/libwebrtc-audio-coding-1.so.3*
%{_libdir}/libwebrtc-audio-processing-1.so.3*

%files devel
%{_libdir}/libwebrtc-audio-coding-1.so
%{_libdir}/libwebrtc-audio-processing-1.so
%{_libdir}/pkgconfig/webrtc-audio-coding-1.pc
%{_libdir}/pkgconfig/webrtc-audio-processing-1.pc
%{_includedir}/webrtc-audio-processing-1/

%changelog
%autochangelog
