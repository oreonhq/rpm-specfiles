%global source1_hash da983fffdbeb902e819bf7d91842a7ea360d60a191ac46855b156a631a9fcbef
%global source0_hash bd2e4c5731380922a8a6a45cc6dce0477bab000c917086f802d983d65441599a
%global vmajor            1
%global vminor            5
%global vpatch            1
%bcond_with replace_coreutils
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
%bcond_without replace_fipscheck
%else
%bcond_with replace_fipscheck
%endif
%if 0%{?fedora} >= 28 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
%bcond_without replace_hmaccalc
%else
%bcond_with replace_hmaccalc
%endif
%if 0%{?fedora} >= 29 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
%bcond_without test_package
%else
%bcond_with test_package
%endif
%bcond_without cppcheck
%bcond_without test
%bcond_without fuzz_test
%bcond_without doc
%bcond_without clang_sa
%global min_kernel_ver    4.10.0
%if %{lua:print(rpm.vercmp('99.0.0', posix.uname('%r')));} >= 0
%global with_sysctl_tweak 1
%else
%global with_sysctl_tweak 0
%endif
%global test_optmem_max   %(%{__cat} /proc/sys/net/core/optmem_max || echo 0)
%global giturl            https://github.com/smuellerDD/%{name}
%if %{with replace_coreutils}
%global coreutils_evr     8.29-1%{?dist}
%endif
%if %{with replace_fipscheck}
%global fipscheck_evr     1.5.0-9
%endif
%if %{with replace_hmaccalc}
%global hmaccalc_evr      0.9.14-10%{?dist}
%endif
%global apps_coreutils sha1sum sha224sum sha256sum sha384sum sha512sum md5sum sm3sum
%global apps_hmaccalc sha1hmac sha224hmac sha256hmac sha384hmac sha512hmac sm3hmac
%global apps_fipscheck fipscheck fipshmac
%if %{lua:print(rpm.vercmp(posix.uname('%r'), '3.19'));} >= 0
%global sha512hmac bin/kcapi-hasher -n sha512hmac
%global fipshmac   bin/kcapi-hasher -n fipshmac
%else
%global sha512hmac bash %{SOURCE2}
%global fipshmac   bash %{SOURCE3}
%endif
%define __spec_install_post                                      \
%{?__debug_package:%{__debug_install_post}}                      \
%{__arch_install_post}                                           \
%{__os_install_post}                                             \
bin_path=%{buildroot}%{_bindir}                                  \
lib_path=%{buildroot}%{_libdir}                                  \
{ %sha512hmac "$bin_path"/kcapi-hasher || exit 1; } |            \\\
  cut -f 1 -d ' ' >"$lib_path"/hmaccalc/kcapi-hasher.hmac        \
{ %sha512hmac "$lib_path"/libkcapi.so.%{version} || exit 1; } |  \\\
  cut -f 1 -d ' ' >"$lib_path"/hmaccalc/libkcapi.so.%{version}.hmac \
%{__ln_s} libkcapi.so.%{version}.hmac                            \\\
  "$lib_path"/hmaccalc/libkcapi.so.%{vmajor}.hmac                \
%{nil}
Name:           libkcapi
Version:        %{vmajor}.%{vminor}.%{vpatch}
Release:        1%{?dist}
Summary:        User space interface to the Linux Kernel Crypto API
License:        BSD-3-Clause OR GPL-2.0-only
URL:            https://www.chronox.de/%{name}/
Source0:        https://www.chronox.de/%{name}/releases/%{version}/%{name}-%{version}.tar.xz
Source1:        https://www.chronox.de/%{name}/releases/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        sha512hmac-openssl.sh
Source3:        fipshmac-openssl.sh
%if %{with doc}
%endif
%if %{with clang_sa}
%endif
%if %{with cppcheck}
%endif
Requires:       systemd
Obsoletes:      %{name}-replacements <= %{version}-%{release}
# oreon:deps
BuildRequires:  bash
BuildRequires:  clang
BuildRequires:  coreutils
BuildRequires:  cppcheck
BuildRequires:  docbook-utils-pdf
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  hardlink
BuildRequires:  kernel-headers
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  perl-interpreter
BuildRequires:  systemd
BuildRequires:  xmlto
# /oreon:deps
%description
libkcapi allows user-space to access the Linux kernel crypto API.

