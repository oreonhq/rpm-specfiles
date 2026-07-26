%global source0_hash 807f069c54dc20cb47b21c1f6acafdd9c649f3ae015609040d6182cab01140f4

%bcond_with snapshot_build

%if %{with snapshot_build}
# Unlock LLVM Snapshot LUA functions
%{llvm_sb}
%endif

# We are building with clang for faster/lower memory LTO builds.
# See https://docs.fedoraproject.org/en-US/packaging-guidelines/#_compiler_macros
%global toolchain clang

# Opt out of https://fedoraproject.org/wiki/Changes/fno-omit-frame-pointer
# https://bugzilla.redhat.com/show_bug.cgi?id=2158587
%undefine _include_frame_pointers

# Components enabled if supported by target architecture:
%define gold_arches %{ix86} x86_64 aarch64 %{power64} s390x
%ifarch %{gold_arches}
  %bcond_without gold
%else
  %bcond_with gold
%endif

%bcond_without compat_build
%bcond check 0

%ifarch %ix86 riscv64
# Disable LTO on x86 in order to reduce memory consumption
%bcond_with lto_build
%elif %{with snapshot_build}
# Disable LTO to speed up builds
%bcond_with lto_build
%else
%bcond_without lto_build
%endif

%global maj_ver 17
%global min_ver 0
%global patch_ver 6
#global rc_ver 4

%if %{with snapshot_build}
%undefine rc_ver
%global maj_ver %{llvm_snapshot_version_major}
%global min_ver %{llvm_snapshot_version_minor}
%global patch_ver %{llvm_snapshot_version_patch}
%endif

%global llvm_srcdir llvm-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:rc%{rc_ver}}.src
%global cmake_srcdir cmake-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:rc%{rc_ver}}.src
%global third_party_srcdir third-party-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:rc%{rc_ver}}.src

%if %{with compat_build}
%global pkg_name llvm%{maj_ver}
%global exec_suffix -%{maj_ver}
%global install_prefix %{_libdir}/%{name}
%global install_bindir %{install_prefix}/bin
%global install_includedir %{install_prefix}/include
%global install_libdir %{install_prefix}/lib

%global pkg_includedir %{_includedir}/%{name}
%global pkg_datadir %{install_prefix}/share
%else
%global pkg_name llvm
%global install_prefix /usr
%global install_bindir %{_bindir}
%global install_libdir %{_libdir}
%global install_includedir %{_includedir}
%global pkg_datadir %{_datadir}
%global exec_suffix %{nil}
%endif

%if 0%{?rhel}
%global targets_to_build "X86;AMDGPU;PowerPC;NVPTX;SystemZ;AArch64;ARM;Mips;BPF;WebAssembly"
%global experimental_targets_to_build ""
%else
%global targets_to_build "all"
%global experimental_targets_to_build "AVR"
%endif

%global build_install_prefix %{buildroot}%{install_prefix}

# Lower memory usage of dwz on s390x
%global _dwz_low_mem_die_limit_s390x 1
%global _dwz_max_die_limit_s390x 1000000

%global llvm_triple %{_target_platform}

# https://fedoraproject.org/wiki/Changes/PythonSafePath#Opting_out
# Don't add -P to Python shebangs
# The executable Python scripts in /usr/share/opt-viewer/ import each other
%undefine _py3_shebang_P

Name:		%{pkg_name}
Version:	%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:~rc%{rc_ver}}%{?llvm_snapshot_version_suffix:~%{llvm_snapshot_version_suffix}}
Release:	9%{?dist}
Summary:	The Low Level Virtual Machine

