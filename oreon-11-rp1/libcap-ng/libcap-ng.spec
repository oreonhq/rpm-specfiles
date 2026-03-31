%global bpf_supported_arches aarch64 x86_64 ppc64le riscv64 s390x
Summary: Alternate posix capabilities library
Name: libcap-ng
Version: 0.9.1
Release: 1%{?dist}
License: LGPL-2.0-or-later
URL: https://github.com/stevegrubb/libcap-ng
Source0: %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: gcc make
BuildRequires: autoconf automake libtool
BuildRequires: kernel-headers >= 2.6.11 
BuildRequires: libattr-devel
%ifarch %{bpf_supported_arches}
# These next ones are needed by cap-audit
BuildRequires: clang
BuildRequires: bpftool libbpf-devel
BuildRequires: audit-libs-devel
%endif

%description
Libcap-ng is a library that makes using posix capabilities easier

%package devel
Summary: Header files for libcap-ng library
License: LGPL-2.0-or-later
Requires: kernel-headers >= 2.6.11
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
The libcap-ng-devel package contains the files needed for developing
applications that need to use the libcap-ng library.

%package python3
Summary: Python3 bindings for libcap-ng library
License: LGPL-2.0-or-later
BuildRequires: python3-devel swig python-unversioned-command
Requires: %{name}%{?_isa} = %{version}-%{release}

%description python3
The libcap-ng-python3 package contains the bindings so that libcap-ng
and can be used by python3 applications.

%package utils
Summary: Utilities for analyzing and setting file capabilities
License: GPL-2.0-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}
%ifarch %{bpf_supported_arches}
Provides: %{name}-audit
Obsoletes: %{name}-audit < %{version}-%{release}
%endif

%description utils
The libcap-ng-utils package contains applications to analyze the
posix capabilities of all the program running on a system. It also
lets you set the file system based capabilities, and use cap-audit
to determine the necessary capabilities for a program.

%prep
%setup -q
touch NEWS
autoreconf -fv --install

%build
%configure --libdir=%{_libdir} \
%ifarch %{bpf_supported_arches}
	 --enable-cap-audit=yes \
%endif
	--with-python3

%make_build CFLAGS="%{optflags}"

%install
%make_install

# Remove a couple things so they don't get picked up
rm -f $RPM_BUILD_ROOT%{_libdir}/libcap-ng.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libcap-ng.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libdrop_ambient.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libdrop_ambient.a
rm -f $RPM_BUILD_ROOT%{_libdir}/python%{python3_version}/site-packages/_capng.a
rm -f $RPM_BUILD_ROOT%{_libdir}/python%{python3_version}/site-packages/_capng.la

%check
make check

%ldconfig_scriptlets

%files
%license COPYING.LIB
%{_libdir}/libcap-ng.so.*
%{_libdir}/libdrop_ambient.so.*
%attr(0644,root,root) %{_mandir}/man7/*

%files devel
%attr(0644,root,root) %{_mandir}/man3/*
%attr(0644,root,root) %{_includedir}/cap-ng.h
%{_libdir}/libcap-ng.so
%{_libdir}/libdrop_ambient.so
%attr(0644,root,root) %{_datadir}/aclocal/cap-ng.m4
%{_libdir}/pkgconfig/libcap-ng.pc

%files python3
%attr(755,root,root) %{python3_sitearch}/*

%files utils
%license COPYING
%attr(0755,root,root) %{_bindir}/filecap
%attr(0755,root,root) %{_bindir}/netcap
%attr(0755,root,root) %{_bindir}/pscap
%attr(0644,root,root) %{_mandir}/man8/filecap.8.gz
%attr(0644,root,root) %{_mandir}/man8/netcap.8.gz
%attr(0644,root,root) %{_mandir}/man8/pscap.8.gz
%ifarch %{bpf_supported_arches}
%attr(0755,root,root) %{_bindir}/cap-audit
%attr(0644,root,root) %{_mandir}/man8/cap-audit.8.gz
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9.1-1
- Prepare for Oreon 11 (RP1)
