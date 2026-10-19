%global source0_hash 021173bdc1814b1d0541c4426277d39df2b629af53151999b137e015418f76c0
%global debug_package %{nil}
%bcond_without doc
Name:    mmtf-cpp
Version: 1.1.0
Release:        1%{?dist}
Summary:        The Macromolecular Transmission Format (MMTF) header only files
License: MIT
URL:     https://github.com/rcsb/%{name}
Source0:        https://github.com/rcsb/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake3
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  msgpack-devel
# /oreon:deps
%description
The Macromolecular Transmission Format (MMTF) is a new compact binary format to transmit and
store biomolecular structures for fast 3D visualization and analysis.
This package holds the C++-03 compatible API, encoding and decoding libraries.

%package devel
Summary: Development files for %{name}
Requires: msgpack-devel%{?_isa} >= 2.1.5
Provides: %{name}-static = %{version}-%{release}
%description devel
Header only files for developing applications that use mmtf-cpp.

%if %{with doc}
%package doc
Summary: Documentation files
BuildRequires:  doxygen
BuildArch: noarch
%description doc
HTML documentation files for mmtf-cpp.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%if 0%{?el7}
%{?dts:source /opt/rh/devtoolset-8/enable}
%endif
%cmake
%cmake_build
%if %{with doc}
pushd docs
doxygen
popd
%endif
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mmtf-cpp-devel -f %{oreon_filedir}/mmtf-cpp-devel.list
%files -n mmtf-cpp-doc -f %{oreon_filedir}/mmtf-cpp-doc.list

%changelog

%autochangelog
