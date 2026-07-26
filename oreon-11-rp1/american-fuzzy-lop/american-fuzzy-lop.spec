%global source0_hash 31dfc52377ade25a5e9222b3b229cec1696578856a562f41a197a00815798fb1

# We need to rebuild this package every time the clang major version
# changes, since clang releases are not ABI compatible between major
# versions. See also https://bugzilla.redhat.com/1544964.

Version:       4.35c
%global forgeurl https://github.com/AFLplusplus/AFLplusplus/
%global commit   afbcb07e7602791390adfc63932efcd14d39bab8
%forgemeta

Name:          american-fuzzy-lop
Summary:       Practical, instrumentation-driven fuzzer for binary formats
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:       Apache-2.0

Release:       5%{?dist}
URL:           %{forgeurl}
Source0:       %{forgesource}

# For running the tests:
Source1:       hello.c

# Only specific architectures are supported by upstream.
# On non-x86 only afl-clang-fast* are built.
# i686 support was silently removed in AFL++ 4.10c
# s390x breaks GCC see https://bugzilla.redhat.com/show_bug.cgi?id=2375376
ExclusiveArch: x86_64

BuildRequires: gcc
BuildRequires: gcc-plugin-devel

BuildRequires: clang
BuildRequires: llvm-devel
%ifarch x86_64
BuildRequires: lld
%endif
%global llvm_config /usr/bin/llvm-config
%global clang /usr/bin/clang
%global lld /usr/bin/ld.lld
%global clang_major %(command -v %{clang} >/dev/null && %{clang} --version | sed -n -r 's/clang version ([0-9]+).*/\\1/p')

BuildRequires: make

Requires:      gcc

%global afl_helper_path %{_libdir}/afl

%description
American fuzzy lop uses a novel type of compile-time instrumentation
and genetic algorithms to automatically discover clean, interesting
test cases that trigger new internal states in the targeted
binary. This substantially improves the functional coverage for the
fuzzed code. The compact synthesized corpuses produced by the tool are
also useful for seeding other, more labor- or resource-intensive
testing regimes down the road.

Compared to other instrumented fuzzers, afl-fuzz is designed to be
practical: it has a modest performance overhead, uses a variety of
highly effective fuzzing strategies, requires essentially no
configuration, and seamlessly handles complex, real-world use cases -
say, common image parsing or file compression libraries.

%package clang
Summary:       Clang and clang++ support for %{name}
Requires:      %{name} = %{version}-%{release}

%if "%{clang_major}" != ""
Requires:      clang(major) = %{clang_major}
%endif
%ifarch x86_64
Requires:      %{lld}
%endif
# This ensures that AFL_USE_ASAN=1 works out of the box.  However as
# it is not strictly required to use AFL, make it optional.
Recommends:    compiler-rt

