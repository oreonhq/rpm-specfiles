# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash fba09d8df1f1b9072aeae8e78b2bd43c5afef20b2f6deefa633aa14a377a8dd2
%global source1_hash 18c2fd8e8ae2346fc24dc0957c499892cedc8004bc7a3061e90b244f1b2720a6
%global source2_hash 11197db7d14c377d77cc931c089246da99800ba4b2e87884449f60ceb5dfe4ea
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:            libtdb
Version:         1.4.15
Release:         1%{?dist}
Summary:         The tdb library
License:         LGPL-3.0-or-later
URL:             http://tdb.samba.org/
Source0:        https://www.samba.org/ftp/tdb/tdb-%{version}.tar.gz
Source1:        https://www.samba.org/ftp/tdb/tdb-%{version}.tar.asc
Source2:         tdb.keyring

BuildRequires: oreon-rpm-macros
BuildRequires: make
BuildRequires: clang
BuildRequires: gnupg2
BuildRequires: libxslt
BuildRequires: docbook-style-xsl
BuildRequires: python3-devel

Provides: bundled(libreplace)
Obsoletes: python2-tdb < 1.4.2-1

%description
A library that implements a trivial database.

%package         devel
Summary:         Header files need to link the Tdb library

Requires: libtdb = %{version}-%{release}

%description devel
Header files needed to develop programs that link against the Tdb library.

%package -n tdb-tools
Summary:         Developer tools for the Tdb library

Requires: libtdb = %{version}-%{release}

%description -n tdb-tools
Tools to manage Tdb files

%package -n python3-tdb
Summary: Python3 bindings for the Tdb library
Requires: libtdb = %{version}-%{release}
%{?python_provide:%python_provide python3-tdb}

%description -n python3-tdb
Python3 bindings for libtdb

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n tdb-%{version} -p1

%build
zcat %{SOURCE0} | gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} -
export PYTHONARCHDIR=%{python3_sitearch}
%configure --disable-rpath \
           --bundled-libraries=NONE \
           --builtin-libraries=replace

%make_build

%check
%make_build check

%install
%make_install

%files
%license LICENSE
%{_libdir}/libtdb.so.*

%files devel
%doc docs/README
%{_includedir}/tdb.h
%{_libdir}/libtdb.so
%{_libdir}/pkgconfig/tdb.pc

%files -n tdb-tools
%{_bindir}/tdbbackup
%{_bindir}/tdbdump
%{_bindir}/tdbtool
%{_bindir}/tdbrestore
%{_mandir}/man8/tdbbackup.8*
%{_mandir}/man8/tdbdump.8*
%{_mandir}/man8/tdbtool.8*
%{_mandir}/man8/tdbrestore.8*

%files -n python3-tdb
%{python3_sitearch}/__pycache__/_tdb_text.cpython*.py[co]
%{python3_sitearch}/tdb.cpython*.so
%{python3_sitearch}/_tdb_text.py

%ldconfig_scriptlets

%changelog
%autochangelog
