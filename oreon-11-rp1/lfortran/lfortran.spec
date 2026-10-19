%global source0_hash 961d84f49d07951a279b7835e0f9864489a167a80a8c3c502a797fb6c61669c7
Version:        0.66.0
Name:           lfortran
Release:        1%{?dist}
Summary:        A modern Fortran compiler
License:        BSD-3-Clause AND Apache-2.0 WITH LLVM-exception
URL:            https://lfortran.org/
Source0:        https://github.com/lfortran/lfortran/releases/download/v%{version}/lfortran-%{version}.tar.gz
ExclusiveArch: x86_64
%global with_jupyter 1
Requires: kokkos-devel
Requires: %{name}-shared%{?_isa} = %{version}-%{release}
%global lfortran_desc \
LFortran is a modern open-source (BSD licensed) interactive Fortran \
compiler built on top of LLVM. It can execute user's code interactively \
to allow exploratory work (much like Python, MATLAB or Julia) as well as \
compile to binaries with the goal to run user's code on modern \
architectures such as multi-core CPUs and GPUs.
# oreon:deps
BuildRequires:  binutils-devel
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  cppzmq-devel
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
BuildRequires:  json-devel
BuildRequires:  kokkos-devel
BuildRequires:  libffi-devel
BuildRequires:  libunwind-devel
BuildRequires:  libuuid-devel
BuildRequires:  llvm-devel
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
BuildRequires:  rapidjson-devel
BuildRequires:  re2c
BuildRequires:  xeus-devel
BuildRequires:  xeus-zmq-devel
BuildRequires:  xtl-devel
BuildRequires:  zlib-ng-compat-devel
BuildRequires:  zlib-ng-compat-static
# /oreon:deps
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

%package jupyter
Summary:   Jupyter kernel for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}
Requires:  jupyterlab
Requires:  python-jupyter-filesystem
%description jupyter
%{lfortran_desc}

This package contains the jupyter kernel for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n lfortran-devel -f %{oreon_filedir}/lfortran-devel.list
%files -n lfortran-static -f %{oreon_filedir}/lfortran-static.list
%files -n lfortran-shared -f %{oreon_filedir}/lfortran-shared.list
%files -n lfortran-jupyter -f %{oreon_filedir}/lfortran-jupyter.list

%changelog

%autochangelog
