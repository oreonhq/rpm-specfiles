%global source0_hash 82f8de9eefdb374544f49371456060b68a9c27e275d690e9548d902e0be163e4
Name:           python-sphinx-argparse-cli
Version:        1.23.0
Release:        1%{?dist}
Summary:        render CLI arguments _sub-commands friendly_ defined by argparse module
License:        MIT
URL:            https://github.com/tox-dev/sphinx-argparse-cli
Source0:        https://files.pythonhosted.org/packages/source/s/sphinx_argparse_cli/sphinx_argparse_cli-%{version}.tar.gz
BuildArch:      noarch
Patch:          no-coverage.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatch-vcs) >= 0.5
BuildRequires:  python3dist(hatchling) >= 1.30.1
Requires:       python3-sphinx-argparse-cli = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sphinx-argparse-cli
Summary:        render CLI arguments _sub-commands friendly_ defined by argparse module
# oreon:reqs
Requires:       python3dist(sphinx) >= 9.0.4
# /oreon:reqs
%description -n python3-sphinx-argparse-cli

%prep
%global oreon_srcdir sphinx_argparse_cli-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinx-argparse-cli usr/lib/python3*/site-packages/sphinx_argparse_cli* usr/lib64/python3*/site-packages/sphinx_argparse_cli* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinx_argparse_cli* usr/lib64/python3*/site-packages/sphinx_argparse_cli* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sphinx-argparse-cli -f %{oreon_filedir}/python3-sphinx-argparse-cli.list

%changelog

%autochangelog
