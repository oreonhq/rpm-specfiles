%global source0_hash ee885a46859235ae62d27ce612ee49b6a330fd0eac276e7f58b6018d8af859d1
Name:           python-openneuro-py
Version:        2026.7.1
Release:        1%{?dist}
Summary:        A Python client for OpenNeuro.
License:        GPL-3.0-only
URL:            https://github.com/openneuro-py/openneuro-py
Source0:        https://files.pythonhosted.org/packages/source/o/openneuro_py/openneuro_py-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-openneuro-py = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-openneuro-py
Summary:        A Python client for OpenNeuro.
# oreon:reqs
Requires:       python3dist(niquests) >= 3.7.2
Requires:       python3dist(pydantic) >= 2
Requires:       python3dist(rich) >= 13.8
Requires:       python3dist(typer) >= 0.24.0
Requires:       python3dist(wcmatch) >= 10.1
# /oreon:reqs
%description -n python3-openneuro-py

%prep
%global oreon_srcdir openneuro_py-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-openneuro-py usr/lib/python3*/site-packages/openneuro_py* usr/lib64/python3*/site-packages/openneuro_py* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/openneuro_py* usr/lib64/python3*/site-packages/openneuro_py* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-openneuro-py -f %{oreon_filedir}/python3-openneuro-py.list

%changelog

%autochangelog
