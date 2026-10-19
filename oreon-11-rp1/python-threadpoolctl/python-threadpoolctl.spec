%global source0_hash 61348cfb77d53b9242e0017029244b559b810c142ced65b4e21eeca1843959a7
Name:           python-threadpoolctl
Version:        3.7.0
Release:        1%{?dist}
Summary:        threadpoolctl
License:        BSD-3-Clause
URL:            https://github.com/joblib/threadpoolctl
Source0:        https://files.pythonhosted.org/packages/source/t/threadpoolctl/threadpoolctl-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 5
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-threadpoolctl = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-threadpoolctl
Summary:        threadpoolctl
%description -n python3-threadpoolctl

%prep
%global oreon_srcdir threadpoolctl-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-threadpoolctl usr/lib/python3*/site-packages/threadpoolctl* usr/lib64/python3*/site-packages/threadpoolctl* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/threadpoolctl* usr/lib64/python3*/site-packages/threadpoolctl* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-threadpoolctl -f %{oreon_filedir}/python3-threadpoolctl.list

%changelog

%autochangelog