This library uses the netlink interface and exports easy to use APIs
so that a developer does not need to consider the low-level netlink
interface handling.

The library does not implement any cipher algorithms.  All consumer
requests are sent to the kernel for processing.  Results from the
kernel crypto API are returned to the consumer via the library API.

The kernel interface and therefore this library can be used by
unprivileged processes.

%package        devel
Summary:        Development files for the %{name} package
Requires:       %{name}%{?_isa} == %{version}-%{release}
%description    devel
Header files for applications that use %{name}.

%if %{with doc}
%package        doc
Summary:        User documentation for the %{name} package
BuildArch:      noarch
Requires:       %{name} == %{version}-%{release}
%description    doc
User documentation for %{name}.
%endif

%package        hasher
Summary:        Common %{name} hashing application
Requires:       %{name}%{?_isa}    == %{version}-%{release}
%description    hasher
Provides The kcapi-hasher binary used by other %{name} subpackages.

%if %{with replace_coreutils}
%package        checksum
Summary:        Drop-in replacement for *sum utils provided by the %{name} package
Requires:       %{name}-hasher%{?_isa} == %{version}-%{release}
Requires:       coreutils%{?_isa}  >= %{coreutils_evr}
Conflicts:      coreutils          < %{coreutils_evr}
Conflicts:      coreutils-single
%description    checksum
Provides drop-in replacements for sha*sum tools (from package
coreutils) using %{name}.
%endif

%if %{with replace_fipscheck}
%package        fipscheck
Summary:        Drop-in replacements for fipscheck/fipshmac provided by the %{name} package
Requires:       %{name}-hasher%{?_isa} == %{version}-%{release}
Obsoletes:      fipscheck         <= %{fipscheck_evr}
Provides:       fipscheck         == %{fipscheck_evr}.1
Provides:       fipscheck%{?_isa} == %{fipscheck_evr}.1
%description    fipscheck
Provides drop-in replacements for fipscheck and fipshmac tools (from
package fipscheck) using %{name}.
%endif

%if %{with replace_hmaccalc}
%package        hmaccalc
Summary:        Drop-in replacements for hmaccalc provided by the %{name} package
Requires:       %{name}-hasher%{?_isa} == %{version}-%{release}
Obsoletes:      hmaccalc          <= %{hmaccalc_evr}
Provides:       hmaccalc          == %{hmaccalc_evr}.1
Provides:       hmaccalc%{?_isa}  == %{hmaccalc_evr}.1
%description    hmaccalc
Provides drop-in replacements for sha*hmac tools (from package
hmaccalc) using %{name}.
%endif

%package        static
Summary:        Static library for -static linking with %{name}
Requires:       %{name}-devel%{?_isa} == %{version}-%{release}
%description    static
This package contains the %{name} static libraries for -static
linking.  You don't need this, unless you link statically, which
is highly discouraged.

%package        tools
Summary:        Utility applications for the %{name} package
Requires:       %{name}%{?_isa}        == %{version}-%{release}
Requires:       %{name}-hasher%{?_isa} == %{version}-%{release}
%description    tools
Utility applications that are provided with %{name}.  This includes
tools to use message digests, symmetric ciphers and random number
generators implemented in the Linux kernel from command line.

