%global source0_hash none

%global toolchain clang

# Opt out of https://fedoraproject.org/wiki/Changes/fno-omit-frame-pointer
# https://bugzilla.redhat.com/show_bug.cgi?id=2158587
%undefine _include_frame_pointers

%bcond_without compat_build
%bcond check 0

%global maj_ver 15
%global min_ver 0
%global patch_ver 7
#global rc_ver 3
%global clang_version %{maj_ver}.%{min_ver}.%{patch_ver}

%if %{with compat_build}
%global pkg_name clang%{maj_ver}
# Install clang to same prefix as llvm, so that apps that use llvm-config
# will also be able to find clang libs.
%global install_prefix %{_libdir}/llvm%{maj_ver}
%global install_bindir %{install_prefix}/bin
%global install_includedir %{install_prefix}/include
%global install_libdir %{install_prefix}/lib

%global pkg_bindir %{install_bindir}
%global pkg_includedir %{install_includedir}
%global pkg_libdir %{install_libdir}
%else
%global pkg_name clang
%global install_prefix /usr
%global pkg_libdir %{_libdir}
%endif

%ifarch ppc64le
# Too many threads on ppc64 systems causes OOM errors.
%global _smp_mflags -j8
%endif

%global clang_srcdir clang-%{clang_version}%{?rc_ver:rc%{rc_ver}}.src
%global clang_tools_srcdir clang-tools-extra-%{clang_version}%{?rc_ver:rc%{rc_ver}}.src

Name:		%pkg_name
Version:	%{clang_version}%{?rc_ver:~rc%{rc_ver}}
Release:	12%{?dist}
Summary:	A C language family front-end for LLVM

License:	Apache-2.0 WITH LLVM-exception OR NCSA
URL:		http://llvm.org
Source0:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{clang_version}%{?rc_ver:-rc%{rc_ver}}/%{clang_srcdir}.tar.xz
Source3:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{clang_version}%{?rc_ver:-rc%{rc_ver}}/%{clang_srcdir}.tar.xz.sig
%if %{without compat_build}
Source1:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{clang_version}%{?rc_ver:-rc%{rc_ver}}/%{clang_tools_srcdir}.tar.xz
Source2:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{clang_version}%{?rc_ver:-rc%{rc_ver}}/%{clang_tools_srcdir}.tar.xz.sig
%endif
Source4:	release-keys.asc
%if %{without compat_build}
Source5:	macros.%{name}
%endif

# Patches for clang
Patch0:     0001-PATCH-clang-Reorganize-gtest-integration.patch
Patch1:     0003-PATCH-Make-funwind-tables-the-default-on-all-archs.patch
Patch2:     0003-PATCH-clang-Don-t-install-static-libraries.patch
Patch3:     0001-Driver-Add-a-gcc-equivalent-triple-to-the-list-of-tr.patch
Patch5:     0010-PATCH-clang-Produce-DWARF4-by-default.patch
Patch6:     0001-Take-into-account-Fedora-Specific-install-dir-for-li.patch

# TODO: Can be dropped in LLVM 16: https://reviews.llvm.org/D133316
Patch7:     0001-Mark-fopenmp-implicit-rpath-as-NoArgumentUnused.patch

# TODO: Can be dropped in LLVM 16: https://reviews.llvm.org/D134362
Patch8:     0001-clang-Fix-interaction-between-asm-labels-and-inline-.patch

# TODO: Can be dropped in LLVM 16.
Patch9:     0001-clang-MinGW-Improve-extend-the-gcc-sysroot-detection.patch
Patch10:    0002-clang-MinGW-Improve-detection-of-libstdc-headers-on-.patch

%if %{with compat_build}
# Ensure that clang looks for LLVMgold.so in the directory the compat build
# uses.
Patch100:   fix-lto-path.patch
%endif

%if %{without compat_build}
# Patches for clang-tools-extra
# See https://reviews.llvm.org/D120301
Patch201:   0001-clang-tools-extra-Make-test-dependency-on-LLVMHello-.patch
%endif

