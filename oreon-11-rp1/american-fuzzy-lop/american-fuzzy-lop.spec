%global source0_hash 31dfc52377ade25a5e9222b3b229cec1696578856a562f41a197a00815798fb1
Version:       5.03c
%global forgeurl https://github.com/AFLplusplus/AFLplusplus/
%global commit   afbcb07e7602791390adfc63932efcd14d39bab8
%forgemeta
Name:          american-fuzzy-lop
Summary:        Practical, instrumentation-driven fuzzer for binary formats
License:       Apache-2.0
Release:        1%{?dist}
URL:           %{forgeurl}
Source0:        %{forgeurl}archive/%{commit}/AFLplusplus-%{commit}.tar.gz
Source1:       hello.c
ExclusiveArch: x86_64
%ifarch x86_64
%endif
%global llvm_config /usr/bin/llvm-config
%global clang /usr/bin/clang
%global lld /usr/bin/ld.lld
%global clang_major %(command -v %{clang} >/dev/null && %{clang} --version | sed -n -r 's/clang version ([0-9]+).*/\\1/p')
Requires:      gcc
%global afl_helper_path %{_libdir}/afl
# oreon:deps
BuildRequires:  clang
BuildRequires:  gcc
BuildRequires:  gcc-plugin-devel
BuildRequires:  llvm-devel
BuildRequires:  make
# /oreon:deps
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
Recommends:    compiler-rt
%description clang
This subpackage contains clang and clang++ support for
%{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%define _lto_cflags %{nil}
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
rm $RPM_BUILD_ROOT%{_bindir}/afl-clang
rm $RPM_BUILD_ROOT%{_bindir}/afl-clang++
rm $RPM_BUILD_ROOT%{_bindir}/afl-gcc
rm $RPM_BUILD_ROOT%{_bindir}/afl-g++
rm $RPM_BUILD_ROOT%{_mandir}/man8/afl-cc.8*
rm $RPM_BUILD_ROOT%{_mandir}/man8/afl-c++.8*
%endif
%ifarch x86_64
install -m 0755 afl-compiler-rt.o $RPM_BUILD_ROOT%{afl_helper_path}/
%endif
chmod -x $RPM_BUILD_ROOT%{afl_helper_path}/*.o
%if 0%{?__isa_bits} == 64
rm -f $RPM_BUILD_ROOT%{afl_helper_path}/afl-compiler-rt-32.o
rm -f $RPM_BUILD_ROOT%{afl_helper_path}/afl-llvm-rt-32.o
rm -f $RPM_BUILD_ROOT%{afl_helper_path}/afl-llvm-rt-lto-32.o
%endif
mv $RPM_BUILD_ROOT%{_pkgdocdir} pkg-docs
%oreon_autofiles american-fuzzy-lop-clang usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

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
test -n '%{clang_major}'
%files -f %{oreon_filedir}/main.list
%files -n american-fuzzy-lop-clang -f %{oreon_filedir}/american-fuzzy-lop-clang.list

%changelog

%autochangelog
