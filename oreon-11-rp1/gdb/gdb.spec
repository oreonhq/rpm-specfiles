%global source0_hash 14996f5f74c9f68f5a543fdc45bca7800207f91f92aeea6c2e791822c7c6d876

# rpmbuild parameters:
# --with testsuite: Run the testsuite (biarch if possible).  Default is without.
# --with buildisa: Use %%{?_isa} for BuildRequires
# --with asan: gcc -fsanitize=address
# --without python: No python support.
# --with profile: gcc -fprofile-generate / -fprofile-use: Before better
#                 workload gets run it decreases the general performance now.
# --define 'scl somepkgname': Independent packages by scl-utils-build.
# --define 'tests "TEST1 ... TESTN": Limit testing to specified tests.

# Turn off the brp-python-bytecompile automagic
%global _python_bytecompile_extra 0

# Disable LTO until upstream fixes GDB's ODR woes.
%define _lto_cflags %{nil}

%{?scl:%scl_package gdb}
%{!?scl:
 %global pkg_name %{name}
 %global _root_prefix %{_prefix}
 %global _root_datadir %{_datadir}
 %global _root_libdir %{_libdir}
}

# If we're on Fedora or RHEL 9+, we will build the gdb-minimal package.
# Never build the -minimal package on SCLs, since it's unneeded there.
%if 0%{?fedora} || (0%{?rhel} > 8 && 0%{!?scl:1})
  %global _build_minimal 1
%endif

# Include support for Guile? This is enabled on RHEL 8 and
# Fedora < 38.
%if (0%{?fedora:1} && 0%{?fedora} < 38) || (0%{?rhel:1} && 0%{?rhel} == 8)
  %define use_guile 1
%endif

Name: %{?scl_prefix}gdb

# Freeze it when GDB gets branched
%global snapsrc    20220501
# See timestamp of source gnulib installed into gnulib/ .
%global snapgnulib 20220501
%global tarname gdb-%{version}
Version: 17.1

# The release always contains a leading reserved number, start it at 1.
# `upstream' is not a part of `name' to stay fully rpm dependencies compatible for the testing.
Release: 6%{?dist}

License: GPL-3.0-or-later AND BSD-3-Clause AND FSFAP AND LGPL-2.1-or-later AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain AND GFDL-1.3-or-later AND LGPL-2.0-or-later WITH GCC-exception-2.0 AND GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-2.0-or-later WITH GNU-compiler-exception AND MIT
# Do not provide URL for snapshots as the file lasts there only for 2 days.
# ftp://sourceware.org/pub/gdb/releases/FIXME{tarname}.tar.xz
Source: https://sourceware.org/pub/gdb/releases/%{tarname}.tar.xz
URL: https://gnu.org/software/gdb/

# For our convenience
%global gdb_src %{tarname}
%global gdb_build build-%{_target_platform}
%if 0%{?_build_minimal}
  %global gdb_build_minimal %{gdb_build}-minimal
%endif

# error: Installed (but unpackaged) file(s) found: /usr/lib/debug/usr/bin/gdb-gdb.py
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/PBOJDOFMWTRV3ZOKNV5HN7IBX5EPHDHF/
%undefine _debuginfo_subpackages

# For DTS RHEL<=7 GDB it is better to use none than a Requires dependency.
%if 0%{!?rhel:1}
Recommends: dnf-command(debuginfo-install)
%endif

%if 0%{!?scl:1}
Summary: A GNU source-level debugger for C, C++, Fortran, Go and other languages
Requires: gdb-headless%{?_isa} = %{version}-%{release}

%description
GDB, the GNU debugger, allows you to debug programs written in C, C++,
Fortran, Go, and other languages, by executing them in a controlled
fashion and printing their data.

If you want to use GDB for development purposes, you should install
the 'gdb' package which will install 'gdb-headless' and possibly other
useful packages too.

%package headless

# gdb-add-index also uses 'readelf' and 'objcopy', both of which are
# in the binutils package.  (BZ 2275274)
Requires: binutils
%endif
# endif !scl

Summary: A GNU source-level debugger for C, C++, Fortran, Go and other languages

%ifarch %{arm} riscv64
  %global have_inproctrace 0
%else
  %global have_inproctrace 1
%endif

# https://fedorahosted.org/fpc/ticket/43 https://fedorahosted.org/fpc/ticket/109
Provides: bundled(libiberty) = %{snapsrc}
Provides: bundled(gnulib) = %{snapgnulib}
# The libraries in the top-level directory (libbfd, libopcodes,
# libctf) are covered by the "bundled(binutils)" below.  See ticket
# #109, as mentioned above.
Provides: bundled(binutils) = %{snapsrc}
# https://fedorahosted.org/fpc/ticket/130
Provides: bundled(md5-gcc) = %{snapsrc}

# https://fedoraproject.org/wiki/Packaging:Guidelines#BuildRequires_and_.25.7B_isa.7D
%if 0%{?_with_buildisa:1} || 0%{?_with_testsuite:1}
  %global buildisa %{?_isa}
%else
  %global buildisa %{nil}
%endif

