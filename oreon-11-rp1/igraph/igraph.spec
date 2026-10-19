%global source0_hash 969f2d7d22f67e788d8638c9a8c96615f50d7819c08978b3ef4a787bb6daa96c
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
%global blaslib flexiblas
%global cmake_blas_flags -DBLA_VENDOR=FlexiBLAS
%else
%global blaslib openblas
%global blasvar o
%global cmake_blas_flags -DBLAS_LIBRARIES=%{_libdir}/lib%{blaslib}%{blasvar}.so -DLAPACK_LIBRARIES=%{_libdir}/lib%{blaslib}%{blasvar}.so
%endif
Name:               igraph
Version:            1.0.1
Release:        1%{?dist}
Summary:        Library for creating and manipulating graphs
License:             GPL-2.0-or-later
URL:                http://igraph.sourceforge.net/
Source0:        https://github.com/igraph/igraph/releases/download/%{version}/igraph-%{version}.tar.gz
# oreon:deps
BuildRequires:  arpack-devel
BuildRequires:  cmake
BuildRequires:  flexiblas-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glpk-devel
BuildRequires:  gmp-devel
BuildRequires:  libxml2-devel
# /oreon:deps
%description
igraph is a C library for complex network analysis and graph theory, with emphasis on efficiency, portability and ease of use.

%package devel
Requires:   %{name} = %{version}-%{release}
Requires:   pkgconfig
Summary:    Development files for igraph
%description devel
The %{name}-devel package contains the header files and some
documentation needed to develop application with %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%cmake \
    -DIGRAPH_ENABLE_LTO=AUTO \
    -DIGRAPH_ENABLE_TLS=1 \
    -DIGRAPH_USE_INTERNAL_BLAS=0 \
    -DIGRAPH_USE_INTERNAL_LAPACK=0 \
    -DIGRAPH_USE_INTERNAL_ARPACK=0 \
    -DIGRAPH_USE_INTERNAL_GLPK=0 \
    -DIGRAPH_USE_INTERNAL_GMP=0 \
    %{cmake_blas_flags} \
    -DIGRAPH_GRAPHML_SUPPORT=1 \
    -DCMAKE_INSTALL_INCLUDEDIR=include/
%cmake_build
%install
%cmake_install
install -Dm0644 doc/igraph.3 %{buildroot}/%{_mandir}/man3/igraph.3
find . -name '.arch-ids' | xargs rm -rf
%ifnarch ppc64le
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export FLEXIBLAS=netlib
%cmake_build --target check
%endif
%files -f %{oreon_filedir}/main.list
%files -n igraph-devel -f %{oreon_filedir}/igraph-devel.list

%changelog

%autochangelog
