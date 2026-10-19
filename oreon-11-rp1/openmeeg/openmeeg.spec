%global source0_hash 29485a732e3555425889cfd28474fccd2b3e76b51bb694fc83d86ca052e70884
%bcond_with vtk
%bcond_without python
%bcond_without hdf5
%bcond_without matio
%bcond_with cgal
%bcond_without doc
%bcond check 0
%ifarch %{power64} 
%bcond_without openblas
%else
%bcond_with openblas
%endif
%bcond_with debug
%define _lto_cflags %{nil}
ExcludeArch: s390x
Name:    openmeeg
Version: 2.5.16
Release:        1%{?dist}
Summary:        Low-frequency bio-electromagnetism solving forward problems in the field of EEG and MEG
License: CeCILL-B
URL:     http://openmeeg.github.io/
Source0:        https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:  %{name}-use_builtin_find_blas_lapack.patch
Patch1:  %{name}-fix-cmake4.patch
%if %{with openblas}
%else
%endif
%{?fedora:BuildRequires: gifticlib-devel}
%{?fedora:BuildRequires: nifticlib-devel}
%if %{with hdf5}
%endif
%if %{with matio}
%endif
%if %{with vtk}
%endif
%if %{with cgal}
%endif
%global openmeeg_cmake_options \\\
%if %{with debug} \
        -DCMAKE_BUILD_TYPE=Debug \\\
        -DCMAKE_CXX_FLAGS_DEBUG:STRING="-O0 -g -fPIC" \\\
%else \
        -DCMAKE_BUILD_TYPE=Release \\\
        -DCMAKE_CXX_FLAGS_DEBUG:STRING="%{build_cxxflags}" \\\
%endif \
        -DUSE_PROGRESSBAR=ON \\\
        -DBUILD_SHARED_LIBS:BOOL=ON \\\
        -DBUILD_SHARED_LIBS_OpenMEEG:BOOL=ON \\\
        -DBUILD_SHARED_LIBS_matio:BOOL=ON \\\
        -DBUILD_SHARED_LIBS_zlib:BOOL=ON \\\
        -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \\\
        -DCMAKE_SKIP_RPATH:BOOL=YES \\\
        -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \\\
        -DCMAKE_INSTALL_INCLUDEDIR:PATH=include/%{name} \\\
        -DUSE_OMP:BOOL=ON \\\
%if %{with python} \
        -DENABLE_PYTHON:BOOL=ON \\\
        -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \\\
        -DPYTHON_VERSION:STRING=%{python3_version} \\\
        -DPYTHON_INSTALL_RELATIVE:BOOL=OFF \\\
%endif \
%if %{with doc} \
        -DBUILD_DOCUMENTATION:BOOL=ON \\\
%endif \
%if %{with check} \
        -DBUILD_TESTING:BOOL=ON \\\
        -DTEST_HEAD3:BOOL=ON \\\
%endif \
        -DBUILD_TOOLS:BOOL=ON \\\
        -DENABLE_PACKAGING:BOOL=OFF \\\
        -DSKIP_GITHUB_TESTS:BOOL=ON \\\
%if %{with cgal} \
        -DUSE_CGAL:BOOL=ON \\\
%endif \
        %{?fedora:-DUSE_GIFTI:BOOL=ON} \\\
%if %{with hdf5} \
        -DUSE_SYSTEM_hdf5:BOOL=ON \\\
%endif \
%if %{with matio} \
        -DUSE_SYSTEM_matio:BOOL=ON \\\
%endif \
%if %{with vtk} \
        -DUSE_VTK:BOOL=ON \\\
%endif \
        -DUSE_SYSTEM_zlib:BOOL=ON \\\
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON -Wno-dev \\\
%if %{with openblas} \
        -DBLAS_mkl_LIBRARY:FILEPATH=%{_libdir}/libopenblas.so \\\
%else \
        -DBLAS_flexiblas_LIBRARY:FILEPATH=%{_libdir}/libflexiblas.so \\\
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  expat-devel
BuildRequires:  flexiblas-devel
BuildRequires:  gcc-c++
BuildRequires:  gifticlib-devel
BuildRequires:  gnuplot
BuildRequires:  graphviz
BuildRequires:  hdf5-devel
BuildRequires:  make
BuildRequires:  matio-devel
BuildRequires:  nifticlib-devel
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-wheel
BuildRequires:  swig
BuildRequires:  zlib-devel
# /oreon:deps
%description
The OpenMEEG software is a C++ package for solving the forward
problems of electroencephalography (EEG) and magnetoencephalography (MEG).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use OpenMEEG.

%if %{with python}
%package        -n python3-openmeeg
Summary:        OpenMEEG binding for Python3
%py_provides    python3-%{name}
%py_provides    python3-OpenMEEG
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-wheel
BuildRequires:  swig
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       swig
%description    -n python3-openmeeg
OpenMEEG binding for Python3.
%endif

%if %{with doc}
%package        doc
Summary:        Documentation files for OpenMEEG
BuildRequires:  doxygen
BuildArch:      noarch
%description    doc
%{summary}.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -N -n %{name}-%{version}

%if %{without openblas}
%patch -P 0 -p1 -b .backup
%endif
%patch -P 1 -p1 -b .backup

%build

%if %{with debug}
export CXXFLAGS="-O0 -g -fPIC"
export CFLAGS="-O0 -g -fPIC"
%endif
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%if %{with openblas}
export CXXFLAGS="%{optflags} -I%{_includedir}/openblas"
%endif
%cmake %{openmeeg_cmake_options}
%cmake_build
%install
%cmake_install
%oreon_autofiles python3-openmeeg usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
export PYTHONPATH=%{buildroot}%{python3_sitearch}/%{name}
%if %{with debug}
export OPENMEEG_DATA_PATH=%{_builddir}/%{name}-%{version}/data
ctest --test-dir %_vpath_builddir -VV --force-new-ctest-process -j1 --output-on-failure --debug
%else
export OPENMEEG_DATA_PATH=%{_builddir}/%{name}-%{version}/data
%ctest
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n openmeeg-devel -f %{oreon_filedir}/openmeeg-devel.list
%files -n python3-openmeeg -f %{oreon_filedir}/python3-openmeeg.list
%files -n openmeeg-doc -f %{oreon_filedir}/openmeeg-doc.list

%changelog

%autochangelog