# https://bugzilla.redhat.com/show_bug.cgi?id=1209492
Recommends: default-yama-scope

# rpm-suggestions.py needs to import rpm which is found in python3-rpm.
Recommends: python3-rpm

BuildRequires: gcc-c++

# GDB patches have the format `gdb-<version>-bz<red-hat-bz-#>-<desc>.patch'.
# They should be created using patch level 1: diff -up ./gdb (or gdb-6.3/gdb).

#=
#push=Should be pushed upstream.
#fedora=Should stay as a Fedora patch.
#fedoratest=Keep it in Fedora only as a regression test safety.

# Cleanup any leftover testsuite processes as it may stuck mock(1) builds.
#=push+jan
Source2: gdb-orphanripper.c

# /etc/gdbinit (from Debian but with Fedora compliant location).
#=fedora
Source4: gdbinit

# Include the auto-generated file containing the "Patch:" directives.
# See README.local-patches for more details.
# Check distro name is included in the version output.
Patch001: gdb-test-show-version.patch

# Update gdb-add-index.sh such that, when the GDB environment
# variable is not set, the script is smarter than just looking for
# 'gdb' in the $PATH.
#
# The actual search order is now: /usr/bin/gdb.minimal, gdb (in the
# $PATH), then /usr/libexec/gdb.
#
# For the rationale of looking for gdb.minimal see:
#
#   https://fedoraproject.org/wiki/Changes/Minimal_GDB_in_buildroot
#
#=fedora
Patch002: gdb-add-index.patch

# Not a backport.  Add a new script which hooks into GDB and suggests
# RPMs to install when GDB finds an objfile with no debug info.
Patch003: gdb-rpm-suggestion-script.patch

# Backport Guinevere Larsen's build warning fixes (RH BZ 2424325).
Patch004: gdb-rhbz2424325-c23-const-build-warnings.patch

# Backport Keith Seitz's C23 const-correctness fixes (pending upstream review).
# Mailing list: https://sourceware.org/pipermail/binutils/2026-January/...
# Posted 2026-01-07, not yet approved.
Patch005: gdb-rhbz2424325-c23-more-const-fixes.patch

# Backport Tom de Vries fix regarding implicit lambda captures
# (RH BZ 2424325).
Patch006: gdb-rhbz2424325-c++20-implicit-lambda-capture.patch

# Backport of upstream commit 70b66cf338b14336 to address RHBZ
# 2402580.  This backport can be dropped when rebasing to GDB 18.
# There were some moderate merge conflicts which needed resolving
# when backporting this fix.
Patch007: gdb-rhbz2403580-misplaced-symtabs.patch

# Backport of three upstream patches.  The first two relate to index
# generation, while the third relates to symbol lookup, but is needed
# so that the tests from the earlier two patches will pass.
#
# These backports will all drop out when rebasing onto GDB 18.
Patch008: gdb-index-generation-fixes.patch

# Backport of upstream commit f08ffbbf2691bad2d5df660ee644647687775f0c
# Can be dropped on a rebase to gdb 17.2 or 18.1
Patch009: gdb-rhbz2435950-skip-revert.patch

# Backport of upstream commit c1da013915e from Kevin Buettner
# (RHBZ 2413405).
Patch010: gdb-rhbz2413405-gcore-unreadable-pages.patch

# Backport of upstream commit d2cc16cd7fc from Jan Vrany fixing
# FAILs in gdb.base/fileio.exp caused by macro expansion of path
# components (e.g. "linux") in OUTDIR.
Patch011: gdb-fileio-test-fixes.patch

BuildRequires: readline-devel%{buildisa} >= 7.0
BuildRequires: ncurses-devel%{buildisa} texinfo gettext flex bison
BuildRequires: expat-devel%{buildisa}
# gdb/minidebug.c uses the xz library to handle compressed debuginfo.
BuildRequires: xz-devel%{buildisa}
# dlopen() no longer makes rpm-libsFIXME{?_isa} (it's .so) a mandatory dependency.
BuildRequires: rpm-devel%{buildisa}
BuildRequires: zlib-devel%{buildisa} libselinux-devel%{buildisa}
%if 0%{!?_without_python:1}
  %global __python %{__python3}
BuildRequires: python3-devel%{buildisa}
%endif
# gdb-doc in PDF, see: https://bugzilla.redhat.com/show_bug.cgi?id=919891#c10
BuildRequires: texinfo-tex
BuildRequires: texlive-collection-latexrecommended
# Permit rebuilding *.[0-9] files even if they are distributed in gdb-*.tar:
BuildRequires: /usr/bin/pod2man
BuildRequires: libbabeltrace-devel%{buildisa}
%if %{defined use_guile}
    %if 0%{!?rhel:1}
BuildRequires: guile22-devel%{buildisa}
    %endif
    # Guile is only supported prior to RHEL9, where it was called "guile".
    %if 0%{?rhel:1} && 0%{?rhel} < 9
BuildRequires: guile-devel%{buildisa}
    %endif
%endif

# Add support for Intel Processor Trace on eligible architectures.
%global have_libipt 0
%ifarch %{ix86} x86_64
%global have_libipt 1
BuildRequires: libipt-devel%{buildisa}
%endif

