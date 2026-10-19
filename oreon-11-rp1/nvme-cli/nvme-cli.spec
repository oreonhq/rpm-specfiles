%global source0_hash 8a6879f1f2af53743c03a8f77f247261306300d3f3b0edfd242c5f646bdfdccb
%{!?version_no_tilde: %define version_no_tilde %{shrink:%(echo '%{version}' | tr '~' '-')}}
%global nmlibdir %{_prefix}/lib/NetworkManager
Name:           nvme-cli
Version:        3.1
Release:        1%{?dist}
Summary:        NVMe management command line interface
License:        GPL-2.0-only
URL:            https://github.com/linux-nvme/nvme-cli
Source0:        https://github.com/linux-nvme/nvme-cli/archive/refs/tags/v%{version}.tar.gz#/nvme-cli-%{version}.tar.gz
Source1:        99-nvme-nbft-connect.sh
Source2:        99-nvme-nbft-no-ignore-carrier.conf
Requires:       util-linux
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  json-c-devel
BuildRequires:  libnvme-devel
BuildRequires:  meson
BuildRequires:  openssl-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  xmlto
BuildRequires:  zlib-devel
# /oreon:deps
%description
nvme-cli provides NVM-Express user space tooling for Linux.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{version_no_tilde}

%build

%meson -Dudevrulesdir=%{_udevrulesdir} -Dsystemddir=%{_unitdir} -Ddocs=all -Ddocs-build=true -Dhtmldir=%{_pkgdocdir}
%meson_build
%install
%meson_install
%{__install} -pm 644 README.md %{buildroot}%{_pkgdocdir}
mkdir -p $RPM_BUILD_ROOT%{nmlibdir}/dispatcher.d
mkdir -p $RPM_BUILD_ROOT%{nmlibdir}/conf.d
%{__install} -pm 755 %{SOURCE1} $RPM_BUILD_ROOT%{nmlibdir}/dispatcher.d/
%{__install} -pm 644 %{SOURCE2} $RPM_BUILD_ROOT%{nmlibdir}/conf.d/
rm -f %{buildroot}%{_sysconfdir}/nvme/hostid
rm -f %{buildroot}%{_sysconfdir}/nvme/hostnqn
rm -f %{buildroot}/usr/lib/dracut/dracut.conf.d/70-nvmf-autoconnect.conf
mv %{buildroot}%{_pkgdocdir}/nvme %{buildroot}%{_pkgdocdir}/html
rm -rf %{buildroot}%{_pkgdocdir}/nvme
%oreon_autofiles main

%post

%systemd_post nvmefc-boot-connections.service
%systemd_post nvmf-autoconnect.service
%systemd_post nvmf-connect@.service
%systemd_post nvmf-connect-nbft.service
if [ -S /run/udev/control ]; then
    udevadm control --reload
    udevadm trigger
fi
%preun

%systemd_preun nvmefc-boot-connections.service
%systemd_preun nvmf-autoconnect.service
%systemd_preun nvmf-connect@.service
%systemd_preun nvmf-connect-nbft.service
%postun

%systemd_postun nvmefc-boot-connections.service
%systemd_postun nvmf-autoconnect.service
%systemd_postun nvmf-connect@.service
%systemd_postun nvmf-connect-nbft.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