License:	Apache-2.0 WITH LLVM-exception OR NCSA
URL:		http://llvm.org
%if %{with snapshot_build}
Source0:	%{llvm_snapshot_source_prefix}llvm-%{llvm_snapshot_yyyymmdd}.src.tar.xz
Source2:	%{llvm_snapshot_source_prefix}cmake-%{llvm_snapshot_yyyymmdd}.src.tar.xz
Source4:	%{llvm_snapshot_source_prefix}third-party-%{llvm_snapshot_yyyymmdd}.src.tar.xz
%{llvm_snapshot_extra_source_tags}
%else
Source0:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-rc%{rc_ver}}/%{llvm_srcdir}.tar.xz
Source1:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-rc%{rc_ver}}/%{llvm_srcdir}.tar.xz.sig
Source2:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-rc%{rc_ver}}/%{cmake_srcdir}.tar.xz
Source3:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-rc%{rc_ver}}/%{cmake_srcdir}.tar.xz.sig
Source4:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-rc%{rc_ver}}/%{third_party_srcdir}.tar.xz
Source5:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-rc%{rc_ver}}/%{third_party_srcdir}.tar.xz.sig
Source6:	release-keys.asc
%endif

# Backport of https://reviews.llvm.org/D156485 for rhbz#2262260.
Patch0: 0001-PEI-Don-t-zero-out-noreg-operands.patch

# RHEL-specific patch to avoid unwanted recommonmark dep
Patch101:	0101-Deactivate-markdown-doc.patch

BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	clang
BuildRequires:	cmake
BuildRequires:	ninja-build
BuildRequires:	zlib-devel
BuildRequires:	libffi-devel
BuildRequires:	ncurses-devel
BuildRequires:	python3-psutil
BuildRequires:	python3-sphinx
%if %{undefined rhel}
BuildRequires:	python3-recommonmark
%endif
BuildRequires:	multilib-rpm-config
%if %{with gold}
BuildRequires:	binutils-devel
%endif
%ifarch %{valgrind_arches}
# Enable extra functionality when run the LLVM JIT under valgrind.
BuildRequires:	valgrind-devel
%endif
# LLVM's LineEditor library will use libedit if it is available.
BuildRequires:	libedit-devel
# We need python3-devel for %%py3_shebang_fix
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools

# For origin certification
BuildRequires:	gnupg2

Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

Provides:	llvm(major) = %{maj_ver}

%description
LLVM is a compiler infrastructure designed for compile-time, link-time,
runtime, and idle-time optimization of programs from arbitrary programming
languages. The compiler infrastructure includes mirror sets of programming
tools as well as libraries with equivalent functionality.

%package devel
Summary:	Libraries and header files for LLVM
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
# The installed LLVM cmake files will add -ledit to the linker flags for any
# app that requires the libLLVMLineEditor, so we need to make sure
# libedit-devel is available.
Requires:	libedit-devel
# The installed cmake files reference binaries from llvm-test, llvm-static, and
# llvm-gtest.  We tried in the past to split the cmake exports for these binaries
# out into separate files, so that llvm-devel would not need to Require these packages,
# but this caused bugs (rhbz#1773678) and forced us to carry two non-upstream
# patches.
Requires:	%{name}-static%{?_isa} = %{version}-%{release}
Requires:	%{name}-test%{?_isa} = %{version}-%{release}
Requires:	%{name}-googletest%{?_isa} = %{version}-%{release}

Requires(post):	%{_sbindir}/alternatives
Requires(postun):	%{_sbindir}/alternatives

Provides:	llvm-devel(major) = %{maj_ver}

%description devel
This package contains library and header files needed to develop new native
programs that use the LLVM infrastructure.

%package doc
Summary:	Documentation for LLVM
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation for the LLVM compiler infrastructure.

%package libs
Summary:	LLVM shared libraries

%description libs
Shared libraries for the LLVM compiler infrastructure.

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%package static
Summary:	LLVM static libraries
Conflicts:	%{name}-devel < 8

Provides:	llvm-static(major) = %{maj_ver}

%description static
Static libraries for the LLVM compiler infrastructure.

%package cmake-utils
Summary: CMake utilities shared across LLVM subprojects

%description cmake-utils
CMake utilities shared across LLVM subprojects.
This is for internal use by LLVM packages only.

