%global source0_hash 425611e6b031c7a81fc72f82187498de827af708bbc0c8e2d31e52ca566871c6
Name: opencryptoki
Summary:        Implementation of the PKCS#11 (Cryptoki) specification v3.0 and partially v3.1
Version: 3.27.0
Release:        1%{?dist}
License: CPL-1.0
URL: https://github.com/opencryptoki/opencryptoki
Source0:        https://github.com/opencryptoki/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: opencryptoki.module
Source2: opencryptoki.sysusers.conf
Patch1: opencryptoki-3.25.0-p11sak.patch
Patch2: opencryptoki-3.24.0-tmpfiles-image-mode.patch
Patch3: opencryptoki-lockdir-image-mode.patch
Requires(pre): coreutils
Requires: (selinux-policy >= 34.9-1 if selinux-policy-targeted)
%if 0%{?tmptok}
%endif
%{?sysusers_requires_compat}
%ifarch s390 s390x
%endif
Requires: openssl >= 1:3.5.1
Requires(pre): %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}(token)
Requires(post): systemd diffutils
Requires(preun): systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  expect
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  jq
BuildRequires:  libcap-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openldap-devel
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Opencryptoki implements the PKCS#11 specification  v3.0 and partially v3.1
for a set of cryptographic hardware, such as IBM 4767, 4768, 4769 and 4770
crypto cards, and the Trusted Platform Module (TPM) chip. Opencryptoki also
brings a software token implementation that can be used without any cryptographic
hardware.
This package contains the Slot Daemon (pkcsslotd) and general utilities.

%package libs
Summary: The run-time libraries for opencryptoki package
Requires(pre): shadow-utils
%description libs
Opencryptoki implements the PKCS#11 specification  v3.0 and partially v3.1
for a set of cryptographic hardware, such as IBM 4767, 4768, 4769 and 4770
crypto cards, and the Trusted Platform Module (TPM) chip. Opencryptoki also
brings a software token implementation that can be used without any cryptographic
hardware.
This package contains the PKCS#11 library implementation, and requires
at least one token implementation (packaged separately) to be fully
functional.

%package devel
Summary: Development files for openCryptoki
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
This package contains the development header files for building
opencryptoki and PKCS#11 based applications

%package swtok
Summary: The software token implementation for opencryptoki
Requires(pre): %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Provides: %{name}(token)
%description swtok
Opencryptoki implements the PKCS#11 specification  v3.0 and partially v3.1
for a set of cryptographic hardware, such as IBM 4767, 4768, 4769 and 4770
crypto cards, and the Trusted Platform Module (TPM) chip. Opencryptoki also
brings a software token implementation that can be used without any cryptographic
hardware.
This package brings the software token implementation to use opencryptoki
without any specific cryptographic hardware.

%package tpmtok
Summary: Trusted Platform Module (TPM) device support for opencryptoki
Requires(pre): %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Provides: %{name}(token)
%description tpmtok
Opencryptoki implements the PKCS#11 specification  v3.0 and partially v3.1
for a set of cryptographic hardware, such as IBM 4767, 4768, 4769 and 4770
crypto cards, and the Trusted Platform Module (TPM) chip. Opencryptoki also
brings a software token implementation that can be used without any cryptographic
hardware.
This package brings the necessary libraries and files to support
Trusted Platform Module (TPM) devices in the opencryptoki stack.

%package icsftok
Summary: ICSF token support for opencryptoki
Requires(pre): %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Provides: %{name}(token)
%description icsftok
Opencryptoki implements the PKCS#11 specification  v3.0 and partially v3.1
for a set of cryptographic hardware, such as IBM 4767, 4768, 4769 and 4770
crypto cards, and the Trusted Platform Module (TPM) chip. Opencryptoki also
brings a software token implementation that can be used without any cryptographic
hardware.
This package brings the necessary libraries and files to support
ICSF token in the opencryptoki stack.

%package icatok
Summary: ICA cryptographic devices (clear-key) support for opencryptoki
Requires(pre): %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Provides: %{name}(token)
%description icatok
Opencryptoki implements the PKCS#11 specification  v3.0 and partially v3.1
for a set of cryptographic hardware, such as IBM 4767, 4768, 4769 and 4770
crypto cards, and the Trusted Platform Module (TPM) chip. Opencryptoki also
brings a software token implementation that can be used without any cryptographic
hardware.
This package brings the necessary libraries and files to support ICA
devices in the opencryptoki stack. ICA is an interface to IBM
cryptographic hardware such as IBM 4767, 4768, 4769 and 4770 that uses the
"accelerator" or "clear-key" path.

