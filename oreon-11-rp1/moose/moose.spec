%global source0_hash f58c3db113a2f1e9388af467fdf8056bcaec33c4511478ecd5cefe53b5f11f34

# for F < 33
# If it isn't defined, undefine doesn't do anything, so no conditional required
%undefine __cmake_in_source_build

#global commit 0e12e41b52deb8ea746bc760cddd6e100ca5cfd8
#global shortcommit %%(c=%{commit}; echo ${c:0:7})

Name:           moose
Version:        3.1.5
%global codename chamcham
Release:        32%{?dist}%{?prerelease:.%{prerelease}}%{?commit:.git%{shortcommit}}
Summary:        Multiscale Neuroscience and Systems Biology Simulator
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            http://moose.ncbs.res.in/
%if %{defined commit}
Source0:        https://github.com/BhallaLab/moose-core/archive/%{commit}.tar.gz#/moose-core-%{shortcommit}.tar.gz
%else
Source0:        https://github.com/BhallaLab/moose-core/archive/v%{version}.tar.gz#/moose-core-%{version}.tar.gz
%endif

# Fix segfault on py3.9
# https://github.com/BhallaLab/moose-core/pull/420
Patch0:         c570f7c057f9c0ca7360c82a8932bcb0df222da9.patch
Patch1:         665c532745987fb1c7a8fc2a9a57bffa330480b4.patch
# ppc defines a different suffix which breaks the build
Patch2:         0001-Use-.so-suffix-for-all-arches.patch
# Python 3.10 support
# https://github.com/BhallaLab/moose-core/issues/437
Patch3:         moose-python3.10.patch

ExcludeArch: s390x

BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  rsync
BuildRequires:  tar
BuildRequires:  readline-devel
BuildRequires:  ncurses-devel
BuildRequires:  zlib-devel
BuildRequires:  gsl-devel
BuildRequires:  hdf5-devel
BuildRequires:  tinyxml-devel
BuildRequires:  muParser-devel
BuildRequires:  libsbml-devel
# for tests
BuildRequires:  checksec
BuildRequires:  procps-ng
BuildRequires:  openssl

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-numpy
BuildRequires:  python3-libsbml

%description
MOOSE is the base and numerical core for large, detailed simulations
including Computational Neuroscience and Systems Biology. MOOSE spans
the range from single molecules to subcellular networks, from single
cells to neuronal networks, and to still larger systems. It is
backwards-compatible with GENESIS, and forward compatible with Python
and XML-based model definition standards like SBML and NeuroML.

MOOSE uses Python as its primary scripting language. For backward
compatibility we have a GENESIS scripting module, but this is
deprecated. MOOSE numerical code is written in C++.

%package -n python3-%{name}
Summary:  %{summary}

Requires: python3-numpy
Requires: python3-matplotlib
Requires: python3-matplotlib-qt5
Requires: python3-lxml

%description -n python3-%{name}
This package contains the %{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n moose-core-%{version} -S git

# Remove O3 flag set in CMakeLists
sed -i 's/-O3//' CMakeLists.txt

%global py_setup setup.cmake.py

%build
# On armv7 we get a failure with LTO.
# Disable LTO for armv7
%ifarch armv7hl
%define _lto_cflags %{nil}
%endif

cmake_opts=(
        -DBUILD_SHARED_LIBS:BOOL=OFF
        -DCMAKE_SKIP_RPATH:BOOL=ON
        -DCMAKE_C_FLAGS="%optflags"
        -DCMAKE_CXX_FLAGS="%optflags"
        -DCMAKE_EXE_LINKER_FLAGS="$LDFLAGS -Wl,--build-id"
        -DCMAKE_MODULE_LINKER_FLAGS="$LDFLAGS -Wl,--build-id"
        -DVERSION_MOOSE=%{version}
        -DCMAKE_BUILD_TYPE="Release|RelWithDebugInfo"
        -DCMAKE_INSTALL_DO_STRIP=0
        -DPYTHON_EXECUTABLE=%{__python3}
)

CXXFLAGS="%optflags -DH5_USE_110_API" \
%cmake "${cmake_opts[@]}"
%cmake_build

pushd %{__cmake_builddir}/python
%py3_build
popd

%install
install -vD %{__cmake_builddir}/moose.bin %{buildroot}%{_bindir}/moose
install -vDt %{buildroot}%{_libdir}/ %{__cmake_builddir}/libmoose.so

pushd %{__cmake_builddir}/python
%py3_install \--install-lib=%{python3_sitearch}
# this is necessary for the dependency generator to work
chmod +x %{buildroot}%{python3_sitearch}/moose/_moose*.so
popd

%check
checksec --file=%{buildroot}%{_bindir}/moose

pushd %{__cmake_builddir}
# test_streamer fails randomly when quitting moose every once in a while.
ctest --output-on-failure -V -E 'test_streamer'
# ctest --output-on-failure -V -E 'test_streamer|test_pyrun'
popd

PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} -c \
    'import moose; element = moose.Neutral("/yyy"); print(element.path)'

%global _docdir_fmt %{name}

%files
%{_bindir}/moose
%{_libdir}/libmoose.so
%license LICENSE
%doc README.md

%files -n python3-%{name}
%{python3_sitearch}/moose
%{python3_sitearch}/rdesigneur
%{python3_sitearch}/pymoose-%{version}-py%{python3_version}.egg-info
%license LICENSE
%doc README.md

%changelog
%autochangelog
