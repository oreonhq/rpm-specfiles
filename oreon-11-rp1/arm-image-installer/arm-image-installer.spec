%global source0_hash 3092f98f9d23db8ec9262a4fbd5960193617a5430f3b037e793422a2aa3c6e90

Name:		arm-image-installer
Version:	5.3
Release:	3%{?dist}
Summary:	Writes binary image files to any specified block device
License:	GPL-2.0-or-later
URL:		https://github.com/fedora-arm/arm-image-installer/
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch
Requires:	btrfs-progs
Requires:	e2fsprogs
Requires:	libselinux-utils
Requires:	parted
Requires:	sudo
Requires:	util-linux
Requires:	xfsprogs
Requires:	xz

%description
Allows one to first select a source image (local or remote). The image must be
a binary file containing: [MBR + Partitions + File Systems + Data]. A
destination block device should then be selected for final installation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
echo "skipping..."

%install
install -d %{buildroot}%{_datadir}/arm-image-installer
install -d %{buildroot}%{_datadir}/arm-image-installer/socs.d
install -pm 644 socs.d/* %{buildroot}%{_datadir}/arm-image-installer/socs.d/
install -d %{buildroot}%{_datadir}/arm-image-installer/boards.d
install -pm 644 boards.d/* %{buildroot}%{_datadir}/arm-image-installer/boards.d/

install -d %{buildroot}%{_bindir}
install -pm 0755 arm-image-installer %{buildroot}%{_bindir}/
install -pm 0755 rpi-uboot-update %{buildroot}%{_bindir}/
install -pm 0755 spi-flashing-disk %{buildroot}%{_bindir}/
install -pm 0755 update-uboot %{buildroot}%{_bindir}/
install -pm 0755 update-x13s-bios %{buildroot}%{_bindir}/
ln -s /usr/bin/arm-image-installer %{buildroot}%{_bindir}/fedora-arm-image-installer

%files
%license COPYING
%doc AUTHORS README TODO SUPPORTED-BOARDS
%{_bindir}/arm-image-installer
%{_bindir}/fedora-arm-image-installer
%{_bindir}/rpi-uboot-update
%{_bindir}/spi-flashing-disk
%{_bindir}/update-uboot
%{_bindir}/update-x13s-bios
%{_datadir}/arm-image-installer/

%changelog
%autochangelog
