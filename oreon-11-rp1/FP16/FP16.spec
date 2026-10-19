%global source0_hash e7b509c76a2ea162ebdda77fb6b6f51f2f37dedee0866077d428e214516f0c2b
%global commit0 98b0a46bce017382a6351a19577ec43a715b6835
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20240619
%bcond check 1
Summary:        Conversion to/from half-precision floating point format
Name:           FP16
License:        MIT
Version:        1.0^git%{date0}.%{shortcommit0}
Release:        1%{?dist}
BuildArch:      noarch
URL:            https://github.com/Maratyszcza/%{name}
Source0:        https://github.com/Maratyszcza/%{name}/archive/%{commit0}/%{name}-98b0a46.tar.gz
Patch0:         0001-Revert-Remove-PeachPy-implementations.patch
%if %{with check}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  python3-devel
# /oreon:deps
%description
Header-only library for conversion to/from half-precision floating point formats

* Supports IEEE and ARM alternative half-precision floating-point format
  *  Property converts infinities and NaNs
  *  Properly converts denormal numbers, even on systems without denormal
     support
* Header-only library, no installation or build required
* Compatible with C99 and C++11
* Fully covered with unit tests and microbenchmarks

%package devel
Summary:        Conversion to/from half-precision floating point format
Provides:       %{name}-static = %{version}-%{release}
Requires: python3dist(peachpy)
%description devel
Header-only library for conversion to/from half-precision floating point formats

* Supports IEEE and ARM alternative half-precision floating-point format
  *  Property converts infinities and NaNs
  *  Properly converts denormal numbers, even on systems without denormal
     support
* Header-only library, no installation or build required
* Compatible with C99 and C++11
* Fully covered with unit tests and microbenchmarks

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit0}

%build

%cmake \
       -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
       -DFP16_USE_SYSTEM_LIBS=ON \
       -DFP16_BUILD_TESTS=OFF \
       -DFP16_BUILD_BENCHMARKS=OFF \
       -DFETCHCONTENT_FULLY_DISCONNECTED=ON \
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{python3_sitelib}/fp16
cp -p include/fp16/*.py %{buildroot}%{python3_sitelib}/fp16
%oreon_autofiles FP16-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n FP16-devel -f %{oreon_filedir}/FP16-devel.list

%changelog

%autochangelog
