%global source0_hash 1e727b8933ec51a77a9a9d9afcf8e688bce45d907c13e36ab7393fe36e703182
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: expat
Version: 2.8.5
Release: 1%{?dist}
Summary: XML parser library
License: MIT
URL: https://libexpat.github.io/
Source0: https://github.com/libexpat/libexpat/releases/download/R_2_8_5/expat-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
expat is an XML parser library written in C.

%package devel
Summary: XML parser library
Requires: expat%{?_isa} = %{version}-%{release}
Provides: pkgconfig(expat)

%description devel
expat is an XML parser library written in C.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_configure --disable-static --without-docbook
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_docdir}

%files
%license COPYING
%{_bindir}/xmlwf
%{_libdir}/libexpat.so.1
%{_libdir}/libexpat.so.1.*
%{_mandir}/man1/xmlwf.1*

%files devel
%{_includedir}/expat.h
%{_includedir}/expat_config.h
%{_includedir}/expat_external.h
%{_libdir}/libexpat.so
%{_libdir}/pkgconfig/expat.pc
%{_libdir}/cmake/expat-%{version}
