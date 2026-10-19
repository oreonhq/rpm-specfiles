%global source0_hash b2d746eb1b768a6f9087e5c7c91f87fb9d40c7fdc777550dc00397af428a0654
Name:           python-pytest-subprocess
Version:        1.6.0
Release:        1%{?dist}
Summary:        A plugin to fake subprocess for pytest
License:        MIT
URL:            https://github.com/aklajnert/pytest-subprocess
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_subprocess/pytest_subprocess-%{version}.tar.gz
BuildArch:      noarch
Patch:          https://github.com/aklajnert/pytest-subprocess/commit/be30d9a94ba45afb600717e3fcd95b8b2ff2c60e.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pytest-subprocess = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-subprocess
Summary:        A plugin to fake subprocess for pytest
%description -n python3-pytest-subprocess

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pytest_subprocess-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-subprocess usr/lib/python3*/site-packages/pytest_subprocess* usr/lib64/python3*/site-packages/pytest_subprocess* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_subprocess* usr/lib64/python3*/site-packages/pytest_subprocess* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-subprocess -f %{oreon_filedir}/python3-pytest-subprocess.list

%changelog

%autochangelog
