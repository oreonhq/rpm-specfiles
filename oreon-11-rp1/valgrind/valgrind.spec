# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 8d54c717029106f1644aadaf802ab9692e53d93dd015cbd19e74190eba616bd7
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%{?scl:%scl_package valgrind}

Summary: Dynamic analysis tools to detect memory or thread bugs and profile
Name: %{?scl_prefix}valgrind
Version: 3.26.0
Release: 5%{?dist}
Epoch: 1

# This ignores licenses that are only found in the test or perf sources
# we only care about those license statements found in sources that end
# up in the binary packages. One piece of code for which we don't have
# a license specifier is in coregrind/m_main.c for some Hacker's Delight
# public domain code, which is only compiled into Darwin binaries, which
# we don't create. Also some subpackages have their own license tags.
License: GPL-3.0-or-later AND bzip2-1.0.6 AND (GPL-3.0-or-later AND LGPL-2.0-or-later) AND (GPL-3.0-or-later AND ISC) AND (GPL-3.0-or-later AND Unlicense) AND (GPL-3.0-or-later AND Zlib) AND (GPL-3.0-or-later WITH GCC-exception-2.0) AND (LGPL-2.0-or-later WITH GCC-exception-2.0) AND (GPL-3.0-or-later AND BSD-3-Clause) AND (GPL-3.0-or-later AND (MIT OR NCSA)) AND CMU-Mach AND (GPL-3.0-or-later AND X11 AND BSD-3-Clause) AND X11 AND (GPL-3.0-or-later AND LGPL-2.0-or-later) AND (GPL-2.0-or-later WITH Autoconf-exception-generic) AND (GPL-3.0-or-later WITH Autoconf-exception-generic-3.0) AND FSFULLR AND FSFAP AND FSFUL AND FSFULLRWD
URL: https://www.valgrind.org/

# Are we building for a Software Collection?
%{?scl:%global is_scl 1}
%{!?scl:%global is_scl 0}

# We never want the openmpi subpackage when building a software collecton.
# We always want it for fedora.
# We only want it for older rhel.
# And on fedora > 39 i386 dropped openmpi.
%if %{is_scl}
  %global build_openmpi 0
%else
  %if 0%{?fedora}
    %ifarch %{ix86}
      %global build_openmpi (%{?fedora} < 40)
    %else
      %global build_openmpi 1
    %endif
  %endif
  %if 0%{?rhel}
    %if 0%{?rhel} > 7
      %global build_openmpi 0
    %else
      %global build_openmpi 1
    %endif
  %endif
%endif

# We only want to build the valgrind-tools-devel package for Fedora proper
# as convenience. But not for DTS or RHEL.
%if %{is_scl}
  %global build_tools_devel 0
%else
  %if 0%{?rhel}
    %global build_tools_devel 0
  %else
    %global build_tools_devel 1
  %endif
%endif

# Whether to run the full regtest or only a limited set
# The full regtest includes gdb_server integration tests
# and experimental tools.
# Don't run them when creating scl, the gdb_server tests might hang.
%if %{is_scl}
  %global run_full_regtest 0
%else
  %global run_full_regtest 1
%endif

# Generating minisymtabs doesn't really work for the staticly linked
# tools. Note (below) that we don't strip the vgpreload libraries at all
# because valgrind might read and need the debuginfo in those (client)
# libraries for better error reporting and sometimes correctly unwinding.
# So those will already have their full symbol table.
%undefine _include_minidebuginfo

Source0: https://sourceware.org/pub/valgrind/valgrind-%{version}.tar.bz2

# Needs investigation and pushing upstream
Patch1: valgrind-3.9.0-cachegrind-improvements.patch

# Make ld.so supressions slightly less specific.
Patch2: valgrind-3.9.0-ldso-supp.patch

# Add some stack-protector
Patch3: valgrind-3.26.0-some-stack-protector.patch

# Add some -Wl,z,now.
Patch4: valgrind-3.26.0-some-Wl-z-now.patch

