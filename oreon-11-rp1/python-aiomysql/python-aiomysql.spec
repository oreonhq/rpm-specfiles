%global source0_hash 72d15ef5cfc34c03468eb41e1b90adb9fd9347b0b589114bd23ead569a02ac1a
Name:           python-aiomysql
Version:        0.3.2
Release:        1%{?dist}
Summary:        MySQL driver for asyncio.
License:        MIT
URL:            https://github.com/aio-libs/aiomysql
Source0:        https://files.pythonhosted.org/packages/source/a/aiomysql/aiomysql-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 80
BuildRequires:  python3dist(setuptools-scm[toml]) < 10
BuildRequires:  python3dist(setuptools-scm[toml]) >= 7
Requires:       python3-aiomysql = %{version}-%{release}
# /oreon:deps
%package -n       python3-aiomysql+sa
Summary:        Metapackage for python3-aiomysql sa extras
Requires:       python3-aiomysql = %{version}-%{release}
Requires:       python3dist(sqlalchemy) >= 1.3
Requires:       python3dist(sqlalchemy) < 1.4
Provides:       python3dist(aiomysql[sa]) = %{version}-%{release}

%description -n python3-aiomysql+sa
Metapackage for python3-aiomysql sa extras.

%package -n       python3-aiomysql+rsa
Summary:        Metapackage for python3-aiomysql rsa extras
Requires:       python3-aiomysql = %{version}-%{release}
Requires:       python3dist(pymysql[rsa]) >= 1.0
Provides:       python3dist(aiomysql[rsa]) = %{version}-%{release}

%description -n python3-aiomysql+rsa
Metapackage for python3-aiomysql rsa extras.

%description

%package -n     python3-aiomysql
Summary:        MySQL driver for asyncio.
# oreon:reqs
Requires:       python3dist(pymysql) >= 1.0
# /oreon:reqs
%description -n python3-aiomysql

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir aiomysql-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-aiomysql usr/lib/python3*/site-packages/aiomysql* usr/lib64/python3*/site-packages/aiomysql* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/aiomysql* usr/lib64/python3*/site-packages/aiomysql* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-aiomysql -f %{oreon_filedir}/python3-aiomysql.list

%changelog

%autochangelog
