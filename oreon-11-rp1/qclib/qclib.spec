%global source0_hash be058fce3ab471fbc11a45c0ab9b3ec68e064c16632413346df3275a7cb5f3be
Name:		qclib
Version:	2.5.2
Release:        1%{?dist}
Summary:        Library for extraction of system information for Linux on z Systems
License:	BSD-3-Clause
URL:		https://github.com/ibm-s390-linux/qclib
Source0:        https://github.com/ibm-s390-linux/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:	s390 s390x
Requires:	glibc-gconv-extra
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  glibc-static
BuildRequires:  make
BuildRequires:  which
# /oreon:deps
%description
%{summary}.

%package devel
Summary:	Development library and headers for qclib
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
qclib provides a C API for extraction of system information for Linux on z
Systems.
For instance, it will provide the number of CPUs
 * on the machine (CEC, Central Electronic Complex) layer
 * on the PR/SM (Processor Resource/Systems Manager) layer, i.e. visible to
   LPARs, including LPAR groups in z/VM hosts, guests and CPU pools
 * in KVM hosts and guests

This allows calculating the upper limit of CPU resources a highest level guest
can use. For example: If an LPAR on a z13 provides 4 CPUs to a z/VM hyper-visor,
and the hyper-visor provides 8 virtual CPUs to a guest, qclib can be used to
retrieve all of these numbers, and it can be concluded that not more capacity
than 4 CPUs can be used by the software running in the guest.

This package provides the development libraries and headers for qclib.

%package static
Summary:	Static library for qclib
Requires:	%{name}-devel = %{version}-%{release}
Provides:	%{name}-static = %{version}-%{release}
%description static
%{summary}. This package provides static libraries for qclib.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

make V=1 CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" %{?_smp_mflags} all doc
%install
%make_install V=1 DOCDIR=%{_docdir}
make DESTDIR=%{buildroot} DOCDIR=%{_docdir} installdoc
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test-sh test
%files -f %{oreon_filedir}/main.list
%files -n qclib-devel -f %{oreon_filedir}/qclib-devel.list
%files -n qclib-static -f %{oreon_filedir}/qclib-static.list

%changelog

%autochangelog
