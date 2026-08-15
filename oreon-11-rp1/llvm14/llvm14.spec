%global source0_hash 050922ecaaca5781fdf6631ea92bc715183f202f9d2f15147226f023414f619a

# We are building with clang for faster/lower memory LTO builds.
# See https://docs.fedoraproject.org/en-US/packaging-guidelines/#_compiler_macros
%global toolchain clang

# Components enabled if supported by target architecture:
%define gold_arches %{ix86} x86_64 %{arm} aarch64 %{power64} s390x
%ifarch %{gold_arches}
  %bcond_without gold
%else
  %bcond_with gold
%endif

%bcond_without compat_build
%bcond check 1

#global rc_ver 4
%global maj_ver 14
%global min_ver 0
%global patch_ver 6
%if !%{maj_ver} && 0%{?rc_ver}
%global abi_revision 2
%endif
%global llvm_srcdir llvm-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:rc%{rc_ver}}.src

%if %{with compat_build}
%global pkg_name llvm%{maj_ver}
%global exec_suffix -%{maj_ver}
%global install_prefix %{_libdir}/%{name}
%global install_bindir %{install_prefix}/bin
%global install_includedir %{install_prefix}/include
%global install_libdir %{install_prefix}/lib

%global pkg_bindir %{install_bindir}
%global pkg_includedir %{_includedir}/%{name}
%global pkg_libdir %{install_libdir}
%else
%global pkg_name llvm
%global install_prefix /usr
%global install_libdir %{_libdir}
%global pkg_bindir %{_bindir}
%global pkg_libdir %{install_libdir}
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

%ifarch %{arm}
# koji overrides the _gnu variable to be gnu, which is not correct for clang, so
# we need to hard-code the correct triple here.
%global llvm_triple armv7l-redhat-linux-gnueabihf
%else
%global llvm_triple %{_host}
%endif

# https://fedoraproject.org/wiki/Changes/PythonSafePath#Opting_out
# Don't add -P to Python shebangs
# The executable Python scripts in /usr/share/opt-viewer/ import each other
%undefine _py3_shebang_P

Name:		%{pkg_name}
Version:	%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:~rc%{rc_ver}}
Release:	1%{?dist}
Summary:	The Low Level Virtual Machine

License:	NCSA
URL:		http://llvm.org
Source0:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-rc%{rc_ver}}/%{llvm_srcdir}.tar.xz
Source1:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-rc%{rc_ver}}/%{llvm_srcdir}.tar.xz.sig
Source2:	tstellar-gpg-key.asc

%if %{without compat_build}
Source3:	run-lit-tests
Source4:	lit.fedora.cfg.py
%endif

%if 0%{?abi_revision}
Patch0:		0001-cmake-Allow-shared-libraries-to-customize-the-soname.patch
%endif
Patch1:		0001-XFAIL-missing-abstract-variable.ll-test-on-ppc64le.patch
Patch2:		0001-Disable-CrashRecoveryTest.DumpStackCleanup-test-on-a.patch
Patch3:		test-go-py-pipes.patch
Patch4: cstdint.patch
Patch5: 141083.patch

BuildRequires:	sed
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
BuildRequires:	python3-recommonmark
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
# The installed cmake files reference binaries from llvm-test and llvm-static.
# We tried in the past to split the cmake exports for these binaries out into
# separate files, so that llvm-devel would not need to Require these packages,
# but this caused bugs (rhbz#1773678) and forced us to carry two non-upstream
# patches.
Requires:	%{name}-static%{?_isa} = %{version}-%{release}
%if %{without compat_build}
Requires:	%{name}-test%{?_isa} = %{version}-%{release}
%endif

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

%package static
Summary:	LLVM static libraries
Conflicts:	%{name}-devel < 8

Provides:	llvm-static(major) = %{maj_ver}

%description static
Static libraries for the LLVM compiler infrastructure.

%if %{without compat_build}

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

%endif

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{llvm_srcdir} -p2

