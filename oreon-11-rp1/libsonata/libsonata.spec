%global source0_hash ae92bfc9fae8961b920ed82b7076a918a6c06f0a6cc618c1b25e1f0e693ce915
%bcond tests 1
%bcond regenerate_test_data 1
Name:           libsonata
Version:        0.2.0
%global so_version 0.2
Release:        1%{?dist}
Summary:        A Python and C++ interface to the SONATA format
License:        LGPL-3.0-only AND BSL-1.0 AND MIT AND CC0-1.0
SourceLicense:  %{license} AND BSD-3-Clause
URL:            https://github.com/openbraininstitute/libsonata
Source0:        https://github.com/openbraininstitute/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          0001-Remove-pybind-redeclarations.patch
Patch:          0002-Use-std-filesystem.patch
Patch:          0003-Substitute-ghc-in-tests.patch
Patch:          0004-Include-catch-catch_all.hpp-instead-of-catch-catch.h.patch
Patch:          0005-Link-Catch2-Catch2WithMain-instead-of-Catch2-Catch2.patch
Patch:          %{url}/pull/1.patch
ExcludeArch:    %{ix86}
%if %{with regenerate_test_data}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-libsonata = %{version}-%{release}
# /oreon:deps
%package -n       python3-libsonata+docs
Summary:        Metapackage for python3-libsonata docs extras
Requires:       python3-libsonata = %{version}-%{release}
Provides:       python3dist(libsonata[docs]) = %{version}-%{release}

%description -n python3-libsonata+docs
Metapackage for python3-libsonata docs extras.

%description

%package devel
Summary:        Development files for %{name}
License:        LGPL-3.0-only
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       optional-lite-devel optional-lite-static
Requires:       variant-lite-devel variant-lite-static
%description devel

%package -n python3-libsonata
Summary:        Development files for libsonata
# oreon:reqs
Requires:       python3dist(numpy) >= 1.17.3
# /oreon:reqs
%description -n python3-libsonata

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n libsonata-%{version} -S git
rm -rf libsonata.egg-info
rm -rf extlib/{Catch2,Highfive,fmt,nlohmann}

# Unbundle gulrak-filesystem
echo '#include <ghc/filesystem.hpp>' > extlib/filesystem.hpp
# Unbundle optional-lite
echo '#include <nonstd/optional.hpp>' > include/bbp/sonata/optional.hpp
# Unbundle variant-lite
echo '#include <nonstd/variant.hpp>' > include/bbp/sonata/variant.hpp

# Avoid bundling in the Python extension. We must use a patch since we cannot
# pass CMake options directly to the build system for the Python extension.
sed -r -i 's/(-DEXTLIB_FROM_SUBMODULES=)ON/\1OFF/' setup.py

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

# Upstream builds against an old numpy for binary compatibility on PyPI, but we
# just build with the system numpy.
tomcli set pyproject.toml lists replace build-system.requires \
    oldest-supported-numpy numpy

%if %{with regenerate_test_data}
# These are the files that generate.py actually writes:
pushd tests/data
rm nodes1.h5 edges1.h5 spikes.h5 somas.h5 elements.h5
popd
%endif

%build

export CMAKE_GENERATOR='Ninja'
%cmake \
    -DEXTLIB_FROM_SUBMODULES:BOOL=OFF \
    -DSONATA_CXX_WARNINGS:BOOL=OFF \
    -DSONATA_PYTHON:BOOL=OFF \
    -DSONATA_TESTS:BOOL=ON \
    -DSONATA_VERSION="%{version}"
%cmake_build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
export SONATA_BUILD_TYPE='RelWithDebInfo'
export VERBOSE=''
%pyproject_wheel
%install
%cmake_install
rm -rf %{buildroot}/%{_libdir}/libsonata.a
%pyproject_install
%oreon_autofiles python3-libsonata usr/lib/python3*/site-packages/libsonata* usr/lib64/python3*/site-packages/libsonata* usr/bin/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/lib/python3*/site-packages/libsonata* usr/lib64/python3*/site-packages/libsonata* usr/bin/*

%check

%if %{with regenerate_test_data}
pushd tests/data
%{py3_test_envvars} %{python3} generate.py
popd
%endif
%ctest tests
mkdir _empty
cp -rp python/tests _empty/
%pytest -v _empty/tests
%files
%files -n libsonata-devel -f %{oreon_filedir}/libsonata-devel.list
%files -n python3-libsonata -f %{oreon_filedir}/python3-libsonata.list

%changelog

%autochangelog
