%global source0_hash a3c25d871fab549122b2340810de1f99481002c942a2132476b062aacdbf6e92
Name:           python-qemu-qmp
Version:        0.0.6
Release:        1%{?dist}
Summary:        QEMU Monitor Protocol library
License:        ...
URL:            https://www.qemu.org/
Source0:        https://files.pythonhosted.org/packages/source/q/qemu_qmp/qemu_qmp-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-qemu-qmp = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-qemu-qmp
Summary:        QEMU Monitor Protocol library
%description -n python3-qemu-qmp

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir qemu_qmp-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-qemu-qmp usr/lib/python3*/site-packages/qemu_qmp* usr/lib64/python3*/site-packages/qemu_qmp* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/qemu_qmp* usr/lib64/python3*/site-packages/qemu_qmp* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-qemu-qmp -f %{oreon_filedir}/python3-qemu-qmp.list

%changelog

%autochangelog
