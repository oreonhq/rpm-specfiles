%global source0_hash e9c0826dda2855745eb63b3fd8e33b6ac8881188f2ba91e51a516ed833fc0cb8
Name:           python-cli-helpers
Version:        2.15.1
Release:        1%{?dist}
Summary:        Helpers for building command-line apps
License:        ...
URL:            https://github.com/dbcli/cli_helpers
Source0:        https://files.pythonhosted.org/packages/source/c/cli_helpers/cli_helpers-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-cli-helpers = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-cli-helpers
Summary:        Helpers for building command-line apps
%description -n python3-cli-helpers

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir cli_helpers-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cli-helpers usr/lib/python3*/site-packages/cli_helpers* usr/lib64/python3*/site-packages/cli_helpers* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cli_helpers* usr/lib64/python3*/site-packages/cli_helpers* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cli-helpers -f %{oreon_filedir}/python3-cli-helpers.list

%changelog

%autochangelog