# VALGRIND_3_26_BRANCH patches
Patch5: 0001-Prepare-NEWS-for-branch-3.26-fixes.patch
Patch6: 0002-Bug-511972-valgrind-3.26.0-tests-fail-to-build-on-up.patch
Patch7: 0003-readlink-proc-self-exe-overwrites-buffer-beyond-its-.patch
Patch8: 0004-Linux-DRD-suppression-add-an-entry-for-__is_decorate.patch
Patch9: 0005-Linux-Helgrind-add-a-suppression-for-_dl_allocate_tl.patch
Patch10: 0006-Disable-linux-madvise-MADV_GUARD_INSTALL.patch
Patch11: 0007-Bug-514613-Unclosed-leak_summary-still_reachable-tag.patch
Patch12: 0008-Bug-514206-Assertion-sr_isError-sr-failed-mmap-fd-po.patch

# Refix for https://bugs.kde.org/show_bug.cgi?id=514613
Patch100: 0001-Refix-still_reachable-xml-closing-tag-and-add-testca.patch

BuildRequires: make
BuildRequires: glibc-devel

%if %{build_openmpi}
BuildRequires: openmpi-devel
%endif

%if %{run_full_regtest}
BuildRequires: gdb
%endif

# gdbserver_tests/filter_make_empty uses ps in test
BuildRequires: procps

# Some testcases require g++ to build
BuildRequires: gcc-c++

# check_headers_and_includes uses Getopt::Long
%if 0%{?fedora}
BuildRequires: perl-generators
%endif
BuildRequires: perl(Getopt::Long)

# We always autoreconf
BuildRequires: automake
BuildRequires: autoconf

# For make check validating the documentation
BuildRequires: docbook-dtds

# For testing debuginfod-find
%if 0%{?fedora} > 29 || 0%{?rhel} > 7
BuildRequires: elfutils-debuginfod
BuildRequires: elfutils-debuginfod-client
# For using debuginfod at runtime
Recommends: elfutils-debuginfod-client
%endif

# Optional subpackages
Recommends: %{?scl_prefix}valgrind-docs = %{epoch}:%{version}-%{release}
Recommends: %{?scl_prefix}valgrind-scripts = %{epoch}:%{version}-%{release}
Recommends: %{?scl_prefix}valgrind-gdb = %{epoch}:%{version}-%{release}

# For running the testsuite.
# Some of the python scripts require python 3.9+
BuildRequires: python3-devel

%{?scl:Requires:%scl_runtime}

# We could use %%valgrind_arches as defined in redhat-rpm-config
# But that is really for programs using valgrind, it defines the
# set of architectures that valgrind works correctly on.
ExclusiveArch: %{ix86} x86_64 ppc ppc64 ppc64le s390x armv7hl aarch64 riscv64

# Define valarch, the architecture name that valgrind uses
# And only_arch, the configure option to only build for that arch.
%ifarch %{ix86}
%define valarch x86
%define only_arch --enable-only32bit
%endif
%ifarch x86_64
%define valarch amd64
%define only_arch --enable-only64bit
%endif
%ifarch ppc
%define valarch ppc32
%define only_arch --enable-only32bit
%endif
%ifarch ppc64
%define valarch ppc64be
%define only_arch --enable-only64bit
%endif
%ifarch ppc64le
%define valarch ppc64le
%define only_arch --enable-only64bit
%endif
%ifarch s390x
%define valarch s390x
%define only_arch --enable-only64bit
%endif
%ifarch armv7hl
%define valarch arm
%define only_arch --enable-only32bit
%endif
%ifarch aarch64
%define valarch arm64
%define only_arch --enable-only64bit
%endif
%ifarch riscv64
%define valarch riscv64
%define only_arch --enable-only64bit
%endif

%description
Valgrind is an instrumentation framework for building dynamic analysis
tools. There are Valgrind tools that can automatically detect many
memory management and threading bugs, and profile your programs in
detail. You can also use Valgrind to build new tools. The Valgrind
distribution currently includes six production-quality tools: a memory
error detector (memcheck, the default tool), two thread error
detectors (helgrind and drd), a cache and branch-prediction profiler
(cachegrind), a call-graph generating cache and branch-prediction
profiler (callgrind), and a heap profiler (massif).

