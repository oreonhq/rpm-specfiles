%define libapivermajor 1
%define libapiversion %{libapivermajor}.10

# % define buildid .local

Name:    keyutils
Version: 1.6.3
Release: 7%{?buildid}%{?dist}
Summary: Linux Key Management Utilities
License: GPL-2.0-or-later AND LGPL-2.1-or-later
Url:   https://git.kernel.org/pub/scm/linux/kernel/git/dhowells/keyutils.git

Source0:        https://git.kernel.org/pub/scm/linux/kernel/git/dhowells/keyutils.git/snapshot/keyutils-1.6.3.tar.gz
# oreon url source checksums begin
%global source0_sha256 a61d5706136ae4c05bd48f86186bcfdbd88dd8bd5107e3e195c924cfc1b39bb4
%global source0_file keyutils-1.6.3.tar.gz
# oreon url source checksums end

BuildRequires: gcc
BuildRequires: glibc-kernheaders >= 2.4-9.1.92
BuildRequires: make
BuildRequires: g++
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/keyutils-1.6.3.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a61d5706136ae4c05bd48f86186bcfdbd88dd8bd5107e3e195c924cfc1b39bb4" || { echo "oreon: Source0 SHA256 mismatch for keyutils-1.6.3.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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

%files
%doc README
%license LICENCE.GPL
%config(noreplace) %{_sysconfdir}/*
%{_bindir}/keyctl
%{_sbindir}/key.dns_resolver
%{_sbindir}/request-key
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*

%files libs
%license LICENCE.LGPL
%{_libdir}/libkeyutils.so.%{libapiversion}
%{_libdir}/libkeyutils.so.%{libapivermajor}
%{_mandir}/man7/*

%files libs-devel
%{_libdir}/libkeyutils.so
%{_includedir}/keyutils.h
%{_libdir}/pkgconfig/libkeyutils.pc
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.3-7
- Prepare for Oreon 11 (RP1)
