%global source0_hash 6e414deadb06de391909610178711fee5ab08990bafe7dd5b1b8bf4c4fc6f6b7

Name:           pyodbc
Version:        5.1.0
Release:        7%{?dist}
Summary:        Python DB API 2.0 Module for ODBC
License:        MIT-0
URL:            https://github.com/mkleehammer/pyodbc
Source0:        https://github.com/mkleehammer/pyodbc/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Fix build with Python 3.13
# https://github.com/mkleehammer/pyodbc/pull/1361
# https://bugzilla.redhat.com/show_bug.cgi?id=2246290
Patch:          0001-Adjust-for-_PyLong_AsByteArray-signature-change-in-P.patch
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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.1.0-7
- Prepare for Oreon 11 (RP1)
