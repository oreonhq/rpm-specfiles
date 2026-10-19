%global source0_hash 51a9c5f7b2f8e636f04c6cada605d9b6a3bf1348fdf945a3d8869b19bba0ee08
Name:           python-pydantic
Version:        2.13.5
Release:        1%{?dist}
Summary:        Data validation using Python type hints
License:        MIT
URL:            https://github.com/pydantic/pydantic
Source0:        https://files.pythonhosted.org/packages/source/p/pydantic/pydantic-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pydantic = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pydantic
Summary:        Data validation using Python type hints
%description -n python3-pydantic

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pydantic-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pydantic usr/lib/python3*/site-packages/pydantic* usr/lib64/python3*/site-packages/pydantic* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pydantic* usr/lib64/python3*/site-packages/pydantic* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pydantic -f %{oreon_filedir}/python3-pydantic.list

%changelog

%autochangelog
