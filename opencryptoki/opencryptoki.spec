Name: opencryptoki
Summary: Implementation of the PKCS#11 (Cryptoki) specification v3.0 and partially v3.1
Version: 3.26.0
Release: 2%{?dist}
License: CPL-1.0
URL: https://github.com/opencryptoki/opencryptoki
Source0: https://github.com/opencryptoki/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# p11-kit default path
Source1: opencryptoki.module
# sysusers.d config file to allow rpm to create users/groups automatically
Source2: opencryptoki.sysusers.conf

# fix install problem in buildroot
Patch1: opencryptoki-3.25.0-p11sak.patch

# tmpfiles.d config files for image mode
Patch2: opencryptoki-3.24.0-tmpfiles-image-mode.patch

# everything using /var/lock should be fixed in the end to use /run/lock
# https://gitlab.com/fedora/bootc/base-images/-/issues/48
Patch3: opencryptoki-lockdir-image-mode.patch

Requires(pre): coreutils
Requires: (selinux-policy >= 34.9-1 if selinux-policy-targeted)
BuildRequires: gcc gcc-c++
BuildRequires: openssl-devel >= 3.5.1
# testcases require 'openssl' command line tool
BuildRequires: openssl >= 3.5.1
# testcases require 'jq' command line tool
BuildRequires: jq 
%if 0%{?tmptok}
BuildRequires: trousers-devel
%endif
BuildRequires: openldap-devel
BuildRequires: autoconf automake libtool
BuildRequires: bison flex
BuildRequires: libcap-devel
BuildRequires: expect
BuildRequires: make
# sysusers_create_compat macro
BuildRequires: systemd-rpm-macros
%{?sysusers_requires_compat}
%ifarch s390 s390x
BuildRequires: libica-devel >= 3.3
# for /usr/include/libudev.h
BuildRequires: systemd-devel
%endif
Requires: openssl >= 1:3.5.1
Requires(pre): %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}(token)
Requires(post): systemd diffutils
Requires(preun): systemd
Requires(postun): systemd


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
%autosetup -p1


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

# Install sysusers.d config file
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/%{name}.sysusers.conf

# Install tmpfiles.d config files
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

# convert absolute links to relative links.
rm -f %{buildroot}%{_libdir}/%{name}/methods && ln -fs ../../bin %{buildroot}%{_libdir}/%{name}/methods
rm -f %{buildroot}%{_libdir}/pkcs11/methods && ln -fs ../../bin %{buildroot}%{_libdir}/pkcs11/methods

%check
make check

%pre
# don't touch opencryptoki.conf even if it is unchanged due to new tokversion
# backup config file. bz#2044179
%global cfile /etc/opencryptoki/opencryptoki.conf
%global csuffix .rpmsave.XyoP
if test $1 -gt 1 && test -f %{cfile} ; then
    cp -p %{cfile} %{cfile}%{csuffix}
fi

%pre libs
%sysusers_create_compat %{SOURCE2}

%post
# restore the config file from %pre
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