# See https://bugzilla.redhat.com/show_bug.cgi?id=1593280
# DTS RHEL-6 has mpfr-2 while GDB requires mpfr-3 on RHEL-7, RHEL-8, and
# Fedora < 32, and mpfr-4 on Fedora 32+ and RHEL-9+.
BuildRequires: mpfr-devel%{buildisa}
BuildRequires: source-highlight-devel
%if 0%{!?rhel:1}
BuildRequires: xxhash-devel
%endif

# Include debuginfod support.
BuildRequires: elfutils-debuginfod-client-devel

# Workaround for missing boost-devel dependency (rhbz 1718480)
BuildRequires: boost-devel

%if 0%{?_with_testsuite:1}

# Ensure the devel libraries are installed for both multilib arches.
%global bits_local %{?_isa}
%global bits_other %{?_isa}
%ifarch ppc
  %global bits_other (%{__isa_name}-64)
%endif

%ifarch x86_64
  %if 0%{?fedora:1} || 0%{?rhel} < 10
    %global bits_other (%{__isa_name}-32)
  %endif
%endif

BuildRequires: sharutils dejagnu

# Test supported SCL toolchain components.
BuildRequires: %{?scl_testing_prefix}gcc %{?scl_testing_prefix}gcc-c++ %{?scl_testing_prefix}gcc-gfortran

# Fedora supports Objective C.
%if 0%{!?rhel:1}
BuildRequires: gcc-objc
%endif

BuildRequires: systemtap-sdt-devel
BuildRequires: opencl-headers ocl-icd-devel%{bits_local} ocl-icd-devel%{bits_other}

%if 0%{!?rhel:1}
BuildRequires: gcc-go
BuildRequires: libgo-devel%{bits_local} libgo-devel%{bits_other}
%endif

%if 0%{!?rhel:1}
  %ifnarch s390x
# Fedora s390x does not support fpc.
BuildRequires: fpc
  %endif
%endif

%if 0%{!?rhel:1}
BuildRequires: gcc-gnat
BuildRequires: libgnat%{bits_local} libgnat%{bits_other}
%endif
BuildRequires: glibc-devel%{bits_local} glibc-devel%{bits_other}
BuildRequires: libgcc%{bits_local} libgcc%{bits_other}
BuildRequires: libgfortran%{bits_local} libgfortran%{bits_other}
# libstdc++-devel of matching bits is required only for g++ -static.
BuildRequires: libstdc++%{bits_local} libstdc++%{bits_other}
%ifarch %{ix86} x86_64
BuildRequires: libquadmath%{bits_local} libquadmath%{bits_other}
%endif
# multilib glibc-static is open Bug 488472:
%if 0%{?rhel:1}
BuildRequires: glibc-static%{bits_other}
%endif
BuildRequires: valgrind%{bits_local} valgrind%{bits_other}
BuildRequires: xz
BuildRequires: rust
BuildRequires: elfutils-debuginfod
%endif
# endif _with_testsuite
BuildRequires: make gmp-devel

%{?scl:Requires:%scl_runtime}

# FIXME: The text needs to be duplicated to prevent 2 empty heading lines.
%if 0%{!?scl:1}
%description headless
GDB, the GNU debugger, allows you to debug programs written in C, C++,
Java, and other languages, by executing them in a controlled fashion
and printing their data.
%else
%description
GDB, the GNU debugger, allows you to debug programs written in C, C++,
Java, and other languages, by executing them in a controlled fashion
and printing their data.
%endif

%if 0%{?_build_minimal}
%package minimal
Summary: A GNU source-level debugger for C, C++, Fortran, Go and other languages (minimal version)
# gdb-add-index is shared with gdb-headless and it must be from same version
Conflicts: %{name}-headless < %{version}-%{release}
Conflicts: %{name}-headless > %{version}-%{release}

%description minimal
GDB, the GNU debugger, allows you to debug programs written in C, C++,
Fortran, Go, and other languages, by executing them in a controlled
fashion and printing their data.

This package provides a minimal version of GDB, tailored to be used by
the Fedora buildroot.  It should probably not be used by end users.
%endif
# endif _build_minimal

%package gdbserver
Summary: A standalone server for GDB (the GNU source-level debugger)

%description gdbserver
GDB, the GNU debugger, allows you to debug programs written in C, C++,
Fortran, Go, and other languages, by executing them in a controlled
fashion and printing their data.

This package provides a program that allows you to run GDB on a different
machine than the one which is running the program being debugged.

%package doc
Summary: Documentation for GDB (the GNU source-level debugger)
License: GFDL-1.3-or-later
BuildArch: noarch
%if 0%{?scl:1}
# As of F-28, packages won't need to call /sbin/install-info by hand
# anymore.  We make an exception for DTS here.
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/MP2QVJZBOJZEOQO2G7UB2HLXKXYPF2G5/
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info
%endif

%description doc
GDB, the GNU debugger, allows you to debug programs written in C, C++,
Java, and other languages, by executing them in a controlled fashion
and printing their data.

This package provides INFO, HTML and PDF user manual for GDB.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{gdb_src}

