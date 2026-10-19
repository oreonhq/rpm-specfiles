%global source0_hash 399040138e0ca62fa2bcabd63da9af4431a246ef7a654561a0ca3cb00010a539
%global bpf_supported_arches aarch64 x86_64 ppc64le riscv64 s390x
Summary:        Alternate posix capabilities library
Name: libcap-ng
Version: 0.9.6
Release:        1%{?dist}
License: LGPL-2.0-or-later
URL: https://github.com/stevegrubb/libcap-ng
Source0:        https://github.com/stevegrubb/libcap-ng/archive/refs/tags/v0.9.6.tar.gz#/libcap-ng-0.9.6.tar.gz
%ifarch %{bpf_supported_arches}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  kernel-headers
BuildRequires:  libattr-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  python-unversioned-command
BuildRequires:  python3-devel
BuildRequires:  swig
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
rm -f $RPM_BUILD_ROOT%{_libdir}/libcap-ng.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libcap-ng.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libdrop_ambient.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libdrop_ambient.a
rm -f $RPM_BUILD_ROOT%{_libdir}/python%{python3_version}/site-packages/_capng.a
rm -f $RPM_BUILD_ROOT%{_libdir}/python%{python3_version}/site-packages/_capng.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%check

make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libcap-ng-devel -f %{oreon_filedir}/libcap-ng-devel.list
%files -n libcap-ng-python3 -f %{oreon_filedir}/libcap-ng-python3.list
%files -n libcap-ng-utils -f %{oreon_filedir}/libcap-ng-utils.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9.1-1
- Prepare for Oreon 11 (RP1)
