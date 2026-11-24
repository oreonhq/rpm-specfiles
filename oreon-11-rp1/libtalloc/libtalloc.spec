# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 912afa237510ae542a7733998eb18a12bcda35ab6729c8e2ddb43e8d0ebab007
%global source1_hash c4c2b6f9f39a62146c5c52e52ce8843086bc6373c7e8a1b2ce0f80bcbe734913
%global source2_hash e88528311b8fc3c0acb520ac6c46f598a44b777239c75078827e02ed388b88e6
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global source2_key_fpr 9147A339719518EE9011BCB54793916113084025

Name:            libtalloc
Version:         2.5.0
Release:         1%{?dist}
Summary:         The talloc library
License:         LGPL-3.0-or-later
URL:             https://talloc.samba.org/

Source0:        https://www.samba.org/ftp/talloc/talloc-%{version}.tar.gz
Source1:        https://www.samba.org/ftp/talloc/talloc-%{version}.tar.asc
Source2:        talloc.keyring

BuildRequires: oreon-rpm-macros
BuildRequires: make
BuildRequires: clang
BuildRequires: libxslt
BuildRequires: docbook-style-xsl
BuildRequires: python3-devel
BuildRequires: doxygen
BuildRequires: gnupg2

Provides: bundled(libreplace)
Obsoletes: python2-talloc < 2.2.0-1
Obsoletes: python2-talloc-devel < 2.2.0-1

%description
A library that implements a hierarchical allocator with destructors.

%package devel
Summary:         Developer tools for the Talloc library

Requires: libtalloc = %{version}-%{release}

%description devel
Header files needed to develop programs that link against the Talloc library.

%package -n python3-talloc
Summary:         Python bindings for the Talloc library

Requires: libtalloc = %{version}-%{release}
%{?python_provide:%python_provide python3-talloc}

%description -n python3-talloc
Python 3 libraries for creating bindings using talloc

%package -n python3-talloc-devel
Summary:         Development libraries for python3-talloc

Requires: python3-talloc = %{version}-%{release}
%{?python_provide:%python_provide python3-talloc-devel}

%description -n python3-talloc-devel
Development libraries for python3-talloc

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n talloc-%{version} -p1

%build
zcat %{SOURCE0} | gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} -

export PYTHONARCHDIR=%{python3_sitearch}
%configure --disable-rpath \
           --disable-rpath-install \
           --bundled-libraries=NONE \
           --builtin-libraries=replace \
           --disable-silent-rules

%make_build
doxygen doxy.config

%check
%make_build check

%install
%make_install

cp -a doc/man/man3 %{buildroot}%{_mandir}

%files
%license LICENSE
%{_libdir}/libtalloc.so.*

%files devel
%{_includedir}/talloc.h
%{_libdir}/libtalloc.so
%{_libdir}/pkgconfig/talloc.pc
%{_mandir}/man3/talloc*.3*
%{_mandir}/man3/libtalloc*.3*

%files -n python3-talloc
%{_libdir}/libpytalloc-util.cpython*.so.*
%{python3_sitearch}/talloc.cpython*.so

%files -n python3-talloc-devel
%{_includedir}/pytalloc.h
%{_libdir}/pkgconfig/pytalloc-util.cpython-*.pc
%{_libdir}/libpytalloc-util.cpython*.so

%ldconfig_scriptlets
%ldconfig_scriptlets -n python3-talloc

%changelog
%autochangelog
