%global source0_hash abdcfc74b8656173f762655a8d4d44f551342ac9574f1e7afa5cfc7bcd950e65
Name:           python-virt-firmware
Version:        26.9
Release:        1%{?dist}
Summary:        tools for virtual machine firmware volumes
License:        ...
URL:            https://gitlab.com/kraxel/virt-firmware
Source0:        https://files.pythonhosted.org/packages/source/v/virt_firmware/virt_firmware-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-virt-firmware = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-virt-firmware
Summary:        tools for virtual machine firmware volumes
%description -n python3-virt-firmware

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir virt_firmware-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-virt-firmware usr/lib/python3*/site-packages/virt_firmware* usr/lib64/python3*/site-packages/virt_firmware* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/virt_firmware* usr/lib64/python3*/site-packages/virt_firmware* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-virt-firmware -f %{oreon_filedir}/python3-virt-firmware.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.2-1
- Prepare for Oreon 11 (RP1)
