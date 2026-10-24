%global source0_hash c25a4838fc8e4c1c8aacb8bd620edb3084a3d63bf8987fdad3ca2758c63240f9
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: popt
Version: 1.19
Release: 1%{?dist}
Summary: C library for parsing command line parameters
License: MIT
URL: https://github.com/rpm-software-management/popt
Source0: https://ftp.osuosl.org/pub/rpm/popt/releases/popt-1.x/popt-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
popt is a C library for parsing command line parameters.

%package devel
Summary: C library for parsing command line parameters
Requires: popt%{?_isa} = %{version}-%{release}
Provides: pkgconfig(popt)

%description devel
popt is a C library for parsing command line parameters.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_configure --disable-static --disable-nls
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la

%files
%license COPYING
%{_libdir}/libpopt.so.0
%{_libdir}/libpopt.so.0.*
%{_mandir}/man3/popt.3*

%files devel
%{_includedir}/popt.h
%{_libdir}/libpopt.so
%{_libdir}/pkgconfig/popt.pc
