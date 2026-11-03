%global source0_hash 97203a72cae99ab89a067fe2210c1cbf052bc492b479eca7d226d9830883b0bd
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: acl
Version: 2.3.2
Release: 2%{?dist}
Summary: Access control list utilities
License: GPL-2.0-or-later AND LGPL-2.1-or-later
URL: https://savannah.nongnu.org/projects/acl
Source0: https://download.savannah.gnu.org/releases/acl/acl-%{version}.tar.xz
Requires: libacl%{?_isa} = %{version}-%{release}

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: libattr-devel

%description
acl is a set of tools for manipulating access control lists.

%package -n libacl
Summary: Dynamic library for acl

%description -n libacl
Shared libacl library.

%package -n libacl-devel
Summary: Development files for libacl
Obsoletes: acl-devel < 2.3.2-2
Requires: libacl%{?_isa} = %{version}-%{release}

%description -n libacl-devel
Headers and development library for libacl.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_configure --disable-static --disable-nls
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_docdir}

%files
%license doc/COPYING
%license doc/COPYING.LGPL
%{_bindir}/chacl
%{_bindir}/getfacl
%{_bindir}/setfacl
%{_mandir}/man1/chacl.1*
%{_mandir}/man1/getfacl.1*
%{_mandir}/man1/setfacl.1*
%{_mandir}/man5/acl.5*

%ldconfig_scriptlets -n libacl

%files -n libacl
%license doc/COPYING.LGPL
%{_libdir}/libacl.so.1
%{_libdir}/libacl.so.1.*

%files -n libacl-devel
%{_includedir}/acl
%{_includedir}/sys/acl.h
%{_libdir}/libacl.so
%{_libdir}/pkgconfig/libacl.pc
%{_mandir}/man3/acl_*.3*