# Files have `# <number> <file>' statements breaking VPATH / find-debuginfo.sh .
(cd gdb;rm -fv $(perl -pe 's/\\\n/ /' <Makefile.in|sed -n 's/^YYFILES = //p'))

# *.info* is needlessly split in the distro tar; also it would not get used as
# we build in GDB_BUILD, just to be sure.
find -name "*.info*"|xargs rm -f

# Apply patches defined on _gdb.spec.Patch.include

# Include the auto-generated patch directives.
# See README.local-patches for more details.
%patch -p1 -P001
%patch -p1 -P002
%patch -p1 -P003
%patch -p1 -P004
%patch -p1 -P005
%patch -p1 -P006
%patch -p1 -P007
%patch -p1 -P008
%patch -p1 -P009
%patch -p1 -P010
%patch -p1 -P011

find -name "*.orig" | xargs rm -f
! find -name "*.rej" # Should not happen.

# In the past a distro name prefix was added to the version string in
# version.in.
#
# However, placing text at the start of version.in can cause problems;
# GDB will have a version string that starts with text rather than a
# number as is the case with upstream GDB, and for most (all?) other
# distros.
#
# GDB's version string is exposed to users as part of the Python API,
# and it is not uncommon for users to try and grok the version number
# from this string.  Having Fedora/RHEL GDB not start with the major
# version number can be unexpected, and might cause tools/script that
# work for other builds of GDB to fail with Fedora/RHEL GDB.
#
# So, we switched to use the more standard --with-pkgversion configure
# option.  This ensures the distro name is still included in the 'gdb
# --version' output, but the text is no longer part of the string
# exposed in the Python API.
#
# Unfortunately, for RHEL the dist_name macro is not defined.  At
# least not on RHEL 9 or earlier.  So, if dist_name is not defined,
# but the rhel macro is, then we use a hard-coded RHEL appropriate
# string.
#
# FIXME: It would be nice to rewrite this using elif, but this is not
# supported on older (pre 9) RHEL systems.

%if 0%{?dist_name:1}
  %global pkgversion_configure_flag --with-pkgversion=%{dist_name}
%else
  %if 0%{?fedora:1}
    %global pkgversion_configure_flag --with-pkgversion=Fedora Linux
  %endif

  %if 0%{?rhel:1}
    %global pkgversion_configure_flag --with-pkgversion=Red Hat Enterprise Linux
  %endif
%endif

# Change the version that gets printed by GDB.  The 'version' here is
# usually the same as the original upstream version on which we are
# based.  The 'release' is new information we're adding and identifies
# the modifications we've made to upstream.
cat > gdb/version.in << _FOO
%{?version_prefix:%version_prefix }%{version}-%{release}
_FOO

