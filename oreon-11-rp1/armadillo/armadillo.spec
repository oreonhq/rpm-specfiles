%global source0_hash 58fa258d0e1f93074c9afa792027fc259b85cb974ccc0b932b061d4ada5bd83a
Name:           armadillo
Version:        15.4.2
Release:        1%{?dist}
Summary:        Fast C++ matrix library with syntax similar to MATLAB and Octave
License:        Apache-2.0
URL:            http://arma.sourceforge.net/
Source0:        http://sourceforge.net/projects/arma/files/%{name}-%{version}.tar.xz
%undefine __cmake_in_source_build
%global extra_options %{nil}
%{!?openblas_arches:%global openblas_arches x86_64 %{ix86} armv7hl %{power64} aarch64}
%ifarch %{openblas_arches}
%endif
# oreon:deps
BuildRequires:  SuperLU-devel
BuildRequires:  arpack-devel
BuildRequires:  cmake
BuildRequires:  flexiblas-devel
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  make
# /oreon:deps
%description
Armadillo is a C++ linear algebra library (matrix maths)
aiming towards a good balance between speed and ease of use.
Integer, floating point and complex numbers are supported,
as well as a subset of trigonometric and statistics functions.
Various matrix decompositions are provided through optional
integration with LAPACK and ATLAS libraries.
A delayed evaluation approach is employed (during compile time)
to combine several operations into one and reduce (or eliminate)
the need for temporaries. This is accomplished through recursive
templates and template meta-programming.
This library is useful if C++ has been decided as the language
of choice (due to speed and/or integration capabilities), rather
than another language like Matlab or Octave.

%package devel
Summary:        Development headers and documentation for the Armadillo C++ library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libstdc++-devel
Requires:       arpack-devel
Requires:       hdf5-devel
Requires:       SuperLU-devel
Requires:  atlas-devel
Requires:  lapack-devel
%ifarch %{openblas_arches}
Requires:  openblas-devel
%endif
%description devel
This package contains files necessary for development using the
Armadillo C++ library. It contains header files, example programs,
and user documentation (API reference guide).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i 's/\r//' README.md
rm -rf examples/*win64*
sed -i 's/cmake_minimum_required(VERSION 3.5)/cmake_minimum_required(VERSION 3.5...3.30)/' CMakeLists.txt

%build

%cmake %{extra_options} -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build
%install
%cmake_install
%oreon_autofiles armadillo-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%cmake %{extra_options} -DBUILD_SMOKE_TEST=ON
%ctest
%files -f %{oreon_filedir}/main.list
%files -n armadillo-devel -f %{oreon_filedir}/armadillo-devel.list

%changelog

%autochangelog
