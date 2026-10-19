%global source1_hash 29576c617ba8396faee093a1fa73e23497df7fc9f1315f6d719d910e9e0d0ac9
%global source0_hash 596150b677a200d08785c0327b8f77beb2ac3b165a1d4075993ddfa219756f09
Name:           archlinux-keyring
Version:        20260909
Release:        1%{?dist}
Url:            https://archlinux.org/packages/core/any/archlinux-keyring/
Source0:        https://gitlab.archlinux.org/archlinux/archlinux-keyring/-/archive/%{version}/archlinux-keyring-%{version}.tar.gz
Source1:        https://gitlab.archlinux.org/archlinux/archlinux-keyring/-/releases/%{version}/downloads/archlinux-keyring-%{version}.tar.gz.sig
Source2:        gpgkey-02FD1C7A934E614545849F19A6234074498E9CEE.gpg
License:        LicenseRef-Fedora-Public-Domain
Summary:        GPG keys used by Arch Linux distribution to sign packages
BuildArch:      noarch
%if 0%{?el9}
%else
%endif
Requires:       pacman-filesystem
Requires:       keyrings-filesystem
# oreon:deps
BuildRequires:  keyrings-filesystem
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  sequoia-sq
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
A set of GPG keys used to sign packages in the Arch distribution, which can
be used to verify that downloaded Arch packages are valid.

This package simply packages the GPG keyring as published by Arch developers
into an RPM package to allow for safe and convenient installation on Fedora
systems.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sq verify --signer-file=%{SOURCE2} --message %{SOURCE1} --output tmp.tar.gz
tar -xvf tmp.tar.gz

%if 0%{?el9}
sed -i 's|/usr/bin/env python3|/usr/bin/env python3.11|' keyringctl
%endif

%build

mkdir build
make wkd_sync_service SCRIPT_TARGET_DIR=%{_bindir}
%install
install -Dt %{buildroot}%{_bindir}/ wkd_sync/archlinux-keyring-wkd-sync
install -Dt %{buildroot}%{_unitdir}/ \
  wkd_sync/archlinux-keyring-wkd-sync.timer \
  build/archlinux-keyring-wkd-sync.service
install -m0644 -Dt %{buildroot}%{_datadir}/pacman/keyrings/ \
  archlinux-keyring-%{version}/{archlinux.gpg,archlinux-revoked,archlinux-trusted}
mkdir -p %{buildroot}%{_keyringsdir}/
ln --relative -s %{_datadir}/pacman/keyrings/archlinux.gpg %{buildroot}%{_keyringsdir}/
%oreon_autofiles main

%posttrans

if [ $1 == 1 ] && [ -x /usr/bin/pacman-key ] && ! /usr/bin/pacman-key -l &>/dev/null; then
    /usr/bin/pacman-key --init && \
    /usr/bin/pacman-key --populate archlinux --updatedb || :
fi
%transfiletriggerin -- /usr/bin/pacman-key
if [ -x /usr/bin/pacman-key ] && ! /usr/bin/pacman-key -l &>/dev/null; then
    /usr/bin/pacman-key --init && \
    /usr/bin/pacman-key --populate archlinux --updatedb || :
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