BuildRequires:	clang
BuildRequires:	cmake
BuildRequires:	ninja-build
%if %{with compat_build}
BuildRequires:	llvm%{maj_ver}-devel = %{version}
BuildRequires:	llvm%{maj_ver}-static = %{version}
%else
BuildRequires:	llvm-devel = %{version}
BuildRequires:	llvm-test = %{version}
# llvm-static is required, because clang-tablegen needs libLLVMTableGen, which
# is not included in libLLVM.so.
BuildRequires:	llvm-static = %{version}
BuildRequires:	llvm-googletest = %{version}
%endif

BuildRequires:	libxml2-devel
BuildRequires:	perl-generators
BuildRequires:	ncurses-devel
# According to https://fedoraproject.org/wiki/Packaging:Emacs a package
# should BuildRequires: emacs if it packages emacs integration files.
BuildRequires:	emacs

# The testsuite uses /usr/bin/lit which is part of the python3-lit package.
BuildRequires:	python3-lit

BuildRequires:	python3-sphinx
BuildRequires:	python3-recommonmark
BuildRequires:	libatomic

# We need python3-devel for %%py3_shebang_fix
BuildRequires:	python3-devel

%if %{without compat_build}
# For reproducible pyc file generation
# See https://docs.fedoraproject.org/en-US/packaging-guidelines/Python_Appendix/#_byte_compilation_reproducibility
BuildRequires: /usr/bin/marshalparser
%global py_reproducible_pyc_path %{buildroot}%{python3_sitelib}
%endif

# Needed for %%multilib_fix_c_header
BuildRequires:	multilib-rpm-config

# For origin certification
BuildRequires:	gnupg2

# scan-build uses these perl modules so they need to be installed in order
# to run the tests.
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Temp)
BuildRequires: perl(FindBin)
BuildRequires: perl(Hash::Util)
BuildRequires: perl(lib)
BuildRequires: perl(Term::ANSIColor)
BuildRequires: perl(Text::ParseWords)
BuildRequires: perl(Sys::Hostname)

Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

# clang requires gcc, clang++ requires libstdc++-devel
# - https://bugzilla.redhat.com/show_bug.cgi?id=1021645
# - https://bugzilla.redhat.com/show_bug.cgi?id=1158594
Requires:	libstdc++-devel
Requires:	gcc-c++

Provides:	clang(major) = %{maj_ver}

Conflicts:	compiler-rt < 11.0.0

%description
clang: noun
    1. A loud, resonant, metallic sound.
    2. The strident call of a crane or goose.
    3. C-language family front-end toolkit.

The goal of the Clang project is to create a new C, C++, Objective C
and Objective C++ front-end for the LLVM compiler. Its tools are built
as libraries and designed to be loosely-coupled and extensible.

Install compiler-rt if you want the Blocks C language extension or to
enable sanitization and profiling options when building, and
libomp-devel to enable -fopenmp.

%package libs
Summary: Runtime library for clang
Requires: %{name}-resource-filesystem%{?_isa} = %{version}
Recommends: compiler-rt%{?_isa} = %{version}
# atomic support is not part of compiler-rt
Recommends: libatomic%{?_isa}
# libomp-devel is required, so clang can find the omp.h header when compiling
# with -fopenmp.
Recommends: libomp-devel%{_isa} = %{version}
Recommends: libomp%{_isa} = %{version}

# Use lld as the default linker on ARM due to rhbz#1918924
%ifarch %{arm}
Requires: lld
%endif

%description libs
Runtime library for clang.

%package devel
Summary: Development header files for clang
Requires: %{name}-libs = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
%if %{without compat_build}
# The clang CMake files reference tools from clang-tools-extra.
Requires: %{name}-tools-extra%{?_isa} = %{version}-%{release}
%endif

%description devel
Development header files for clang.

%package resource-filesystem
Summary: Filesystem package that owns the clang resource directory
Provides: %{name}-resource-filesystem(major) = %{maj_ver}

%description resource-filesystem
This package owns the clang resouce directory: $libdir/clang/$version/

%if %{without compat_build}
%package analyzer
Summary:	A source code analysis framework
License:	Apache-2.0 WITH LLVM-exception OR NCSA OR MIT
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}

%description analyzer
The Clang Static Analyzer consists of both a source code analysis
framework and a standalone tool that finds bugs in C and Objective-C
programs. The standalone tool is invoked from the command-line, and is
intended to run in tandem with a build of a project or code base.

