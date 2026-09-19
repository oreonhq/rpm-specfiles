%global source0_hash none

%{?mingw_package_header}

# Disable debuginfo subpackages and debugsource packages for now to use old logic
%undefine _debugsource_packages
%undefine _debuginfo_subpackages

# Override the __debug_install_post argument as this package
# contains both native as well as cross compiled binaries
%global __debug_install_post %%{mingw_debug_install_post}; %{_bindir}/find-debuginfo.sh %{?_missing_build_ids_terminate_build:--strict-build-id} %{?_find_debuginfo_opts} "%{_builddir}/%%{?buildsubdir}" %{nil}

%global pkgname llvm
%global libver 21

Name:          mingw-%{pkgname}
Version:       21.1.8
Release:       2%{?dist}
Summary:       LLVM for MinGW
# Only on i686: ld: out of memory allocating 1174616688 bytes after a total of 1517842432 bytes
ExcludeArch:   i686

License:       NCSA
URL:           http://llvm.org
Source0: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}/llvm-project-%{version}.src.tar.xz
# Set LLVM_INCLUDE_BENCHMARKS=OFF by default
Patch0:        llvm-no-benchmarks.patch
# Don't export all symbols
# Avoid ld: error: export ordinal too large
Patch1:        llvm-shlib-syms.patch

BuildRequires: chrpath
BuildRequires: make
BuildRequires: cmake
BuildRequires: gcc-c++

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-libffi
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-libffi
BuildRequires: mingw64-zlib

%description
LLVM for MinGW.

%package -n mingw32-%{pkgname}
Summary:       LLVM for MinGW Windows

%description -n mingw32-%{pkgname}
LLVM for MinGW Windows.

%package -n mingw32-%{pkgname}-static
Summary:       LLVM for MinGW Windows - Static libraries
Requires:      mingw32-%{pkgname} = %{version}-%{release}
BuildArch:     noarch

%description -n mingw32-%{pkgname}-static
LLVM for MinGW Windows - Static libraries.

%package -n mingw32-%{pkgname}-tools
Summary:       LLVM for MinGW Windows - Runtime tools
Requires:      mingw32-%{pkgname} = %{version}-%{release}
BuildArch:     noarch

%description -n mingw32-%{pkgname}-tools
LLVM for MinGW Windows - Runtime tools.

%package -n mingw64-%{pkgname}
Summary:       LLVM for MinGW Windows

%description -n mingw64-%{pkgname}
LLVM for MinGW Windows.

%package -n mingw64-%{pkgname}-static
Summary:       LLVM for MinGW Windows - Static libraries
Requires:      mingw64-%{pkgname} = %{version}-%{release}
BuildArch:     noarch

%description -n mingw64-%{pkgname}-static
LLVM for MinGW Windows - Static libraries

%package -n mingw64-%{pkgname}-tools
Summary:       LLVM for MinGW Windows - Runtime tools
Requires:      mingw64-%{pkgname} = %{version}-%{release}
BuildArch:     noarch

%description -n mingw64-%{pkgname}-tools
LLVM for MinGW Windows - Runtime tools.

%{?mingw_debug_package}

%prep
%autosetup -p1 -n llvm-project-%{version}.src

%build
pushd llvm

# Decrease debuginfo verbosity to reduce memory consumption during final library linking
# Technically only necessary on %%{arm}, but effectively needed everywhere to avoid the build failing due to
#   The following noarch package built differently on different architectures: [...]
mingw32_cflags_="%(echo %mingw32_cflags | sed 's/-g /-g1 /')"
mingw64_cflags_="%(echo %mingw64_cflags | sed 's/-g /-g1 /')"
export MINGW32_CFLAGS="${mingw32_cflags_}"
export MINGW32_CXXFLAGS="${mingw32_cflags_}"
export MINGW64_CFLAGS="${mingw64_cflags_}"
export MINGW64_CXXFLAGS="${mingw64_cflags_}"

# Create toolchain for native build, see cmake/modules/CrossCompile.cmake
# (note that for the native build llvm_create_cross_target_internal is invoked with toolchain = "", hence
# the toolchain file is just .cmake)
cat > cmake/platforms/.cmake <<EOF
SET(CMAKE_SYSTEM_NAME Linux)
SET(CMAKE_CROSSCOMPILING FALSE)

SET(CMAKE_C_COMPILER gcc)
SET(CMAKE_CXX_COMPILER g++)

SET(CMAKE_C_FLAGS "%{optflags}")
SET(CMAKE_CXX_FLAGS "%{optflags}")
SET(CMAKE_EXE_LINKER_FLAGS "%{__global_ldflags}")
EOF

# Build native llvm-tblgen, rather than depending on version-matching native package
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_SKIP_RPATH=ON -DBUILD_SHARED_LIBS=OFF -DLLVM_INCLUDE_TESTS=OFF
%cmake_build --target llvm-tblgen

