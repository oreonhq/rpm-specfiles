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
# oreon url source checksums begin
%global source0_sha256 6e414deadb06de391909610178711fee5ab08990bafe7dd5b1b8bf4c4fc6f6b7
%global source0_file 5.1.0.tar.gz
# oreon url source checksums end
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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/5.1.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "6e414deadb06de391909610178711fee5ab08990bafe7dd5b1b8bf4c4fc6f6b7" || { echo "oreon: Source0 SHA256 mismatch for 5.1.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
