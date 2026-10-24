%global source0_hash 97203a72cae99ab89a067fe2210c1cbf052bc492b479eca7d226d9830883b0bd
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: acl
Version: 2.3.2
Release: 1%{?dist}
Summary: Access control list utilities
License: GPL-2.0-or-later AND LGPL-2.1-or-later
URL: https://savannah.nongnu.org/projects/acl
Source0: https://download.savannah.gnu.org/releases/acl/acl-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: attr-devel
%endif

%description
acl is a set of tools for manipulating access control lists.

%package devel
Summary: Access control list utilities
Requires: acl%{?_isa} = %{version}-%{release}
Provides: pkgconfig(libacl)

%description devel
acl is a set of tools for manipulating access control lists.

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
%{_bindir}/chacl
%{_bindir}/getfacl
%{_bindir}/setfacl
%{_libdir}/libacl.so.1
%{_libdir}/libacl.so.1.*
%{_mandir}/man1/chacl.1*
%{_mandir}/man1/getfacl.1*
%{_mandir}/man1/setfacl.1*
%{_mandir}/man5/acl.5*

%files devel
%{_includedir}/acl
%{_includedir}/sys/acl.h
%{_libdir}/libacl.so
%{_libdir}/pkgconfig/libacl.pc
%{_mandir}/man3/acl_*.3*