CMAKE_OPTS="
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DLLVM_INCLUDE_DOCS=OFF \
     -DLLVM_INCLUDE_UTILS=OFF \
     -DLLVM_INCLUDE_EXAMPLES=OFF \
     -DLLVM_INCLUDE_TESTS=OFF \
     -DLLVM_BUILD_TOOLS=OFF \
     -DBUILD_SHARED_LIBS=OFF \
     -DLLVM_BUILD_LLVM_DYLIB=ON \
     -DLLVM_ENABLE_BINDINGS=OFF \
     -DLLVM_ENABLE_FFI=ON \
     -DLLVM_ENABLE_RTTI=ON \
     -DLLVM_ENABLE_Z3_SOLVER=OFF \
     -DLLVM_INCLUDE_BENCHMARKS=OFF \
     -DLLVM_ENABLE_ASSERTIONS=OFF \
     -DLLVM_TARGETS_TO_BUILD="X86" \
     -DLLVM_TARGET_ARCH="X86" \
     -DLLVM_NATIVE_TOOL_DIR=../%{_vpath_builddir}/bin/ \
     -DLLVM_INFERRED_HOST_TRIPLE=%{_target}
"
mkdir build_win32
pushd build_win32
%mingw32_cmake \
    $CMAKE_OPTS \
    -DLLVM_DEFAULT_TARGET_TRIPLE=%{mingw32_target} \
    -DFFI_INCLUDE_DIR=%{mingw32_libdir}/libffi-%{ffi_ver}/include

popd

mkdir build_win64
pushd build_win64
%mingw64_cmake \
    $CMAKE_OPTS \
    -DLLVM_DEFAULT_TARGET_TRIPLE=%{mingw64_target} \
    -DFFI_INCLUDE_DIR=%{mingw64_libdir}/libffi-%{ffi_ver}/include
popd

%mingw_make_build

popd

%install
pushd llvm

%mingw_make_install

# Unversioned symlink
ln -s %{mingw32_libdir}/libLLVM-%{libver}.dll.a %{buildroot}%{mingw32_libdir}/libLLVM.dll.a
ln -s %{mingw64_libdir}/libLLVM-%{libver}.dll.a %{buildroot}%{mingw64_libdir}/libLLVM.dll.a

# Remove unused files
rm -rf %{buildroot}%{mingw32_datadir}/opt-viewer
rm -rf %{buildroot}%{mingw64_datadir}/opt-viewer

# Install llvm-tblgen to host tools dir, can be used to cross-compile mingw-clang
install -Dpm 0755 %{_vpath_builddir}/bin/llvm-tblgen %{buildroot}%{_prefix}/%{mingw32_target}/bin/llvm-tblgen
install -Dpm 0755 %{_vpath_builddir}/bin/llvm-tblgen %{buildroot}%{_prefix}/%{mingw64_target}/bin/llvm-tblgen

# Kill rpaths
chrpath --delete %{buildroot}%{_prefix}/%{mingw32_target}/bin/llvm-tblgen
chrpath --delete %{buildroot}%{_prefix}/%{mingw64_target}/bin/llvm-tblgen

popd

%files -n mingw32-%{pkgname}
%license LICENSE.TXT
%{mingw32_bindir}/llvm-tblgen.exe
%{mingw32_bindir}/libLLVM-%{libver}.dll
%{mingw32_bindir}/libLTO.dll
%{mingw32_bindir}/libRemarks.dll
%{mingw32_includedir}/llvm/
%{mingw32_includedir}/llvm-c/
%{mingw32_libdir}/cmake/llvm/
%{mingw32_libdir}/libLLVM-%{libver}.dll.a
%{mingw32_libdir}/libLLVM.dll.a
%{mingw32_libdir}/libLTO.dll.a
%{mingw32_libdir}/libRemarks.dll.a
%{_prefix}/%{mingw32_target}/bin/llvm-tblgen

%files -n mingw32-%{pkgname}-static
%{mingw32_libdir}/libLLVM*.a
%exclude %{mingw32_libdir}/libLLVM*.dll.a

%files -n mingw32-%{pkgname}-tools
%exclude %{mingw32_bindir}/llvm-tblgen.exe
%{mingw32_bindir}/*.exe

%files -n mingw64-%{pkgname}
%license LICENSE.TXT
%{mingw64_bindir}/llvm-tblgen.exe
%{mingw64_bindir}/libLLVM-%{libver}.dll
%{mingw64_bindir}/libLTO.dll
%{mingw64_bindir}/libRemarks.dll
%{mingw64_includedir}/llvm/
%{mingw64_includedir}/llvm-c/
%{mingw64_libdir}/cmake/llvm/
%{mingw64_libdir}/libLLVM.dll.a
%{mingw64_libdir}/libLLVM-%{libver}.dll.a
%{mingw64_libdir}/libLTO.dll.a
%{mingw64_libdir}/libRemarks.dll.a
%{_prefix}/%{mingw64_target}/bin/llvm-tblgen

%files -n mingw64-%{pkgname}-static
%{mingw64_libdir}/libLLVM*.a
%exclude %{mingw64_libdir}/libLLVM*.dll.a

%files -n mingw64-%{pkgname}-tools
%exclude %{mingw64_bindir}/llvm-tblgen.exe
%{mingw64_bindir}/*.exe

%changelog
%autochangelog
