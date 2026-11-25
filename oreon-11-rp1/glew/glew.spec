# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b64790f94b926acd7e8f84c5d6000a86cb43967bd1e688b03089079799c9e889

Name:           glew
Version:        2.3.1
Release:        1%{?dist}
Summary:        OpenGL Extension Wrangler Library
License:        BSD-3-Clause AND MIT
URL:            https://github.com/nigels-com/glew
Source0:        https://github.com/nigels-com/glew/releases/download/glew-%{version}/glew-%{version}.tgz

BuildRequires:  oreon-rpm-macros
BuildRequires:  clang
BuildRequires:  make
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(x11)

%description
GLEW is a C/C++ library that determines which OpenGL extensions are
available at run time and exposes them through a single header.

%package devel
Summary:        Development files for GLEW
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glu)

%description devel
Headers and pkg-config files for applications that use GLEW.

%package tools
Summary:        Utility programs for GLEW
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
Command-line utilities shipped with GLEW.

%prep
%oreon_sha256
%autosetup

%build
export CC=clang
export LD=clang
export AR=llvm-ar
%make_build SYSTEM=linux-clang STRIP= \
    CFLAGS.EXTRA='%{optflags} -fPIC' \
    GLEW_PREFIX=%{_prefix} GLEW_DEST=%{_prefix} \
    LIBDIR=%{_libdir} includedir=%{_includedir} \
    BINDIR=%{_bindir} PKGDIR=%{_libdir}/pkgconfig

%install
make SYSTEM=linux-clang STRIP= install.all DESTDIR=%{buildroot} \
    GLEW_PREFIX=%{_prefix} GLEW_DEST=%{_prefix} \
    LIBDIR=%{_libdir} includedir=%{_includedir} \
    BINDIR=%{_bindir} PKGDIR=%{_libdir}/pkgconfig
find %{buildroot} -name '*.a' -delete
chmod 0755 %{buildroot}%{_libdir}/libGLEW.so*

%ldconfig_scriptlets

%files
%license LICENSE.txt
%{_libdir}/libGLEW.so.2.3*

%files devel
%{_includedir}/GL/glew.h
%{_includedir}/GL/glxew.h
%{_includedir}/GL/wglew.h
%{_includedir}/GL/eglew.h
%{_libdir}/libGLEW.so
%{_libdir}/pkgconfig/glew.pc

%files tools
%{_bindir}/glewinfo
%{_bindir}/visualinfo
