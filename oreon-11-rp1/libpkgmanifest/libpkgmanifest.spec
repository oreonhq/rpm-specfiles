%global source0_hash 7b268f9c12f06137493def0d18bb7d8f59f2af0d26c1f9c0d531dabb80ae2854

%bcond python 0
%bcond test 0

Name:           libpkgmanifest
Version:        0.5.9
Release:        1%{?dist}
Summary:        Library for working with RPM manifests
License:        LGPL-2.1-or-later
URL:            https://github.com/rpm-software-management/libpkgmanifest
Source0:        https://github.com/rpm-software-management/libpkgmanifest/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-build-Turn-compiler-warnings-into-errors-only-for-ou.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(yaml-cpp) >= 0.7.0
%if %{with test}
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gtest)
%endif
%if %{with python}
BuildRequires:  python3-devel
BuildRequires:  swig >= 4.2.0
%endif

%description
C++ library for parsing and generating RPM manifests.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
%cmake -G Ninja \
    -DWITH_DOCS=OFF \
    -DWITH_PYTHON=%{?with_python:ON}%{?!with_python:OFF} \
    -DWITH_TESTS=%{?with_test:ON}%{?!with_test:OFF} \
    -DWITH_CODE_COVERAGE=OFF \
    -DVERSION_MAJOR=0 \
    -DVERSION_MINOR=5 \
    -DVERSION_PATCH=9
%cmake_build

%check
%if %{with test}
%ctest
%endif

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libpkgmanifest.so.0{,.*}

%files devel
%doc docs/design
%{_includedir}/libpkgmanifest/
%{_libdir}/libpkgmanifest.so
%{_libdir}/pkgconfig/libpkgmanifest.pc
