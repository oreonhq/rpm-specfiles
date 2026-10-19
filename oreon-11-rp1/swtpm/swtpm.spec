%global source0_hash f61cf6f1e9bbcb4cefb30b70cafaf1c4df54c6961e65cfa63830e8ad0e220134
%bcond_without gnutls
%global selinuxtype targeted
%global moduletype  contrib
%global modulename  swtpm
Summary:        TPM Emulator
Name:           swtpm
Version:        0.10.2
Release:        1%{?dist}
License:        BSD-3-Clause
Url:            https://github.com/stefanberger/swtpm
Source0:        https://github.com/stefanberger/swtpm/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%if %{with gnutls}
%endif
Requires:       %{name}-libs = %{version}-%{release}
Requires:       libtpms >= 0.10.0
Requires:       (%{name}-selinux if selinux-policy-targeted)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  expect
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  gmp-devel
BuildRequires:  gnutls
BuildRequires:  gnutls-devel
BuildRequires:  gnutls-utils
BuildRequires:  json-glib-devel
BuildRequires:  libseccomp-devel
BuildRequires:  libtasn1
BuildRequires:  libtasn1-devel
BuildRequires:  libtool
BuildRequires:  libtpms-devel
BuildRequires:  make
BuildRequires:  net-tools
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(systemd)
BuildRequires:  python3-devel
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildRequires:  socat
BuildRequires:  softhsm
BuildRequires:  tpm2-abrmd
BuildRequires:  tpm2-pkcs11
BuildRequires:  tpm2-pkcs11-tools
BuildRequires:  tpm2-tools
BuildRequires:  tpm2-tss
# /oreon:deps
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
%global oreon_srcdir %{name}-%{version}
%oreon_prep
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

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
%files -f %{oreon_filedir}/main.list
%files -n swtpm-libs -f %{oreon_filedir}/swtpm-libs.list
%files -n swtpm-devel -f %{oreon_filedir}/swtpm-devel.list
%files -n swtpm-tools -f %{oreon_filedir}/swtpm-tools.list
%files -n swtpm-tools-pkcs11 -f %{oreon_filedir}/swtpm-tools-pkcs11.list
%files -n swtpm-selinux -f %{oreon_filedir}/swtpm-selinux.list
%files -n swtpm-tests -f %{oreon_filedir}/swtpm-tests.list

%changelog

%autochangelog