# Remove the info and other generated files added by the FSF release
# process.
rm -f libdecnumber/gstdint.h
rm -f bfd/doc/*.info
rm -f bfd/doc/*.info-*
rm -f gdb/doc/*.info
rm -f gdb/doc/*.info-*

mv -f readline/readline/doc readline-doc
rm -rf readline/readline/*
mv -f readline-doc readline/readline/doc

rm -rf zlib texinfo

%build

# A set of common GDB configure flags, which are used for both minimal
# and non-minimal compilations.
COMMON_GDB_CONFIGURE_FLAGS="\
        --prefix=%{_prefix}                                     \
        --libdir=%{_libdir}                                     \
        --sysconfdir=%{_sysconfdir}                             \
        --mandir=%{_mandir}                                     \
        --infodir=%{_infodir}                                   \
        --with-gdb-datadir=%{_datadir}/gdb                      \
        --enable-gdb-build-warnings=,-Wno-unused,-Wno-deprecated-declarations,-Wno-unused-function,-Wno-stringop-overflow\
%ifarch %{ix86}
,-Wno-format-overflow\
%endif
        --enable-build-with-cxx                                 \
%ifnarch %{ix86} alpha ppc s390 s390x x86_64 ppc64 ppc64le %{arm} aarch64 riscv64
        --disable-werror                                        \
%else
        --enable-werror                                         \
%endif
        --with-separate-debug-dir=/usr/lib/debug                \
        --disable-sim                                           \
        --disable-rpath                                         \
        --without-stage1-ldflags                                \
        --disable-libmcheck                                     \
        --with-system-readline                                  \
        --without-libunwind                                     \
        --enable-64-bit-bfd                                     \
        --with-system-zlib                                      \
        --with-lzma                                             \
        --with-debuginfod                                       \
%if 0%{?rhel:1}
        --disable-libctf                                        \
%endif
        --disable-gdb-compile
"

# The base set of targets that Fedora and RHEL support.  These are the
# targets that every GDB build, regardless of host architecture,
# supports debugging.  This means that these targets can be used as
# remote debug targets.
ENABLED_TARGETS="aarch64-linux-gnu,powerpc-linux-gnu,riscv64-linux-gnu,s390-linux-gnu,x86_64-redhat-linux-gnu"

# Fedora, and older RHEL also have 32-bit ARM support.
%if 0%{?fedora:1} || (0%{?rhel:1} && 0%{?rhel} < 10)
ENABLED_TARGETS="$ENABLED_TARGETS,arm-linux-gnu"
%endif

# Identify the build directory with the version of gdb as well as the
# architecture, to allow for mutliple versions to be installed and
# built.
# Initially we're in the GDB_SRC directory.

for fprofile in %{?_with_profile:-fprofile} ""
do

# We will first build the minimal version of GDB.
%if 0%{?_build_minimal}
mkdir %{gdb_build_minimal}$fprofile
cd %{gdb_build_minimal}$fprofile

# The configure flags we will use when building gdb-minimal.
GDB_MINIMAL_CONFIGURE_FLAGS="\
    --without-babeltrace \
    --without-expat \
    --disable-tui \
    --without-python \
    --without-guile \
    --disable-inprocess-agent \
    --without-intel-pt \
    --disable-unit-tests \
    --disable-source-highlight"

# Populate CFLAGS, LDFLAGS, CC, CXX, etc.
%set_build_flags
CFLAGS="$CFLAGS %{?_with_asan:-fsanitize=address}"
LDFLAGS="$LDFLAGS %{?_with_asan:-fsanitize=address}"
CXXFLAGS="$CXXFLAGS %{?_with_asan:-fsanitize=address}"

# --htmldir and --pdfdir are not used as they are used from GDB_BUILD.
../configure                                                    \
        ${COMMON_GDB_CONFIGURE_FLAGS}                           \
        ${GDB_MINIMAL_CONFIGURE_FLAGS}                          \
%if 0%{?pkgversion_configure_flag:1}
        "%{pkgversion_configure_flag}"                          \
%endif
        --with-auto-load-dir='$debugdir:$datadir/auto-load%{?scl::%{_root_datadir}/gdb/auto-load}'      \
        --with-auto-load-safe-path='$debugdir:$datadir/auto-load%{?scl::%{_root_datadir}/gdb/auto-load}'        \
        --enable-targets=${ENABLED_TARGETS}     \
        %{_target_platform}

# Prepare gdb/config.h first.
%make_build CFLAGS="$CFLAGS $FPROFILE_CFLAGS" LDFLAGS="$LDFLAGS $FPROFILE_CFLAGS" V=1 maybe-configure-gdb
perl -i.relocatable -pe 's/^(D\[".*_RELOCATABLE"\]=" )1(")$/${1}0$2/' gdb/config.status

%make_build CFLAGS="$CFLAGS $FPROFILE_CFLAGS" LDFLAGS="$LDFLAGS $FPROFILE_CFLAGS" V=1

cd ..
%endif
# endif _build_minimal

# Now we build the full GDB.
mkdir %{gdb_build}$fprofile
cd %{gdb_build}$fprofile

export CFLAGS="$RPM_OPT_FLAGS %{?_with_asan:-fsanitize=address} -DDNF_DEBUGINFO_INSTALL"
export LDFLAGS="%{?__global_ldflags} %{?_with_asan:-fsanitize=address}"
export CXXFLAGS="$CFLAGS"

# The configure flags we will use when building the full GDB.
GDB_FULL_CONFIGURE_FLAGS="\
        --with-system-gdbinit=%{_sysconfdir}/gdbinit            \
        --with-babeltrace                                       \
        --with-expat                                            \
$(: ppc64 host build crashes on ppc variant of libexpat.so )    \
        --without-libexpat-prefix                               \
        --enable-tui                                            \
%if 0%{!?_without_python:1}
        --with-python=%{__python}                               \
%else
        --without-python                                        \
%endif
%if %{defined use_guile}
        --with-guile                                            \
%else
        --without-guile                                         \
%endif
%if %{have_inproctrace}
        --enable-inprocess-agent                                \
%else
        --disable-inprocess-agent                               \
%endif
%if %{have_libipt}
        --with-intel-pt                                         \
%else
        --without-intel-pt                                      \
%endif
%if 0%{!?rhel:1}
        --with-xxhash                                           \
%endif
        --enable-unit-tests"

# --htmldir and --pdfdir are not used as they are used from GDB_BUILD.
../configure                                                    \
        ${COMMON_GDB_CONFIGURE_FLAGS}                           \
        ${GDB_FULL_CONFIGURE_FLAGS}                             \
%if 0%{?pkgversion_configure_flag:1}
        "%{pkgversion_configure_flag}"                          \
%endif
        --with-auto-load-dir='$debugdir:$datadir/auto-load%{?scl::%{_root_datadir}/gdb/auto-load}'      \
        --with-auto-load-safe-path='$debugdir:$datadir/auto-load%{?scl::%{_root_datadir}/gdb/auto-load}'        \
        --enable-targets=${ENABLED_TARGETS}     \
        %{_target_platform}

if [ -z "%{!?_with_profile:no}" ]
then
  # Run all the configure tests being incompatible with $FPROFILE_CFLAGS.
  %make_build configure-host configure-target
  %make_build clean

  # Workaround -fprofile-use:
  # linux-x86-low.c:2225: Error: symbol `start_i386_goto' is already defined
  %make_build -C gdb/gdbserver linux-x86-low.o
fi

# Global CFLAGS would fail on:
# conftest.c:1:1: error: coverage mismatch for function 'main' while reading counter 'arcs'
if [ "$fprofile" = "-fprofile" ]
then
  FPROFILE_CFLAGS='-fprofile-generate'
elif [ -z "%{!?_with_profile:no}" ]
then
  FPROFILE_CFLAGS='-fprofile-use'
  # We cannot use -fprofile-dir as the bare filenames clash.
  (cd ../${builddir}-fprofile;
   # It was 333 on x86_64.
   test $(find -name "*.gcda"|wc -l) -gt 300
   find -name "*.gcda" | while read -r i
   do
     ln $i ../${builddir}/$i
   done
  )
else
  FPROFILE_CFLAGS=""
fi

# Prepare gdb/config.h first.
%make_build CFLAGS="$CFLAGS $FPROFILE_CFLAGS" LDFLAGS="$LDFLAGS $FPROFILE_CFLAGS" V=1 maybe-configure-gdb
perl -i.relocatable -pe 's/^(D\[".*_RELOCATABLE"\]=" )1(")$/${1}0$2/' gdb/config.status

%make_build CFLAGS="$CFLAGS $FPROFILE_CFLAGS" LDFLAGS="$LDFLAGS $FPROFILE_CFLAGS" V=1

! grep '_RELOCATABLE.*1' gdb/config.h

if [ "$fprofile" = "-fprofile" ]
then
  cd gdb
  cp -p gdb gdb-withindex
  PATH="$PWD:$PATH" sh ../../gdb/gdb-add-index $PWD/gdb-withindex
  ./gdb -nx -ex q ./gdb-withindex
  ./gdb -nx -readnow -ex q ./gdb-withindex
  cd ..
fi

cd ..

done  # fprofile

cd %{gdb_build}

%make_build \
     -C gdb/doc {gdb,annotate}{.info,/index.html,.pdf} MAKEHTMLFLAGS=--no-split MAKEINFOFLAGS=--no-split V=1

# Copy the <sourcetree>/gdb/NEWS file to the directory above it.
cp $RPM_BUILD_DIR/%{gdb_src}/gdb/NEWS $RPM_BUILD_DIR/%{gdb_src}

%check
# Initially we're in the GDB_SRC directory.
cd %{gdb_build}

# We always run the unittests.
(cd gdb; make run GDBFLAGS='-batch -ex "maintenance selftest"')

%if 0%{!?_with_testsuite:1}
echo ====================TESTSUITE DISABLED=========================
%else
echo ====================TESTING=========================
cd gdb
gcc -o ./orphanripper %{SOURCE2} -Wall -lutil -ggdb2
# Need to use a single --ignore option, second use overrides first.
# No `%{?_smp_mflags}' here as it may race.
# WARNING: can't generate a core file - core tests suppressed - check ulimit
# "readline-overflow.exp" - Testcase is broken, functionality is OK.
(
  # ULIMIT required for `gdb.base/auxv.exp'.
  ulimit -H -c
  ulimit -c unlimited || :

  # Setup $CHECK as `check//unix/' or `check//unix/-m64' for explicit bitsize.
  # Never use two different bitsizes as it fails on ppc64.
  echo 'int main (void) { return 0; }' >biarch.c
  CHECK=""
  for BI in -m64 -m32 -m31 ""
  do
    # Do not use size-less options if any of the sizes works.
    # On ia64 there is no -m64 flag while we must not leave a bare `check' here
    # as it would switch over some testing scripts to the backward compatibility
    # mode: when `make check' was executed from inside the testsuite/ directory.
    if [ -z "$BI" -a -n "$CHECK" ];then
      continue
    fi
    # Do not use $RPM_OPT_FLAGS as the other non-size options will not be used
    # in the real run of the testsuite.
    if ! gcc $BI -o biarch biarch.c
    then
      continue
    fi
    CHECK="$CHECK check//unix/$BI check//native-gdbserver/$BI check//native-extended-gdbserver/$BI"
  done
  # Do not try -m64 inferiors for -m32 GDB as it cannot handle inferiors larger
  # than itself.
  # s390 -m31 still uses the standard ELF32 binary format.
  gcc $RPM_OPT_FLAGS -o biarch biarch.c
  RPM_SIZE="$(file ./biarch|sed -n 's/^.*: ELF \(32\|64\)-bit .*$/\1/p')"
  if [ "$RPM_SIZE" != "64" ]
  then
    CHECK="$(echo " $CHECK "|sed 's#check//unix/-m64 check//native-gdbserver/-m64 check//native-extended-gdbserver/-m64# #')"
  fi

  # Disable some problematic testcases.
  # RUNTESTFLAGS='--ignore ...' is not used below as it gets separated by the
  # `check//...' target spawn and too much escaping there would be dense.
  for test in                           \
    gdb.base/readline-overflow.exp      \
    gdb.base/bigcore.exp                \
%if 0%{?rhel} < 7 
    gdb.base/gnu-debugdata.exp          \
    gdb.base/access-mem-running.exp     \
    gdb.threads/access-mem-running-thread-exit.exp \
%endif
  ; do
    mv -f ../../gdb/testsuite/$test ../gdb/testsuite/$test-DISABLED || :
  done

  # Run all the scheduled testsuite runs also in the PIE mode.
  # See also: gdb-runtest-pie-override.exp
  ###CHECK="$(echo $CHECK|sed 's#check//unix/[^ ]*#& &/-fPIC/-pie#g')"

TESTS=""
%if 0%{?tests:1}
  for test in %{tests}; do
    TESTS="${TESTS:+$TESTS }$test"
  done
%endif
  ./orphanripper make %{?_smp_mflags} -k $CHECK TESTS="$TESTS" || :
)
for t in sum log
do
  for file in testsuite*/gdb.$t
  do
    suffix="${file#testsuite}"
    suffix="${suffix%/gdb.$t}"
    ln $file gdb-%{_target_platform}$suffix.$t || :
  done
