%global source4_hash c9bff75738922193e67fa726fa225535870d2aa1059f91452c411736284ad566
%global source3_hash e3a994d82e644b03a792a930f574002658412f62407f5fee083f2555c5f23118
%global source2_hash 20e50fe7aae3e56378ebf0417d9de904f55a0e61e4df315333e632a4d3555d95
%global source1_hash 06ae367f70e34e5e5b27fac2296f7bdf33e36d5c016b1545020239fc49e5dd56
%global source0_hash 5d5e29ceacef6d024f3a1fa8178ae77a31fe41ebee82b36e76af5c65cd0f353b
%global cmake_module_ver 2018.02
Name:          lunchbox
Version:       1.17.0
Release:        18%{?dist}
Summary:        C++ library for multi-threaded programming
License:       Boost and LGPLv2 and LGPLv3
URL:           http://www.equalizergraphics.com/
Source0:        https://github.com/Eyescale/Lunchbox/archive/%{version}/%{name}-%{version}.tar.gz
Source1:       https://github.com/Eyescale/CMake/archive/refs/tags/%{cmake_module_ver}.tar.gz
Source2:       https://www.gnu.org/licenses/old-licenses/lgpl-2.1.txt
Source3:       https://www.gnu.org/licenses/lgpl-3.0.txt
Source4:       https://www.boost.org/LICENSE_1_0.txt
Provides:      bundled(eyescale-cmake-common) = %{cmake_module_ver}
Patch:         lunchbox-1.17.0-docdir-override.patch
Patch:         lunchbox-1.17.0-nanosleep-fix.patch
Patch:         lunchbox-1.17.0-cmake-4-fix.patch
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel
BuildRequires:  servus-devel
# /oreon:deps
%description
Lunchbox is C++ library for multi-threaded programming, providing
OS abstraction, utility classes and high-performance primitives,
such as atomic variables, spin locks and lock-free containers.

%package devel
Summary:       Development files for lunchbox
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for lunchbox.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a 1 -n Lunchbox-%{version}

# drop bundled pthreads
rm -f pthreads/*.tar.gz

mv CMake-%{cmake_module_ver}/* CMake/common/
rm -f CMake-%{cmake_module_ver}/.gitignore
rmdir CMake-%{cmake_module_ver}
%autopatch -p1

cp -at . %{SOURCE2} %{SOURCE3} %{SOURCE4}

# perf-memory test failing
# https://github.com/Eyescale/Lunchbox/issues/330
rm -f tests/perf/memory.cpp

# drop tests failing on armv7hl
# https://github.com/Eyescale/Lunchbox/issues/333
%ifarch armv7hl
pushd tests
rm -f bitOperation.cpp intervalSet.cpp result.cpp string.cpp
popd
%endif

# drop failing debug test
# https://github.com/Eyescale/Lunchbox/issues/336
pushd tests
rm -f debug.cpp
popd

%build

%cmake -DCOMMON_DOC_DIR=%{_docdir}/%{name} -DCOMMON_FIND_PACKAGE_QUIET=OFF
%cmake_build
%install
%cmake_install
rm -rf %{buildroot}%{_datadir}/Lunchbox/tests
mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{_datadir}/Lunchbox/benchmarks/* %{buildroot}%{_bindir}
rmdir %{buildroot}%{_datadir}/Lunchbox/benchmarks
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n lunchbox-devel -f %{oreon_filedir}/lunchbox-devel.list

%changelog

%autochangelog
