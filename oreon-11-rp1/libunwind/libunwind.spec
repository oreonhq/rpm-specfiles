# The testsuite does not pass on all targets.
#
# aarch64
#     Gtest-exc
#     Ltest-exc
#     Gtest-trace
#     Ltest-trace
#     Ltest-init-local-signal
#     Ltest-mem-validate: https://github.com/libunwind/libunwind/issues/388
#     test-reg-state
#     Ltest-varargs
#     Lrs-race
#     test-ptrace
#     run-check-namespace: https://github.com/libunwind/libunwind/issues/389
#     run-ptrace-mapper
#     run-ptrace-misc
# i686
#     Ltest-mem-validate: https://github.com/libunwind/libunwind/issues/391
#     test-async-sig
#     test-ptrace
# ppc64le
#     Gtest-exc
#     Ltest-exc
#     Gtest-resume-sig
#     Ltest-resume-sig
#     Gtest-resume-sig-rt
#     Ltest-resume-sig-rt
#     test-ptrace
#     run-check-namespace
#     run-ptrace-mapper
#     run-ptrace-misc
#
# s390x
#     Gtest-resume-sig-rt
#     Ltest-resume-sig-rt
#     test-ptrace

%ifarch i686 ppc64le s390x
%global test_failure_override true
%else
%global test_failure_override false
%endif

# %%global prerel rc2

Summary: An unwinding library
Name: libunwind
Version: 1.8.1
Release: 3%{?dist}
License: MIT
URL: http://savannah.nongnu.org/projects/libunwind
Source: https://github.com/libunwind/libunwind/releases/download/v%{version}/%{name}-%{version}.tar.gz

#Fedora specific patch
Patch1: libunwind-arm-default-to-exidx.patch
# Make libunwind.h multilib friendly
Patch2: libunwind-1.3.1-multilib-fix.patch
Patch5: libunwind-no-dl-iterate-phdr.patch
# Fix C23 issue
Patch6: https://github.com/libunwind/libunwind/commit/457612f470f8c0e718cdf7f14ef1ecb583f3b3a6.patch

ExclusiveArch: %{arm} aarch64 hppa ia64 mips ppc %{power64} s390x %{ix86} x86_64 riscv64

BuildRequires: automake libtool autoconf texlive-latex2man
BuildRequires: make
BuildRequires: gcc-c++

# host != target would cause REMOTE_ONLY build even if building i386 on x86_64.
%global _host %{_target_platform}

%description
Libunwind provides a C ABI to determine the call-chain of a program.

%package devel
Summary: Development package for libunwind
Requires: libunwind%{_isa} = %{version}-%{release}

%description devel
The libunwind-devel package includes the libraries and header files for
libunwind.

%package tests
Summary: Test binaries for libunwind
Requires: libunwind%{_isa} = %{version}-%{release}

%description tests
Test executables for libunwind. Not needed for library functionality.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%ifarch aarch64
# LTO causes FTBFS on aarch64 (rhbz#2261344)
%global _lto_cflags %{nil}
%endif

%global optflags %{optflags} -fcommon
aclocal
libtoolize --force
autoheader
automake --add-missing
autoconf
%configure --enable-static --enable-shared --enable-setjmp=no
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# /usr/include/libunwind-ptrace.h
# [...] aren't really part of the libunwind API.  They are implemented in
# a archive library called libunwind-ptrace.a.
mv -f $RPM_BUILD_ROOT%{_libdir}/libunwind-ptrace.a $RPM_BUILD_ROOT%{_libdir}/libunwind-ptrace.a-save
rm -f $RPM_BUILD_ROOT%{_libdir}/libunwind*.a
mv -f $RPM_BUILD_ROOT%{_libdir}/libunwind-ptrace.a-save $RPM_BUILD_ROOT%{_libdir}/libunwind-ptrace.a

# The tests want this one.
# rm -f $RPM_BUILD_ROOT%{_libdir}/libunwind-ptrace*.so*

# fix multilib conflicts
touch -r NEWS $RPM_BUILD_ROOT%{_includedir}/libunwind.h

%check
echo ====================TESTING=========================
if ! make check ; then
    echo ====================FAILED TESTS=====================
    cat tests/test-suite.log || true
    %{test_failure_override}
fi
echo ====================TESTING END=====================

%ldconfig_scriptlets

%files
%license COPYING
%doc README NEWS
%{_libdir}/libunwind*.so.*

%files devel
%{_libdir}/libunwind*.so
%{_libdir}/libunwind-ptrace.a
%{_libdir}/pkgconfig/libunwind*.pc
%{_mandir}/*/*
# <unwind.h> does not get installed for REMOTE_ONLY targets - check it.
%{_includedir}/unwind.h
%{_includedir}/libunwind*.h

%files tests
%{_libexecdir}/libunwind

%changelog
* Sat Apr 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8.1-3
- Import from Fedora dist-git f43 for Oreon 11