done
# `tar | bzip2 | uuencode' may have some piping problems in Brew.
tar cjf gdb-%{_target_platform}.tar.bz2 gdb-%{_target_platform}*.{sum,log}
uuencode gdb-%{_target_platform}.tar.bz2 gdb-%{_target_platform}.tar.bz2
cd ../..
echo ====================TESTING END=====================
%endif
# endif _testsuite

%install
# Initially we're in the GDB_SRC directory.
%if 0%{?_build_minimal}
cd %{gdb_build_minimal}
rm -rf $RPM_BUILD_ROOT

%make_install %{?_smp_mflags}

# Delete everything except the 'gdb' binary, and then rename it to
# 'gdb.minimal'.
rm -rfv $RPM_BUILD_ROOT%{_prefix}/{include,lib*,share}
rm -fv $RPM_BUILD_ROOT%{_bindir}/{gcore,gdbserver,gstack,gdb-add-index}
mv $RPM_BUILD_ROOT%{_bindir}/gdb $RPM_BUILD_ROOT%{_bindir}/gdb.minimal

cd ..
%endif
# endif _build_minimal

# Install the full build.

cd %{gdb_build}

# We must remove the $RPM_BUILD_ROOT directory ourselves if we're not
# building gdb-minimal.
%if 0%{!?_build_minimal}
rm -rf $RPM_BUILD_ROOT
%endif

