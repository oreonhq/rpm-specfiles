%global source0_hash f2e97b0ab7ce293681ab701915766190d607a1dba7fae8a718138150b700a70b
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: attr
Version: 2.5.2
Release: 2%{?dist}
Summary: Utilities for filesystem extended attributes
License: GPL-2.0-or-later AND LGPL-2.1-or-later
URL: https://savannah.nongnu.org/projects/attr
Source0: https://download.savannah.gnu.org/releases/attr/attr-%{version}.tar.xz
Requires: libattr%{?_isa} = %{version}-%{release}

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make

%description
attr is a set of tools for manipulating filesystem extended attributes.

%package -n libattr
Summary: Dynamic library for attr

%description -n libattr
Shared libattr library.

%package -n libattr-devel
Summary: Development files for libattr
Obsoletes: attr-devel < 2.5.2-2
Requires: libattr%{?_isa} = %{version}-%{release}

%description -n libattr-devel
Headers and development library for libattr.

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
%{_bindir}/attr
%{_bindir}/getfattr
%{_bindir}/setfattr
%{_mandir}/man1/attr.1*
%{_mandir}/man1/getfattr.1*
%{_mandir}/man1/setfattr.1*

%ldconfig_scriptlets -n libattr

%files -n libattr
%license doc/COPYING.LGPL
%config(noreplace) %{_sysconfdir}/xattr.conf
%{_libdir}/libattr.so.1
%{_libdir}/libattr.so.1.*

%files -n libattr-devel
%{_includedir}/attr
%{_libdir}/libattr.so
%{_libdir}/pkgconfig/libattr.pc
%{_mandir}/man3/attr_*.3*
