%global source0_hash b431f6e3c1a29fa9394143885edb7b013510f103f0870f45be4b8a7aade91961
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: keyutils
Version: 1.6.3
Release: 10%{?dist}
Summary: Linux key management utilities
License: GPL-2.0-or-later AND LGPL-2.1-or-later
URL: https://git.kernel.org/pub/scm/linux/kernel/git/dhowells/keyutils.git
Source0: https://git.kernel.org/pub/scm/linux/kernel/git/dhowells/keyutils.git/snapshot/v%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: file

Requires: keyutils-libs%{?_isa} = %{version}-%{release}

%description
Utilities to control the Linux kernel key management facility.

%package libs
Summary: Linux key management library

%description libs
Shared library for the Linux key management facility.

%package libs-devel
Summary: Development files for the Linux key management library
Requires: keyutils-libs%{?_isa} = %{version}-%{release}
Obsoletes: keyutils-devel < 1.6.3-10

%description libs-devel
Header, pkg-config file, and man pages for libkeyutils.

%prep
%oreon_sha256
%autosetup -n v%{version} -p1

%build
make %{?_smp_mflags} NO_ARLIB=1 BINDIR=%{_bindir} SBINDIR=%{_sbindir} LIBDIR=%{_libdir} USRLIBDIR=%{_libdir} MANDIR=%{_mandir} INCLUDEDIR=%{_includedir} SHAREDIR=%{_datadir}/keyutils ETCDIR=%{_sysconfdir} CFLAGS="%{_oreon_cflags} -fPIC"

%install
make install DESTDIR=%{buildroot} NO_ARLIB=1 BINDIR=%{_bindir} SBINDIR=%{_sbindir} LIBDIR=%{_libdir} USRLIBDIR=%{_libdir} MANDIR=%{_mandir} INCLUDEDIR=%{_includedir} SHAREDIR=%{_datadir}/keyutils ETCDIR=%{_sysconfdir}
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done

%ldconfig_scriptlets libs

%files
%license LICENCE.GPL
%{_bindir}/keyctl
%{_sbindir}/request-key
%{_sbindir}/key.dns_resolver
%config(noreplace) %{_sysconfdir}/request-key.conf
%dir %{_sysconfdir}/request-key.d
%dir %{_datadir}/keyutils
%{_datadir}/keyutils/request-key-debug.sh
%{_mandir}/man1/keyctl.1*
%{_mandir}/man5/request-key.conf.5*
%{_mandir}/man5/key.dns_resolver.conf.5*
%{_mandir}/man7/keyutils.7*
%{_mandir}/man7/asymmetric-key.7*
%{_mandir}/man8/request-key.8*
%{_mandir}/man8/key.dns_resolver.8*

%files libs
%license LICENCE.LGPL
%{_libdir}/libkeyutils.so.1
%{_libdir}/libkeyutils.so.1.*

%files libs-devel
%{_includedir}/keyutils.h
%{_libdir}/libkeyutils.so
%{_libdir}/pkgconfig/libkeyutils.pc
%{_mandir}/man3/*.3*
