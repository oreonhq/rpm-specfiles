%global source0_hash fdfccacba1c77d9b4ffefae7258c760c99e3c8a2823ca87ea5b11a50d297a73b

# header-only library
%global debug_package %{nil}
%bcond check 0

Name:           spectra
Version:        1.2.0
Release:        %autorelease
Summary:        A header-only C++ library for large scale eigenvalue problems
License:        MPL-2.0
URL:            https://github.com/yixuan/spectra
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         spectra-fix.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
%if %{with check}
BuildRequires:  eigen3-devel
%endif

%global _description %{expand:
Spectra stands for Sparse Eigenvalue Computation Toolkit as a Redesigned ARPACK.
It is a C++ library for large scale eigenvalue problems, built on top of Eigen,
an open source linear algebra library.

Spectra is implemented as a header-only C++ library, whose only dependency,
Eigen, is also header-only. Hence Spectra can be easily embedded in C++ projects
that require calculating eigenvalues of large matrices.}

%description
%_description

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
Requires:       eigen3-devel

%description    devel
%_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -C

%build
%cmake \
%if %{with check}
    -DBUILD_TESTS=ON \
%endif

%cmake_build

%install
%cmake_install

%check
# https://github.com/yixuan/spectra/issues/177
%ifarch s390x
%ctest -E Example1
%else
%ctest
%endif

%files devel
%license LICENSE
%doc README.md
%{_includedir}/Spectra/
%{_datadir}/cmake/Spectra

%changelog
%autochangelog
