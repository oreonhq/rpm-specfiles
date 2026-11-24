# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 3a0b13815f582c661d2388ffcabc2f1ea82f471783c400f765f2ec6c81065f6a
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global sovermajor 0

Summary: DTS Coherent Acoustics decoder library
Name: libdca
Version: 0.0.7
Release: 1%{?dist}
License: GPL-2.0-or-later
URL: https://code.videolan.org/videolan/libdca
Source0:        http://download.videolan.org/pub/videolan/%{name}/%{version}/%{name}-%{version}.tar.bz2

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: automake
BuildRequires: libtool
BuildRequires: make

%description
libdca is a free library for decoding DTS Coherent Acoustics streams. It is
released under the terms of the GPL license. The DTS Coherent Acoustics
standard is used in a variety of applications, including DVD, DTS audio CD and
radio broadcasting.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.

Install %{name}-devel if you wish to develop or compile
applications that use %{name}.

%package tools
Summary: Various tools for use with %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
Various tools that use %{name}.

%prep
%oreon_sha256
%autosetup

iconv -f ISO8859-1 -t UTF-8 AUTHORS > tmp; mv tmp AUTHORS

%build
%ifarch %{ix86}
export  LDFLAGS+="-Wl,-z,notext"
%endif
autoreconf -fiv
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install

find $RPM_BUILD_ROOT -name '*.la' -or -name '*.a' | xargs rm -f

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%{_libdir}/%{name}.so.%{sovermajor}{,.*}

%files tools
%{_bindir}/*
%{_mandir}/man1/*

%files devel
%doc TODO doc/%{name}.txt
%{_libdir}/pkgconfig/libd??.pc
%{_includedir}/d??.h
%{_libdir}/%{name}.so

%changelog
%autochangelog
