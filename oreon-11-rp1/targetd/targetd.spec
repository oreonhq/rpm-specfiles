%global source0_hash 1590ea211ee187e07ba019d2a359c83ca07ec10c05696eff951aaaf719b844bb

Name:           targetd
License:        GPL-3.0-only
Summary:        Service to make storage remotely configurable
Version:        0.10.4
Release:        11%{?dist}
URL:            https://github.com/open-iscsi/targetd
Source:         https://github.com/open-iscsi/targetd/archive/v%{version}/targetd-%{version}.tar.gz
Source1:        targetd.service
Patch1:         0001_rtslib_fb_api_fix.patch
BuildArch:      noarch
BuildRequires:  systemd-rpm-macros
BuildRequires:  python3-devel python3-gobject-base python3-blockdev libblockdev-lvm
Requires:       python3-PyYAML python3-setproctitle python3-rtslib target-restore
Requires:       nfs-utils, btrfs-progs, python3-blockdev, libblockdev-lvm 

%description
targetd turns the machine into a remotely-configurable storage appliance.
It supports an HTTP/jsonrpc-2.0 interface to let a remote
administrator allocate volumes from an LVM volume group, and export
those volumes over iSCSI.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
mkdir -p %{buildroot}%{_mandir}/man8/
mkdir -p %{buildroot}%{_mandir}/man5/
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/target/
install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/targetd.service
install -m 644 targetd.yaml %{buildroot}%{_sysconfdir}/target/targetd.yaml
install -m 644 targetd.8 %{buildroot}%{_mandir}/man8/
install -m 644 targetd.yaml.5 %{buildroot}%{_mandir}/man5/
%pyproject_install
%pyproject_save_files -l targetd

%check
%pyproject_check_import

%post
%systemd_post targetd.service

%preun
%systemd_preun targetd.service

%postun
%systemd_postun_with_restart targetd.service

%files -f %{pyproject_files}
%{_bindir}/targetd
%{_unitdir}/targetd.service
%doc README.md API.md client
%{_mandir}/man8/targetd.8*
%{_mandir}/man5/targetd.yaml.5*
%config(noreplace) %{_sysconfdir}/target/targetd.yaml

%changelog
%autochangelog
