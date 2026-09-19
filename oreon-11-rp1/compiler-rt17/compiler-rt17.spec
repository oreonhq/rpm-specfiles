%global source0_hash 11b8d09dcf92a0f91c5c82defb5ad9ff4acf5cf073a80c317204baa922d136b4

%bcond_with snapshot_build

%if %{with snapshot_build}
# Unlock LLVM Snapshot LUA functions
%{llvm_sb_verbose}
%{llvm_sb}
%endif

%global toolchain clang

# Opt out of https://fedoraproject.org/wiki/Changes/fno-omit-frame-pointer
# https://bugzilla.redhat.com/show_bug.cgi?id=2158587
%undefine _include_frame_pointers

%bcond_without compat_build

%global maj_ver 17
%global min_ver 0
%global patch_ver 6
#global rc_ver 4
%if %{with snapshot_build}
%global maj_ver %{llvm_snapshot_version_major}
%global min_ver %{llvm_snapshot_version_minor}
%global patch_ver %{llvm_snapshot_version_patch}
%undefine rc_ver
%endif
%global compiler_rt_version %{maj_ver}.%{min_ver}.%{patch_ver}

%global crt_srcdir compiler-rt-%{compiler_rt_version}%{?rc_ver:rc%{rc_ver}}.src

%if %{with compat_build}
%global pkg_name compiler-rt%{maj_ver}
%global llvm_pkg_name llvm%{maj_ver}
%else
%global pkg_name compiler-rt
%global llvm_pkg_name llvm
%endif

# see https://sourceware.org/bugzilla/show_bug.cgi?id=25271
%global optflags %(echo %{optflags} -D_DEFAULT_SOURCE)

# see https://gcc.gnu.org/bugzilla/show_bug.cgi?id=93615
%global optflags %(echo %{optflags} -Dasm=__asm__)

Name:		%{pkg_name}
Version:	%{compiler_rt_version}%{?rc_ver:~rc%{rc_ver}}%{?llvm_snapshot_version_suffix:~%{llvm_snapshot_version_suffix}}
Release:	6%{?dist}
Summary:	LLVM "compiler-rt" runtime libraries

License:	Apache-2.0 WITH LLVM-exception OR NCSA OR MIT
URL:		http://llvm.org
%if %{with snapshot_build}
Source0:    %{llvm_snapshot_source_prefix}compiler-rt-%{llvm_snapshot_yyyymmdd}.src.tar.xz
%{llvm_snapshot_extra_source_tags}
%else
Source0:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{compiler_rt_version}%{?rc_ver:-rc%{rc_ver}}/%{crt_srcdir}.tar.xz
Source1:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{compiler_rt_version}%{?rc_ver:-rc%{rc_ver}}/%{crt_srcdir}.tar.xz.sig
Source2:	release-keys.asc
%endif

Patch0:		0001-compiler-rt-Fix-FLOAT16-feature-detection.patch

%if %{with compat_build}
BuildRequires:	clang%{maj_ver}
%else
BuildRequires:	clang
%endif
BuildRequires:	cmake
BuildRequires:	ninja-build
BuildRequires:	python3
# We need python3-devel for %%py3_shebang_fix
BuildRequires:	python3-devel
BuildRequires:	%{llvm_pkg_name}-devel = %{version}
BuildRequires:	%{llvm_pkg_name}-cmake-utils = %{version}
BuildRequires:	zlib-devel

# For gpg source verification
BuildRequires:	gnupg2

%if %{with compat_build}
Requires: clang%{maj_ver}-resource-filesystem%{?isa} = %{version}
%else
Requires: clang-resource-filesystem%{?isa} = %{version}
%endif
Provides: %{name}(major) = %{maj_ver}

%description
The compiler-rt project is a part of the LLVM project. It provides
implementation of the low-level target-specific hooks required by
code generation, sanitizer runtimes and profiling library for code
instrumentation, and Blocks C language extension.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{crt_srcdir} -p2

# compiler-rt does not allow configuring LLVM_COMMON_CMAKE_UTILS.
%if %{with compat_build}
ln -s %{_libdir}/llvm%{maj_ver}/share/llvm/cmake ../cmake
%else
ln -s %{_datadir}/llvm/cmake ../cmake
%endif

%py3_shebang_fix lib/hwasan/scripts/hwasan_symbolize

%build
# Copy CFLAGS into ASMFLAGS, so -fcf-protection is used when compiling assembly files.
export ASMFLAGS=$CFLAGS

%cmake	-GNinja \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
%if %{without compat_build}
	-DCMAKE_MODULE_PATH=%{_libdir}/cmake/llvm \
%else
	-DLLVM_CMAKE_DIR="%{_libdir}/llvm%{maj_ver}/lib/cmake/llvm" \
	-DCMAKE_CXX_COMPILER=%{_bindir}/clang++-%{maj_ver} \
	-DCMAKE_C_COMPILER=%{_bindir}/clang-%{maj_ver} \
%endif
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DCOMPILER_RT_INSTALL_PATH=%{_prefix}/lib/clang/%{maj_ver} \
	-DLLVM_ENABLE_PER_TARGET_RUNTIME_DIR=ON \
	\
%if %{with snapshot_build}
	-DLLVM_VERSION_SUFFIX="%{llvm_snapshot_version_suffix}" \
%endif
	\
%if 0%{?__isa_bits} == 64
	-DLLVM_LIBDIR_SUFFIX=64 \
%else
	-DLLVM_LIBDIR_SUFFIX= \
%endif
	-DCOMPILER_RT_INCLUDE_TESTS:BOOL=OFF # could be on?

%cmake_build

%install

%cmake_install
%ifarch ppc64le
# Fix install path on ppc64le so that the directory name matches the triple used
# by clang.
mv %{buildroot}%{_prefix}/lib/clang/%{maj_ver}/lib/powerpc64le-redhat-linux-gnu %{buildroot}%{_prefix}/lib/clang/%{maj_ver}/lib/ppc64le-redhat-linux-gnu
%endif
%ifarch %{ix86}
# Fix install path on ix86 so that the directory name matches the triple used
# by clang on both actual ix86 and on x86_64 with -m32:
%if "%{_target_cpu}" != "i386"
ln -s i386-redhat-linux-gnu %{buildroot}%{_prefix}/lib/clang/%{maj_ver}/lib/%{_target_cpu}-redhat-linux-gnu
%endif
%endif

%check
#%%cmake_build --target check-compiler-rt

%files
%license LICENSE.TXT
%ifarch x86_64 aarch64
%{_prefix}/lib/clang/%{maj_ver}/bin/*
%endif
%{_prefix}/lib/clang/%{maj_ver}/include/*
%{_prefix}/lib/clang/%{maj_ver}/lib/*
%{_prefix}/lib/clang/%{maj_ver}/share/*
#%ifarch x86_64 aarch64
#{_bindir}/hwasan_symbolize
#%endif

%changelog
%autochangelog
