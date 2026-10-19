%global source0_hash 0cf0633b1d4bdc890e4cf0f0f2cc4bd6a5caa31963f41d6dd75f2bf5e97dfd17
Name:    nvme-stas
Summary:        NVMe STorage Appliance Services
Version: 3.1
Release:        1%{?dist}
License: Apache-2.0
URL:     https://github.com/linux-nvme/nvme-stas
Source0:        https://github.com/linux-nvme/nvme-stas/archive/refs/tags/v%{version}.tar.gz#/nvme-stas-%{version}.tar.gz
BuildArch:     noarch
Requires:      avahi
Requires:      python3-libnvme >= 1.12
Requires:      python3-dasbus
Requires:      python3-pyudev
Requires:      python3-systemd
Requires:      python3-gobject
Requires:      python3-lxml
# oreon:deps
BuildRequires:  docbook-style-xsl
BuildRequires:  glib2-devel
BuildRequires:  libnvme-devel
BuildRequires:  libxslt
BuildRequires:  meson
BuildRequires:  python3-dasbus
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel
BuildRequires:  python3-libnvme
BuildRequires:  python3-lxml
BuildRequires:  python3-pyudev
BuildRequires:  python3-systemd
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
nvme-stas is a Central Discovery Controller (CDC) client for Linux. It
handles Asynchronous Event Notifications (AEN), Automated NVMe subsystem
connection controls, Error handling and reporting, and Automatic (zeroconf)
and Manual configuration. nvme-stas is composed of two daemons:
stafd (STorage Appliance Finder) and stacd (STorage Appliance Connector).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{version_no_tilde}

%build

%meson -Dman=true -Dhtml=true
%meson_build
%install
%meson_install
%oreon_autofiles main

%post

%systemd_post stacd.service
%systemd_post stafd.service
%preun

%systemd_preun stacd.service
%systemd_preun stafd.service
%postun

%systemd_postun_with_restart stacd.service
%systemd_postun_with_restart stafd.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
