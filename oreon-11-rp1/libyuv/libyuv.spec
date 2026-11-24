# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 95841282a49bbad508c51e8c8af17d909cb0671486d600785256fe5b5a45336d
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global git_commit 6067afde563c3946eebd94f146b3824ab7a97a9c
%global git_date 20260213

Name:		libyuv
Summary:	YUV conversion and scaling functionality library
Version:	0
Release:        %{autorelease}
License:	BSD-3-Clause
Url:		https://chromium.googlesource.com/libyuv/libyuv
VCS:		git:%{url}
Source0:	%{url}/+archive/%{git_commit}.tar.gz
Patch:		libyuv-0001-Use-a-proper-so-version.patch
Patch:		libyuv-0002-Link-against-shared-library.patch
Patch:		libyuv-0003-Use-GNUInstallDirs-during-installation.patch
Patch:		libyuv-0004-Use-CTest-switches-for-testing.patch
Patch:		libyuv-0005-arch-s390x-disable-little-endian-tests.patch
Patch:		libyuv-0006-Don-t-install-tools-and-static-lib.patch
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:	cmake
BuildRequires:	cmake(GTest)
BuildRequires:	pkgconfig(libjpeg)

%description
This is an open source project that includes YUV conversion and scaling
functionality. Converts all webcam formats to YUV (I420). Convert YUV to
formats for rendering/effects. Rotate by 90 degrees to adjust for mobile
devices in portrait mode. Scale YUV to prepare content for compression,
with point, bilinear or box filter.

%package devel
Summary: The development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Additional header files for development with %{name}.

%prep
%oreon_sha256
%autosetup -p1 -c %{name}-%{version}

cat > %{name}.pc << EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: %{name}
Description: %{summary}
Version: %{version}
Libs: -lyuv
EOF

%build
%{cmake} -DUNIT_TEST=TRUE
%{cmake_build}

%install
%{cmake_install}
install -D -p -m 0644  %{name}.pc %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

%check
%ifnarch s390x
%{ctest}
%endif

%files
%license LICENSE
%doc AUTHORS PATENTS README.md
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/%{name}
%{_includedir}/%{name}.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
