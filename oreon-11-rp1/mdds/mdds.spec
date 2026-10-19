%global source0_hash 7eb71ae35bcfbea27c6f1ab094ce4fbd4093eb396d5eebe926c0d77280bc7791
%global debug_package %{nil}
%global apiversion 3.2
Name: mdds
Version: 3.2.1
Release:        1%{?dist}
Summary:        A collection of multi-dimensional data structures and indexing algorithms
License: MIT
URL: https://gitlab.com/mdds/mdds
Source0:        https://gitlab.com/mdds/mdds/-/archive/%{version}/mdds-%{version}.tar.bz2
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
%{name} is a collection of multi-dimensional data structures and
indexing algorithms.

%package devel
Summary: Headers for %{name}
BuildArch: noarch
Requires: boost-devel
Provides: %{name}-static = %{version}-%{release}
%description devel
%{name} is a collection of multi-dimensional data structures and
indexing algorithms.
 
It implements the following data structures:
* segment tree
* flat segment tree 
* rectangle set
* point quad tree
* multi type matrix
* multi type vector

See README.md for a brief description of the structures.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p0

%build

./autogen.sh
%configure
%install
%make_install
rm -rf %{buildroot}%{_docdir}/%{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check %{?_smp_mflags}
%files -f %{oreon_filedir}/main.list
%files -n mdds-devel -f %{oreon_filedir}/mdds-devel.list

%changelog

%autochangelog
