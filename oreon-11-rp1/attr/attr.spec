%global source0_hash f2e97b0ab7ce293681ab701915766190d607a1dba7fae8a718138150b700a70b
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: attr
Version: 2.5.2
Release: 1%{?dist}
Summary: Utilities for filesystem extended attributes
License: GPL-2.0-or-later AND LGPL-2.1-or-later
URL: https://savannah.nongnu.org/projects/attr
Source0: https://download.savannah.gnu.org/releases/attr/attr-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
attr is a set of tools for manipulating filesystem extended attributes.

%package devel
Summary: Utilities for filesystem extended attributes
Requires: attr%{?_isa} = %{version}-%{release}
Provides: pkgconfig(libattr)

%description devel
attr is a set of tools for manipulating filesystem extended attributes.

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
%license doc/COPYING
%license doc/COPYING.LGPL
%{_bindir}/attr
%{_bindir}/getfattr
%{_bindir}/setfattr
%{_libdir}/libattr.so.1
%{_libdir}/libattr.so.1.*
%{_mandir}/man1/attr.1*
%{_mandir}/man1/getfattr.1*
%{_mandir}/man1/setfattr.1*

%files devel
%{_includedir}/attr
%{_libdir}/libattr.so
%{_libdir}/pkgconfig/libattr.pc
%{_mandir}/man3/attr_*.3*
