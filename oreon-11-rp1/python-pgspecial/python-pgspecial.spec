%global source0_hash da6c7fcc7bef7bb0132dc2046f74ec6513b1fe6f0c80e5528d630d14b7c4849d
Name:           python-pgspecial
Version:        2.2.1
Release:        1%{?dist}
Summary:        Python implementation of postgres meta (backslash) commands
License:        BSD-3-Clause
URL:            https://www.dbcli.com
Source0:        https://files.pythonhosted.org/packages/source/p/pgspecial/pgspecial-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
This package provides an API to execute meta-commands (AKA “special”, or
“backslash commands”) on PostgreSQL.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64.0
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-pgspecial = %{version}-%{release}
# /oreon:deps
%package -n       python3-pgspecial+dev
Summary:        Metapackage for python3-pgspecial dev extras
Requires:       python3-pgspecial = %{version}-%{release}
Requires:       python3dist(pytest) >= 6.2.4
Requires:       python3dist(codecov) >= 1.5.1
Requires:       python3dist(pre-commit) >= 1.16.0
Requires:       python3dist(configobj) >= 5.0.6
Requires:       python3dist(ruff) >= 0.11.7
Requires:       python3dist(tox) >= 4.8.0
Requires:       python3dist(pdbpp) >= 0.10.3
Provides:       python3dist(pgspecial[dev]) = %{version}-%{release}

%description -n python3-pgspecial+dev
Metapackage for python3-pgspecial dev extras.

%description %{common_description}

%package -n     python3-pgspecial
Summary:        Python implementation of postgres meta (backslash) commands
# oreon:reqs
Requires:       python3dist(click) >= 4.1
Requires:       python3dist(psycopg) >= 3.0.10
Requires:       python3dist(sqlparse) >= 0.1.19
# /oreon:reqs
%description -n python3-pgspecial %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pgspecial usr/lib/python3*/site-packages/pgspecial* usr/lib64/python3*/site-packages/pgspecial* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pgspecial* usr/lib64/python3*/site-packages/pgspecial* usr/bin/*

%check

%pytest
%files
%files -n python3-pgspecial -f %{oreon_filedir}/python3-pgspecial.list

%changelog

%autochangelog