%package devel
Summary: Development files for valgrind aware programs
# This is really Hybrid-BSD
# https://fedoraproject.org/wiki/Licensing:BSD#Hybrid_BSD_(half_BSD,_half_zlib)
# But that doesnt have a SPDX identifier yet
# https://gitlab.com/fedora/legal/fedora-license-data/-/issues/422
License: bzip2-1.0.6
# These are just the header files, so strictly speaking you don't
# need valgrind itself unless you are testing your builds. This used
# to be a Requires, so people might depend on the package pulling in
# the core valgrind package, so make it at least a weak dependency.
Recommends: %{?scl_prefix}valgrind = %{epoch}:%{version}-%{release}

%description devel
Header files and libraries for development of valgrind aware programs.

%package docs
Summary: Documentation for valgrind tools, scripts and gdb integration
License: GFDL-1.2-or-later

%description docs
Documentation in html and pdf, plus man pages for valgrind tools and scripts.

%package scripts
Summary: Scripts for post-processing valgrind tool output
License: GPL-3.0-or-later AND (GPL-3.0-or-later OR MPL-2.0)
# Most scripts can be used as is for post-processing a valgrind tool run.
# But callgrind_control uses vgdb.
Recommends: %{?scl_prefix}valgrind-gdb = %{epoch}:%{version}-%{release}

%description scripts
Perl and Python scripts for post-processing valgrind tool output.

%package gdb
Summary: Tools for integrating valgrind and gdb
License: GPL-3.0-or-later
Requires: %{?scl_prefix}valgrind = %{epoch}:%{version}-%{release}
# vgdb can be used without gdb, just to control valgrind.
# But normally you use it together with both valgrind and gdb.
Recommends: gdb

%description gdb
Tools and support files for integrating valgrind and gdb.

%if %{build_tools_devel}
%package tools-devel
Summary: Development files for building valgrind tools.
Requires: %{?scl_prefix}valgrind-devel = %{epoch}:%{version}-%{release}
Provides: %{name}-static = %{epoch}:%{version}-%{release}

%description tools-devel
Header files and libraries for development of valgrind tools.
%endif

%if %{build_openmpi}
%package openmpi
Summary: OpenMPI support for valgrind
# See above, Hybrid-BSD like.
License: bzip2-1.0.6
Requires: %{?scl_prefix}valgrind = %{epoch}:%{version}-%{release}

%description openmpi
A wrapper library for debugging OpenMPI parallel programs with valgrind.
See the section on Debugging MPI Parallel Programs with Valgrind in the
Valgrind User Manual for details.
%endif

%prep
%oreon_verify_sources
%setup -q -n %{?scl:%{pkg_name}}%{!?scl:%{name}}-%{version}

%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p1

%patch -P100 -p1

%build
# LTO triggers undefined symbols in valgrind.  But valgrind has a
# --enable-lto configure time option that we will use instead.
%define _lto_cflags %{nil}

# Some patches (might) touch Makefile.am or configure.ac files.
# Just always autoreconf so we don't need patches to prebuild files.
./autogen.sh

%if %{build_openmpi}
%define mpiccpath %{!?scl:%{_libdir}}%{?scl:%{_root_libdir}}/openmpi/bin/mpicc
%else
# We explicitly don't want the libmpi wrapper. So make sure that configure
# doesn't pick some random mpi compiler that happens to be installed.
%define mpiccpath /bin/false
%endif

# Filter out "hardening" flags that don't make sense for valgrind.
# -fstack-protector just cannot work (valgrind would have to implement
# its own version since it doesn't link with glibc and handles stack
# setup itself). We patch some flags back in just for those helper
# programs where it does make sense.
#
# -Wl,-z,now doesn't make sense for static linked tools
# and would prevent using the vgpreload libraries on binaries that
# don't link themselves against libraries (like pthread) which symbols
# are needed (but only if the inferior itself would use them).
#
# -O2 doesn't work for the vgpreload libraries either. They are meant
# to not be optimized to show precisely what happened. valgrind adds
# -O2 itself wherever suitable.
#
# On ppc64[be] -fexceptions is troublesome.
# It might cause an undefined reference to `_Unwind_Resume'
# in libcoregrind-ppc64be-linux.a(libcoregrind_ppc64be_linux_a-readelf.o):
# In function `read_elf_symtab__ppc64be_linux.
#
# Also disable strict symbol checks because the vg_preload library
# will use hidden/undefined symbols from glibc like __libc_freeres.
%undefine _strict_symbol_defs_build

