# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2cb894b873aac5fc9e9b6228d4e795f7236d16e429ed2de8f95179a131be3a68

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global glib2_version 2.45.8

Name: libxmlb
Version: 0.3.30
Release: 2%{?dist}
Summary: Library for querying compressed XML metadata
License: LGPL-2.1-or-later
URL: https://github.com/hughsie/libxmlb
Source0: https://github.com/hughsie/libxmlb/releases/download/%{version}/libxmlb-%{version}.tar.xz
Source1: libxmlb-%{version}.tar.xz.asc
Source2: gpgkey-163EB50119225DB3DF8F49EA17ACBA8DFA970E17.gpg

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: gnupg2
BuildRequires: gobject-introspection-devel
%if %{without bootstrap}
BuildRequires: gtk-doc
BuildRequires: shared-mime-info
%endif
BuildRequires: libzstd-devel
BuildRequires: meson
BuildRequires: python3-setuptools
BuildRequires: xz-devel

Requires: glib2%{?_isa} >= %{glib2_version}
Requires: shared-mime-info

%description
XML is slow to parse and strings inside the document cannot be memory mapped as
they do not have a trailing NUL char. The libxmlb library takes XML source, and
converts it to a structured binary representation with a deduplicated string
table, where the strings have the NULs included.

This allows an application to mmap the binary XML file, do an XPath query and
return some strings without actually parsing the entire document. This is all
done using (almost) zero allocations and no actual copying of the binary data.

%package devel
Summary: Development package for libxmlb
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: pkgconfig(xmlb) = %{version}

%description devel
Files for development with libxmlb.

%package tests
Summary: Files for installed tests
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tests
Executable and data files for installed tests.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1

%build
%meson \
%if %{with bootstrap}
    -Dgtkdoc=false \
%else
    -Dgtkdoc=true \
%endif
    -Dtests=true \
    -Dlzma=enabled \
    -Dzstd=enabled
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_bindir}/xb-tool
%{_mandir}/man1/xb-tool.1*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Xmlb-2.0.typelib
%{_libdir}/libxmlb.so.2*

%files devel
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Xmlb-2.0.gir
%if %{without bootstrap}
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/libxmlb
%endif
%{_includedir}/libxmlb-2
%{_libdir}/libxmlb.so
%{_libdir}/pkgconfig/xmlb.pc

%files tests
%dir %{_libexecdir}/installed-tests/libxmlb
%{_libexecdir}/installed-tests/libxmlb/xb-self-test
%{_libexecdir}/installed-tests/libxmlb/test.*
%dir %{_datadir}/installed-tests/libxmlb
%{_datadir}/installed-tests/libxmlb/libxmlb.test

%changelog
%autochangelog
