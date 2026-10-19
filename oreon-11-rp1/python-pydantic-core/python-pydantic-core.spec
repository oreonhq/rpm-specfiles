%global source0_hash 67440399d87a2c160ddff9dc013d12812785cfde18b648a295d57043f034a9fb
Name:           python-pydantic-core
Version:        2.49.0
Release:        1%{?dist}
Summary:        Core functionality for Pydantic validation and serialization
License:        MIT
URL:            https://github.com/pydantic
Source0:        https://files.pythonhosted.org/packages/source/p/pydantic_core/pydantic_core-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(maturin) < 2
BuildRequires:  python3dist(maturin) >= 1.15.0
Requires:       python3-pydantic-core = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pydantic-core
Summary:        Core functionality for Pydantic validation and serialization
# oreon:reqs
Requires:       python3dist(typing-extensions) >= 4.16.0
# /oreon:reqs
%description -n python3-pydantic-core

%prep
%global oreon_srcdir pydantic_core-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pydantic-core usr/lib/python3*/site-packages/pydantic_core* usr/lib64/python3*/site-packages/pydantic_core* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pydantic_core* usr/lib64/python3*/site-packages/pydantic_core* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pydantic-core -f %{oreon_filedir}/python3-pydantic-core.list

%changelog

%autochangelog
