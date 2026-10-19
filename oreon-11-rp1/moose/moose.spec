%global source0_hash f58c3db113a2f1e9388af467fdf8056bcaec33c4511478ecd5cefe53b5f11f34
%undefine __cmake_in_source_build
Name:           moose
Version:        4.1.0
%global codename chamcham
Release:        1%{?dist}
Summary:        Multiscale Neuroscience and Systems Biology Simulator
License:        GPL-3.0-only
URL:            http://moose.ncbs.res.in/
%if %{defined commit}
Source0:        https://github.com/BhallaLab/%{name}-core/archive/v%{version}.tar.gz#/%{name}-core-%{version}.tar.gz
%else
%endif
Patch0:         c570f7c057f9c0ca7360c82a8932bcb0df222da9.patch
Patch1:         665c532745987fb1c7a8fc2a9a57bffa330480b4.patch
Patch2:         0001-Use-.so-suffix-for-all-arches.patch
Patch3:         moose-python3.10.patch
ExcludeArch: s390x
# oreon:deps
BuildRequires:  checksec
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  gsl-devel
BuildRequires:  hdf5-devel
BuildRequires:  libsbml-devel
BuildRequires:  make
BuildRequires:  muParser-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl
BuildRequires:  procps-ng
BuildRequires:  python3-devel
BuildRequires:  python3-libsbml
BuildRequires:  python3-numpy
BuildRequires:  python3-setuptools
BuildRequires:  readline-devel
BuildRequires:  rsync
BuildRequires:  tar
BuildRequires:  tinyxml-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
Summary:        Multiscale Neuroscience and Systems Biology Simulator
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
chmod +x %{buildroot}%{python3_sitearch}/moose/_moose*.so
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

checksec --file=%{buildroot}%{_bindir}/moose
pushd %{__cmake_builddir}
ctest --output-on-failure -V -E 'test_streamer'
popd
PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} -c \
    'import moose; element = moose.Neutral("/yyy"); print(element.path)'
%global _docdir_fmt %{name}
%files -f %{oreon_filedir}/main.list
%files -n python3-moose -f %{oreon_filedir}/python3-moose.list

%changelog

%autochangelog
