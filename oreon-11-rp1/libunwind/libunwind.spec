%global source0_hash be30d910e67f58d82e753231f1357f326a1a088acf126b21ff77e60aab19b90b
%ifarch i686 ppc64le s390x x86_64
%global test_failure_override true
%else
%global test_failure_override false
%endif
Summary:        An unwinding library
Name: libunwind
Version: 1.8.3
Release:        1%{?dist}
License: MIT
URL: http://savannah.nongnu.org/projects/libunwind
Source0:        https://github.com/libunwind/libunwind/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch1: libunwind-arm-default-to-exidx.patch
Patch2: libunwind-1.3.1-multilib-fix.patch
Patch5: libunwind-no-dl-iterate-phdr.patch
Patch6: https://github.com/libunwind/libunwind/commit/457612f470f8c0e718cdf7f14ef1ecb583f3b3a6.patch
ExclusiveArch: %{arm} aarch64 hppa ia64 mips ppc %{power64} s390x %{ix86} x86_64 riscv64
%global _host %{_target_platform}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  texlive-latex2man
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%ifarch aarch64
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
mv -f $RPM_BUILD_ROOT%{_libdir}/libunwind-ptrace.a $RPM_BUILD_ROOT%{_libdir}/libunwind-ptrace.a-save
rm -f $RPM_BUILD_ROOT%{_libdir}/libunwind*.a
mv -f $RPM_BUILD_ROOT%{_libdir}/libunwind-ptrace.a-save $RPM_BUILD_ROOT%{_libdir}/libunwind-ptrace.a
touch -r NEWS $RPM_BUILD_ROOT%{_includedir}/libunwind.h
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

echo ====================TESTING=========================
if ! make check ; then
    echo ====================FAILED TESTS=====================
    cat tests/test-suite.log || true
    %{test_failure_override}
fi
echo ====================TESTING END=====================
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libunwind-devel -f %{oreon_filedir}/libunwind-devel.list
%files -n libunwind-tests -f %{oreon_filedir}/libunwind-tests.list

%changelog

%autochangelog
