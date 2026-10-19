%global source0_hash 4f4f4399e6a7646917716d7dc06f814d32f94f30fb51d61b5c760e8f6d3ba53b
Name:           python-stone
Version:        3.5.4
Release:        1%{?dist}
Summary:        Stone is an interface description language _IDL_ for APIs.
License:        MIT
URL:            https://github.com/dropbox/stone
Source0:        https://files.pythonhosted.org/packages/source/s/stone/stone-%{version}.tar.gz
BuildArch:      noarch
Patch:          0001-Remove-pytest-runner-setup.py-test-support.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 83.0.0
BuildRequires:  python3dist(setuptools-scm) < 11
BuildRequires:  python3dist(setuptools-scm) >= 10.2.1
Requires:       python3-stone = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-stone
Summary:        Stone is an interface description language _IDL_ for APIs.
%description -n python3-stone

%prep
%global oreon_srcdir stone-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-stone usr/lib/python3*/site-packages/stone* usr/lib64/python3*/site-packages/stone* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/stone* usr/lib64/python3*/site-packages/stone* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-stone -f %{oreon_filedir}/python3-stone.list

%changelog

%autochangelog
