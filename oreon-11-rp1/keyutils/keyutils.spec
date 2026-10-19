%global source0_hash a61d5706136ae4c05bd48f86186bcfdbd88dd8bd5107e3e195c924cfc1b39bb4
%define libapivermajor 1
%define libapiversion %{libapivermajor}.10
Name:    keyutils
Version: 1.6.3
Release:        1%{?dist}
Summary:        Linux Key Management Utilities
License: GPL-2.0-or-later AND LGPL-2.1-or-later
Url:   https://git.kernel.org/pub/scm/linux/kernel/git/dhowells/keyutils.git
Source0:        https://git.kernel.org/pub/scm/linux/kernel/git/dhowells/keyutils.git/snapshot/keyutils-1.6.3.tar.gz
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  g++
BuildRequires:  gcc
BuildRequires:  glibc-kernheaders
BuildRequires:  make
# /oreon:deps
%description
Utilities to control the kernel key management facility and to provide
a mechanism by which the kernel call back to user space to get a key
instantiated.

%package libs
Summary: Key utilities library
%description libs
This package provides a wrapper library for the key management facility system
calls.

%package libs-devel
Summary: Development package for building Linux key management utilities
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description libs-devel
This package provides headers and libraries for building key utilities.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

make \
	NO_ARLIB=1 \
	ETCDIR=%{_sysconfdir} \
	LIBDIR=%{_libdir} \
	USRLIBDIR=%{_libdir} \
	BINDIR=%{_bindir} \
	SBINDIR=%{_sbindir} \
	MANDIR=%{_mandir} \
	INCLUDEDIR=%{_includedir} \
	SHAREDIR=%{_datadir}/%{name} \
	RELEASE=.%{release} \
	NO_GLIBC_KEYERR=1 \
	CFLAGS="-Wall $RPM_OPT_FLAGS" \
	LDFLAGS="%{?__global_ldflags}"
%install
make \
	NO_ARLIB=1 \
	DESTDIR=$RPM_BUILD_ROOT \
	ETCDIR=%{_sysconfdir} \
	LIBDIR=%{_libdir} \
	USRLIBDIR=%{_libdir} \
	BINDIR=%{_bindir} \
	SBINDIR=%{_sbindir} \
	MANDIR=%{_mandir} \
	INCLUDEDIR=%{_includedir} \
	SHAREDIR=%{_datadir}/%{name} \
	install
%ldconfig_scriptlets libs
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n keyutils-libs -f %{oreon_filedir}/keyutils-libs.list
%files -n keyutils-libs-devel -f %{oreon_filedir}/keyutils-libs-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.3-7
- Prepare for Oreon 11 (RP1)
