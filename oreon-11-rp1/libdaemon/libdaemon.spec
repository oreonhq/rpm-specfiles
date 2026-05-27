%global source0_hash fd23eb5f6f986dcc7e708307355ba3289abe03cc381fc47a80bca4a50aa6b834

Name: libdaemon
Version: 0.14
Release: 33%{?dist}
Summary: Library for writing UNIX daemons
License: LGPL-2.1-or-later
URL: http://0pointer.de/lennart/projects/libdaemon/
Source0: http://0pointer.de/lennart/projects/libdaemon/%{name}-%{version}.tar.gz

# Requires lynx to build the docs
BuildRequires:  gcc
BuildRequires:  lynx
BuildRequires: make

%description
libdaemon is a lightweight C library which eases the writing of UNIX daemons.
It consists of the following parts:
* A wrapper around fork() which does the correct daemonization
  procedure of a process
* A wrapper around syslog() for simpler and compatible log output to
  Syslog or STDERR
* An API for writing PID files
* An API for serializing UNIX signals into a pipe for usage with
  select() or poll()
* An API for running subprocesses with STDOUT and STDERR redirected
  to syslog.

%package devel
Summary: Libraries and header files for libdaemon development
Requires: libdaemon = %{version}-%{release}

%description devel
The libdaemon-devel package contains the header files and libraries
necessary for developing programs using libdaemon.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT \( -name *.a -o -name *.la \) -exec rm {} \;

rm $RPM_BUILD_ROOT/%{_datadir}/doc/libdaemon/README
rm $RPM_BUILD_ROOT/%{_datadir}/doc/libdaemon/README.html
rm $RPM_BUILD_ROOT/%{_datadir}/doc/libdaemon/style.css

%ldconfig_scriptlets

%files
%doc LICENSE README
%{_libdir}/*so.*

%files devel
%doc doc/README.html doc/style.css
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.14-33
- Prepare for Oreon 11 (RP1)
