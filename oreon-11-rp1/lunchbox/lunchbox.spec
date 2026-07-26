%global source0_hash 06ae367f70e34e5e5b27fac2296f7bdf33e36d5c016b1545020239fc49e5dd56

%global cmake_module_ver 2018.02

Name:          lunchbox
Version:       1.17.0
Release:       18%{?dist}
Summary:       C++ library for multi-threaded programming
# Boost license: lunchbox/atomic.h, lunchbox/any.h
# LGPLv3 license: e.g. any.cpp and lfVector.h
# the rest is under LGPLv2
License:       Boost and LGPLv2 and LGPLv3
URL:           http://www.equalizergraphics.com/
Source0:       https://github.com/Eyescale/Lunchbox/archive/%{version}/%{name}-%{version}.tar.gz
# https://github.com/Eyescale/Lunchbox/issues/329
Source1:       https://github.com/Eyescale/CMake/archive/refs/tags/%{cmake_module_ver}.tar.gz
# https://github.com/Eyescale/Lunchbox/issues/331
Source2:       https://www.gnu.org/licenses/old-licenses/lgpl-2.1.txt
Source3:       https://www.gnu.org/licenses/lgpl-3.0.txt
Source4:       https://www.boost.org/LICENSE_1_0.txt
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: servus-devel
BuildRequires: qt5-qtbase-devel
Provides:      bundled(eyescale-cmake-common) = %{cmake_module_ver}
# https://github.com/Eyescale/CMake/pull/601
Patch:         lunchbox-1.17.0-docdir-override.patch
# https://github.com/Eyescale/Lunchbox/pull/334
Patch:         lunchbox-1.17.0-nanosleep-fix.patch
# https://github.com/Eyescale/Lunchbox/pull/335
# https://github.com/Eyescale/CMake/pull/606
Patch:         lunchbox-1.17.0-cmake-4-fix.patch

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

# Drop tests from the installation according to the package review
rm -rf %{buildroot}%{_datadir}/Lunchbox/tests

# Move benchmark binaries to the correct place
mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{_datadir}/Lunchbox/benchmarks/* %{buildroot}%{_bindir}
rmdir %{buildroot}%{_datadir}/Lunchbox/benchmarks

%check
%ctest

%files
%license lgpl-2.1.txt lgpl-3.0.txt LICENSE_1_0.txt
%doc %{_docdir}/%{name}
# https://github.com/Eyescale/Lunchbox/issues/332
%{_libdir}/libLunchbox.so.1.*
%{_libdir}/libLunchbox.so.10

%files devel
%{_bindir}/perf-*
%{_includedir}/lunchbox
%{_libdir}/libLunchbox*.so
%{_datadir}/Lunchbox

%changelog
%autochangelog
