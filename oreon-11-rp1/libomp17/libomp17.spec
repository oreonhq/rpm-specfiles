%global source0_hash 74334cbb4dc8b73a768448a7561d5a3540404940b2267b1fb9813a6464b320de

%bcond_with snapshot_build
%bcond_without compat_build

%if %{with snapshot_build}
# Unlock LLVM Snapshot LUA functions
%{llvm_sb}
%endif

%global maj_ver 17
%global libomp_version %{maj_ver}.0.6
#global rc_ver 4
%global libomp_srcdir openmp-%{libomp_version}%{?rc_ver:rc%{rc_ver}}.src
%global so_suffix %{maj_ver}

%if %{with snapshot_build}
%undefine rc_ver
%global maj_ver %{llvm_snapshot_version_major}
%global libomp_version %{llvm_snapshot_version}
%global so_suffix %{maj_ver}%{llvm_snapshot_version_suffix}
%endif

%global toolchain clang

# Opt out of https://fedoraproject.org/wiki/Changes/fno-omit-frame-pointer
# https://bugzilla.redhat.com/show_bug.cgi?id=2158587
%undefine _include_frame_pointers

%ifarch ppc64le
%global libomp_arch ppc64
%else
%global libomp_arch %{_arch}
%endif

%if %{with compat_build}
%global pkg_name libomp%{maj_ver}
%global install_prefix %{_libdir}/llvm%{maj_ver}
%global install_libdir %{install_prefix}/lib
%global install_datadir %{install_prefix}/share
%else
%global pkg_name libomp
%global install_prefix %{_prefix}
%global install_libdir %{_libdir}
%global install_datadir %{_datadir}
%endif

Name: %{pkg_name}
Version: %{libomp_version}%{?rc_ver:~rc%{rc_ver}}%{?llvm_snapshot_version_suffix:~%{llvm_snapshot_version_suffix}}
Release: 2%{?dist}
Summary: OpenMP runtime for clang

License: Apache-2.0 WITH LLVM-exception OR NCSA
URL: http://openmp.llvm.org
%if %{with snapshot_build}
Source0: %{llvm_snapshot_source_prefix}openmp-%{llvm_snapshot_yyyymmdd}.src.tar.xz
%{llvm_snapshot_extra_source_tags}
%else
Source0: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{libomp_version}%{?rc_ver:-rc%{rc_ver}}/%{libomp_srcdir}.tar.xz
Source1: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{libomp_version}%{?rc_ver:-rc%{rc_ver}}/%{libomp_srcdir}.tar.xz.sig
Source2: release-keys.asc
%endif

BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: elfutils-libelf-devel
BuildRequires: perl
BuildRequires: perl-Data-Dumper
BuildRequires: perl-Encode
BuildRequires: libffi-devel

# For gpg source verification
BuildRequires:	gnupg2

# libomptarget needs the llvm cmake files
BuildRequires: llvm-devel(major) = %{maj_ver}
%if %{with compat_build}
BuildRequires: llvm%{maj_ver}-cmake-utils
BuildRequires: clang%{maj_ver}
BuildRequires: clang%{maj_ver}-tools-extra
%else
BuildRequires: clang >= %{maj_ver}
BuildRequires: llvm-cmake-utils
# For clang-offload-packager
BuildRequires: clang-tools-extra
%endif

Requires: elfutils-libelf%{?isa}

# libomp does not support s390x.
ExcludeArch: s390x

%description
OpenMP runtime for clang.

%package devel
Summary: OpenMP header files
Requires: %{name}%{?isa} = %{version}-%{release}
%if %{with compat_build}
Requires: clang%{maj_ver}-resource-filesystem%{?isa} = %{version}
%else
Requires: clang-resource-filesystem%{?isa} = %{version}
%endif

%description devel
OpenMP header files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{without snapshot_build}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%autosetup -n %{libomp_srcdir} -p2

%build
%cmake	-GNinja \
%if %{with compat_build}
	-DCMAKE_CXX_COMPILER=clang++-%{maj_ver} \
	-DCMAKE_C_COMPILER=clang-%{maj_ver} \
%endif
	-DLIBOMP_INSTALL_ALIASES=OFF \
	-DCMAKE_MODULE_PATH=%{install_datadir}/llvm/cmake/Modules \
	-DLLVM_DIR=%{install_libdir}/cmake/llvm \
	-DCMAKE_INSTALL_INCLUDEDIR=%{_prefix}/lib/clang/%{maj_ver}/include \
%if %{with compat_build}
	-DCMAKE_INSTALL_PREFIX=%{install_prefix} \
%else
%if 0%{?__isa_bits} == 64
	-DOPENMP_LIBDIR_SUFFIX=64 \
%else
	-DOPENMP_LIBDIR_SUFFIX= \
%endif
%endif
%if %{with snapshot_build}
	-DLLVM_VERSION_SUFFIX="%{llvm_snapshot_version_suffix}" \
%endif
	-DCMAKE_SKIP_RPATH:BOOL=ON

%cmake_build

%install
%cmake_install

# Remove static libraries with equivalent shared libraries
rm -rf %{buildroot}%{install_libdir}/libarcher_static.a

%check
%cmake_build --target check-openmp

%files
%license LICENSE.TXT
%{install_libdir}/libomp.so
%{install_libdir}/libompd.so
%ifnarch %{arm}
%{install_libdir}/libarcher.so
%endif
%ifnarch %{ix86} %{arm}
# libomptarget is not supported on 32-bit systems.
%{install_libdir}/libomptarget.rtl.amdgpu.so.%{so_suffix}
%{install_libdir}/libomptarget.rtl.cuda.so.%{so_suffix}
%{install_libdir}/libomptarget.rtl.%{libomp_arch}.so.%{so_suffix}
%{install_libdir}/libomptarget.so.%{so_suffix}
%endif

%files devel
%{_prefix}/lib/clang/%{maj_ver}/include/omp.h
%ifnarch %{arm}
%{_prefix}/lib/clang/%{maj_ver}/include/omp-tools.h
%{_prefix}/lib/clang/%{maj_ver}/include/ompt.h
%{_prefix}/lib/clang/%{maj_ver}/include/ompt-multiplex.h
%endif
%{install_libdir}/cmake/openmp/FindOpenMPTarget.cmake
%ifnarch %{ix86} %{arm}
# libomptarget is not supported on 32-bit systems.
%{install_libdir}/libomptarget.rtl.amdgpu.so
%{install_libdir}/libomptarget.rtl.cuda.so
%{install_libdir}/libomptarget.rtl.%{libomp_arch}.so
%{install_libdir}/libomptarget.devicertl.a
%{install_libdir}/libomptarget-amdgpu-*.bc
%{install_libdir}/libomptarget-nvptx-*.bc
%{install_libdir}/libomptarget.so
%endif

%changelog
%autochangelog
