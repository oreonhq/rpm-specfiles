%global source0_hash 0d621e562fd932ccf67b9660fb018e468a683d7b827541df27813228c996bb11
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libcap
Version: 2.78
Release: 1%{?dist}
Summary: POSIX capability library
License: BSD-3-Clause OR GPL-2.0-only
URL: https://sites.google.com/site/fullycapable/
Source0: https://mirrors.edge.kernel.org/pub/linux/libs/security/linux-privs/libcap2/libcap-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
libcap is a library for getting and setting POSIX capabilities.

%package devel
Summary: POSIX capability library
Requires: libcap%{?_isa} = %{version}-%{release}
Provides: pkgconfig(libcap)
Provides: pkgconfig(libpsx)

%description devel
libcap is a library for getting and setting POSIX capabilities.

%prep
%oreon_sha256
%autosetup -p1

%build
export CFLAGS="%{_oreon_cflags} -fPIC"
export LDFLAGS="%{_oreon_ldflags}"
make -C libcap %{?_smp_mflags} prefix=%{_prefix} lib=lib64 PAM_CAP=no RAISE_SETFCAP=no GOLANG=no
make -C progs %{?_smp_mflags} prefix=%{_prefix} lib=lib64 PAM_CAP=no RAISE_SETFCAP=no GOLANG=no
make -C doc prefix=%{_prefix} lib=lib64 PAM_CAP=no

%install
export CFLAGS="%{_oreon_cflags} -fPIC"
export LDFLAGS="%{_oreon_ldflags}"
make -C libcap install DESTDIR=%{buildroot} prefix=%{_prefix} lib=lib64 PAM_CAP=no RAISE_SETFCAP=no GOLANG=no
make -C progs install DESTDIR=%{buildroot} prefix=%{_prefix} lib=lib64 PAM_CAP=no RAISE_SETFCAP=no GOLANG=no
make -C doc install DESTDIR=%{buildroot} prefix=%{_prefix} lib=lib64 PAM_CAP=no
rm -f %{buildroot}%{_libdir}/*.a

%files
%license License
%{_sbindir}/capsh
%{_sbindir}/getcap
%{_sbindir}/getpcaps
%{_sbindir}/setcap
%{_libdir}/libcap.so.2
%{_libdir}/libcap.so.2.*
%{_libdir}/libpsx.so.2
%{_libdir}/libpsx.so.2.*
%{_mandir}/man1/capsh.1*
%{_mandir}/man5/capability.conf.5*
%{_mandir}/man7/cap_text_formats.7*
%{_mandir}/man8/getcap.8*
%{_mandir}/man8/getpcaps.8*
%{_mandir}/man8/setcap.8*
%{_mandir}/man8/captree.8*
%{_mandir}/man8/pam_cap.8*

%files devel
%{_includedir}/sys/capability.h
%{_includedir}/sys/psx_syscall.h
%{_libdir}/libcap.so
%{_libdir}/libpsx.so
%{_libdir}/pkgconfig/libcap.pc
%{_libdir}/pkgconfig/libpsx.pc
%{_mandir}/man3/cap*.3*
%{_mandir}/man3/libcap.3*
%{_mandir}/man3/libpsx.3*
%{_mandir}/man3/psx_*.3*
%{_mandir}/man3/__psx_syscall.3*
