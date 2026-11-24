# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 80cb62e62defeee67ea1885a6f72d97ac81404f8fde9cded62fb51524808a30c
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global giturl https://github.com/uxlfoundation/oneTBB

Name:    tbb
Summary: The Threading Building Blocks library abstracts low-level threading details
Version: 2023.2.0
Release: 1%{?dist}
License: Apache-2.0 AND BSD-3-Clause
URL:     https://uxlfoundation.github.io/oneTBB/
VCS:     git:%{giturl}.git

Source0: %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz
Source7: tbbmalloc.pc
Source8: tbbmalloc_proxy.pc

Patch:   %{giturl}/pull/2239.patch

BuildRequires: oreon-rpm-macros
BuildRequires: cmake
BuildRequires: clang
BuildRequires: hwloc
BuildRequires: hwloc-devel
BuildRequires: python3-devel
BuildRequires: %{py3_dist setuptools}
BuildRequires: swig

Provides: oneTBB = %{version}-%{release}

Obsoletes:     tbb-doc < 2022.2.0

%description
Threading Building Blocks (TBB) is a C++ runtime library that
abstracts the low-level threading details necessary for optimal
multi-core performance.  It uses common C++ templates and coding style
to eliminate tedious threading implementation work.

TBB requires fewer lines of code to achieve parallelism than other
threading models.  The applications you write are portable across
platforms.  Since the library is also inherently scalable, no code
maintenance is required as more processor cores become available.

%package bind
Summary: NUMA support library for TBB
Requires: %{name}%{?_isa} = %{version}-%{release}

Provides: oneTBB-bind = %{version}-%{release}

%description bind
NUMA support library for TBB, allowing the binding of tasks to selected
CPU cores.

%package devel
Summary: The Threading Building Blocks C++ headers and shared development libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-bind%{?_isa} = %{version}-%{release}

Provides: oneTBB-devel = %{version}-%{release}

%description devel
Header files and shared object symlinks for the Threading Building
Blocks (TBB) C++ libraries.

%package -n python3-%{name}
Summary: Python 3 TBB module
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{name}
Python 3 TBB module.

%prep
%oreon_sha256
%autosetup -p1 -n oneTBB-%{version}

%generate_buildrequires
%pyproject_buildrequires -d python

%build
export TBBROOT=$PWD
export PYTHONPATH=$(sed "s,%{_prefix},$PWD/%{_vpath_builddir}/python/build," <<< %{python3_sitearch})
%cmake \
    -DCMAKE_CXX_STANDARD=20 \
    -DTBB4PY_BUILD:BOOL=ON \
    -DTBB_STRICT:BOOL=OFF \
    -DTCM_BUILD:BOOL=OFF
%cmake_build

unset PYTHONPATH
export LD_LIBRARY_PATH=$(ls -1d $PWD/%{_vpath_builddir}/*relwithdebinfo)
export LDFLAGS="-L $LD_LIBRARY_PATH %{build_ldflags}"
%pyproject_wheel -d python

%install
%cmake_install

rm -fr %{buildroot}%{python3_sitearch}
cd python
%pyproject_install
%pyproject_save_files -L TBB tbb
cd -

mkdir -p %{buildroot}/%{_libdir}/pkgconfig
for file in %{SOURCE7} %{SOURCE8}; do
    target=%{buildroot}/%{_libdir}/pkgconfig/$(basename ${file})
    sed 's/@VERSION@/%{version}/' $file > $target
    touch -r $file $target
done

if [ -f %{buildroot}/%{_libdir}/pkgconfig/%{name}32.pc ]; then
    ln %{buildroot}/%{_libdir}/pkgconfig/%{name}32.pc %{buildroot}/%{_libdir}/pkgconfig/%{name}.pc
fi

rm -fr %{buildroot}%{_datadir}/doc

%check
ctest --output-on-failure --force-new-ctest-process

%files
%doc README.md
%license LICENSE.txt
%{_libdir}/libtbb.so.12{,.*}
%{_libdir}/libtbbmalloc.so.2{,.*}
%{_libdir}/libtbbmalloc_proxy.so.2{,.*}
%{_libdir}/libirml.so.1

%files bind
%{_libdir}/libtbbbind_2_5.so.3{,.*}

%files devel
%doc cmake/README.md
%{_includedir}/oneapi/
%{_includedir}/tbb/
%{_libdir}/*.so
%{_libdir}/cmake/TBB/
%{_libdir}/pkgconfig/*.pc

%files -n python3-%{name} -f %{pyproject_files}
%doc python/README.md

%changelog
%autochangelog