%if %{with test_package}
%package        tests
Summary:        Testing scripts for the %{name} package
Requires:       %{name}%{?_isa}       == %{version}-%{release}
Requires:       %{name}-tools%{?_isa} == %{version}-%{release}
%if %{with replace_hmaccalc}
Requires:       %{name}-hmaccalc%{?_isa} == %{version}-%{release}
%endif
%if %{with replace_coreutils}
Requires:       %{name}-checksum%{?_isa} == %{version}-%{release}
%endif
Requires:       coreutils
Requires:       openssl
Requires:       perl-interpreter
%description    tests
Auxiliary scripts for testing %{name}.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p 1 -S git

# Work around https://bugzilla.redhat.com/show_bug.cgi?id=2258240
sed -i -e 's|XML V45|XML V4.1.2|' -e 's|/xml/4\.5/|/xml/4.1.2/|' \
    lib/doc/libkcapi.tmpl

%{_bindir}/autoreconf -fiv

%build

%configure               \
  --libdir=%{_libdir}    \
  --disable-silent-rules \
  --enable-kcapi-encapp  \
  --enable-kcapi-dgstapp \
  --enable-kcapi-hasher  \
  --enable-kcapi-rngapp  \
  --enable-kcapi-speed   \
  --enable-kcapi-test    \
  --enable-shared        \
  --enable-static        \
  --enable-sum-prefix=   \
  --enable-sum-dir=%{_libdir} \
  --with-pkgconfigdir=%{_libdir}/pkgconfig
%if %{with doc}
%make_build all doc
%else
%make_build all man
%endif
%install
%make_install
%{__mkdir_p} %{buildroot}%{_sysctldir}
%{__install} -Dpm 0644 -t %{buildroot}%{_sysctldir} \
  %{sysctl_prio}-%{name}-optmem_max.conf
%{__mkdir_p} %{buildroot}%{_pkgdocdir}
%{__install} -Dpm 0644 -t %{buildroot}%{_pkgdocdir} \
%if %{with doc}
  doc/%{name}.p{df,s}                               \
%endif
  README.md CHANGES.md TODO
%if %{with doc}
%{__cp} -pr lib/doc/html %{buildroot}%{_pkgdocdir}
%endif
%if %{with replace_coreutils}
for app in %apps_coreutils; do
  %{__ln_s} ../libexec/libkcapi/$app %{buildroot}%{_bindir}/$app
done
%endif
%if %{with replace_fipscheck}
for app in %apps_fipscheck; do
  %{__ln_s} ../libexec/libkcapi/$app %{buildroot}%{_bindir}/$app
done
%endif
%if %{with replace_hmaccalc}
for app in %apps_hmaccalc; do
  %{__ln_s} ../libexec/libkcapi/$app %{buildroot}%{_bindir}/$app
done
%endif
%{_bindir}/find %{buildroot} -type f -name '*.la' -print -delete
%{_bindir}/find %{buildroot} -type f -name '*.hmac' -print -delete
%{_bindir}/find %{buildroot} -type f -size 0 -print -delete
%if %{with doc}
%{_bindir}/find %{buildroot}%{_pkgdocdir} -type f -print | \
  %{_bindir}/xargs %{__chmod} -c 0644
%{_bindir}/find %{buildroot}%{_pkgdocdir} -type d -print | \
  %{_bindir}/xargs %{__chmod} -c 0755
%endif
for d in %{_mandir} %{_pkgdocdir}; do
  %{_bindir}/hardlink -cfv %{buildroot}$d
done
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.*

%check

%if %{with clang_sa}
%make_build scan
%endif
%if %{with cppcheck}
%make_build cppcheck CPPCHECK="cppcheck --check-level=exhaustive -UCHECK_DIR"
%endif
%if %{with test}
%if %{test_optmem_max} >= 20480
%if %{lua:print(rpm.vercmp(posix.uname('%r'), '5.1'));} >= 0
pushd test
%if %{with fuzz_test}
ENABLE_FUZZ_TEST=1 \
%endif
NO_32BIT_TEST=1    \
  ./test-invocation.sh
popd
%endif
%endif
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
