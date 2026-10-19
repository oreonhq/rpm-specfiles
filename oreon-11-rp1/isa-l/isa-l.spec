%global source0_hash d9f7179ab0e14a3db9b610fac22793854a1435e8423ec9ce07f4cbedc5f92f5e
Name:		isa-l
Version:	2.32.1
Release:        1%{?dist}
Summary:        Intel(R) Intelligent Storage Acceleration Library
License:	BSD-3-Clause
URL:		https://github.com/intel/isa-l
Source0:        https://github.com/intel/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:	%{ix86}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  nasm
# /oreon:deps
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
%configure --disable-static
%make_build
%install
%make_install
rm %{buildroot}%{_libdir}/*.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%make_build check
%make_build test
%make_build perf
%files -f %{oreon_filedir}/main.list
%files -n isa-l-devel -f %{oreon_filedir}/isa-l-devel.list
%files -n isa-l-tools -f %{oreon_filedir}/isa-l-tools.list

%changelog

%autochangelog