%files
%doc ChangeLog FAQ README.md
%doc doc/opencryptoki-howto.md
%doc doc/README.token_data
%doc %{_docdir}/%{name}/*.conf
%dir %{_sysconfdir}/%{name}
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%verify(not md5 size mtime) %attr(0640, root, pkcs11) %config(noreplace) %{_sysconfdir}/%{name}/p11sak_defined_attrs.conf
%verify(not md5 size mtime) %attr(0640, root, pkcs11) %config(noreplace) %{_sysconfdir}/%{name}/strength.conf
%verify(not md5 size mtime) %attr(0640, root, pkcs11) %config(noreplace) %{_sysconfdir}/%{name}/p11kmip.conf
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/pkcsslotd.service
%{_sbindir}/p11sak
%{_sbindir}/p11kmip
%{_sbindir}/pkcstok_migrate
%{_sbindir}/pkcsconf
%{_sbindir}/pkcsslotd
%{_sbindir}/pkcsstats
%{_sbindir}/pkcshsm_mk_change
%{_sbindir}/pkcstok_admin
%{_mandir}/man1/p11sak.1*
%{_mandir}/man1/pkcstok_migrate.1*
%{_mandir}/man1/pkcsconf.1*
%{_mandir}/man1/p11kmip.1*
%{_mandir}/man1/pkcsstats.1*
%{_mandir}/man1/pkcshsm_mk_change.1*
%{_mandir}/man1/pkcstok_admin.1*
%{_mandir}/man5/policy.conf.5*
%{_mandir}/man5/strength.conf.5*
%{_mandir}/man5/p11kmip.conf.5*
%{_mandir}/man5/%{name}.conf.5*
%{_mandir}/man5/p11sak_defined_attrs.conf.5*
%{_mandir}/man7/%{name}.7*
%{_mandir}/man8/pkcsslotd.8*
%{_libdir}/opencryptoki/methods
%{_libdir}/pkcs11/methods
%dir %attr(770,root,pkcs11) %{_sharedstatedir}/%{name}
%dir %attr(770,root,pkcs11) %{_sharedstatedir}/%{name}/HSM_MK_CHANGE
%ghost %dir %attr(770,root,pkcs11) %{_rundir}/lock/%{name}
%ghost %dir %attr(770,root,pkcs11) %{_rundir}/lock/%{name}/*
%dir %attr(710,pkcsslotd,pkcs11) /run/%{name}

%files libs
%license LICENSE
%{_sysconfdir}/ld.so.conf.d/*
# Unversioned .so symlinks usually belong to -devel packages, but opencryptoki
# needs them in the main package, because:
#   documentation suggests that programs should dlopen "PKCS11_API.so".
%dir %{_libdir}/opencryptoki
%{_libdir}/opencryptoki/libopencryptoki.*
%{_libdir}/opencryptoki/PKCS11_API.so
%dir %{_libdir}/opencryptoki/stdll
%dir %{_libdir}/pkcs11
%{_libdir}/pkcs11/libopencryptoki.so
%{_libdir}/pkcs11/PKCS11_API.so
%{_libdir}/pkcs11/stdll
%dir %attr(770,root,pkcs11) %{_localstatedir}/log/opencryptoki
%{_sysusersdir}/%{name}.sysusers.conf

%files devel
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%files swtok
%{_libdir}/opencryptoki/stdll/libpkcs11_sw.*
%{_libdir}/opencryptoki/stdll/PKCS11_SW.so
%dir %attr(770,root,pkcs11) %{_sharedstatedir}/%{name}/swtok/
%dir %attr(770,root,pkcs11) %{_sharedstatedir}/%{name}/swtok/TOK_OBJ/
%{_tmpfilesdir}/%{name}-swtok.conf

%if 0%{?tmptok}
%files tpmtok
%doc doc/README.tpm_stdll
%{_libdir}/opencryptoki/stdll/libpkcs11_tpm.*
%{_libdir}/opencryptoki/stdll/PKCS11_TPM.so
%dir %attr(770,root,pkcs11) %{_sharedstatedir}/%{name}/tpm/
%{_tmpfilesdir}/%{name}-tpmtok.conf
%endif

%files icsftok
%doc doc/README.icsf_stdll
%{_sbindir}/pkcsicsf
%{_mandir}/man1/pkcsicsf.1*
%{_libdir}/opencryptoki/stdll/libpkcs11_icsf.*
%{_libdir}/opencryptoki/stdll/PKCS11_ICSF.so
%dir %attr(770,root,pkcs11) %{_sharedstatedir}/%{name}/icsf/
%{_tmpfilesdir}/%{name}-icsftok.conf

%ifarch s390 s390x
%files icatok
%{_libdir}/opencryptoki/stdll/libpkcs11_ica.*
%{_libdir}/opencryptoki/stdll/PKCS11_ICA.so
%dir %attr(770,root,pkcs11) %{_sharedstatedir}/%{name}/lite/
%dir %attr(770,root,pkcs11) %{_sharedstatedir}/%{name}/lite/TOK_OBJ/
%{_tmpfilesdir}/%{name}-icatok.conf
%endif

%ifarch s390 s390x x86_64 ppc64le
%files ccatok
%doc doc/README.cca_stdll
%config(noreplace) %{_sysconfdir}/%{name}/ccatok.conf
%{_sbindir}/pkcscca
%{_mandir}/man1/pkcscca.1*
%{_libdir}/opencryptoki/stdll/libpkcs11_cca.*
%{_libdir}/opencryptoki/stdll/PKCS11_CCA.so
%dir %attr(770,root,pkcs11) %{_sharedstatedir}/%{name}/ccatok/
%dir %attr(770,root,pkcs11) %{_sharedstatedir}/%{name}/ccatok/TOK_OBJ/
%{_tmpfilesdir}/%{name}-ccatok.conf
%endif

%ifarch s390 s390x
%files ep11tok
%doc doc/README.ep11_stdll
%config(noreplace) %{_sysconfdir}/%{name}/ep11tok.conf
%config(noreplace) %{_sysconfdir}/%{name}/ep11cpfilter.conf
%{_sbindir}/pkcsep11_migrate
%{_sbindir}/pkcsep11_session
%{_mandir}/man1/pkcsep11_migrate.1*
%{_mandir}/man1/pkcsep11_session.1*
%{_libdir}/opencryptoki/stdll/libpkcs11_ep11.*
%{_libdir}/opencryptoki/stdll/PKCS11_EP11.so
%dir %attr(770,root,pkcs11) %{_sharedstatedir}/%{name}/ep11tok/
%dir %attr(770,root,pkcs11) %{_sharedstatedir}/%{name}/ep11tok/TOK_OBJ/
%{_tmpfilesdir}/%{name}-ep11tok.conf
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.26.0-2
- Prepare for Oreon 11 (RP1)
