# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 03754aede79530baa0e862e1aad5527e9c1bd3371736b1ab5a2bc769e4a3d680
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro}

%global make_flags \\\
        LIBDIR=%{_libdir} \\\
        CC=%{__cc} \\\
        GIT2LOG=: \\\
        VERSION=%%{version} \\\
        MAJOR_VERSION=%%(echo %{version} |cut -d. -f1) \\\
        CFLAGS="-fPIC %{optflags}" \\\
        LDFLAGS="-fPIC %{__global_ldflags}"

Name:           libx86emu
Version:        3.7
Release:        1%{?dist}
Summary:        x86 emulation library

License:        HPND-sell-variant
URL:            https://github.com/wfeldt/libx86emu
Source0:        https://github.com/wfeldt/libx86emu/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires:  clang
BuildRequires:  make

%description
Small x86 emulation library with focus of easy usage and extended execution
logging functions. The library features an API to create emulation objects
for x86 architecture.

%package devel
Summary:        Development files for libx86emu
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for developing with libx86emu, a x86 emulation
library.

%prep
%oreon_sha256
%autosetup

%build
%make_build %{make_flags} shared

%ldconfig_scriptlets

%install
%make_install %{make_flags}

%files
%{_libdir}/libx86emu.so.*
%doc README.md
%license LICENSE

%files devel
%{_includedir}/x86emu.h
%{_libdir}/libx86emu.so

%changelog
%autochangelog
