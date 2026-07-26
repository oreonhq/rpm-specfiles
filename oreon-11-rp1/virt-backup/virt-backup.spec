%global source0_hash ddd28bba65ebfa6004da8b8687d6592c1d27876c859dfa25f8bfcb6a2fe100de

Name:           virt-backup
Version:        0.2.25
Release:        16%{?dist}
Summary:        Backup script for libvirt managed VM

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://git.fws.fr/fws/virt-backup
Source0:        https://git.fws.fr/fws/%{name}/archive/%{name}-%{version}-1.tar.gz

# Working with upstream to be more packager & distro friendly.
Patch0:         virt-backup-update.patch

BuildArch:      noarch

BuildRequires:  perl-generators

Requires:       bzip2
Requires:       chunkfs
Requires:       gzip
Requires:       lvm2
Requires:       lzop
Requires:       qemu-img
Requires:       util-linux
Requires:       xz

%description
This script allows you to backup Virtual Machines managed by libvirt.
It has only be tested with KVM based VM
This script will dump (or mount as a set of chunks):
 * each block devices
 * optionnally the memory (if --state flag is given)
 * the XML description of the VM

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}

%build
# Nothing to build

%install
# Install backup script
mkdir -p %{buildroot}%{_bindir}
install -m 0755 virt-backup %{buildroot}%{_bindir}/

# Create backup dir
mkdir -p %{buildroot}%{_sharedstatedir}/libvirt/backup

%files
%doc README
%license COPYING
%{_bindir}/%{name}
%dir %attr(0770, qemu, qemu) %{_sharedstatedir}/libvirt/backup

%changelog
%autochangelog
