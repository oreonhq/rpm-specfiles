%global source0_hash 96d33abb4bb0070c7be0fed4246cd38416188325f820468214471938545b1ac8
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: mpdecimal
Version: 4.0.1
Release: 1%{?dist}
Summary: Library for arbitrary precision decimal floating point arithmetic
License: BSD-2-Clause
URL: https://www.bytereef.org/mpdecimal/
Source0: https://www.bytereef.org/software/mpdecimal/releases/mpdecimal-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
libmpdec is a library for arbitrary precision decimal floating point arithmetic.

%package devel
Summary: Library for arbitrary precision decimal floating point arithmetic
Requires: mpdecimal%{?_isa} = %{version}-%{release}
Provides: pkgconfig(libmpdec)

%description devel
libmpdec is a library for arbitrary precision decimal floating point arithmetic.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_configure --disable-static --disable-cxx
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_docdir}

%files
%license COPYRIGHT.txt
%{_libdir}/libmpdec.so.4
%{_libdir}/libmpdec.so.4.*
%{_mandir}/man3/libmpdec.3*
%{_mandir}/man3/mpdecimal.3*

%files devel
%{_includedir}/mpdecimal.h
%{_libdir}/libmpdec.so
%{_libdir}/pkgconfig/libmpdec.pc
