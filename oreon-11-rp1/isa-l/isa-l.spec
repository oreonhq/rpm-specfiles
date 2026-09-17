%global source0_hash 7a194ff80d0f7e20615c497654e8a51b0184d0c79e2e265c7f555f52a26a05a4

Name:		isa-l
Version:	2.32.0
Release:	1%{?dist}
Summary:	Intel(R) Intelligent Storage Acceleration Library

License:	BSD-3-Clause
URL:		https://github.com/intel/isa-l
Source0:	%{url}/archive/v%{version}/isa-l-%{version}.tar.gz

ExcludeArch:	%{ix86}

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	make
%if %{?rhel}%{!?rhel:0} == 8
#		Use a newer compiler for EPEL 8 - default fails for aarch64:
¤		fatal error: arm_sve.h: No such file or directory
BuildRequires:	gcc-toolset-12-gcc
BuildRequires:	gcc-toolset-12-annobin-plugin-gcc
%else
BuildRequires:	gcc
%endif
BuildRequires:	nasm

%description
Collection of low-level functions used in storage applications.
Contains fast erasure codes that implement a general Reed-Solomon type
encoding for blocks of data that helps protect against erasure of
whole blocks. The general ISA-L library contains an expanded set of
functions used for data protection, hashing, encryption, etc.

This package contains the shared library.

%package devel
Summary:	Intel(R) Intelligent Storage Acceleration Library - devel files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Collection of low-level functions used in storage applications.
Contains fast erasure codes that implement a general Reed-Solomon type
encoding for blocks of data that helps protect against erasure of
whole blocks. The general ISA-L library contains an expanded set of
functions used for data protection, hashing, encryption, etc.

This package contains the development files needed to build against
the shared library.

%package tools
Summary:	Intel(R) Intelligent Storage Acceleration Library - tool
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description tools
Collection of low-level functions used in storage applications.
Contains fast erasure codes that implement a general Reed-Solomon type
encoding for blocks of data that helps protect against erasure of
whole blocks. The general ISA-L library contains an expanded set of
functions used for data protection, hashing, encryption, etc.

This package contains CLI tools.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
autoreconf -v -f -i

%if %{?rhel}%{!?rhel:0} == 8
. /opt/rh/gcc-toolset-12/enable
%endif

%configure --disable-static
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/*.la

%check
%make_build check
%make_build test
%make_build perf

%files
%{_libdir}/libisal.so.2*
%license LICENSE

%files devel
%{_includedir}/isa-l.h
%{_includedir}/isa-l
%{_libdir}/libisal.so
%{_libdir}/pkgconfig/libisal.pc
%doc examples

%files tools
%{_bindir}/igzip
%{_mandir}/man1/igzip.1*

%changelog
%autochangelog
