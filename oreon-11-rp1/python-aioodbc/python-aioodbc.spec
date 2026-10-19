%global source0_hash cbccd89ce595c033a49c9e6b4b55bbace7613a104b8a46e3d4c58c4bc4f25075
Name:           python-aioodbc
Version:        0.5.0
Release:        1%{?dist}
Summary:        ODBC driver for asyncio.
License:        ...
URL:            https://github.com/jettify/uddsketch
Source0:        https://files.pythonhosted.org/packages/source/a/aioodbc/aioodbc-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 45
BuildRequires:  python3dist(setuptools-scm) >= 6.2
Requires:       python3-aioodbc = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-aioodbc
Summary:        ODBC driver for asyncio.
%description -n python3-aioodbc

%prep
%global oreon_srcdir aioodbc-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-aioodbc usr/lib/python3*/site-packages/aioodbc* usr/lib64/python3*/site-packages/aioodbc* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/aioodbc* usr/lib64/python3*/site-packages/aioodbc* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-aioodbc -f %{oreon_filedir}/python3-aioodbc.list

%changelog

%autochangelog
