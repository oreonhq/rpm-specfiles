%global source0_hash 0ab06e5c506c7ed5f072faa4c04477c65624e4a1ff62eee8c0d996ef850ec51c
Name:           mlpack
Version:        4.8.0
Release:        1%{?dist}
Summary:        Fast, header-only C++ machine learning library
License:        BSD-3-Clause AND Apache-2.0 AND (MIT OR Unlicense)
URL:            http://www.mlpack.org
Source0:        http://www.mlpack.org/files/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
ExcludeArch:    s390
ExcludeArch:	s390x
%if 0%{?el7} || 0%{?el8}
%global min_stb_image 2.28-0.39.20231011gitbeebb24
%else
%global min_stb_image 2.28^20231011gitbeebb24-12
%endif
# oreon:deps
BuildRequires:  armadillo-devel
BuildRequires:  cereal-devel
BuildRequires:  cli11-devel
BuildRequires:  cmake
BuildRequires:  ensmallen-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkg-config
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-pandas
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  stb_image-devel
BuildRequires:  stb_image-static
BuildRequires:  stb_image_resize2-devel
BuildRequires:  stb_image_resize2-static
BuildRequires:  stb_image_write-devel
BuildRequires:  stb_image_write-static
BuildRequires:  txt2man
# /oreon:deps
%description
mlpack is a C++ machine learning library with emphasis on scalability, speed,
and ease-of-use. Its aim is to make machine learning possible for novice users
by means of a simple, consistent API, while simultaneously exploiting C++
language features to provide maximum performance and maximum flexibility for
expert users. mlpack outperforms competing machine learning libraries by large
margins.

# Licenses and information files
%package licenses
Summary:        Licenses and information files for mlpack (machine learning library)
%description licenses
mlpack is a C++ machine learning library with emphasis on scalability, speed,
and ease-of-use. Its aim is to make machine learning possible for novice users
by means of a simple, consistent API, while simultaneously exploiting C++
language features to provide maximum performance and maximum flexibility for
expert users. mlpack outperforms competing machine learning libraries by large
margins.  This package provides the command-line executables which run mlpack
methods and related documentation.

# Executables.
%package bin
Summary:        Command-line executables for mlpack (machine learning library)
Requires:       %{name}-licenses
Requires:       armadillo
%description bin
mlpack is a C++ machine learning library with emphasis on scalability, speed,
and ease-of-use. Its aim is to make machine learning possible for novice users
by means of a simple, consistent API, while simultaneously exploiting C++
language features to provide maximum performance and maximum flexibility for
expert users. mlpack outperforms competing machine learning libraries by large
margins.  This package provides the command-line executables which run mlpack
methods and related documentation.

# Development headers.
%package devel
Summary:   Development headers for mlpack (C++ machine learning library)
Requires:  %{name}-licenses
Requires:  armadillo-devel >= 10.8.2
Requires:  ensmallen-devel >= 2.10.0
Requires:  cereal-devel
Requires:  lapack-devel
Requires:  pkg-config
Requires:  stb_image-devel%{?_isa} >= %{min_stb_image}
Requires:  stb_image_write-devel%{?_isa}
Provides:  %{name}-static = %{version}-%{release}
%description devel
mlpack is a C++ machine learning library with emphasis on scalability, speed,
and ease-of-use. Its aim is to make machine learning possible for novice users
by means of a simple, consistent API, while simultaneously exploiting C++
language features to provide maximum performance and maximum flexibility for
expert users. mlpack outperforms competing machine learning libraries by large
margins.  This package provides the headers to compile applications against
mlpack.

%package python3
Summary:   Python 3 bindings for mlpack (C++ machine learning library)
Requires:  %{name}-licenses
Requires:  python3
Requires:  python3-numpy
Requires:  python3-pandas
Requires:  python3-Cython
%description python3
mlpack is a C++ machine learning library with emphasis on scalability, speed,
and ease-of-use.  Its aim is to make machine learning possible for novice users
by means of a simple, consistent API, while simultaneously exploiting C++
language features to provide maximum performance and maximum flexibility for
expert users.  mlpack outperforms competing machine learning libraries by large
margins.  This package provides the Python bindings for mlpack.

# For the F20 unversioned documentation change.  This evaluates to
# %%{_pkgdocdir} if on F20 and %%{_docdir}/%%{name}-%%{version} otherwise.
%global our_docdir %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}

# Disable LTO: it takes too much memory.
%define _lto_cflags %{nil}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{python3} -m ensurepip --upgrade
%{cmake} \
    -D CMAKE_INSTALL_LIBDIR=%{_libdir} \
    -D BUILD_TESTS=OFF \
    -D BUILD_PYTHON_BINDINGS=ON \
    -D PYTHON_EXECUTABLE=%{python3} \
    -D STB_IMAGE_INCLUDE_DIR=%{_includedir} \
    -D USE_SYSTEM_STB=ON
%ifarch armv7hl
cmake -B %{__cmake_builddir} \
      -D CMAKE_C_FLAGS="`echo %{optflags} | sed 's/-pipe//g' | sed 's/$/ --param ggc-min-heapsize=32768 --param ggc-min-expand=1/'`" -D CMAKE_CXX_FLAGS="`echo %{optflags} | sed 's/-pipe//g' | sed 's/$/ --param ggc-min-heapsize=32768 --param ggc-min-expand=1/'`" .
%endif
%ifarch i686
cmake -B %{__cmake_builddir} \
      -D CMAKE_C_FLAGS="`echo %{optflags} | sed 's/-pipe//g' | sed 's/$/ --param ggc-min-heapsize=32768 --param ggc-min-expand=1/'`" -D CMAKE_CXX_FLAGS="`echo %{optflags} | sed 's/-pipe//g' | sed 's/$/ --param ggc-min-heapsize=32768 --param ggc-min-expand=1/'`" .
%endif
%ifarch ppc64le
cmake -B %{__cmake_builddir} \
      -D CMAKE_C_FLAGS="`echo %{optflags} | sed 's/-pipe//g' | sed 's/$/ --param ggc-min-heapsize=32768 --param ggc-min-expand=1/'`" -D CMAKE_CXX_FLAGS="`echo %{optflags} | sed 's/-pipe//g' | sed 's/$/ --param ggc-min-heapsize=32768 --param ggc-min-expand=1/'`" .
%endif
%{cmake_build}
%install
%{cmake_install}
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mlpack-licenses -f %{oreon_filedir}/mlpack-licenses.list
%files -n mlpack-bin -f %{oreon_filedir}/mlpack-bin.list
%files -n mlpack-devel -f %{oreon_filedir}/mlpack-devel.list
%files -n mlpack-python3 -f %{oreon_filedir}/mlpack-python3.list

%changelog

%autochangelog
