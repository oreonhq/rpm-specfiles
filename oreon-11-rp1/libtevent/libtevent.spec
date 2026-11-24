# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash e53b1ac288d017d66dde0471cd429a806168ecf07179d7f019572d7a7e05f0d6
%global source1_hash 1b9dfa04b6cb111b4cbd477155be5a675981ed545cc75cf1832961917a83a8d4
%global source2_hash 11197db7d14c377d77cc931c089246da99800ba4b2e87884449f60ceb5dfe4ea
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global talloc_version 2.5.0

Name:           libtevent
Version:        0.17.2
Release:        1%{?dist}
Summary:        The tevent library
License:        LGPL-3.0-or-later
URL:            http://tevent.samba.org/
Source0:        https://www.samba.org/ftp/tevent/tevent-%{version}.tar.gz
Source1:        https://www.samba.org/ftp/tevent/tevent-%{version}.tar.asc
Source2:        tevent.keyring

BuildRequires: oreon-rpm-macros
BuildRequires: docbook-style-xsl
BuildRequires: doxygen
BuildRequires: clang
BuildRequires: gnupg2
BuildRequires: libcmocka-devel >= 1.1.3
BuildRequires: libtalloc-devel >= %{talloc_version}
BuildRequires: libxslt
BuildRequires: make
BuildRequires: python3-devel
BuildRequires: python3-talloc-devel >= %{talloc_version}

Provides: bundled(libreplace)
Obsoletes: python2-tevent < 0.10.0-1

%description
Tevent is an event system based on the talloc memory management library.
Tevent has support for many event types, including timers, signals, and
the classic file descriptor events.
Tevent also provide helpers to deal with asynchronous code providing the
tevent_req (Tevent Request) functions.

%package devel
Summary:        Developer tools for the Tevent library

Requires: libtevent%{?_isa} = %{version}-%{release}
Requires: libtalloc-devel%{?_isa} >= %{talloc_version}

%description devel
Header files needed to develop programs that link against the Tevent library.

%package -n python3-tevent
Summary:        Python 3 bindings for the Tevent library

Requires: libtevent%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-tevent}

%description -n python3-tevent
Python 3 bindings for libtevent

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n tevent-%{version} -p1

%build
export PYTHONARCHDIR=%{python3_sitearch}
%configure --disable-rpath \
           --bundled-libraries=NONE \
           --builtin-libraries=replace

%make_build

doxygen doxy.config

%check
%make_build check

%install
%make_install

rm -f doc/man/man3/todo*
install -d -m0755 %{buildroot}%{_mandir}
cp -a doc/man/man3 %{buildroot}%{_mandir}

%files
%license LICENSE
%{_libdir}/libtevent.so.*

%files devel
%{_includedir}/tevent.h
%{_libdir}/libtevent.so
%{_libdir}/pkgconfig/tevent.pc
%{_mandir}/man3/tevent*.gz

%files -n python3-tevent
%{python3_sitearch}/tevent.py
%{python3_sitearch}/__pycache__/tevent.*
%{python3_sitearch}/_tevent.cpython*.so

%ldconfig_scriptlets

%changelog
%autochangelog
