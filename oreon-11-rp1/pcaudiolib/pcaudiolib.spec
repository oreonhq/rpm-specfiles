# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 699a5a347b1e12dc5b122e192e19f4db01621826bf41b9ebefb1cbc63ae2180b
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           pcaudiolib
Version:        1.1
Release:        1%{?dist}
Summary:        Portable C Audio Library

License:        GPL-3.0-or-later
URL:            https://github.com/rhdunn/pcaudiolib
Source0:        %{url}/archive/%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  alsa-lib-devel
BuildRequires:  pulseaudio-libs-devel

%description
The Portable C Audio Library (pcaudiolib) provides a C API to different
audio devices.

%package devel
Summary: Development files for pcaudiolib
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for the Portable C Audio Library.

%prep
%oreon_sha256
%autosetup
rm -rf src/TPCircularBuffer

%build
./autogen.sh
%configure --without-coreaudio
%make_build

%install
%make_install
rm -vf %{buildroot}%{_libdir}/*.{a,la}

%ldconfig_scriptlets

%files
%license COPYING
%doc README.md
%doc AUTHORS
%doc CHANGELOG.md
%{_libdir}/libpcaudio.so.*

%files devel
%{_libdir}/libpcaudio.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/audio.h

%changelog
%autochangelog
