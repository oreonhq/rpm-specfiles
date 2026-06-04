%global source0_hash 4624bc68aa5c550cd311d928cffadbb2359a4479ac1e7514886f409124e2eec1

Name:		qclib
Version:	2.5.1
Release:	3%{?dist}
Summary:	Library for extraction of system information for Linux on z Systems
License:	BSD-3-Clause
URL:		https://github.com/ibm-s390-linux/qclib
Source0:        https://github.com/ibm-s390-linux/qclib/archive/refs/tags/2.5.1/qclib-2.5.1.tar.gz
ExclusiveArch:	s390 s390x
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	glibc-static
BuildRequires:	doxygen
BuildRequires:	which
# for EBCDIC to ASCII conversion
Requires:	glibc-gconv-extra

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
%autosetup -n qclib-2.5.1


%build
make V=1 CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" %{?_smp_mflags} all doc


%install
%make_install V=1 DOCDIR=%{_docdir}
make DESTDIR=%{buildroot} DOCDIR=%{_docdir} installdoc


%check
make test-sh test


%files
%dir %{_docdir}/%{name}
%license %{_docdir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/README.md
%{_bindir}/zhypinfo
%{_bindir}/zname
%{_libdir}/libqc.so.*
%{_mandir}/man8/zhypinfo.8*
%{_mandir}/man8/zname.8*

%files devel
%doc %{_docdir}/%{name}/html/
%{_libdir}/libqc*.so
%{_includedir}/query_capacity.h

%files static
%{_libdir}/libqc*.a


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5.1-3
- Import
