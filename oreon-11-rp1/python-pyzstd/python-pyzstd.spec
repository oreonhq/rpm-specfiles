%global source0_hash 36723d3c915b3981de9198d0a2c82b2f5fe3eaa36e4d8d586937830a8afc7d72
Name:           python-pyzstd
Version:        0.19.1
Release:        1%{?dist}
Summary:        Support for Zstandard _zstd_ compression
License:        BSD-3-Clause
URL:            https://github.com/Rogdham/pyzstd
Source0:        https://files.pythonhosted.org/packages/source/p/pyzstd/pyzstd-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyzstd = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyzstd
Summary:        Support for Zstandard _zstd_ compression
# oreon:reqs
Requires:       python3dist(backports.zstd) >= 1.0.0
Requires:       python3dist(typing-extensions) >= 4.13.2
# /oreon:reqs
%description -n python3-pyzstd

%prep
%global oreon_srcdir pyzstd-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyzstd usr/lib/python3*/site-packages/pyzstd* usr/lib64/python3*/site-packages/pyzstd* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyzstd* usr/lib64/python3*/site-packages/pyzstd* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyzstd -f %{oreon_filedir}/python3-pyzstd.list

%changelog

%autochangelog
