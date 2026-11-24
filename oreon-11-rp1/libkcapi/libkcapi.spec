# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash bd2e4c5731380922a8a6a45cc6dce0477bab000c917086f802d983d65441599a
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global vmajor            1
%global vminor            5
%global vpatch            1

%bcond_with replace_coreutils
%bcond_without replace_fipscheck
%bcond_without replace_hmaccalc
%bcond_without test_package
%bcond_without cppcheck

%bcond_without test
%bcond_without fuzz_test
%bcond_with doc
%bcond_without clang_sa

%global min_kernel_ver    4.10.0

%if %{lua:print(rpm.vercmp('99.0.0', posix.uname('%r')));} >= 0
%global with_sysctl_tweak 1
%else
%global with_sysctl_tweak 0
%endif

%if %{with_sysctl_tweak}
%global sysctl_prio       50

%global sysctl_optmem_max 81920

%global distroname_ext    oreon
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

Patch0:         001-fix-test.patch

BuildRequires: oreon-rpm-macros
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  clang
BuildRequires:  git-core
BuildRequires:  hardlink
BuildRequires:  kernel-headers >= %{min_kernel_ver}
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  perl-interpreter
BuildRequires:  systemd
BuildRequires:  xmlto
%if %{with doc}
BuildRequires:  docbook-utils-pdf
%endif
%if %{with cppcheck}
BuildRequires:  cppcheck >= 2.4
%endif

Requires:       systemd

Obsoletes:      %{name}-replacements <= %{version}-%{release}

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
%oreon_sha256
%autosetup -p 1 -S git

sed -i -e 's|XML V45|XML V4.1.2|' -e 's|/xml/4\.5/|/xml/4.1.2/|' \
    lib/doc/libkcapi.tmpl

%if %{with_sysctl_tweak}
%{__cat} << EOF > README.%{distroname_ext}
This package increases the default limit of the ancillary buffer size
per kernel socket defined in \`net.core.optmem_max\` to %{sysctl_optmem_max} bytes.

For this preset to become active it requires a reboot after the
installation of this package.  You can also manually increase this
limit by invocing \`sysctl net.core.optmem_max=%{sysctl_optmem_max}\` as the
super-user, e.g. using \`su\` or \`sudo\` on the terminal.

This is done to provide consumers of the new Linux Kernel Crypto API
User Space Interface a well sufficient and reasonable maximum limit
by default, especially when using AIO with a larger amount of IOVECs.

For further information about the AF_ALG kernel socket and AIO, see
the discussion at the kernel-crypto mailing-list:
https://www.mail-archive.com/linux-crypto@vger.kernel.org/msg30417.html

See the instructions given in '%{_sysctldir}/50-default.conf',
if you need or want to override the preset made by this package.
EOF

%{__cat} << EOF > %{sysctl_prio}-%{name}-optmem_max.conf

net.core.optmem_max = %{sysctl_optmem_max}
EOF
%endif

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
%if %{with_sysctl_tweak}
  README.%{distroname_ext}                          \
%endif
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

%files
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README.md
%license COPYING*
%{_libdir}/%{name}.so.%{vmajor}
%{_libdir}/%{name}.so.%{version}
%{_libdir}/hmaccalc/%{name}.so.%{vmajor}.hmac
%{_libdir}/hmaccalc/%{name}.so.%{version}.hmac
%if %{with_sysctl_tweak}
%doc %{_pkgdocdir}/README.%{distroname_ext}
%{_sysctldir}/%{sysctl_prio}-%{name}-optmem_max.conf
%endif

%files          devel
%doc %{_pkgdocdir}/CHANGES.md
%doc %{_pkgdocdir}/TODO
%{_includedir}/kcapi.h
%{_mandir}/man3/kcapi_*.3.*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%if %{with doc}
%files          doc
%doc %{_pkgdocdir}/html
%doc %{_pkgdocdir}/%{name}.pdf
%doc %{_pkgdocdir}/%{name}.ps
%endif

%files          hasher
%{_bindir}/kcapi-hasher
%{_libexecdir}/%{name}/md5sum
%{_libexecdir}/%{name}/sha*sum
%{_libexecdir}/%{name}/sm*sum
%{_libexecdir}/%{name}/fips*
%{_libexecdir}/%{name}/sha*hmac
%{_libexecdir}/%{name}/sm*hmac
%{_libdir}/hmaccalc/kcapi-hasher.hmac
%{_mandir}/man1/kcapi-hasher.1.*

%if %{with replace_coreutils}
%files          checksum
%{_bindir}/md5sum
%{_bindir}/sha*sum
%{_bindir}/sm*sum
%endif

%if %{with replace_fipscheck}
%files          fipscheck
%{_bindir}/fips*
%endif

%if %{with replace_hmaccalc}
%files          hmaccalc
%{_bindir}/sha*hmac
%{_bindir}/sm*hmac
%endif

%files          static
%{_libdir}/%{name}.a

%files          tools
%{_bindir}/kcapi
%{_bindir}/kcapi-convenience
%{_bindir}/kcapi-dgst
%{_bindir}/kcapi-enc
%{_bindir}/kcapi-enc-test-large
%{_bindir}/kcapi-rng
%{_bindir}/kcapi-speed
%{_mandir}/man1/kcapi-dgst.1.*
%{_mandir}/man1/kcapi-enc.1.*
%{_mandir}/man1/kcapi-rng.1.*

%if %{with test_package}
%files          tests
%{_libexecdir}/%{name}/kcapi
%{_libexecdir}/%{name}/kcapi-convenience
%{_libexecdir}/%{name}/kcapi-enc-test-large
%{_libexecdir}/%{name}/*.sh
%endif

%changelog
%autochangelog
