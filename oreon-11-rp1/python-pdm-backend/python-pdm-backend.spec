%global source0_hash c41a852ccbf4b567b033db9b2ae78660d7a4ea49307719959ab88a01f0aabb2e
Name:           python-pdm-backend
Version:        2.4.9
Release:        1%{?dist}
Summary:        The build backend used by PDM that supports latest packaging standards
License:        MIT
URL:            https://github.com/pdm-project/pdm-backend
Source0:        https://files.pythonhosted.org/packages/source/p/pdm_backend/pdm_backend-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pdm-backend = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pdm-backend
Summary:        The build backend used by PDM that supports latest packaging standards
# oreon:reqs
Requires:       python3dist(importlib-metadata) >= 3.6
# /oreon:reqs
%description -n python3-pdm-backend

%prep
%global oreon_srcdir pdm_backend-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pdm-backend usr/lib/python3*/site-packages/pdm_backend* usr/lib64/python3*/site-packages/pdm_backend* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pdm_backend* usr/lib64/python3*/site-packages/pdm_backend* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pdm-backend -f %{oreon_filedir}/python3-pdm-backend.list

%changelog

%autochangelog
