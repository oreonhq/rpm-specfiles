# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash be30d910e67f58d82e753231f1357f326a1a088acf126b21ff77e60aab19b90b

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

# known upstream test failures on these arches, see
# https://github.com/libunwind/libunwind/issues/388
# https://github.com/libunwind/libunwind/issues/389
# https://github.com/libunwind/libunwind/issues/391
%ifarch i686 ppc64le s390x
%global test_failure_override true
%else
%global test_failure_override false
%endif

Summary: An unwinding library
Name: libunwind
Version: 1.8.3
Release: 2%{?dist}
License: MIT
URL: https://savannah.nongnu.org/projects/libunwind
Source0: https://github.com/libunwind/libunwind/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1: https://github.com/libunwind/libunwind/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
# Stephen M. Webb, 42FA3D4C00D0AA116C3F45DAA4CCF616E0FF69D2
Source2: gpgkey-42FA3D4C00D0AA116C3F45DAA4CCF616E0FF69D2.gpg
Patch1: libunwind-arm-default-to-exidx.patch
Patch2: libunwind-1.3.1-multilib-fix.patch
Patch5: libunwind-no-dl-iterate-phdr.patch
Patch6: libunwind-gtest-nomalloc-proto.patch
Patch7: libunwind-s390x-glibc-mmap.patch
Patch8: libunwind-s390x-backtrace-1.patch
Patch9: libunwind-s390x-backtrace-2.patch
Patch10: libunwind-s390x-backtrace-3.patch
ExclusiveArch: %{arm} aarch64 hppa ia64 mips ppc %{power64} s390x %{ix86} x86_64 riscv64

BuildRequires: oreon-rpm-macros
BuildRequires: gnupg2
BuildRequires: automake
BuildRequires: libtool
BuildRequires: autoconf
%if %{without bootstrap}
BuildRequires: texlive-latex2man
%endif
BuildRequires: make
BuildRequires: gcc-c++

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
%oreon_sha256

%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1 -n %{name}-%{version}

%build
%global optflags %{optflags} -fcommon
aclocal
libtoolize --force
autoheader
automake --add-missing
autoconf
%configure --enable-static --enable-shared --enable-setjmp=no --disable-cxx-exceptions
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# libunwind-ptrace.a is the only archive that is part of the api
mv -f $RPM_BUILD_ROOT%{_libdir}/libunwind-ptrace.a $RPM_BUILD_ROOT%{_libdir}/libunwind-ptrace.a-save
rm -f $RPM_BUILD_ROOT%{_libdir}/libunwind*.a
mv -f $RPM_BUILD_ROOT%{_libdir}/libunwind-ptrace.a-save $RPM_BUILD_ROOT%{_libdir}/libunwind-ptrace.a

# multilib
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
%{_includedir}/unwind.h
%{_includedir}/libunwind*.h

%files tests
%{_libexecdir}/libunwind

%changelog
%autochangelog