%ifarch ppc64
CFLAGS="`echo " %{optflags} " | sed 's/ -fstack-protector\([-a-z]*\) / / g;s/ -O2 / /g;s/ -fexceptions / /g;'`"
%else
CFLAGS="`echo " %{optflags} " | sed 's/ -fstack-protector\([-a-z]*\) / / g;s/ -O2 / /g;'`"
%endif
export CFLAGS

# Older Fedora/RHEL only had __global_ldflags.
# Even older didn't even have that (so we don't need to scrub them).
%if 0%{?build_ldflags:1}
LDFLAGS="`echo " %{build_ldflags} "    | sed 's/ -Wl,-z,now / / g;'`"
%else
%if 0%{?__global_ldflags:1}
LDFLAGS="`echo " %{__global_ldflags} " | sed 's/ -Wl,-z,now / / g;'`"
%endif
%endif
export LDFLAGS

%configure \
  --with-mpicc=%{mpiccpath} \
  %{only_arch} \
  GDB=%{_bindir}/gdb \
  --with-gdbscripts-dir=%{_datadir}/gdb/auto-load \
  --enable-lto

%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install
mkdir docs/installed
mv $RPM_BUILD_ROOT%{_datadir}/doc/valgrind/* docs/installed/
rm -f docs/installed/*.ps

# We want the MPI wrapper installed under the openmpi libdir so the script
# generating the MPI library requires picks them up and sets up the right
# openmpi libmpi.so requires. Install symlinks in the original/upstream
# location for backwards compatibility.
%if %{build_openmpi}
pushd $RPM_BUILD_ROOT%{_libdir}
mkdir -p openmpi/valgrind
cd valgrind
mv libmpiwrap-%{valarch}-linux.so ../openmpi/valgrind/
ln -s ../openmpi/valgrind/libmpiwrap-%{valarch}-linux.so
popd
%endif

%if %{build_tools_devel}
%ifarch %{ix86} x86_64
# To avoid multilib clashes in between i?86 and x86_64,
# tweak installed <valgrind/config.h> a little bit.
for i in HAVE_PTHREAD_CREATE_GLIBC_2_0 HAVE_PTRACE_GETREGS HAVE_AS_AMD64_FXSAVE64; do
  sed -i -e 's,^\(#define '$i' 1\|/\* #undef '$i' \*/\)$,#ifdef __x86_64__\n# define '$i' 1\n#endif,' \
    $RPM_BUILD_ROOT%{_includedir}/valgrind/config.h
