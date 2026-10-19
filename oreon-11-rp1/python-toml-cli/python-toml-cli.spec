%global source0_hash ec61fbfe5f0d6f2d6bfd9e1127cad38a797b8685a93589f2e22efd168b0cc866
Name:           python-toml-cli
Version:        0.8.2
Release:        1%{?dist}
Summary:        Command line interface to read and write keys/values to/from toml files
License:        MIT AND (Apache-2.0 OR BSD-2-Clause)
URL:            https://github.com/mrijken/toml-cli
Source0:        https://files.pythonhosted.org/packages/source/t/toml_cli/toml_cli-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-toml-cli = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-toml-cli
Summary:        Command line interface to read and write keys/values to/from toml files
# oreon:reqs
Requires:       python3dist(jmespath) >= 1.0.1
Requires:       python3dist(regex) >= 2020.7.14
Requires:       python3dist(tomlkit) >= 0.13.3
Requires:       python3dist(typer) >= 0.16.0
# /oreon:reqs
%description -n python3-toml-cli

%prep
%global oreon_srcdir toml_cli-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-toml-cli usr/lib/python3*/site-packages/toml_cli* usr/lib64/python3*/site-packages/toml_cli* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/toml_cli* usr/lib64/python3*/site-packages/toml_cli* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-toml-cli -f %{oreon_filedir}/python3-toml-cli.list

%changelog

%autochangelog
