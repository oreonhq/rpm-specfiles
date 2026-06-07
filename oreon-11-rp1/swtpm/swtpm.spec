%global source0_hash f8da11cadfed27e26d26c5f58a7b8f2d14d684e691927348906b5891f525c684

%bcond_without gnutls

# Macros needed by SELinux
%global selinuxtype targeted
%global moduletype  contrib
%global modulename  swtpm

Summary: TPM Emulator
Name:           swtpm
Version:        0.10.1
Release:        3%{?dist}
License:        BSD-3-Clause
Url:            https://github.com/stefanberger/swtpm
Source0:        https://github.com/stefanberger/swtpm/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# tests: Retry NVWrite command after 0x922 return code and inc lockout counter
Patch0:        4da66c66f92438443e66b67555673c9cb898b0ae.patch

BuildRequires: make
BuildRequires:  git-core
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  libtpms-devel >= 0.6.0
BuildRequires:  expect
BuildRequires:  net-tools
BuildRequires:  openssl-devel
BuildRequires:  socat
BuildRequires:  tpm2-tss
BuildRequires:  softhsm
BuildRequires:  json-glib-devel
%if %{with gnutls}
BuildRequires:  gnutls >= 3.4.0
BuildRequires:  gnutls-devel
BuildRequires:  gnutls-utils
BuildRequires:  libtasn1-devel
BuildRequires:  libtasn1
%endif
BuildRequires:  selinux-policy-devel
BuildRequires:  gcc
BuildRequires:  libseccomp-devel
BuildRequires:  tpm2-pkcs11 tpm2-pkcs11-tools tpm2-tools tpm2-abrmd
BuildRequires:  python3-devel
BuildRequires:  gmp-devel

Requires:       %{name}-libs = %{version}-%{release}
Requires:       libtpms >= 0.10.0
Requires:       (%{name}-selinux if selinux-policy-targeted)

%description
TPM emulator built on libtpms providing TPM functionality for QEMU VMs

%package        libs
Summary:        Private libraries for swtpm TPM emulators
License:        BSD-3-Clause

%description    libs
A private library with callback functions for libtpms based swtpm TPM emulator

%package        devel
Summary:        Include files for the TPM emulator's CUSE interface for usage by clients
License:        BSD-3-Clause
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
Include files for the TPM emulator's CUSE interface.

%package        tools
Summary:        Tools for the TPM emulator
License:        BSD-3-Clause
Requires:       swtpm = %{version}-%{release}
# tpm2-tss for tss account
Requires:       tpm2-tss bash gnutls-utils

%description    tools
Tools for the TPM emulator from the swtpm package

%package        tools-pkcs11
Summary:        Tools for creating a local CA based on a TPM pkcs11 device
License:        BSD-3-Clause
Requires:       swtpm-tools = %{version}-%{release}
Requires:       tpm2-pkcs11 tpm2-pkcs11-tools tpm2-tools tpm2-abrmd
Requires:       expect gnutls-utils

%description   tools-pkcs11
Tools for creating a local CA based on a pkcs11 device

%package        selinux
Summary:        SELinux security policy for swtpm
Requires(post): swtpm = %{version}-%{release}
BuildArch:      noarch
%if ! 0%{?flatpak}
%{?selinux_requires}
%endif

%description    selinux
SELinux security policy for swtpm.

%package        tests
Summary:        Installed swtpm tests
Requires:       swtpm-tools-pkcs11 = %{version}-%{release}

%description    tests
Installed swtpm tests

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git -n %{name}-%{version} -p1

%build

NOCONFIGURE=1 ./autogen.sh
%configure \
%if %{with gnutls}
        --with-gnutls \
%endif
        --without-cuse

%make_build

%check
make %{?_smp_mflags} check VERBOSE=1

%install

%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/*.{a,la,so}

%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%{selinux_modules_install -s %{selinuxtype} %{shrink:
    /usr/share/selinux/packages/swtpm.pp
    /usr/share/selinux/packages/swtpm_svirt.pp
    /usr/share/selinux/packages/swtpm_libvirt.pp} }
restorecon %{_bindir}/swtpm

%postun selinux
if [ $1 -eq  0 ]; then
  %selinux_modules_uninstall -s %{selinuxtype} swtpm_svirt swtpm_libvirt swtpm
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}

%ldconfig_post libs
%ldconfig_postun libs

%files
%license LICENSE
%doc README
%{_bindir}/swtpm
%{_mandir}/man8/swtpm.8*

%files selinux
%{_datadir}/selinux/packages/swtpm.pp
%{_datadir}/selinux/packages/swtpm_libvirt.pp
%{_datadir}/selinux/packages/swtpm_svirt.pp

%files libs
%license LICENSE
%doc README

%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libswtpm_libtpms.so.0
%{_libdir}/%{name}/libswtpm_libtpms.so.0.0.0

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_mandir}/man3/swtpm_ioctls.3*

%files tools
%doc README
%{_bindir}/swtpm_bios
%if %{with gnutls}
%{_bindir}/swtpm_cert
%endif
%{_bindir}/swtpm_setup
%{_bindir}/swtpm_ioctl
%{_bindir}/swtpm_localca
%{_mandir}/man5/swtpm-localca.conf.5*
%{_mandir}/man5/swtpm-localca.options.5*
%{_mandir}/man5/swtpm_setup.conf.5*
%{_mandir}/man8/swtpm_bios.8*
%{_mandir}/man8/swtpm_cert.8*
%{_mandir}/man8/swtpm_ioctl.8*
%{_mandir}/man8/swtpm-localca.8*
%{_mandir}/man8/swtpm_localca.8*
%{_mandir}/man8/swtpm_setup.8*
%config(noreplace) %{_sysconfdir}/swtpm_setup.conf
%config(noreplace) %{_sysconfdir}/swtpm-localca.options
%config(noreplace) %{_sysconfdir}/swtpm-localca.conf
%dir %{_datadir}/swtpm
%{_datadir}/swtpm/swtpm-localca
%{_datadir}/swtpm/swtpm-create-user-config-files
%attr( 750, tss, root) %{_localstatedir}/lib/swtpm-localca

%files tools-pkcs11
%{_mandir}/man8/swtpm-create-tpmca.8*
%{_datadir}/swtpm/swtpm-create-tpmca

%files tests
%{_libexecdir}/installed-tests/swtpm/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.10.1-3
- Prepare for Oreon 11 (RP1)
