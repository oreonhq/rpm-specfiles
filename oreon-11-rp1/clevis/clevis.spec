%global source0_hash 466e9e87fddeb2531259cacd8e19de23cef7c6992ee835a643dad585fc45018f
Name:           clevis
Version:        23
Release:        1%{?dist}
Summary:        Automated decryption framework
License:        GPL-3.0-or-later
URL:            https://github.com/latchset/%{name}
Source0:        https://github.com/latchset/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        clevis.sysusers
Requires:       tpm2-tools >= 4.0.0
Requires:       coreutils
Requires:       jose >= 8
Requires:       curl
Requires:       jq
Requires(post): systemd
Requires:       clevis-pin-tpm2
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  audit-libs-devel
BuildRequires:  bash-completion
BuildRequires:  bash-completion-devel
BuildRequires:  cryptsetup
BuildRequires:  curl
BuildRequires:  desktop-file-utils
BuildRequires:  diffutils
BuildRequires:  dracut
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  jq
BuildRequires:  libjose-devel
BuildRequires:  libluksmeta-devel
BuildRequires:  libudisks2-devel
BuildRequires:  luksmeta
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  opensc
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  pcsc-lite
BuildRequires:  pkgconfig
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  tang
BuildRequires:  tpm2-tools
# /oreon:deps
%description
Clevis is a framework for automated decryption. It allows you to encrypt
data using sophisticated unlocking policies which enable decryption to
occur automatically.

The clevis package provides basic encryption/decryption policy support.
Users can use this directly; but most commonly, it will be used as a
building block for other packages. For example, see the clevis-luks
and clevis-dracut packages for automatic root volume unlocking of
LUKSv1/LUKSv2 volumes during early boot.

%package luks
Summary:        LUKS integration for clevis
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cryptsetup
Requires:       luksmeta >= 8
%description luks
LUKS integration for clevis. This package allows you to bind a LUKS
volume to a clevis unlocking policy. For automated unlocking, an unlocker
will also be required. See, for example, clevis-dracut and clevis-udisks2.

%package systemd
Summary:        systemd integration for clevis
Requires:       %{name}-luks%{?_isa} = %{version}-%{release}
Requires:       systemd%{?_isa} >= 236
%description systemd
Automatically unlocks LUKS _netdev block devices from /etc/crypttab.

%package dracut
Summary:        Dracut integration for clevis
Requires:       %{name}-systemd%{?_isa} = %{version}-%{release}
Requires:       dracut-network
%description dracut
Automatically unlocks LUKS block devices in early boot.

%package udisks2
Summary:        UDisks2/Storaged integration for clevis
Requires:       %{name}-luks%{?_isa} = %{version}-%{release}
%description udisks2
Automatically unlocks LUKS block devices in desktop environments that
use UDisks2 or storaged (like GNOME).

%package pin-pkcs11
Summary:        PKCS#11 for clevis
Requires:       %{name}-systemd%{?_isa} = %{version}-%{release}
Requires:       %{name}-luks%{?_isa} = %{version}-%{release}
Requires:       %{name}-dracut%{?_isa} = %{version}-%{release}
Requires:       pcsc-lite
Requires:       opensc
Requires:       socat
Requires:       openssl
%description pin-pkcs11
Automatically unlocks LUKS block devices through a PKCS#11 device.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Duser=clevis -Dgroup=clevis
%meson_build
%install
%meson_install
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/clevis.conf
%oreon_autofiles clevis-luks usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles clevis-systemd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles clevis-dracut usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles clevis-udisks2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles clevis-pin-pkcs11 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate \
  %{buildroot}/%{_sysconfdir}/xdg/autostart/%{name}-luks-udisks2.desktop
%meson_test
%post systemd

systemctl preset %{name}-luks-askpass.path >/dev/null 2>&1 || :
%files -f %{oreon_filedir}/main.list
%files -n clevis-luks -f %{oreon_filedir}/clevis-luks.list
%files -n clevis-systemd -f %{oreon_filedir}/clevis-systemd.list
%files -n clevis-dracut -f %{oreon_filedir}/clevis-dracut.list
%files -n clevis-udisks2 -f %{oreon_filedir}/clevis-udisks2.list
%files -n clevis-pin-pkcs11 -f %{oreon_filedir}/clevis-pin-pkcs11.list

%changelog

%autochangelog
