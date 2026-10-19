%global source0_hash fdfccacba1c77d9b4ffefae7258c760c99e3c8a2823ca87ea5b11a50d297a73b
%global debug_package %{nil}
%bcond check 0
Name:           spectra
Version:        1.2.0
Release:        1%{?dist}
Summary:        A header-only C++ library for large scale eigenvalue problems
License:        MPL-2.0
URL:            https://github.com/yixuan/spectra
Source0:        https://github.com/yixuan/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         spectra-fix.patch
%if %{with check}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  eigen3-devel
BuildRequires:  gcc-c++
# /oreon:deps
%description
Spectra stands for Sparse Eigenvalue Computation Toolkit as a Redesigned ARPACK.
It is a C++ library for large scale eigenvalue problems, built on top of Eigen,
an open source linear algebra library.

Spectra is implemented as a header-only C++ library, whose only dependency,
Eigen, is also header-only. Hence Spectra can be easily embedded in C++ projects
that require calculating eigenvalues of large matrices.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
Requires:       eigen3-devel
%description    devel
Spectra stands for Sparse Eigenvalue Computation Toolkit as a Redesigned ARPACK.
It is a C++ library for large scale eigenvalue problems, built on top of Eigen,
an open source linear algebra library.

Spectra is implemented as a header-only C++ library, whose only dependency,
Eigen, is also header-only. Hence Spectra can be easily embedded in C++ projects
that require calculating eigenvalues of large matrices.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
%if %{with check}
    -DBUILD_TESTS=ON \
%endif
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ifarch s390x
%ctest -E Example1
%else
%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n spectra-devel -f %{oreon_filedir}/spectra-devel.list

%changelog

%autochangelog
