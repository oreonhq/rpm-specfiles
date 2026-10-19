%global source0_hash 35c3f2a4172b33136ab9f6b3ef1c00260dd2f66f858f24d88418a015f446506c
Name:           python-qrcode
Version:        8.2
Release:        1%{?dist}
Summary:        QR Code image generator
License:        ...
URL:            https://github.com/lincolnloop/python-qrcode
Source0:        https://files.pythonhosted.org/packages/source/q/qrcode/qrcode-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-qrcode = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-qrcode
Summary:        QR Code image generator
%description -n python3-qrcode

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir qrcode-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-qrcode usr/lib/python3*/site-packages/qrcode* usr/lib64/python3*/site-packages/qrcode* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/qrcode* usr/lib64/python3*/site-packages/qrcode* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-qrcode -f %{oreon_filedir}/python3-qrcode.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8.0-1
- Prepare for Oreon 11 (RP1)
