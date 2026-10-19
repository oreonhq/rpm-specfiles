%global source0_hash 86f74ab16363a8d65cb37d4b25735570105307479002b990f4365bd2a15efdd9
Name:           azure-vm-utils
Version:        0.7.0
Release:        1%{?dist}
Summary:        Core utilities and configuration for Linux VMs on Azure
License:        MIT
URL:            https://github.com/Azure/%{name}
Source0:        https://github.com/Azure/azure-vm-utils/archive/refs/tags/v0.7.0.tar.gz#/azure-vm-utils-v0.7.0.tar.gz
Requires:       util-linux
Recommends:     mdadm
Provides:       azure-nvme-utils = %{version}-%{release}
Obsoletes:      azure-nvme-utils < 0.1.3-3
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  json-c-devel
BuildRequires:  libcmocka-devel
BuildRequires:  pkgconfig(libudev)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%post

%systemd_post azure-ephemeral-disk-setup.service
%preun

%systemd_preun azure-ephemeral-disk-setup.service
%postun

%systemd_postun azure-ephemeral-disk-setup.service
%description
This package provides a home for core utilities, udev rules and other
configuration to support Linux VMs on Azure.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake -DVERSION="%{version}-%{release}" -DAZURE_NVME_ID_INSTALL_DIR="%{_bindir}"
%cmake_build
%install
%cmake_install
install -D -m 0755 initramfs/dracut/modules.d/97azure-disk/module-setup.sh %{buildroot}%{_prefix}/lib/dracut/modules.d/97azure-disk/module-setup.sh
install -D -m 0755 initramfs/dracut/modules.d/97azure-unmanaged-sriov/module-setup.sh %{buildroot}%{_prefix}/lib/dracut/modules.d/97azure-unmanaged-sriov/module-setup.sh
rm %{buildroot}%{_bindir}/azure-vm-utils-selftest
rm %{buildroot}%{_mandir}/man8/azure-vm-utils-selftest.8
%oreon_autofiles main

%check

%ctest
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.0-1
- Prepare for Oreon 11 (RP1)