%package ccatok
Summary: CCA cryptographic devices (secure-key) support for opencryptoki
Requires(pre): %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Provides: %{name}(token)
%description ccatok
Opencryptoki implements the PKCS#11 specification  v3.0 and partially v3.1
for a set of cryptographic hardware, such as IBM 4767, 4768, 4769 and 4770
crypto cards, and the Trusted Platform Module (TPM) chip. Opencryptoki also
brings a software token implementation that can be used without any cryptographic
hardware.
This package brings the necessary libraries and files to support CCA
devices in the opencryptoki stack. CCA is an interface to IBM
cryptographic hardware such as IBM 4767, 4768, 4769 and 4770 that uses the
"co-processor" or "secure-key" path.

%package ep11tok
Summary: EP11 cryptographic devices (secure-key) support for opencryptoki
Requires(pre): %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Provides: %{name}(token)
%description ep11tok
Opencryptoki implements the PKCS#11 specification  v3.0 and partially v3.1
for a set of cryptographic hardware, such as IBM 4767, 4768, 4769 and 4770
crypto cards, and the Trusted Platform Module (TPM) chip. Opencryptoki also
brings a software token implementation that can be used without any cryptographic
hardware.
This package brings the necessary libraries and files to support EP11
tokens in the opencryptoki stack. The EP11 token is a token that uses
the IBM Crypto Express adapters (starting with Crypto Express 4S adapters)
configured with Enterprise PKCS#11 (EP11) firmware.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./bootstrap.sh
%configure --with-systemd=%{_unitdir} --enable-testcases	\
    --with-pkcsslotd-user=pkcsslotd --with-pkcs-group=pkcs11 \
%if 0%{?tpmtok}
    --enable-tpmtok \
%else
    --disable-tpmtok \
%endif
%ifarch s390 s390x x86_64 ppc64le
    --enable-ccatok \
%else
    --disable-ccatok \
%endif
%ifarch s390 s390x
    --enable-icatok --enable-ep11tok --enable-pkcsep11_migrate
%else
    --disable-icatok --disable-ep11tok --disable-pkcsep11_migrate --enable-pkcscca_migrate
%endif
%make_build CHGRP=/bin/true
%install
%make_install CHGRP=/bin/true
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/%{name}.sysusers.conf
%ifarch s390 s390x
install -p -D -m 0644 %{name}-icatok.conf %{buildroot}%{_tmpfilesdir}/
install -p -D -m 0644 %{name}-ep11tok.conf %{buildroot}%{_tmpfilesdir}/
%endif
%ifarch s390 s390x x86_64 ppc64le
install -p -D -m 0644 %{name}-ccatok.conf %{buildroot}%{_tmpfilesdir}/
%endif
%if 0%{?tmptok}
install -p -D -m 0644 %{name}-tpmtok.conf %{buildroot}%{_tmpfilesdir}/
%endif
install -p -D -m 0644 %{name}-swtok.conf %{buildroot}%{_tmpfilesdir}/
install -p -D -m 0644 %{name}-icsftok.conf %{buildroot}%{_tmpfilesdir}/
rm -f %{buildroot}%{_libdir}/%{name}/methods && ln -fs ../../bin %{buildroot}%{_libdir}/%{name}/methods
rm -f %{buildroot}%{_libdir}/pkcs11/methods && ln -fs ../../bin %{buildroot}%{_libdir}/pkcs11/methods
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check
%pre

%global cfile /etc/opencryptoki/opencryptoki.conf
%global csuffix .rpmsave.XyoP
if test $1 -gt 1 && test -f %{cfile} ; then
    cp -p %{cfile} %{cfile}%{csuffix}
fi
%pre libs

%sysusers_create_compat %{SOURCE2}
%post

if test $1 -gt 1 && test -f %{cfile} ; then
    if ( ! cmp -s %{cfile} %{cfile}%{csuffix} ) ; then
        cp -p %{cfile} %{cfile}.rpmnew
    fi
    cp -p %{cfile}%{csuffix} %{cfile} && rm -f %{cfile}%{csuffix}
fi
%systemd_post pkcsslotd.service
if test $1 -eq 1; then
	%tmpfiles_create %{name}.conf
fi
%preun

%systemd_preun pkcsslotd.service
%postun

%systemd_postun_with_restart pkcsslotd.service
%files -f %{oreon_filedir}/main.list
%files -n opencryptoki-libs -f %{oreon_filedir}/opencryptoki-libs.list
%files -n opencryptoki-devel -f %{oreon_filedir}/opencryptoki-devel.list
%files -n opencryptoki-swtok -f %{oreon_filedir}/opencryptoki-swtok.list
%files -n opencryptoki-tpmtok -f %{oreon_filedir}/opencryptoki-tpmtok.list
%files -n opencryptoki-icsftok -f %{oreon_filedir}/opencryptoki-icsftok.list
%files -n opencryptoki-icatok -f %{oreon_filedir}/opencryptoki-icatok.list
%files -n opencryptoki-ccatok -f %{oreon_filedir}/opencryptoki-ccatok.list
%files -n opencryptoki-ep11tok -f %{oreon_filedir}/opencryptoki-ep11tok.list

%changelog

%autochangelog
