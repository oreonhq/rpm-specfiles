%global source0_hash defda19b854fa0d3bd4f76ea4ddcba8abd7dcfcdd585a6690ade050744fc5f43
Name:           python-pyproject-hooks
Version:        1.3.3
Release:        1%{?dist}
Summary:        Wrappers to call pyproject.toml-based build backend hooks.
License:        MIT
URL:            https://github.com/pypa/pyproject-hooks
Source0:        https://files.pythonhosted.org/packages/source/p/pyproject_hooks/pyproject_hooks-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 5
BuildRequires:  python3dist(flit-core) >= 3.11
Requires:       python3-pyproject-hooks = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyproject-hooks
Summary:        Wrappers to call pyproject.toml-based build backend hooks.
%description -n python3-pyproject-hooks

%prep
%global oreon_srcdir pyproject_hooks-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyproject-hooks usr/lib/python3*/site-packages/pyproject_hooks* usr/lib64/python3*/site-packages/pyproject_hooks* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyproject_hooks* usr/lib64/python3*/site-packages/pyproject_hooks* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyproject-hooks -f %{oreon_filedir}/python3-pyproject-hooks.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.0-1
- Prepare for Oreon 11 (RP1)
