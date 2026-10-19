%global source0_hash 01c5946f063178cf05a9cac4906eb06ba3b784a0f03a68e8ef757ec368dc077a
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
%global optflags %(echo %{optflags} -Wno-error=template-id-cdtor)
%endif
Name:           hmat-oss
Version:        1.11.1
Release:        1%{?dist}
Summary:        A hierarchical matrix C/C++ library
License:        GPL-2.0-or-later
URL:            https://github.com/jeromerobert/hmat-oss
Source0:        https://github.com/jeromerobert/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  blas-devel
BuildRequires:  blas-static
BuildRequires:  cmake
BuildRequires:  cmake(lapacke)
BuildRequires:  flexiblas-devel
BuildRequires:  gcc-c++
BuildRequires:  lapack-devel
BuildRequires:  lapack-static
BuildRequires:  ninja-build
# /oreon:deps
%description
hmat-oss is hierarchical matrix library written in C++. It has a C API. It
contains a LU and LLt solver, and a few other things.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DBUILD_EXAMPLES=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n hmat-oss-devel -f %{oreon_filedir}/hmat-oss-devel.list

%changelog

%autochangelog