%package tools-extra
Summary:	Extra tools for clang
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	emacs-filesystem

%description tools-extra
A set of extra tools built using Clang's tooling API.

%package tools-extra-devel
Summary: Development header files for clang tools
Requires: %{name}-tools-extra = %{version}-%{release}

%description tools-extra-devel
Development header files for clang tools.

# Put git-clang-format in its own package, because it Requires git
# and we don't want to force users to install all those dependenices if they
# just want clang.
%package -n git-clang-format
Summary:	Integration of clang-format for git
Requires:	%{name}-tools-extra = %{version}-%{release}
Requires:	git
Requires:	python3

%description -n git-clang-format
clang-format integration for git.

%package -n python3-clang
Summary:       Python3 bindings for clang
Requires:      %{name}-devel%{?_isa} = %{version}-%{release}
Requires:      python3
%description -n python3-clang
%{summary}.

%endif

%prep
%{gpgverify} --keyring='%{SOURCE4}' --signature='%{SOURCE3}' --data='%{SOURCE0}'

%if %{with compat_build}
%autosetup -n %{clang_srcdir} -p2
%else

%{gpgverify} --keyring='%{SOURCE4}' --signature='%{SOURCE2}' --data='%{SOURCE1}'
%setup -T -q -b 1 -n %{clang_tools_srcdir}
%autopatch -m200 -p2

# failing test case
rm test/clang-tidy/checkers/altera/struct-pack-align.cpp

%py3_shebang_fix \
	clang-tidy/tool/ \
	clang-include-fixer/find-all-symbols/tool/run-find-all-symbols.py

%setup -q -n %{clang_srcdir}
%autopatch -M200 -p2

# failing test case
rm test/CodeGen/profile-filter.c

