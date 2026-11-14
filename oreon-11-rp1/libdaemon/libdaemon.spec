# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash fd23eb5f6f986dcc7e708307355ba3289abe03cc381fc47a80bca4a50aa6b834

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libdaemon
Version:        0.14
Release:        1%{?dist}
Summary:        Library for writing UNIX daemons
License:        LGPL-2.1-or-later
URL:            https://0pointer.de/lennart/projects/libdaemon/
Source0:        https://0pointer.de/lennart/projects/libdaemon/libdaemon-%{version}.tar.gz

BuildRequires:  oreon-rpm-macros
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  doxygen

%description
libdaemon is a lightweight C library that eases the writing of UNIX daemons.
It consists of the following parts:
 * A wrapper around fork() which does the correct daemonization procedure of
   a process
 * A wrapper around syslog() for simpler and compatible log output to Syslog
   or STDERR
 * An API for writing PID files
 * An API for serializing UNIX signals into a pipe for usage with select()
   or poll()
 * An API for running subprocesses with STDOUT and STDERR redirection

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
This package contains the header files and libraries needed to develop
applications that use libdaemon.

%prep
%oreon_sha256
%autosetup

%build
%configure --disable-static --disable-lynx
%make_build
make -C doc doxygen

%install
%make_install
find %{buildroot} -name '*.la' -delete -print
rm -rf %{buildroot}%{_docdir}

%check
make check

%ldconfig_scriptlets

%files
%license LICENSE
%doc README doc/README.html doc/style.css
%{_libdir}/libdaemon.so.0
%{_libdir}/libdaemon.so.0.*

%files devel
%doc doc/reference/html
%{_includedir}/libdaemon/
%{_libdir}/libdaemon.so
%{_libdir}/pkgconfig/libdaemon.pc

%changelog
%autochangelog