%package test
Summary:	LLVM regression tests
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

Provides:	llvm-test(major) = %{maj_ver}

%description test
LLVM regression tests.

%package googletest
Summary: LLVM's modified googletest sources

%description googletest
LLVM's modified googletest sources.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE6}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%{gpgverify} --keyring='%{SOURCE6}' --signature='%{SOURCE3}' --data='%{SOURCE2}'
%{gpgverify} --keyring='%{SOURCE6}' --signature='%{SOURCE5}' --data='%{SOURCE4}'
%setup -T -q -b 2 -n %{cmake_srcdir}
# TODO: It would be more elegant to set -DLLVM_COMMON_CMAKE_UTILS=%{_builddir}/%{cmake_srcdir},
# but this is not a CACHED variable, so we can't actually set it externally :(
cd ..
mv %{cmake_srcdir} cmake
%setup -T -q -b 4 -n %{third_party_srcdir}
cd ..
mv %{third_party_srcdir} third-party

%setup -T -q -b 0 -n %{llvm_srcdir}
%autopatch -M%{?!rhel:100}%{?rhel:200} -p2

%py3_shebang_fix \
	test/BugPoint/compile-custom.ll.py \
	tools/opt-viewer/*.py \
	utils/update_cc_test_checks.py

%build

%if %{without lto_build}
%global _lto_cflags %nil
%endif

%ifarch s390 s390x %ix86 riscv64
# Decrease debuginfo verbosity to reduce memory consumption during final library linking
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')
%endif

# Copy CFLAGS into ASMFLAGS, so -fcf-protection is used when compiling assembly files.
export ASMFLAGS="%{build_cflags}"

# force off shared libs as cmake macros turns it on.
# TODO: Disable LLVM_UNREACHABLE_OPTIMIZE.
%cmake	-G Ninja \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DLLVM_PARALLEL_LINK_JOBS=1 \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
%ifarch s390 %ix86 riscv64
	-DCMAKE_C_FLAGS_RELWITHDEBINFO="%{optflags} -DNDEBUG" \
	-DCMAKE_CXX_FLAGS_RELWITHDEBINFO="%{optflags} -DNDEBUG" \
%endif
%if %{without compat_build}
%if 0%{?__isa_bits} == 64
	-DLLVM_LIBDIR_SUFFIX=64 \
%else
	-DLLVM_LIBDIR_SUFFIX= \
%endif
%endif
	\
	-DLLVM_TARGETS_TO_BUILD=%{targets_to_build} \
	-DLLVM_ENABLE_LIBCXX:BOOL=OFF \
	-DLLVM_ENABLE_ZLIB:BOOL=ON \
	-DLLVM_ENABLE_FFI:BOOL=ON \
	-DLLVM_ENABLE_RTTI:BOOL=ON \
	-DLLVM_USE_PERF:BOOL=ON \
%if %{with gold}
	-DLLVM_BINUTILS_INCDIR=%{_includedir} \
%endif
	-DLLVM_EXPERIMENTAL_TARGETS_TO_BUILD=%{experimental_targets_to_build} \
	\
	-DLLVM_BUILD_RUNTIME:BOOL=ON \
	\
	-DLLVM_INCLUDE_TOOLS:BOOL=ON \
	-DLLVM_BUILD_TOOLS:BOOL=ON \
	\
	-DLLVM_INCLUDE_TESTS:BOOL=ON \
	-DLLVM_BUILD_TESTS:BOOL=ON \
	-DLLVM_INSTALL_GTEST:BOOL=ON \
	-DLLVM_LIT_ARGS=-v \
	\
	-DLLVM_INCLUDE_EXAMPLES:BOOL=ON \
	-DLLVM_BUILD_EXAMPLES:BOOL=OFF \
	\
	-DLLVM_INCLUDE_UTILS:BOOL=ON \
	-DLLVM_INSTALL_UTILS:BOOL=ON \
	-DLLVM_UTILS_INSTALL_DIR:PATH=bin \
	-DLLVM_TOOLS_INSTALL_DIR:PATH=bin \
	\
	-DLLVM_INCLUDE_DOCS:BOOL=ON \
	-DLLVM_BUILD_DOCS:BOOL=ON \
	-DLLVM_ENABLE_SPHINX:BOOL=ON \
	-DLLVM_ENABLE_DOXYGEN:BOOL=OFF \
	\
%if %{with snapshot_build}
	-DLLVM_VERSION_SUFFIX="%{llvm_snapshot_version_suffix}" \
%else
	-DLLVM_VERSION_SUFFIX='' \
%endif
	-DLLVM_UNREACHABLE_OPTIMIZE:BOOL=ON \
	-DLLVM_BUILD_LLVM_DYLIB:BOOL=ON \
	-DLLVM_LINK_LLVM_DYLIB:BOOL=ON \
	-DLLVM_BUILD_EXTERNAL_COMPILER_RT:BOOL=ON \
	-DLLVM_INSTALL_TOOLCHAIN_ONLY:BOOL=OFF \
	-DLLVM_DEFAULT_TARGET_TRIPLE=%{llvm_triple} \
	-DSPHINX_WARNINGS_AS_ERRORS=OFF \
	-DCMAKE_INSTALL_PREFIX=%{install_prefix} \
	-DLLVM_INSTALL_SPHINX_HTML_DIR=%{_pkgdocdir}/html \
	-DSPHINX_EXECUTABLE=%{_bindir}/sphinx-build-3 \
	-DLLVM_INCLUDE_BENCHMARKS=OFF \
%if %{with lto_build}
	-DLLVM_UNITTEST_LINK_FLAGS="-Wl,-plugin-opt=O0" \
%endif
%ifarch x86_64
	-DCMAKE_SHARED_LINKER_FLAGS="$LDFLAGS -Wl,-z,cet-report=error"
%endif

# Build libLLVM.so first.  This ensures that when libLLVM.so is linking, there
# are no other compile jobs running.  This will help reduce OOM errors on the
# builders without having to artificially limit the number of concurrent jobs.
%cmake_build --target LLVM
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}/%{_bindir}

# Install binaries needed for lit tests
%global test_binaries llvm-isel-fuzzer llvm-opt-fuzzer

for f in %{test_binaries}
do
    install -m 0755 %{_vpath_builddir}/bin/$f %{buildroot}%{install_bindir}
done

# Remove testing of update utility tools
rm -rf test/tools/UpdateTestChecks

# Install libraries needed for unittests
%if %{without compat_build}
%global build_libdir %{_vpath_builddir}/%{_lib}
%else
%global build_libdir %{_vpath_builddir}/lib
%endif

install %{build_libdir}/libLLVMTestingSupport.a %{buildroot}%{install_libdir}
install %{build_libdir}/libLLVMTestingAnnotations.a %{buildroot}%{install_libdir}

# Fix multi-lib
%multilib_fix_c_header --file %{install_includedir}/llvm/Config/llvm-config.h

%if %{without compat_build}

# Fix some man pages
ln -s llvm-config.1 %{buildroot}%{_mandir}/man1/llvm-config%{exec_suffix}-%{__isa_bits}.1

%if %{with gold}
# Add symlink to lto plugin in the binutils plugin directory.
%{__mkdir_p} %{buildroot}%{_libdir}/bfd-plugins/
ln -s -t %{buildroot}%{_libdir}/bfd-plugins/ ../LLVMgold.so
%endif

%else

# Add version suffix to binaries
for f in %{buildroot}/%{install_bindir}/*; do
  filename=`basename $f`
  ln -s ../../%{install_bindir}/$filename %{buildroot}/%{_bindir}/$filename%{exec_suffix}
done

# Create ld.so.conf.d entry
mkdir -p %{buildroot}/etc/ld.so.conf.d
cat >> %{buildroot}/etc/ld.so.conf.d/%{name}-%{_arch}.conf << EOF
%{install_libdir}
EOF

# Add version suffix to man pages and move them to mandir.
mkdir -p %{buildroot}/%{_mandir}/man1
for f in %{build_install_prefix}/share/man/man1/*; do
  filename=`basename $f | cut -f 1 -d '.'`
  mv $f %{buildroot}%{_mandir}/man1/$filename%{exec_suffix}.1
done

%endif

# llvm-config special casing. llvm-config is managed by update-alternatives.
# the original file must remain available for compatibility with the CMake
# infrastructure. Without compat, cmake points to the symlink, with compat it
# points to the original file.

%if %{without compat_build}

mv %{buildroot}/%{install_bindir}/llvm-config %{buildroot}/%{install_bindir}/llvm-config%{exec_suffix}-%{__isa_bits}
# We still maintain a versionned symlink for consistency across llvm versions.
# This is specific to the non-compat build and matches the exec prefix for
# compat builds. An isa-agnostic versionned symlink is also maintained in the (un)install
# steps.
(cd %{buildroot}/%{install_bindir} ; ln -s llvm-config%{exec_suffix}-%{__isa_bits} llvm-config-%{maj_ver}-%{__isa_bits} )
# ghost presence
touch %{buildroot}%{_bindir}/llvm-config-%{maj_ver}

%else

rm %{buildroot}%{_bindir}/llvm-config%{exec_suffix}
(cd %{buildroot}/%{install_bindir} ; ln -s llvm-config llvm-config%{exec_suffix}-%{__isa_bits} )

%endif

# ghost presence
touch %{buildroot}%{_bindir}/llvm-config%{exec_suffix}

mkdir -p %{buildroot}%{pkg_datadir}/llvm/cmake
cp -Rv ../cmake/* %{buildroot}%{pkg_datadir}/llvm/cmake

%check

# non reproducible errors
rm test/tools/dsymutil/X86/swift-interface.test

%if %{with check}
# FIXME: use %%cmake_build instead of %%__ninja
LD_LIBRARY_PATH=%{buildroot}/%{install_libdir}  %{__ninja} check-all -C %{_vpath_builddir}
%endif

%if %{with compat_build}
# Packages that install files in /etc/ld.so.conf have to manually run
# ldconfig.
# See https://bugzilla.redhat.com/show_bug.cgi?id=2001328 and
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/#_linker_configuration_files
%post -p /sbin/ldconfig libs
%postun -p /sbin/ldconfig libs
%endif

%post devel
%{_sbindir}/update-alternatives --install %{_bindir}/llvm-config%{exec_suffix} llvm-config%{exec_suffix} %{install_bindir}/llvm-config%{exec_suffix}-%{__isa_bits} %{__isa_bits}
%if %{without compat_build}
%{_sbindir}/update-alternatives --install %{_bindir}/llvm-config-%{maj_ver} llvm-config-%{maj_ver} %{install_bindir}/llvm-config%{exec_suffix}-%{__isa_bits} %{__isa_bits}

# During the upgrade from LLVM 16 (F38) to LLVM 17 (F39), we found out the
# main llvm-devel package was leaving entries in the alternatives system.
# Try to remove them now.
for v in 14 15 16; do
  if [[ -e %{_bindir}/llvm-config-$v
		&& "x$(%{_bindir}/llvm-config-$v --version | awk -F . '{ print $1 }')" != "x$v" ]]; then
    %{_sbindir}/update-alternatives --remove llvm-config-$v %{install_bindir}/llvm-config%{exec_suffix}-%{__isa_bits}
  fi
done
%endif

%postun devel
if [ $1 -eq 0 ]; then
  %{_sbindir}/update-alternatives --remove llvm-config%{exec_suffix} %{install_bindir}/llvm-config%{exec_suffix}-%{__isa_bits}
fi
%if %{without compat_build}
# When upgrading between minor versions (i.e. from x.y.1 to x.y.2), we must
# not remove the alternative.
# However, during a major version upgrade (i.e. from 16.x.y to 17.z.w), the
# alternative must be removed in order to give priority to a newly installed
# compat package.
if [[ $1 -eq 0
	  || "x$(%{_bindir}/llvm-config-%{maj_ver} --version | awk -F . '{ print $1 }')" != "x%{maj_ver}" ]]; then
  %{_sbindir}/update-alternatives --remove llvm-config-%{maj_ver} %{install_bindir}/llvm-config%{exec_suffix}-%{__isa_bits}
fi
%endif

%files
%license LICENSE.TXT
%exclude %{_mandir}/man1/llvm-config*
%{_mandir}/man1/*
%{install_bindir}/*
%if %{with compat_build}
# This is for all the binaries with the version suffix.
%{_bindir}/*%{exec_suffix}
%endif

%exclude %{_bindir}/llvm-config%{exec_suffix}
%exclude %{install_bindir}/llvm-config%{exec_suffix}-%{__isa_bits}

%exclude %{_bindir}/llvm-config-%{maj_ver}
%exclude %{install_bindir}/llvm-config-%{maj_ver}-%{__isa_bits}
%exclude %{install_bindir}/not
%exclude %{install_bindir}/count
%exclude %{install_bindir}/yaml-bench
%exclude %{install_bindir}/lli-child-target
%exclude %{install_bindir}/llvm-isel-fuzzer
%exclude %{install_bindir}/llvm-opt-fuzzer
%{pkg_datadir}/opt-viewer

%files libs
%license LICENSE.TXT
%{install_libdir}/libLLVM-%{maj_ver}%{?llvm_snapshot_version_suffix:%{llvm_snapshot_version_suffix}}.so
%if %{with gold}
%{install_libdir}/LLVMgold.so
%if %{without compat_build}
%{_libdir}/bfd-plugins/LLVMgold.so
%endif
%endif
%{install_libdir}/libLLVM-%{maj_ver}.%{min_ver}*.so
%{install_libdir}/libLTO.so*
%{install_libdir}/libRemarks.so*
%if %{with compat_build}
%config(noreplace) /etc/ld.so.conf.d/%{name}-%{_arch}.conf
%endif

%files devel
%license LICENSE.TXT

%ghost %{_bindir}/llvm-config%{exec_suffix}
%{install_bindir}/llvm-config%{exec_suffix}-%{__isa_bits}
%{_mandir}/man1/llvm-config*

%{install_includedir}/llvm
%{install_includedir}/llvm-c
%{install_libdir}/libLLVM.so
%{install_libdir}/cmake/llvm
%{install_bindir}/llvm-config-%{maj_ver}-%{__isa_bits}
%ghost %{_bindir}/llvm-config-%{maj_ver}

%files doc
%license LICENSE.TXT
%doc %{_pkgdocdir}/html

%files static
%license LICENSE.TXT
%{install_libdir}/*.a
%exclude %{install_libdir}/libLLVMTestingSupport.a
%exclude %{install_libdir}/libLLVMTestingAnnotations.a
%exclude %{install_libdir}/libllvm_gtest.a
%exclude %{install_libdir}/libllvm_gtest_main.a

%files cmake-utils
%license LICENSE.TXT
%{pkg_datadir}/llvm/cmake

%files test
%license LICENSE.TXT
%{install_bindir}/not
%{install_bindir}/count
%{install_bindir}/yaml-bench
%{install_bindir}/lli-child-target
%{install_bindir}/llvm-isel-fuzzer
%{install_bindir}/llvm-opt-fuzzer

%files googletest
%license LICENSE.TXT
%{install_libdir}/libLLVMTestingSupport.a
%{install_libdir}/libLLVMTestingAnnotations.a
%{install_libdir}/libllvm_gtest.a
%{install_libdir}/libllvm_gtest_main.a
%{install_includedir}/llvm-gtest
%{install_includedir}/llvm-gmock

%changelog
%autochangelog
