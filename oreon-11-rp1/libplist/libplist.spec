%global source0_hash b1f59f7634c58b2481325a23ff4e3bf51574a42d868cbe466d2b39b04550752a
%global forgeurl https://github.com/libimobiledevice/libplist
Name:     libplist
Version:  2.8.0
Release:        1%{?dist}
Summary:        Library for manipulating Apple Binary and XML Property Lists
License:  LGPL-2.0-or-later
URL:      https://www.libimobiledevice.org/
Source0:        https://github.com/libimobiledevice/libplist/releases/download/%{version}/libplist-%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
libplist is a library for manipulating Apple Binary and XML Property Lists

%package  devel
Summary:  Development package for libplist
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
%description devel
%{name}, development headers and libraries.

%package  -n python3-libplist
Summary:  Python3 bindings for libplist
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python3
%description -n python3-libplist
%{name}, python3 libraries and bindings.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libplist-%{version}
%oreon_prep
%build

export PYTHON_VERSION="%{python3_version}"
%configure --disable-static
%make_build
%install
%make_install
%oreon_autofiles python3-libplist usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n libplist-devel -f %{oreon_filedir}/libplist-devel.list
%files -n python3-libplist -f %{oreon_filedir}/python3-libplist.list

%changelog

%autochangelog
