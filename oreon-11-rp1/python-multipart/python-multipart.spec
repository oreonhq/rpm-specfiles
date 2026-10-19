%global source0_hash d6076567b489270271d9ec103d404745da1501ad5b70e3a7f1f07f5623d82850
Name:           python-multipart
Version:        2.0.0
Release:        1%{?dist}
Summary:        Parser for multipart/form-data
License:        MIT
URL:            https://multipart.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/m/multipart/multipart-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.9
Requires:       python3-multipart = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-multipart
Summary:        Parser for multipart/form-data
%description -n python3-multipart

%prep
%global oreon_srcdir multipart-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-multipart usr/lib/python3*/site-packages/multipart* usr/lib64/python3*/site-packages/multipart* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/multipart* usr/lib64/python3*/site-packages/multipart* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-multipart -f %{oreon_filedir}/python3-multipart.list

%changelog

%autochangelog
