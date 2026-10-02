%global source0_hash 9662d791a69bcdd1288f9256a4dd88da3718a5da8128af32afa76b94c24f6b7c

Name:           pyodbc
Version:        5.3.0
Release:        1%{?dist}
Summary:        Python DB API 2.0 Module for ODBC
License:        MIT-0
URL:            https://github.com/mkleehammer/pyodbc
Source0:        https://github.com/mkleehammer/pyodbc/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Fix build with Python 3.13
# https://github.com/mkleehammer/pyodbc/pull/1361
# https://bugzilla.redhat.com/show_bug.cgi?id=2246290
BuildRequires:  gcc-c++
BuildRequires:  unixODBC-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Recommends: (postgresql-odbc if postgresql-server)
Recommends: (mariadb-connector-odbc if mariadb-server)

%global _description\
A Python DB API 2 and 3 module for ODBC. This project provides an up-to-date,\
convenient interface to ODBC using native data types like datetime and\
decimal.

%description %_description

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
%autosetup -n %{name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{name}
%license LICENSE.txt
%doc README.md notes.txt
%{python3_sitearch}/%{name}%{python3_ext_suffix}
%{python3_sitearch}/%{name}-%{version}.dist-info/
%{python3_sitearch}/%{name}.pyi

%changelog
%autochangelog