%py3_shebang_fix \
	test/BugPoint/compile-custom.ll.py \
	tools/opt-viewer/*.py \
	utils/update_cc_test_checks.py

%build

%ifarch s390 s390x riscv64
# No LTO support with Clang on riscv64
# Fails with "exceeded PCRE's backtracking limit"
%global _lto_cflags %nil
%endif

%ifarch s390 s390x %{arm} %ix86 riscv64
# Decrease debuginfo verbosity to reduce memory consumption during final library linking
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')
%endif

# force off shared libs as cmake macros turns it on.
%cmake	-G Ninja \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DLLVM_PARALLEL_LINK_JOBS=1 \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
%ifarch s390 %{arm} %ix86 riscv64
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
	-DLLVM_LIT_ARGS=-v \
	\
	-DLLVM_INCLUDE_EXAMPLES:BOOL=ON \
	-DLLVM_BUILD_EXAMPLES:BOOL=OFF \
	\
	-DLLVM_INCLUDE_UTILS:BOOL=ON \
%if %{with compat_build}
	-DLLVM_INSTALL_UTILS:BOOL=OFF \
%else
	-DLLVM_INSTALL_UTILS:BOOL=ON \
	-DLLVM_UTILS_INSTALL_DIR:PATH=%{_bindir} \
	-DLLVM_TOOLS_INSTALL_DIR:PATH=bin \
%endif
	\
	-DLLVM_INCLUDE_DOCS:BOOL=ON \
	-DLLVM_BUILD_DOCS:BOOL=ON \
	-DLLVM_ENABLE_SPHINX:BOOL=ON \
	-DLLVM_ENABLE_DOXYGEN:BOOL=OFF \
	\
%if %{without compat_build}
	-DLLVM_VERSION_SUFFIX='' \
%endif
	-DLLVM_BUILD_LLVM_DYLIB:BOOL=ON \
	-DLLVM_LINK_LLVM_DYLIB:BOOL=ON \
	-DLLVM_BUILD_EXTERNAL_COMPILER_RT:BOOL=ON \
	-DLLVM_INSTALL_TOOLCHAIN_ONLY:BOOL=OFF \
	%{?abi_revision:-DLLVM_ABI_REVISION=%{abi_revision}} \
	\
	-DLLVM_DEFAULT_TARGET_TRIPLE=%{llvm_triple} \
	-DSPHINX_WARNINGS_AS_ERRORS=OFF \
	-DCMAKE_INSTALL_PREFIX=%{install_prefix} \
	-DLLVM_INSTALL_SPHINX_HTML_DIR=%{_pkgdocdir}/html \
	-DSPHINX_EXECUTABLE=%{_bindir}/sphinx-build-3 \
	-DLLVM_INCLUDE_BENCHMARKS=OFF

# Build libLLVM.so first.  This ensures that when libLLVM.so is linking, there
# are no other compile jobs running.  This will help reduce OOM errors on the
# builders without having to artificially limit the number of concurrent jobs.
%cmake_build --target LLVM
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}/%{_bindir}

%if %{without compat_build}

# Fix some man pages
ln -s llvm-config.1 %{buildroot}%{_mandir}/man1/llvm-config%{exec_suffix}-%{__isa_bits}.1

# Install binaries needed for lit tests
%global test_binaries llvm-isel-fuzzer llvm-opt-fuzzer

for f in %{test_binaries}
do
    install -m 0755 %{_vpath_builddir}/bin/$f %{buildroot}%{_bindir}
done

# Remove testing of update utility tools
rm -rf test/tools/UpdateTestChecks

%multilib_fix_c_header --file %{_includedir}/llvm/Config/llvm-config.h

# Install libraries needed for unittests
%if 0%{?__isa_bits} == 64
%global build_libdir %{_vpath_builddir}/lib64
%else
%global build_libdir %{_vpath_builddir}/lib
%endif

install %{build_libdir}/libLLVMTestingSupport.a %{buildroot}%{_libdir}

%global install_srcdir %{buildroot}%{_datadir}/llvm/src

# Install gtest sources so clang can use them for gtest
install -d %{install_srcdir}
install -d %{install_srcdir}/utils/
cp -R utils/unittest %{install_srcdir}/utils/

# Clang needs these for running lit tests.
cp utils/update_cc_test_checks.py %{install_srcdir}/utils/
cp -R utils/UpdateTestChecks %{install_srcdir}/utils/

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

# Move header files
mkdir -p %{buildroot}/%{pkg_includedir}
ln -s ../../../%{install_includedir}/llvm %{buildroot}/%{pkg_includedir}/llvm
ln -s ../../../%{install_includedir}/llvm-c %{buildroot}/%{pkg_includedir}/llvm-c

# Fix multi-lib
%multilib_fix_c_header --file %{install_includedir}/llvm/Config/llvm-config.h

# Create ld.so.conf.d entry
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
cat >> %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf << EOF
%{pkg_libdir}
EOF

# Add version suffix to man pages and move them to mandir.
mkdir -p %{buildroot}/%{_mandir}/man1
for f in %{build_install_prefix}/share/man/man1/*; do
  filename=`basename $f | cut -f 1 -d '.'`
  mv $f %{buildroot}%{_mandir}/man1/$filename%{exec_suffix}.1
done

# Remove opt-viewer, since this is just a compatibility package.
rm -Rf %{build_install_prefix}/share/opt-viewer

%endif

# llvm-config special casing. llvm-config is managed by update-alternatives.
# the original file must remain available for compatibility with the CMake
# infrastructure. Without compat, cmake points to the symlink, with compat it
# points to the original file.

%if %{without compat_build}

mv %{buildroot}/%{pkg_bindir}/llvm-config %{buildroot}/%{pkg_bindir}/llvm-config%{exec_suffix}-%{__isa_bits}
# We still maintain a versionned symlink for consistency across llvm versions.
# This is specific to the non-compat build and matches the exec prefix for
# compat builds. An isa-agnostic versionned symlink is also maintained in the (un)install
# steps.
(cd %{buildroot}/%{pkg_bindir} ; ln -s llvm-config%{exec_suffix}-%{__isa_bits} llvm-config-%{maj_ver}-%{__isa_bits} )
# ghost presence
touch %{buildroot}%{_bindir}/llvm-config-%{maj_ver}

%else

rm %{buildroot}%{_bindir}/llvm-config%{exec_suffix}
(cd %{buildroot}/%{pkg_bindir} ; ln -s llvm-config llvm-config%{exec_suffix}-%{__isa_bits} )

%endif

# ghost presence
touch %{buildroot}%{_bindir}/llvm-config%{exec_suffix}

%if %{without compat_build}
cp -Rv ../cmake/Modules/* %{buildroot}%{_libdir}/cmake/llvm
%endif

%check
# Disable check section on arm due to some kind of memory related failure.
# Possibly related to https://bugzilla.redhat.com/show_bug.cgi?id=1920183
%ifnarch %{arm}

%ifarch riscv64
rm test/tools/llvm-ar/error-opening-permission.test
rm test/tools/llvm-dwarfdump/X86/output.s
rm test/tools/llvm-ifs/fail-file-write.test

rm unittests/ExecutionEngine/Orc/OrcCAPITest.cpp
sed -i '/OrcCAPITest.cpp/d' unittests/ExecutionEngine/Orc/CMakeLists.txt
%endif

# TODO: Fix the failures below
%ifarch %{arm}
rm test/tools/llvm-readobj/ELF/dependent-libraries.test
%endif

# non reproducible errors
rm test/tools/dsymutil/X86/swift-interface.test

%if %{with check}
# FIXME: use %%cmake_build instead of %%__ninja
LD_LIBRARY_PATH=%{buildroot}/%{pkg_libdir}  %{__ninja} check-all -C %{_vpath_builddir}
%endif

%endif

%ldconfig_scriptlets libs

%post devel
%{_sbindir}/update-alternatives --install %{_bindir}/llvm-config%{exec_suffix} llvm-config%{exec_suffix} %{pkg_bindir}/llvm-config%{exec_suffix}-%{__isa_bits} %{__isa_bits}
%if %{without compat_build}
%{_sbindir}/update-alternatives --install %{_bindir}/llvm-config-%{maj_ver} llvm-config-%{maj_ver} %{pkg_bindir}/llvm-config%{exec_suffix}-%{__isa_bits} %{__isa_bits}
%endif

%postun devel
if [ $1 -eq 0 ]; then
  %{_sbindir}/update-alternatives --remove llvm-config%{exec_suffix} %{pkg_bindir}/llvm-config%{exec_suffix}-%{__isa_bits}
%if %{without compat_build}
  %{_sbindir}/update-alternatives --remove llvm-config-%{maj_ver} %{pkg_bindir}/llvm-config%{exec_suffix}-%{__isa_bits}
%endif
fi

%files
%license LICENSE.TXT
%exclude %{_mandir}/man1/llvm-config*
%{_mandir}/man1/*
%{_bindir}/*

%exclude %{_bindir}/llvm-config%{exec_suffix}
%exclude %{pkg_bindir}/llvm-config%{exec_suffix}-%{__isa_bits}

%if %{without compat_build}
%exclude %{_bindir}/llvm-config-%{maj_ver}
%exclude %{pkg_bindir}/llvm-config-%{maj_ver}-%{__isa_bits}
%exclude %{_bindir}/not
%exclude %{_bindir}/count
%exclude %{_bindir}/yaml-bench
%exclude %{_bindir}/lli-child-target
%exclude %{_bindir}/llvm-isel-fuzzer
%exclude %{_bindir}/llvm-opt-fuzzer
%{_datadir}/opt-viewer
%else
%{pkg_bindir}
%endif

%files libs
%license LICENSE.TXT
%{pkg_libdir}/libLLVM-%{maj_ver}.so
%if %{without compat_build}
%if %{with gold}
%{_libdir}/LLVMgold.so
%{_libdir}/bfd-plugins/LLVMgold.so
%endif
%{_libdir}/libLLVM-%{maj_ver}.%{min_ver}*.so
%{_libdir}/libLLVM-%{maj_ver}.so%{?abi_revision:.%{abi_revision}}
%{_libdir}/libLTO.so*
%else
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf
%if %{with gold}
%{_libdir}/%{name}/lib/LLVMgold.so
%endif
%{pkg_libdir}/libLLVM-%{maj_ver}.%{min_ver}*.so
%{pkg_libdir}/libLTO.so*
%exclude %{pkg_libdir}/libLTO.so
%endif
%{pkg_libdir}/libRemarks.so*

%files devel
%license LICENSE.TXT

%ghost %{_bindir}/llvm-config%{exec_suffix}
%{pkg_bindir}/llvm-config%{exec_suffix}-%{__isa_bits}
%{_mandir}/man1/llvm-config*

%if %{without compat_build}
%{_includedir}/llvm
%{_includedir}/llvm-c
%{_libdir}/libLLVM.so
%{_libdir}/cmake/llvm
%{pkg_bindir}/llvm-config-%{maj_ver}-%{__isa_bits}
%ghost %{_bindir}/llvm-config-%{maj_ver}
%else
%{install_includedir}/llvm
%{install_includedir}/llvm-c
%{pkg_includedir}/llvm
%{pkg_includedir}/llvm-c
%{pkg_libdir}/libLTO.so
%{pkg_libdir}/libLLVM.so
%{pkg_libdir}/cmake/llvm
%endif

%files doc
%license LICENSE.TXT
%doc %{_pkgdocdir}/html

%files static
%license LICENSE.TXT
%if %{without compat_build}
%{_libdir}/*.a
%exclude %{_libdir}/libLLVMTestingSupport.a
%else
%{_libdir}/%{name}/lib/*.a
%endif

%if %{without compat_build}

%files test
%license LICENSE.TXT
%{_bindir}/not
%{_bindir}/count
%{_bindir}/yaml-bench
%{_bindir}/lli-child-target
%{_bindir}/llvm-isel-fuzzer
%{_bindir}/llvm-opt-fuzzer

%files googletest
%license LICENSE.TXT
%{_datadir}/llvm/src/utils
%{_libdir}/libLLVMTestingSupport.a

%endif

%changelog
%autochangelog
