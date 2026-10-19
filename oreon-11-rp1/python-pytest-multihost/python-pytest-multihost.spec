%global source0_hash 4bb63d46f1dc9680ccf64405432cff035f5d8111983a5a11d9757012e1f1033d
Name:           python-pytest-multihost
Version:        3.4
Release:        1%{?dist}
Summary:        Utility for writing multi-host tests for pytest
License:        GPL-3.0-or-later
URL:            https://pagure.io/python-pytest-multihost
Source0:        https://files.pythonhosted.org/packages/source/p/pytest-multihost/pytest-multihost-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pytest-multihost = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-multihost
Summary:        Utility for writing multi-host tests for pytest
%description -n python3-pytest-multihost

%prep
%global oreon_srcdir pytest-multihost-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-multihost usr/lib/python3*/site-packages/pytest_multihost* usr/lib64/python3*/site-packages/pytest_multihost* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_multihost* usr/lib64/python3*/site-packages/pytest_multihost* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-multihost -f %{oreon_filedir}/python3-pytest-multihost.list

%changelog

%autochangelog
