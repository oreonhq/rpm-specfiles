%global source0_hash 9662d791a69bcdd1288f9256a4dd88da3718a5da8128af32afa76b94c24f6b7c
Name:           pyodbc
Version:        5.3.0
Release:        1%{?dist}
Summary:        Python DB API 2.0 Module for ODBC
License:        MIT-0
URL:            https://github.com/mkleehammer/pyodbc
Source0:        https://github.com/mkleehammer/pyodbc/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Recommends: (postgresql-odbc if postgresql-server)
Recommends: (mariadb-connector-odbc if mariadb-server)
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyodbc = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-%{name}
Summary:        Python DB API 2.0 Module for ODBC
%{?python_provide:%python_provide python3-%{name}}
Recommends: (mariadb-connector-odbc if mariadb-server)
Recommends: (postgresql-odbc if postgresql-server)
%description -n python3-%{name}
A Python DB API 2 and 3 module for ODBC. This project provides an up-to-date,
convenient interface to ODBC using native data types like datetime and
decimal.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/pyodbc* usr/lib64/python3*/site-packages/pyodbc* usr/bin/*

%files
%files -n python3-pyodbc -f %{oreon_filedir}/python3-pyodbc.list

%changelog

%autochangelog