done
%endif
%else
# Remove files we aren't going to package.
# See tools-devel files.
rm $RPM_BUILD_ROOT%{_includedir}/valgrind/config.h
rm $RPM_BUILD_ROOT%{_includedir}/valgrind/libvex*h
rm $RPM_BUILD_ROOT%{_includedir}/valgrind/pub_tool_*h
rm -rf $RPM_BUILD_ROOT%{_includedir}/valgrind/vki
rm $RPM_BUILD_ROOT%{_libdir}/valgrind/*.a
%endif

# We don't want debuginfo generated for the vgpreload libraries.
# Turn off execute bit so they aren't included in the debuginfo.list.
# We'll turn the execute bit on again in %%files.
chmod 644 $RPM_BUILD_ROOT%{_libexecdir}/valgrind/vgpreload*-%{valarch}-*so

%check
# Make sure some info about the system is in the build.log
# Add || true because rpm on copr EPEL6 acts weirdly and we don't want
# to break the build.
uname -a
rpm -q glibc gcc binutils || true
%if %{run_full_regtest}
rpm -q gdb || true
%endif

LD_SHOW_AUXV=1 /bin/true
cat /proc/cpuinfo

# Make sure a basic binary runs. There should be no errors.
./vg-in-place --error-exitcode=1 /bin/true --help

# Build the test files with the software collection compiler if available.
%{?scl:PATH=%{_bindir}${PATH:+:${PATH}}}
# Make sure no extra CFLAGS, CXXFLAGS or LDFLAGS leak through,
# the testsuite sets all flags necessary. See also configure above.
%make_build CFLAGS="" CXXFLAGS="" LDFLAGS="" check

# Workaround https://bugzilla.redhat.com/show_bug.cgi?id=1434601
# for gdbserver tests.
export PYTHONCOERCECLOCALE=0

echo ===============TESTING===================
%if %{run_full_regtest}
  make regtest || :
%else
  make nonexp-regtest || :
%endif

# Make sure test failures show up in build.log
# Gather up the diffs (at most the first 20 lines for each one)
MAX_LINES=20
diff_files=`find gdbserver_tests */tests -name '*.diff*' | sort`
if [ z"$diff_files" = z ] ; then
   echo "Congratulations, all tests passed!" >> diffs
else
   for i in $diff_files ; do
      echo "=================================================" >> diffs
      echo $i                                                  >> diffs
      echo "=================================================" >> diffs
      if [ `wc -l < $i` -le $MAX_LINES ] ; then
         cat $i                                                >> diffs
      else
         head -n $MAX_LINES $i                                 >> diffs
         echo "<truncated beyond $MAX_LINES lines>"            >> diffs
      fi
   done
fi
cat diffs
echo ===============END TESTING===============

%{!?_licensedir:%global license %%doc}

%files
%license COPYING
%{_bindir}/valgrind
%dir %{_libexecdir}/valgrind
# Install just the core tools, default suppression and vgpreload libraries.
%{_libexecdir}/valgrind/default.supp
%{_libexecdir}/valgrind/*-*-linux
# Turn on executable bit again for vgpreload libraries.
# Was disabled in %%install to prevent debuginfo stripping.
%attr(0755,root,root) %{_libexecdir}/valgrind/vgpreload_*-%{valarch}-linux.so

%files docs
%license COPYING.DOCS
%doc NEWS README_*
%doc docs/installed/html docs/installed/*.pdf
%{_mandir}/man1/*

%files scripts
%license COPYING
%{_bindir}/callgrind_annotate
%{_bindir}/callgrind_control
%{_bindir}/cg_annotate
%{_bindir}/cg_diff
%{_bindir}/cg_merge
%{_bindir}/ms_print
%{_libexecdir}/valgrind/dh_view.css
%{_libexecdir}/valgrind/dh_view.html
%{_libexecdir}/valgrind/dh_view.js

%files gdb
%license COPYING
%{_bindir}/valgrind-di-server
%{_bindir}/valgrind-listener
%{_bindir}/vgdb
%{_bindir}/vgstack
# gdb register descriptions
%{_libexecdir}/valgrind/*.xml
%{_datadir}/gdb/auto-load/valgrind-monitor.py
%{_datadir}/gdb/auto-load/valgrind-monitor-def.py

%files devel
%dir %{_includedir}/valgrind
%{_includedir}/valgrind/valgrind.h
%{_includedir}/valgrind/cachegrind.h
%{_includedir}/valgrind/callgrind.h
%{_includedir}/valgrind/drd.h
%{_includedir}/valgrind/helgrind.h
%{_includedir}/valgrind/memcheck.h
%{_includedir}/valgrind/dhat.h
%{_libdir}/pkgconfig/valgrind.pc

%if %{build_tools_devel}
%files tools-devel
%license COPYING
%{_includedir}/valgrind/config.h
%{_includedir}/valgrind/libvex*h
%{_includedir}/valgrind/pub_tool_*h
%{_includedir}/valgrind/vki
%dir %{_libdir}/valgrind
%{_libdir}/valgrind/*.a
%endif

%if %{build_openmpi}
%files openmpi
%dir %{_libdir}/valgrind
%{_libdir}/openmpi/valgrind/libmpiwrap*.so
%{_libdir}/valgrind/libmpiwrap*.so
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.26.0-5
- Prepare for Oreon 11 (RP1)
