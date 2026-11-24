# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b111c15fdc8c029989330ff559184198c161100a59312f5dc19ddeb9b5a15889
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global __cmake_in_source_build 1

Name:           soxr
Version:        0.1.3
Release:        1%{?dist}
Summary:        The SoX Resampler library

License:        LGPL-2.1-or-later AND NCL
URL:            https://sourceforge.net/p/soxr/wiki/Home/ 
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-Source.tar.xz

Patch0:         soxr-cmake.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  cmake
Provides:       bundled(pffft)

%description
The SoX Resampler library `libsoxr' performs one-dimensional sample-rate
conversion -- it may be used, for example, to resample PCM-encoded audio.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256
%autosetup -n %{name}-%{version}-Source

%build
export LDFLAGS="-Wl,--as-needed"
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DWITH_CR32S=FALSE \
       -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install
%cmake_install

rm -rf %{buildroot}%{_docdir}/*

%check
%ctest

%ldconfig_scriptlets

%files
%doc NEWS README
%license LICENCE
%{_libdir}/*.so.*

%files devel
%doc examples
%{_includedir}/%{name}*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/soxr-lsr.pc
%{_libdir}/pkgconfig/soxr.pc

%changelog
%autochangelog
