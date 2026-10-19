%global source0_hash 93f2094f219b6fec1e6dbed2e5039fb879272f678646a351b46172f6d0bf110f
Name:           python-pydicom-data
Version:        1.0.0
Release:        1%{?dist}
Summary:        ...
License:        MIT
URL:            https://github.com/pydicom/pydicom-data
Source0:        https://files.pythonhosted.org/packages/source/p/pydicom-data/pydicom-data-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pydicom-data = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pydicom-data
Summary:        ...
%description -n python3-pydicom-data

%prep
%global oreon_srcdir pydicom-data-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pydicom-data usr/lib/python3*/site-packages/pydicom_data* usr/lib64/python3*/site-packages/pydicom_data* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pydicom_data* usr/lib64/python3*/site-packages/pydicom_data* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pydicom-data -f %{oreon_filedir}/python3-pydicom-data.list

%changelog

%autochangelog
