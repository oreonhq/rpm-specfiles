%global source0_hash f07fcec6f01edc4bb18373067494fdcb718186aed720b97ec6c7a5d67b218f69

Name: libcap
Version: 2.77
Release: 3%{?dist}
Summary: Library for getting and setting POSIX.1e capabilities
URL: https://sites.google.com/site/fullycapable/
License: BSD-3-Clause OR GPL-2.0-only

Source0:        https://mirrors.edge.kernel.org/pub/linux/libs/security/linux-privs/libcap2/%{name}-%{version}.tar.gz
Source1:        https://mirrors.edge.kernel.org/pub/linux/libs/security/linux-privs/libcap2/%{name}-%{version}.tar.sign
Source2: https://git.kernel.org/pub/scm/docs/kernel/pgpkeys.git/plain/keys/29EE848AE2CCF3F4.asc
Patch0: _makenames-build.patch

BuildRequires: pam-devel gcc
BuildRequires: make
BuildRequires: glibc-static
BuildRequires: gnupg2

%ifarch %{golang_arches}
BuildRequires: golang >= 1.22
%endif

%if "%{_sbindir}" == "%{_bindir}"
# Compat symlinks for Requires in other packages.
# We rely on filesystem to create the symlinks for us.
Requires:       filesystem(unmerged-sbin-symlinks)
Provides:       /usr/sbin/setcap
%endif

%description
libcap is a library for getting and setting POSIX.1e (formerly POSIX 6)
draft 15 capabilities.

%package static
Summary: Static libraries for libcap development
Requires: %{name} = %{version}-%{release}

%description static
The libcap-static package contains static libraries needed to develop programs
that use libcap and need to be statically linked. 

libcap is a library for getting and setting POSIX.1e (formerly POSIX 6)
draft 15 capabilities.

%package devel
Summary: Development files for libcap
Requires: %{name} = %{version}-%{release}

%description devel
Development files (Headers, etc) for libcap.

libcap is a library for getting and setting POSIX.1e (formerly POSIX 6)
draft 15 capabilities.

Install libcap-devel if you want to develop or compile applications using
libcap.

%ifarch %{golang_arches}
%package -n captree
Summary: Capability inspection utility

%description -n captree
The captree program was inspired by the utility pstree, but it uses the
libcap/cap (Go package) API to explore process runtime state and display
the capability status of processes and threads.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }gzip -cd %{SOURCE0} | %{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data=-
%autosetup -p1


%build
%make_build prefix=%{_prefix} lib=%{_lib} SBINDIR=%{_sbindir} CGO_REQUIRED=1 CGO_CFLAGS="${CFLAGS}" CGO_LDFLAGS="${LDFLAGS}" GO_BUILD_FLAGS="-buildmode=pie -a -v -x -ldflags='-compressdwarf=false -B gobuildid'" all

%check
make test

%install
%make_install prefix=%{_prefix} lib=%{_lib} SBINDIR=%{_sbindir} CGO_REQUIRED=1 CGO_CFLAGS="${CFLAGS}" CGO_LDFLAGS="${LDFLAGS}" GO_BUILD_FLAGS="-buildmode=pie -ldflags='-compressdwarf=false -B gobuildid'"

mkdir -p %{buildroot}/%{_mandir}/man{2,3,5,8}
mv -f doc/*.3 %{buildroot}/%{_mandir}/man3/

chmod +x %{buildroot}/%{_libdir}/*.so.*

%ldconfig_scriptlets

%files
%license License
%doc doc/capability.md
%{_libdir}/libcap.so.2{,.*}
%{_libdir}/libpsx.so.2{,.*}
%{_sbindir}/{capsh,getcap,getpcaps,setcap}
%{_mandir}/man1/capsh.1*
%{_mandir}/man5/capability.conf.5*
%{_mandir}/man7/cap_text_formats.7*
%{_mandir}/man8/{getcap,getpcaps,setcap,pam_cap}.8*
%{_libdir}/security/pam_cap.so
%exclude %{_mandir}/man8/captree.8*

%files static
%{_libdir}/libcap.a
%{_libdir}/libpsx.a

%files devel
%{_includedir}/sys/capability.h
%{_includedir}/sys/psx_syscall.h
%{_libdir}/libcap.so
%{_libdir}/libpsx.so
%{_mandir}/man3/cap*.3*
%{_mandir}/man3/libcap.3*
%{_mandir}/man3/libpsx.3*
%{_mandir}/man3/psx_*.3*
%{_mandir}/man3/__psx_syscall.3*
%{_libdir}/pkgconfig/{libcap,libpsx}.pc

%ifarch %{golang_arches}
%files -n captree
%license License
%{_sbindir}/captree
%{_mandir}/man8/captree.8*
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.77-3
- Prepare for Oreon 11 (RP1)
