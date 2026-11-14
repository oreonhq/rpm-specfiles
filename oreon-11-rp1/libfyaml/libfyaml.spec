# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 9f813cad43777803dc3618d31a2efe3a03fafacf2592fabb383fffa5e185f2ce

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: libfyaml
Version: 0.8
Release: 1%{?dist}
Summary: Complete YAML parser and emitter
License: MIT AND GPL-2.0-only AND BSD-2-Clause
URL: https://github.com/pantoniou/libfyaml
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: LICENSE-GPL-2.0
Source2: LICENSE-BSD-2-Clause
Patch0: obsolete-macros-update.patch

BuildRequires: oreon-rpm-macros
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: check
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: libtool-ltdl-devel
BuildRequires: libyaml-devel
BuildRequires: make
BuildRequires: python3-sphinx
BuildRequires: sed

Provides: bundled(libxxhash)

%description
A fancy 1.2 YAML and JSON parser/writer.

Fully feature complete YAML parser and emitter, supporting
the latest YAML spec and passing the full YAML testsuite.

It is designed to be very efficient, avoiding copies of data,
and has no artificial limits like the 1024 character limit for
implicit keys.

%package -n fyaml-utils
Summary: Utility tools for libfyaml
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n fyaml-utils
Utility tools for libfyaml.

%package devel
Summary: Development files for libfyaml
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: pkgconfig(libfyaml) = %{version}

%description devel
Header files and libraries for libfyaml.

%prep
%oreon_sha256
%autosetup -p1
cp %{SOURCE1} .
cp %{SOURCE2} .

%build
autoreconf -fi
%configure --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

%check
make check

%files
%license LICENSE
%license LICENSE-GPL-2.0
%license LICENSE-BSD-2-Clause
%doc README.md
%doc AUTHORS
%{_libdir}/libfyaml.so.0*

%files -n fyaml-utils
%{_bindir}/fy-compose
%{_bindir}/fy-dump
%{_bindir}/fy-filter
%{_bindir}/fy-join
%{_bindir}/fy-testsuite
%{_bindir}/fy-tool
%{_bindir}/fy-ypath
%{_mandir}/man1/fy-compose.1*
%{_mandir}/man1/fy-dump.1*
%{_mandir}/man1/fy-filter.1*
%{_mandir}/man1/fy-join.1*
%{_mandir}/man1/fy-testsuite.1*
%{_mandir}/man1/fy-tool.1*
%{_mandir}/man1/fy-ypath.1*

%files devel
%{_includedir}/libfyaml.h
%{_libdir}/libfyaml.so
%{_libdir}/pkgconfig/libfyaml.pc

%changelog
%autochangelog
