%global source0_hash 79f3d2c88f44b7eb5cf54d9792e03232297e17f97a179163f2750099a00f164d
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libsepol
Version: 3.11
Release: 1%{?dist}
Summary: SELinux binary policy library
License: LGPL-2.1-or-later
URL: https://github.com/SELinuxProject/selinux
Source0: https://github.com/SELinuxProject/selinux/releases/download/%{version}/libsepol-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: flex
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
libsepol is the library for manipulating SELinux binary policies.

%package devel
Summary: SELinux binary policy library
Requires: libsepol%{?_isa} = %{version}-%{release}
Provides: pkgconfig(libsepol)

%description devel
libsepol is the library for manipulating SELinux binary policies.

%prep
%oreon_sha256
%autosetup -p1

%build
export CFLAGS="%{_oreon_cflags}"
export LDFLAGS="%{_oreon_ldflags}"
make %{?_smp_mflags} PREFIX=%{_prefix} LIBDIR=%{_libdir} SHLIBDIR=%{_libdir}

%install
export CFLAGS="%{_oreon_cflags}"
export LDFLAGS="%{_oreon_ldflags}"
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_libdir} SHLIBDIR=%{_libdir}
rm -f %{buildroot}%{_libdir}/*.a

%files
%license LICENSE
%{_bindir}/chkcon
%{_bindir}/sepol_check_access
%{_bindir}/sepol_compute_av
%{_bindir}/sepol_compute_member
%{_bindir}/sepol_compute_relabel
%{_bindir}/sepol_validate_transition
%{_libdir}/libsepol.so.2
%{_mandir}/man8/chkcon.8*
%{_mandir}/man8/genpolbools.8*
%{_mandir}/man8/genpolusers.8*

%files devel
%{_includedir}/sepol
%{_libdir}/libsepol.so
%{_libdir}/pkgconfig/libsepol.pc
%{_mandir}/man3/sepol_*.3*
