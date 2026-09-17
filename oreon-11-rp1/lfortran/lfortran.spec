%global source0_hash df52fc660c457c197f1ed56cc56b07a8822a9a5a7493e9cfb034f60f0106f05f

Version:        0.59.0
Name:           lfortran
Release:        2%{?dist}
Summary:        A modern Fortran compiler

# Main code is BSD-3-Clause
# src/libasr/codegen/KaleidoscopeJIT.h is available under the Apache 2.0
# License with LLVM exception
License:        BSD-3-Clause AND Apache-2.0 WITH LLVM-exception
URL:            https://lfortran.org/
Source0:        https://github.com/lfortran/lfortran/releases/download/v%{version}/lfortran-%{version}.tar.gz

# https://github.com/lfortran/lfortran/issues/2981
ExclusiveArch: x86_64

%global with_jupyter 1

BuildRequires: binutils-devel
BuildRequires: bison
BuildRequires: cmake
BuildRequires: fmt-devel
BuildRequires: gcc-c++
BuildRequires: json-devel
BuildRequires: libffi-devel
BuildRequires: libunwind-devel
BuildRequires: libuuid-devel
BuildRequires: llvm-devel
BuildRequires: python3-devel
BuildRequires: rapidjson-devel
BuildRequires: re2c
BuildRequires: zlib-ng-compat-devel
BuildRequires: zlib-ng-compat-static
%if %{with_jupyter}
# Needed for Jupyter kernel
BuildRequires: cppzmq-devel
BuildRequires: json-devel
BuildRequires: openssl-devel
BuildRequires: xeus-devel
BuildRequires: xeus-zmq-devel
BuildRequires: xtl-devel
%endif
# For backend=cpp
BuildRequires: kokkos-devel
# Not explicitly linked, hence listed here
Requires: kokkos-devel

Requires: %{name}-shared%{?_isa} = %{version}-%{release}

%global lfortran_desc \
LFortran is a modern open-source (BSD licensed) interactive Fortran \
compiler built on top of LLVM. It can execute user's code interactively \
to allow exploratory work (much like Python, MATLAB or Julia) as well as \
compile to binaries with the goal to run user's code on modern \
architectures such as multi-core CPUs and GPUs.

%description
%{lfortran_desc}

%package devel
Summary:  Development headers and libraries for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{lfortran_desc}

This package contains development headers and libraries for %{name}.

%package static
Summary:   Static runtime library for %{name}

%description static
%{lfortran_desc}

This package contains static runtime library for %{name}.

%package shared
Summary:   Shared runtime library for %{name}

%description shared
%{lfortran_desc}

This package contains shared runtime library for %{name}.

%if %{with_jupyter}
%package jupyter
Summary:   Jupyter kernel for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}
Requires:  jupyterlab
Requires:  python-jupyter-filesystem

%description jupyter
%{lfortran_desc}

This package contains the jupyter kernel for %{name}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# WITH_ZSD is just used to fix static linking of llvm
# not needed on Fedora
# WASM=OFF due to lfortran/lfortran#3899
# WITH_STACKTRACE=OFF due to lfortran/lfortran#5072
%cmake \
       -DWITH_LLVM=ON \
       -DWITH_ZSTD=OFF \
       -DWITH_RUNTIME_LIBRARY=ON \
       -DWITH_FMT=ON \
       -DWITH_JSON=ON \
       -DWITH_KOKKOS=ON \
       -DWITH_STACKTRACE=OFF \
       -DWITH_TARGET_WASM=OFF \
       -DWITH_UNWIND=ON \
       -DWITH_WHEREAMI=ON \
       -DWITH_XEUS=%{with_jupyter} \
       -DWITH_ZLIB=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
# liblfortran_runtime.so is in this package as
# lfortran calls it directly.
%doc README.md
%license LICENSE
%{_bindir}/lfortran
%{_mandir}/man1/lfortran.1.*
%{_libdir}/liblfortran_runtime.so

%files devel
%dir %{_includedir}/lfortran
%dir %{_includedir}/lfortran/impure
%{_includedir}/lfortran/impure/lfortran_intrinsics.h
%dir %{_datadir}/lfortran
%{_datadir}/lfortran/*.py
%{_libdir}/lfortran_*.mod
%{_libdir}/omp_lib.mod

%files static
%{_libdir}/liblfortran_runtime_static.a

%files shared
%{_libdir}/liblfortran_runtime.so.*

%if %{with_jupyter}
%files jupyter
%dir %{_datadir}/jupyter/kernels/fortran
%{_datadir}/jupyter/kernels/fortran/kernel.json
%{_datadir}/jupyter/kernels/fortran/logo-svg.svg
%endif

%changelog
%autochangelog