%description clang
This subpackage contains clang and clang++ support for
%{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build
# This package appears to be failing because links to the LLVM plugins
# are not installed which results in the tools not being able to
# interpret the .o/.a files.  Disable LTO for now
%define _lto_cflags %{nil}

# We used to set CFLAGS/CXXFLAGS = %%{optflags} here, but these break
# the Clang instrumentation in some way.
unset CFLAGS
unset CXXFLAGS

%ifnarch x86_64
AFL_NO_X86=1 \
%endif
LLVM_CONFIG="%{llvm_config}" \
AFL_REAL_LD="%{lld}" \
%{__make} %{?_smp_mflags} \
  PREFIX="%{_prefix}" \
  HELPER_PATH="%{afl_helper_path}" \
  DOC_PATH="%{_pkgdocdir}" \
  MAN_PATH="%{_mandir}/man8" \
  MISC_PATH="%{_pkgdocdir}" \
  source-only

%install
# We used to set CFLAGS/CXXFLAGS = %%{optflags} here, but these break
# the Clang instrumentation in some way.
unset CFLAGS
unset CXXFLAGS

%ifnarch x86_64
AFL_NO_X86=1 \
%endif
LLVM_CONFIG="%{llvm_config}" \
AFL_REAL_LD="%{lld}" \
%{make_install} \
  PREFIX="%{_prefix}" \
  HELPER_PATH="%{afl_helper_path}" \
  DOC_PATH="%{_pkgdocdir}" \
  MAN_PATH="%{_mandir}/man8" \
  MISC_PATH="%{_pkgdocdir}"

%ifnarch x86_64
# On non-x86 these files are built and installed but they don't
# function, so delete them.  Only afl-clang-fast* works.
# afl-clang-fast* is a symlink to afl-cc / afl-c++ so we cannot delete
# those binaries.
rm $RPM_BUILD_ROOT%{_bindir}/afl-clang
rm $RPM_BUILD_ROOT%{_bindir}/afl-clang++
rm $RPM_BUILD_ROOT%{_bindir}/afl-gcc
rm $RPM_BUILD_ROOT%{_bindir}/afl-g++
rm $RPM_BUILD_ROOT%{_mandir}/man8/afl-cc.8*
rm $RPM_BUILD_ROOT%{_mandir}/man8/afl-c++.8*
%endif

%ifarch x86_64
# This file doesn't get installed by 'make install' for some reason:
install -m 0755 afl-compiler-rt.o $RPM_BUILD_ROOT%{afl_helper_path}/
%endif

# Otherwise we see:
# ERROR: No build ID note found in <.o file>
chmod -x $RPM_BUILD_ROOT%{afl_helper_path}/*.o

# This file is created when I build locally, but not when I build in
# Koji.  Remove it so I can build locally.
%if 0%{?__isa_bits} == 64
rm -f $RPM_BUILD_ROOT%{afl_helper_path}/afl-compiler-rt-32.o
rm -f $RPM_BUILD_ROOT%{afl_helper_path}/afl-llvm-rt-32.o
rm -f $RPM_BUILD_ROOT%{afl_helper_path}/afl-llvm-rt-lto-32.o
%endif

# Remove docs since we will package them using %%doc.
mv $RPM_BUILD_ROOT%{_pkgdocdir} pkg-docs

%check
# This just checks that simple programs can be compiled using
# the compiler wrappers.

# Probably users will need to set this manually if they are using
# clang XXX.
export PATH="$(%{llvm_config} --bindir)":$PATH

ln -s %{SOURCE1} hello.cpp
./afl-clang-fast %{SOURCE1} -o hello
./hello
./afl-clang-fast++ hello.cpp -o hello
./hello
./afl-gcc-fast %{SOURCE1} -o hello
./hello
./afl-g++-fast hello.cpp -o hello
./hello

# Also check that we got the %%clang_major macro
test -n '%{clang_major}'

%files
%license docs/COPYING
%doc pkg-docs/*
%ifarch x86_64
%{_bindir}/afl-g++
%{_bindir}/afl-gcc
%endif
%{_bindir}/afl-analyze
%{_bindir}/afl-addseeds
%{_bindir}/afl-cc
%{_bindir}/afl-c++
%{_bindir}/afl-cmin
%{_bindir}/afl-cmin.awk
%{_bindir}/afl-cmin.bash
%{_bindir}/afl-cmin.py
%{_bindir}/afl-fuzz
%{_bindir}/afl-gcc-fast
%{_bindir}/afl-g++-fast
%{_bindir}/afl-gotcpu
%{_bindir}/afl-persistent-config
%{_bindir}/afl-plot
%{_bindir}/afl-showmap
%{_bindir}/afl-system-config
%{_bindir}/afl-tmin
%{_bindir}/afl-whatsup
%dir %{afl_helper_path}
%if 0%{?__isa_bits} == 32
%{afl_helper_path}/afl-compiler-rt-32.o
%else
%{afl_helper_path}/afl-compiler-rt-64.o
%endif
%{afl_helper_path}/afl-compiler-rt.o
%{afl_helper_path}/afl-gcc-cmplog-pass.so
%{afl_helper_path}/afl-gcc-cmptrs-pass.so
%{afl_helper_path}/afl-gcc-pass.so
%{afl_helper_path}/afl-gcc-rt.o
%{afl_helper_path}/afl-llvm-ijon-pass.so
%{afl_helper_path}/injection-pass.so
%ifarch x86_64
%{_mandir}/man8/afl-c++.8*
%{_mandir}/man8/afl-cc.8*
%endif
%{_mandir}/man8/afl-addseeds.8*
%{_mandir}/man8/afl-analyze.8*
%{_mandir}/man8/afl-cmin.8*
%{_mandir}/man8/afl-cmin.awk.8*
%{_mandir}/man8/afl-cmin.bash.8*
%{_mandir}/man8/afl-cmin.py.8*
%{_mandir}/man8/afl-fuzz.8*
%{_mandir}/man8/afl-gcc-fast.8*
%{_mandir}/man8/afl-g++-fast.8*
%{_mandir}/man8/afl-gotcpu.8*
%{_mandir}/man8/afl-plot.8*
%{_mandir}/man8/afl-persistent-config.8*
%{_mandir}/man8/afl-showmap.8*
%{_mandir}/man8/afl-system-config.8*
%{_mandir}/man8/afl-tmin.8*
%{_mandir}/man8/afl-whatsup.8*

%{_includedir}/afl/

%files clang
%license docs/COPYING

%ifarch x86_64
%{_bindir}/afl-clang
%{_bindir}/afl-clang++
%endif
%{_bindir}/afl-clang-fast
%{_bindir}/afl-clang-fast++
%{_bindir}/afl-clang-lto
%{_bindir}/afl-clang-lto++
%{_bindir}/afl-ld-lto
%{_bindir}/afl-lto
%{_bindir}/afl-lto++

%{afl_helper_path}/afl-llvm-dict2file.so
%{afl_helper_path}/afl-llvm-lto-instrumentlist.so
%{afl_helper_path}/afl-llvm-pass.so

%if 0%{?__isa_bits} == 32
%{afl_helper_path}/afl-llvm-rt-lto-32.o
%else
%{afl_helper_path}/afl-llvm-rt-lto-64.o
%endif
%{afl_helper_path}/afl-llvm-rt-lto.o

%{afl_helper_path}/cmplog-instructions-pass.so
%{afl_helper_path}/cmplog-routines-pass.so
%{afl_helper_path}/cmplog-switches-pass.so
%{afl_helper_path}/compare-transform-pass.so
%{afl_helper_path}/dynamic_list.txt
%{afl_helper_path}/libAFLDriver.a*
%{afl_helper_path}/libAFLQemuDriver.a
%{afl_helper_path}/libdislocator.so
%{afl_helper_path}/libtokencap.so
%{afl_helper_path}/SanitizerCoverageLTO.so
%{afl_helper_path}/SanitizerCoveragePCGUARD.so
%{afl_helper_path}/split-compares-pass.so
%{afl_helper_path}/split-switches-pass.so

%{_mandir}/man8/afl-clang-fast.8*
%{_mandir}/man8/afl-clang-fast++.8*
%{_mandir}/man8/afl-clang-lto.8.gz
%{_mandir}/man8/afl-clang-lto++.8.gz
%{_mandir}/man8/afl-lto.8.gz
%{_mandir}/man8/afl-lto++.8.gz

%changelog
%autochangelog
