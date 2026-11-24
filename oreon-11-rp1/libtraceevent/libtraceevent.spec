# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 3bc19dd940914260ba591b5276723bf84bb43f82c7c3d4267622bee4d016ea55
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global __provides_exclude_from ^%{_libdir}/traceevent/plugins

Name: libtraceevent
Version: 1.9.1
Release: 1%{?dist}
License: LGPL-2.1-only AND LGPL-2.1-or-later AND GPL-2.0-only AND GPL-2.0-or-later
Summary: Library to parse raw trace event formats
URL: https://git.kernel.org/pub/scm/libs/libtrace/libtraceevent.git/
Source0: https://git.kernel.org/pub/scm/libs/libtrace/libtraceevent.git/snapshot/libtraceevent-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: make
BuildRequires: xmlto
BuildRequires: asciidoc
BuildRequires: docbook-style-xsl

%description
libtraceevent is a library to parse raw trace event formats.

%package devel
Summary: Development headers of %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers of %{name}.

%prep
%oreon_sha256
%autosetup -p1

%build
MANPAGE_DOCBOOK_XSL=$(rpm -ql docbook-style-xsl | grep manpages/docbook.xsl)
make -O -j1 V=1 VERBOSE=1 CC=%{__cc} CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" prefix=%{_prefix} libdir=%{_libdir} MANPAGE_XSL=$MANPAGE_DOCBOOK_XSL all doc

%install
%make_install CC=%{__cc} prefix=%{_prefix} libdir=%{_libdir} install doc-install
rm -f %{buildroot}%{_libdir}/libtraceevent.a

%files
%license LICENSES/LGPL-2.1
%license LICENSES/GPL-2.0
%{_libdir}/traceevent/
%{_libdir}/libtraceevent.so.%{version}
%{_libdir}/libtraceevent.so.1
%{_mandir}/man3/tep_*.3*
%{_mandir}/man3/libtraceevent.3*
%{_mandir}/man3/trace_seq*.3*
%{_mandir}/man3/kbuffer_*.3*
%{_docdir}/%{name}-doc

%files devel
%{_includedir}/traceevent/
%{_libdir}/libtraceevent.so
%{_libdir}/pkgconfig/libtraceevent.pc

%changelog
%autochangelog