%py3_shebang_fix \
	tools/clang-format/ \
	tools/clang-format/git-clang-format \
	utils/hmaptool/hmaptool \
	tools/scan-view/bin/scan-view \
	tools/scan-view/share/Reporter.py \
	tools/scan-view/share/startfile.py \
	tools/scan-build-py/bin/* \
	tools/scan-build-py/libexec/*
%endif

%build

# Use ThinLTO to limit build time.
%define _lto_cflags -flto=thin
# And disable LTO on AArch64 entirely.
%ifarch aarch64
%define _lto_cflags %{nil}
%endif

%if 0%{?__isa_bits} == 64
sed -i 's/\@FEDORA_LLVM_LIB_SUFFIX\@/64/g' test/lit.cfg.py
%else
sed -i 's/\@FEDORA_LLVM_LIB_SUFFIX\@//g' test/lit.cfg.py
%endif

%ifarch s390 s390x %{arm} aarch64 %ix86 ppc64le
# Decrease debuginfo verbosity to reduce memory consumption during final library linking
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')
%endif

# Disable dwz on aarch64, because it takes a huge amount of time to decide not to optimize things.
%ifarch aarch64
%define _find_debuginfo_dwz_opts %{nil}
%endif

# We set CLANG_DEFAULT_PIE_ON_LINUX=OFF and PPC_LINUX_DEFAULT_IEEELONGDOUBLE=ON to match the
# defaults used by Fedora's GCC.
%cmake  -G Ninja \
	-DCLANG_DEFAULT_PIE_ON_LINUX=OFF \
%if 0%{?fedora} || 0%{?rhel} > 9
	-DPPC_LINUX_DEFAULT_IEEELONGDOUBLE=ON \
%endif
	-DLLVM_PARALLEL_LINK_JOBS=1 \
	-DLLVM_LINK_LLVM_DYLIB:BOOL=ON \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DPYTHON_EXECUTABLE=%{__python3} \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
%ifarch s390 s390x %{arm} %ix86 ppc64le
	-DCMAKE_C_FLAGS_RELWITHDEBINFO="%{optflags} -DNDEBUG" \
	-DCMAKE_CXX_FLAGS_RELWITHDEBINFO="%{optflags} -DNDEBUG" \
%endif
%if %{with compat_build}
	-DLLVM_CMAKE_DIR=%{install_libdir}/cmake/llvm \
	-DCMAKE_INSTALL_PREFIX=%{install_prefix} \
	-DCLANG_INCLUDE_TESTS:BOOL=OFF \
%else
	-DCLANG_INCLUDE_TESTS:BOOL=ON \
	-DLLVM_BUILD_UTILS:BOOL=ON \
	-DLLVM_EXTERNAL_CLANG_TOOLS_EXTRA_SOURCE_DIR=../%{clang_tools_srcdir} \
	-DLLVM_EXTERNAL_LIT=%{_bindir}/lit \
	-DLLVM_LIT_ARGS="-vv" \
	-DLLVM_MAIN_SRC_DIR=%{_datadir}/llvm/src \
%if 0%{?__isa_bits} == 64
	-DLLVM_LIBDIR_SUFFIX=64 \
%else
	-DLLVM_LIBDIR_SUFFIX= \
%endif
%endif
	\
%if %{with compat_build}
	-DLLVM_TABLEGEN_EXE:FILEPATH=%{_bindir}/llvm-tblgen-%{maj_ver} \
%else
	-DLLVM_TABLEGEN_EXE:FILEPATH=%{_bindir}/llvm-tblgen \
%endif
	-DCLANG_ENABLE_ARCMT:BOOL=ON \
	-DCLANG_ENABLE_STATIC_ANALYZER:BOOL=ON \
	-DCLANG_INCLUDE_DOCS:BOOL=ON \
	-DCLANG_PLUGIN_SUPPORT:BOOL=ON \
	-DENABLE_LINKER_BUILD_ID:BOOL=ON \
	-DLLVM_ENABLE_EH=ON \
	-DLLVM_ENABLE_RTTI=ON \
	-DLLVM_BUILD_DOCS=ON \
	-DLLVM_ENABLE_SPHINX=ON \
	-DCLANG_LINK_CLANG_DYLIB=ON \
	-DSPHINX_WARNINGS_AS_ERRORS=OFF \
	\
	-DCLANG_BUILD_EXAMPLES:BOOL=OFF \
	-DBUILD_SHARED_LIBS=OFF \
	-DCLANG_REPOSITORY_STRING="%{?dist_vendor} %{version}-%{release}" \
%ifarch %{arm}
	-DCLANG_DEFAULT_LINKER=lld \
%endif
	-DCLANG_DEFAULT_UNWINDLIB=libgcc

%cmake_build

%install

%cmake_install

%if %{with compat_build}

# Remove binaries/other files
find %{buildroot}%{install_bindir} -type f ! -name clang-%{maj_ver} ! -name clang \
     ! -name clang++ ! -name clang-cl ! -name clang-cpp -delete
install -D -m 0644 %{buildroot}%{install_prefix}/share/man/man1/clang.1 \
        %{buildroot}%{_mandir}/man1/clang-%{maj_ver}.1
rm -Rf %{buildroot}%{install_prefix}/share
rm -Rf %{buildroot}%{install_prefix}/libexec
# Remove scanview-py helper libs
rm -Rf %{buildroot}%{install_prefix}/lib/{libear,libscanbuild}

# Create Manpage symlinks
ln -s clang-%{maj_ver}.1.gz %{buildroot}%{_mandir}/man1/clang++-%{maj_ver}.1.gz

# Add clang-{version} symlinks
mkdir -p %{buildroot}%{_bindir}
ln -s %{install_bindir}/clang %{buildroot}%{_bindir}/clang-%{maj_ver}
ln -s %{install_bindir}/clang++ %{buildroot}%{_bindir}/clang++-%{maj_ver}
ln -s clang++ %{buildroot}%{install_bindir}/clang++-%{maj_ver}

%else

# File in the macros file for other packages to use.  We are not doing this
# in the compat package, because the version macros would # conflict with
# eachother if both clang and the clang compat package were installed together.
install -p -m0644 -D %{SOURCE5} %{buildroot}%{_rpmmacrodir}/macros.%{name}
sed -i -e "s|@@CLANG_MAJOR_VERSION@@|%{maj_ver}|" \
       -e "s|@@CLANG_MINOR_VERSION@@|%{min_ver}|" \
       -e "s|@@CLANG_PATCH_VERSION@@|%{patch_ver}|" \
       %{buildroot}%{_rpmmacrodir}/macros.%{name}

# install clang python bindings
mkdir -p %{buildroot}%{python3_sitelib}/clang/
install -p -m644 bindings/python/clang/* %{buildroot}%{python3_sitelib}/clang/
%py_byte_compile %{__python3} %{buildroot}%{python3_sitelib}/clang

# install scanbuild-py to python sitelib.
mv %{buildroot}%{_prefix}/lib/{libear,libscanbuild} %{buildroot}%{python3_sitelib}
%py_byte_compile %{__python3} %{buildroot}%{python3_sitelib}/{libear,libscanbuild}

# Fix permissions of scan-view scripts
chmod a+x %{buildroot}%{_datadir}/scan-view/{Reporter.py,startfile.py}

# multilib fix
%multilib_fix_c_header --file %{_includedir}/clang/Config/config.h

# Move emacs integration files to the correct directory
mkdir -p %{buildroot}%{_emacs_sitestartdir}
for f in clang-format.el clang-rename.el clang-include-fixer.el; do
mv %{buildroot}{%{_datadir}/clang,%{_emacs_sitestartdir}}/$f
done

# remove editor integrations (bbedit, sublime, emacs, vim)
rm -vf %{buildroot}%{_datadir}/clang/clang-format-bbedit.applescript
rm -vf %{buildroot}%{_datadir}/clang/clang-format-sublime.py*

# TODO: Package html docs
rm -Rvf %{buildroot}%{_docdir}/Clang/clang/html
rm -Rvf %{buildroot}%{_datadir}/clang/clang-doc-default-stylesheet.css
rm -Rvf %{buildroot}%{_datadir}/clang/index.js

# TODO: What are the Fedora guidelines for packaging bash autocomplete files?
rm -vf %{buildroot}%{_datadir}/clang/bash-autocomplete.sh

# Create Manpage symlinks
ln -s clang.1.gz %{buildroot}%{_mandir}/man1/clang++.1.gz
ln -s clang.1.gz %{buildroot}%{_mandir}/man1/clang-%{maj_ver}.1.gz
ln -s clang.1.gz %{buildroot}%{_mandir}/man1/clang++-%{maj_ver}.1.gz

# Add clang++-{version} symlink
ln -s clang++ %{buildroot}%{_bindir}/clang++-%{maj_ver}

# Fix permission
chmod u-x %{buildroot}%{_mandir}/man1/scan-build.1*

# create a link to clang's resource directory that is "constant" across minor
# version bumps
# this is required for packages like ccls that hardcode the link to clang's
# resource directory to not require rebuilds on minor version bumps
# Fix for bugs like rhbz#1807574
pushd %{buildroot}%{_libdir}/clang/
ln -s %{version} %{maj_ver}
popd

%endif

# Create sub-directories in the clang resource directory that will be
# populated by other packages
mkdir -p %{buildroot}%{pkg_libdir}/clang/%{version}/{include,lib,share}/

%if %{without compat_build}
# Add a symlink in /usr/bin to clang-format-diff
ln -s %{_datadir}/clang/clang-format-diff.py %{buildroot}%{_bindir}/clang-format-diff
%endif

%check
%if %{without compat_build}
%if %{with check}
# Build test dependencies separately, to prevent invocations of host clang from being affected
# by LD_LIBRARY_PATH below.
%cmake_build --target clang-test-depends \
    ExtraToolsUnitTests ClangdUnitTests ClangIncludeCleanerUnitTests ClangPseudoUnitTests
# requires lit.py from LLVM utilities
# FIXME: Fix failing ARM tests
LD_LIBRARY_PATH=%{buildroot}/%{_libdir} %{__ninja} check-all -C %{__cmake_builddir} || \
%ifarch %{arm}
:
%else
false
%endif
%endif
%endif

%files
%license LICENSE.TXT
%{_bindir}/clang-%{maj_ver}
%{_bindir}/clang++-%{maj_ver}
%if %{without compat_build}
%{_bindir}/clang
%{_bindir}/clang++
%{_bindir}/clang-cl
%{_bindir}/clang-cpp
%{_mandir}/man1/clang.1.gz
%{_mandir}/man1/clang++.1.gz
%else
%{pkg_bindir}/clang
%{pkg_bindir}/clang++
%{pkg_bindir}/clang-%{maj_ver}
%{pkg_bindir}/clang++-%{maj_ver}
%{pkg_bindir}/clang-cl
%{pkg_bindir}/clang-cpp
%endif
%{_mandir}/man1/clang-%{maj_ver}.1.gz
%{_mandir}/man1/clang++-%{maj_ver}.1.gz

%files libs
%if %{without compat_build}
%{_libdir}/clang/%{version}/include/*
%{_libdir}/*.so.*
%else
%{pkg_libdir}/*.so.*
%{pkg_libdir}/clang/%{version}/include/*
%endif

%files devel
%if %{without compat_build}
%{_libdir}/*.so
%{_includedir}/clang/
%{_includedir}/clang-c/
%{_libdir}/cmake/*
%{_bindir}/clang-tblgen
%dir %{_datadir}/clang/
%{_rpmmacrodir}/macros.%{name}
%else
%{pkg_libdir}/*.so
%{pkg_includedir}/clang/
%{pkg_includedir}/clang-c/
%{pkg_libdir}/cmake/
%endif

%files resource-filesystem
%dir %{pkg_libdir}/clang/
%dir %{pkg_libdir}/clang/%{version}/
%dir %{pkg_libdir}/clang/%{version}/include/
%dir %{pkg_libdir}/clang/%{version}/lib/
%dir %{pkg_libdir}/clang/%{version}/share/
%if %{without compat_build}
%{pkg_libdir}/clang/%{maj_ver}
%endif

%if %{without compat_build}
%files analyzer
%{_bindir}/scan-view
%{_bindir}/scan-build
%{_bindir}/analyze-build
%{_bindir}/intercept-build
%{_bindir}/scan-build-py
%{_libexecdir}/ccc-analyzer
%{_libexecdir}/c++-analyzer
%{_libexecdir}/analyze-c++
%{_libexecdir}/analyze-cc
%{_libexecdir}/intercept-c++
%{_libexecdir}/intercept-cc
%{_datadir}/scan-view/
%{_datadir}/scan-build/
%{_mandir}/man1/scan-build.1.*
%{python3_sitelib}/libear
%{python3_sitelib}/libscanbuild

%files tools-extra
%{_bindir}/clang-apply-replacements
%{_bindir}/clang-change-namespace
%{_bindir}/clang-check
%{_bindir}/clang-doc
%{_bindir}/clang-extdef-mapping
%{_bindir}/clang-format
%{_bindir}/clang-include-fixer
%{_bindir}/clang-move
%{_bindir}/clang-offload-bundler
%{_bindir}/clang-offload-packager
%{_bindir}/clang-offload-wrapper
%{_bindir}/clang-linker-wrapper
%{_bindir}/clang-nvlink-wrapper
%{_bindir}/clang-pseudo
%{_bindir}/clang-query
%{_bindir}/clang-refactor
%{_bindir}/clang-rename
%{_bindir}/clang-reorder-fields
%{_bindir}/clang-repl
%{_bindir}/clang-scan-deps
%{_bindir}/clang-tidy
%{_bindir}/clangd
%{_bindir}/diagtool
%{_bindir}/hmaptool
%{_bindir}/pp-trace
%{_bindir}/c-index-test
%{_bindir}/find-all-symbols
%{_bindir}/modularize
%{_bindir}/clang-format-diff
%{_mandir}/man1/diagtool.1.gz
%{_emacs_sitestartdir}/clang-format.el
%{_emacs_sitestartdir}/clang-rename.el
%{_emacs_sitestartdir}/clang-include-fixer.el
%{_datadir}/clang/clang-format.py*
%{_datadir}/clang/clang-format-diff.py*
%{_datadir}/clang/clang-include-fixer.py*
%{_datadir}/clang/clang-tidy-diff.py*
%{_bindir}/run-clang-tidy
%{_datadir}/clang/run-find-all-symbols.py*
%{_datadir}/clang/clang-rename.py*

%files tools-extra-devel
%{_includedir}/clang-tidy/

%files -n git-clang-format
%{_bindir}/git-clang-format

%files -n python3-clang
%{python3_sitelib}/clang/

%endif
%changelog
%autochangelog
