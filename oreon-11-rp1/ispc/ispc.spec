%global source0_hash 671c79bdff2d97aead3897da1a6b67a163af8c4e329350d07cf3e63d592955ff
%bcond          gcc 0
Name:           ispc
Version:        1.31.0
Release:        1%{?dist}
Summary:        C-based SPMD programming language compiler
License:        BSD-3-Clause
URL:            https://ispc.github.io/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%if %{with gcc}
%endif
%ifarch x86_64
Recommends:     %{name}-gpu%{?_isa}
%endif
ExclusiveArch:  x86_64 aarch64
# oreon:deps
BuildRequires:  bison
BuildRequires:  clang-devel
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  help2man
BuildRequires:  llvm-devel
BuildRequires:  make
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(tbb)
# /oreon:deps
%description
A compiler for a variant of the C programming language with extensions for
"single program, multiple data" (SPMD) programming.

# Development subpackage
%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development headers and CMake configuration for %{name}.

# GPU runtime subpackage (only for x86_64)
%ifarch x86_64
%package gpu
Summary:        GPU runtime for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description gpu
GPU runtime libraries for %{name}, required for running ISPC programs on GPUs.
%endif

# Static libraries subpackage
%package static
Summary:        Static libraries for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%description static
Static libraries for developing programs with %{name}.

%prep

%autosetup -p1 -n %{name}-%{version}

# Remove GCC-only warning suppression
sed -i 's|-Wno-c99-extensions -Wno-deprecated-register||g' CMakeLists.txt

# Fix Python shebangs
%py3_shebang_fix .

%build

%cmake \
    -DCMAKE_BUILD_TYPE=Release \
%if %{with gcc}
    -DCMAKE_C_COMPILER=gcc \
    -DCMAKE_CXX_COMPILER=g++ \
%endif
    -DCMAKE_EXE_LINKER_FLAGS="%{optflags} -fPIE" \
    -DISPC_INCLUDE_EXAMPLES=OFF \
    -DISPC_INCLUDE_TESTS=ON \
%ifarch x86_64
    -DLEVEL_ZERO_INCLUDE_DIR=%{_includedir} \
    -DLEVEL_ZERO_LIB_LOADER=%{_libdir}/libze_loader.so.1 \
    -DISPCRT_BUILD_CPU=ON \
    -DISPCRT_BUILD_GPU=ON \
    -DISPCRT_BUILD_TESTS=OFF \
%endif
    -DLLVM_ENABLE_ASSERTIONS=OFF
%cmake_build
%install
%cmake_install
install -d '%{buildroot}%{_mandir}/man1'
for cmd in %{buildroot}%{_bindir}/*
do
  LD_LIBRARY_PATH='%{buildroot}%{_libdir}' \
      help2man \
      --no-info --no-discard-stderr --version-string='%{version}' \
      --output="%{buildroot}%{_mandir}/man1/$(basename "${cmd}").1" \
      "${cmd}"
done
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

PATH="${PATH}:%{buildroot}%{_bindir}" %{python3} scripts/run_tests.py
%files -f %{oreon_filedir}/main.list
%files -n ispc-devel -f %{oreon_filedir}/ispc-devel.list
%files -n ispc-static -f %{oreon_filedir}/ispc-static.list

%changelog

%autochangelog
