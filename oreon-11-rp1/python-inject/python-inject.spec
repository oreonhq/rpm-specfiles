%global source0_hash 7ded3d40ec4caf3462302e5ea463fce5ab817c6d466eaadfa6ec699904c51cfc
Name:           python-inject
Version:        5.5.0
Release:        1%{?dist}
Summary:        Python dependency injection framework.
License:        Apache-2.0
URL:            https://github.com/ivankorobkov/python-inject
Source0:        https://files.pythonhosted.org/packages/source/i/inject/inject-%{version}.tar.gz
BuildArch:      noarch
Patch0: 0000-asyncio.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-inject = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-inject
Summary:        Python dependency injection framework.
%description -n python3-inject

%prep
%global oreon_srcdir inject-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-inject usr/lib/python3*/site-packages/inject* usr/lib64/python3*/site-packages/inject* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/inject* usr/lib64/python3*/site-packages/inject* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-inject -f %{oreon_filedir}/python3-inject.list

%changelog

%autochangelog