%make_install %{?_smp_mflags}

%if 0%{!?scl:1}
mkdir -p $RPM_BUILD_ROOT%{_prefix}/libexec
mv -f $RPM_BUILD_ROOT%{_bindir}/gdb $RPM_BUILD_ROOT%{_prefix}/libexec/gdb
ln -s -r $RPM_BUILD_ROOT%{_prefix}/libexec/gdb  $RPM_BUILD_ROOT%{_bindir}/gdb
%endif

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/gdbinit.d
touch -r %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/gdbinit.d
sed 's#%%{_sysconfdir}#%{_sysconfdir}#g' <%{SOURCE4} >$RPM_BUILD_ROOT%{_sysconfdir}/gdbinit
touch -r %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/gdbinit

for i in `find $RPM_BUILD_ROOT%{_datadir}/gdb/python/gdb -name "*.py"`
do
  # Files could be also patched getting the current time.
  touch -r $RPM_BUILD_DIR/%{gdb_src}/gdb/version.in $i
done

%if 0%{?_enable_debug_packages:1} && 0%{!?_without_python:1}
mkdir -p $RPM_BUILD_ROOT/usr/lib/debug%{_bindir}
cp -p ./gdb/gdb-gdb.py $RPM_BUILD_ROOT/usr/lib/debug%{_bindir}/
for pyo in "" "-O";do
  # RHEL-5: AttributeError: 'module' object has no attribute 'compile_file'
  %{__python} $pyo -c 'import compileall, re, sys; sys.exit (not compileall.compile_dir("'"$RPM_BUILD_ROOT/usr/lib/debug%{_bindir}"'", 1, "'"/usr/lib/debug%{_bindir}"'"))'
done
%endif

# Compile python files
%if 0%{!?_without_python:1}
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/gdb/python/gdb

# BZ 999645: /usr/share/gdb/auto-load/ needs filesystem symlinks
for i in $(echo bin lib $(basename %{_libdir}) sbin|tr ' ' '\n'|sort -u);do
  # mkdir to satisfy dangling symlinks build check.
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/gdb/auto-load/%{_root_prefix}/$i
  ln -s $(echo %{_root_prefix}|sed 's#^/*##')/$i \
        $RPM_BUILD_ROOT%{_datadir}/gdb/auto-load/$i
done
for i in `find $RPM_BUILD_ROOT%{_datadir}/gdb -name "*.py"`; do
  # Files are installed by install(1) not preserving the timestamps.
  touch -r $RPM_BUILD_DIR/%{gdb_src}/gdb/version.in $i
done
%endif

# Create the folder where GDB expects to find custom JIT readers.
mkdir -p %{buildroot}%{_libdir}/gdb

