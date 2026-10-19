%global source0_hash 325cfbcf0c0296a6dd26f3b088801b7ebb8d6f109c0565c11d2d8c4af3253bff
%bcond tests 1
%global debug_package %{nil}
Name:           highfive
Version:        3.3.0
Release:        1%{?dist}
Summary:        Header-only C++ HDF5 interface
License:        BSL-1.0
URL:            https://highfive-devs.github.io/highfive/
Source0:        https://github.com/highfive-devs/highfive/archive/v%{version}/highfive-%{version}.tar.gz
Patch:          0001-Downstream-only-Patch-all-cmake_minimum_required-fro.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  (cmake(eigen3) with eigen3-static)
BuildRequires:  (cmake(xtensor) with xtensor-static)
BuildRequires:  boost-devel
BuildRequires:  catch-devel
BuildRequires:  cmake
BuildRequires:  cmake(opencv)
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  ninja-build
# /oreon:deps
%description

%package        devel
Summary:        Development files for HighFive
Provides:       highfive%{?_isa} = %{version}-%{release}
Provides:       highfive-static%{?_isa} = %{version}-%{release}
Provides:       highfive-static = %{version}-%{release}
Requires:       hdf5-devel
Requires:       boost-devel
Requires:       (cmake(eigen3) with eigen3-static)
Requires:       (cmake(xtensor) with xtensor-static)
Requires:       cmake(opencv)
%description    devel
The highfive-devel package contains libraries and header files for
developing applications that use HighFive.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%if %{with tests}
CXXFLAGS="${CXXFLAGS} -Wno-deprecated-declarations"
%endif
%cmake \
    -DHIGHFIVE_USE_BOOST:BOOL=TRUE \
    -DHIGHFIVE_USE_XTENSOR:BOOL=TRUE \
    -DHIGHFIVE_USE_EIGEN:BOOL=TRUE \
    -DHIGHFIVE_USE_OPENCV:BOOL=TRUE \
    -DHIGHFIVE_EXAMPLES:BOOL=TRUE \
    -DHIGHFIVE_UNIT_TESTS:BOOL=%{?with_tests:TRUE}%{?!with_tests:FALSE} \
    -DHIGHFIVE_BUILD_DOCS:BOOL=FALSE \
    -GNinja
%cmake_build
%install
%cmake_install
[ ! -d '%{buildroot}/%{_libdir}/cmake/HighFive' ]
install -d '%{buildroot}/%{_libdir}/cmake'
mv -v '%{buildroot}/%{_datadir}/HighFive/CMake' \
    '%{buildroot}/%{_libdir}/cmake/HighFive'
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if %{with tests}
%ctest -VV
%endif
%files -f %{oreon_filedir}/main.list
%files -n highfive-devel -f %{oreon_filedir}/highfive-devel.list

%changelog

%autochangelog
