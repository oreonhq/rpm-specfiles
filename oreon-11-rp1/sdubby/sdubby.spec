%global source0_hash none
Name: sdubby
Version: 1.0
Release:        14%{?dist}
Summary:        Set of systemd-boot shims that don't fit anywhere else in the distro
License: GPL-2.0-or-later
URL:	 https://pagure.io/sdubby.git
BuildArchitectures: noarch
ExclusiveArch: %{efi}
Source1: updateloaderentries.sh
Source2: COPYING
Source3: entries.srel
Source4: updateloaderentries.8
Source5: README.md
Source6: install.conf
Requires: findutils
Requires: util-linux
Requires: systemd-boot
Requires: gawk
Requires: coreutils
Conflicts: grubby
# oreon:deps
BuildRequires:  gzip
# /oreon:deps
%description
This package provides a place to drop systemd-boot shimming
utilities that don't yet have a better place to live. The name
is a play on the grubby package which performs a similar function
for grub2.

%prep

# Make sure the license can be found in mock
cp %{SOURCE2} . || true
cp %{SOURCE5} . || true

%build

%install
mkdir -p %{buildroot}%{_sbindir}/
install -T -m 0755 %{SOURCE1} %{buildroot}%{_sbindir}/updateloaderentries
install --directory %{buildroot}%{efi_esp_root}/loader
install --directory %{buildroot}%{efi_esp_root}/loader/entries
install -T -m 444 %{SOURCE3} %{buildroot}%{efi_esp_root}/loader/entries.srel
ln -sr %{buildroot}%{_sbindir}/updateloaderentries %{buildroot}%{_sbindir}/grubby
install -TD -m 444 %{SOURCE4} %{buildroot}%{_mandir}/man8/updateloaderentries.8
gzip %{buildroot}%{_mandir}/man8/updateloaderentries.8
install -TD -m 444 %{SOURCE6} %{buildroot}%{_sysconfdir}/kernel/install.conf
%oreon_autofiles main

%post

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
