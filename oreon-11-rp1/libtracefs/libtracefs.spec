# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 75187bad93e622c94c4a691173e45f08948d38b9a28e9b855b54a3e956d289a6
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: libtracefs
Version: 1.8.4
Release: 1%{?dist}
License: LGPL-2.1-or-later AND GPL-2.0-or-later AND GPL-2.0-only
Summary: Library for access kernel tracefs
URL: https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git/
Source0: https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git/snapshot/libtracefs-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: make
BuildRequires: xmlto
BuildRequires: asciidoc
BuildRequires: pkgconfig(libtraceevent) >= 1.8.0
Conflicts: trace-cmd < 2.9.1-6

%description
libtracefs is a library for accessing kernel tracefs.

%package devel
Summary: Development headers of %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers of %{name}.

%prep
%oreon_sha256
%autosetup -p1

%build
%set_build_flags
make -O -j1 V=1 VERBOSE=1 CC=%{__cc} prefix=%{_prefix} libdir=%{_libdir} all doc

%install
%make_install CC=%{__cc} prefix=%{_prefix} libdir=%{_libdir} install_doc
rm -f %{buildroot}%{_libdir}/libtracefs.a

%files
%license LICENSES/LGPL-2.1
%license LICENSES/GPL-2.0
%{_libdir}/%{name}.so.1
%{_libdir}/%{name}.so.%{version}
%{_docdir}/libtracefs-doc
%{_mandir}/man1/sqlhist.1*
%{_mandir}/man3/libtracefs.3*
%{_mandir}/man3/tracefs_*
%{_datadir}/bash-completion/completions/tracefs_sql.bash

%files devel
%{_includedir}/tracefs/tracefs.h
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so

%changelog
%autochangelog
