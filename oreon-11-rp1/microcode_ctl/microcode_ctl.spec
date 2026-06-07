%global source0_hash 75fd729182e56a51bc7a6a5becf49b0b266e20cd0c4355f0b490d06aa0d4ba2c

%define upstream_version 2.1-51
%global debug_package %{nil}

Summary:        Tool to transform and deploy CPU microcode update for x86
Name:           microcode_ctl
Version:        2.1
Release:        74%{?dist}
Epoch:          2
License:        GPL-2.0-or-later AND LicenseRef-Fedora-Firmware
URL:            https://pagure.io/microcode_ctl
Source0:        microcode_ctl-%{upstream_version}.tar.xz
ExclusiveArch:  %{ix86} x86_64
BuildRequires: make

%description
The microcode_ctl utility is a companion to the microcode driver written
by Tigran Aivazian <tigran@aivazian.fsnet.co.uk>.

The microcode update is volatile and needs to be uploaded on each system
boot i.e. it doesn't reflash your cpu permanently, reboot and it reverts
back to the old microcode.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n microcode_ctl-2.1-51

%build
make CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} PREFIX=%{_prefix} INSDIR=/usr/sbin install clean

%files
/lib/firmware/*
%dir /usr/share/doc/microcode_ctl
%doc /usr/share/doc/microcode_ctl/*


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2:2.1-74
- Import
