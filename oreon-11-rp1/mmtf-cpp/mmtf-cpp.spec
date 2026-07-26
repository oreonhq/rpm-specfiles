%global source0_hash 021173bdc1814b1d0541c4426277d39df2b629af53151999b137e015418f76c0

%global debug_package %{nil}

%bcond_without doc

# Use devtoolset 9
%if 0%{?rhel} && 0%{?rhel} == 7
%global dts devtoolset-8-
%endif

Name:    mmtf-cpp
Version: 1.1.0
Release: 9%{?dist}
Summary: The Macromolecular Transmission Format (MMTF) header only files
License: MIT
URL:     https://github.com/rcsb/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires: cmake3
BuildRequires: %{?dts}gcc
BuildRequires: %{?dts}gcc-c++
BuildRequires: msgpack-devel >= 2.1.5

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

%autosetup -n %{name}-%{version}

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

%files devel
%doc *.md
%license LICENSE
%{_includedir}/mmtf/
%{_includedir}/mmtf.hpp

%if %{with doc}
%files doc
%license LICENSE
%doc docs/html
%endif

%changelog
%autochangelog