# Remove the files that are part of a gdb build but that are owned and
# provided by other packages.
# These are part of binutils

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/
rm -f $RPM_BUILD_ROOT%{_infodir}/bfd*
rm -f $RPM_BUILD_ROOT%{_infodir}/standard*
rm -f $RPM_BUILD_ROOT%{_infodir}/configure*
rm -f $RPM_BUILD_ROOT%{_infodir}/sframe-spec*
# Just exclude the header files in the top directory, and don't exclude
# the gdb/ directory, as it contains jit-reader.h.
rm -rf $RPM_BUILD_ROOT%{_includedir}/*.h
rm -rf $RPM_BUILD_ROOT/%{_libdir}/lib{bfd*,opcodes*,iberty*,ctf*,sframe*}

# pstack obsoletion

ln -s gstack.1 $RPM_BUILD_ROOT%{_mandir}/man1/pstack.1
ln -s gstack $RPM_BUILD_ROOT%{_bindir}/pstack

# Packaged GDB is not a cross-target one.
(cd $RPM_BUILD_ROOT%{_datadir}/gdb/syscalls
 rm -f mips*.xml
 rm -f sparc*.xml
%ifnarch x86_64
 rm -f amd64-linux.xml
%endif
%ifnarch %{ix86} x86_64
 rm -f i386-linux.xml
%endif
)

# Documentation only for development.
rm -f $RPM_BUILD_ROOT%{_infodir}/gdbint*
rm -f $RPM_BUILD_ROOT%{_infodir}/stabs*
rm -f $RPM_BUILD_ROOT%{_infodir}/ctf-spec*

# Delete this too because the dir file will be updated at rpm install time.
# We don't want a gdb specific one overwriting the system wide one.

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

# These files are unrelated to Fedora Linux.
rm -f $RPM_BUILD_ROOT%{_datadir}/gdb/system-gdbinit/elinos.py
rm -f $RPM_BUILD_ROOT%{_datadir}/gdb/system-gdbinit/wrs-linux.py
rmdir $RPM_BUILD_ROOT%{_datadir}/gdb/system-gdbinit

%files
# File must begin with "/": {GFDL,COPYING3,COPYING,COPYING.LIB,COPYING3.LIB}
%license COPYING3 COPYING COPYING.LIB COPYING3.LIB
%doc README NEWS
%{_bindir}/gdb
%{_bindir}/gcore
%{_mandir}/*/gcore.1*
%{_bindir}/gstack
%{_mandir}/*/gstack.1*
%{_bindir}/pstack
%{_mandir}/*/pstack.1*
# Provide gdb/jit-reader.h so that users are able to write their own GDB JIT
# plugins.
%{_includedir}/gdb
# Export the folder where JIT readers should be placed.
%dir %{_libdir}/gdb
%if 0%{!?scl:1}
%files headless
%{_prefix}/libexec/gdb
%endif
%config(noreplace) %{_sysconfdir}/gdbinit
%{_mandir}/*/gdb.1*
%{_sysconfdir}/gdbinit.d
%{_mandir}/*/gdbinit.5*
%{_bindir}/gdb-add-index
%{_mandir}/*/gdb-add-index.1*
%{_datadir}/gdb

# don't include the files in include, they are part of binutils

%if 0%{?_build_minimal}
%files minimal
%{_bindir}/gdb.minimal
%{_bindir}/gdb-add-index
%endif

%files gdbserver
%{_bindir}/gdbserver
%{_mandir}/*/gdbserver.1*
%if %{have_inproctrace}
%{_libdir}/libinproctrace.so
%endif

%if 0%{!?_without_python:1}
# [rhel] Do not migrate /usr/share/gdb/auto-load/ with symlinks on RHELs.
%if 0%{!?rhel:1}
%pre
for i in $(echo bin lib $(basename %{_libdir}) sbin|tr ' ' '\n'|sort -u);do
  src="%{_datadir}/gdb/auto-load/$i"
  dst="%{_datadir}/gdb/auto-load/%{_root_prefix}/$i"
  if test -d $src -a ! -L $src;then
    if ! rmdir 2>/dev/null $src;then
      mv -n $src/* $dst/
      rmdir $src
    fi
  fi
done
%endif
%endif

%files doc
%doc %{gdb_build}/gdb/doc/{gdb,annotate}.{html,pdf}
%{_infodir}/annotate.info*
%{_infodir}/gdb.info*

%if 0%{?scl:1}
# As of F-28, packages won't need to call /sbin/install-info by hand
# anymore.  We make an exception for DTS here.
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/MP2QVJZBOJZEOQO2G7UB2HLXKXYPF2G5/

%post doc
# This step is part of the installation of the RPM. Not to be confused
# with the 'make install ' of the build (rpmbuild) process.

# For --excludedocs:
if [ -e %{_infodir}/gdb.info.gz ]
then
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/annotate.info.gz || :
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/gdb.info.gz || :
fi

%preun doc
if [ $1 = 0 ]
then
  # For --excludedocs:
  if [ -e %{_infodir}/gdb.info.gz ]
  then
    /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/annotate.info.gz || :
    /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/gdb.info.gz || :
  fi
fi
%endif
# endif scl

%changelog
* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 17.1-6
- Use HTTPS for upstream tarball (spectool has no FTP)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 17.1-5
- Prepare for Oreon 11 (RP1)
