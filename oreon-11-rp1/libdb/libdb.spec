# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash e0a992d740709892e81f9d93f06daf305cf73fb81b545afe72478043172c3628
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: libdb
Version: 5.3.28
Release: 1%{?dist}
Summary: Berkeley DB library
License: Sleepycat
URL: https://www.oracle.com/database/technologies/related/berkeleydb.html
Source0: https://download.oracle.com/berkeley-db/db-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: oreon-rpm-config
BuildRequires: gcc
BuildRequires: make
BuildRequires: patchelf

%description
The Berkeley DB library used by Perl DB_File.

%package devel
Summary: Development files for libdb
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers and the library link for libdb.

%prep
%oreon_sha256
%autosetup -n db-%{version}
cp -f /usr/lib/rpm/oreon/config.guess dist/config.guess
cp -f /usr/lib/rpm/oreon/config.sub dist/config.sub

%build
cd build_unix
%set_build_flags
../dist/configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-shared --disable-static --enable-compat185 --enable-dbm --with-mutex=POSIX/pthreads
%make_build

%install
%make_install -C build_unix
rm -rf %{buildroot}%{_docdir}
rm -f %{buildroot}%{_libdir}/*.la %{buildroot}%{_libdir}/*.a
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f" 2>/dev/null) || continue
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done

%files
%license LICENSE
%{_bindir}/db_*
%{_libdir}/libdb-5*.so

%files devel
%{_includedir}/db.h
%{_includedir}/db_185.h
%{_libdir}/libdb.so
