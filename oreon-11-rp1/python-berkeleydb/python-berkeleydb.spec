%global source0_hash 3f6da579e727cdec7cdf192feaeb2ad58dca7a8479902f20cc2d73b2027b9e54

%global pypi_name berkeleydb
%global pypi_version 18.1.4

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        20%{?dist}
Summary:        Python bindings for Oracle Berkeley DB

# For a breakdown of the licensing, see licenses.txt
License:        BSD-3-Clause AND ZPL-2.0
URL:            https://www.jcea.es/programacion/pybsddb.htm
Source0:        %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  gcc
BuildRequires:  libdb-devel
BuildRequires:  chrpath

%description
This module provides a nearly complete wrapping of the Oracle/Sleepycat C API
for the Database Environment, Database, Cursor, Log Cursor, Sequence and
Transaction objects, and each of these is exposed as a Python type in the
berkeleydb.db module. The database objects can use various access methods:
btree, hash, recno, queue and heap. Complete support of Oracle Berkeley DB
distributed transactions. Complete support for Oracle Berkeley DB Replication
Manager. Complete support for Oracle Berkeley DB Base Replication.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
This module provides a nearly complete wrapping of the Oracle/Sleepycat C API
for the Database Environment, Database, Cursor, Log Cursor, Sequence and
Transaction objects, and each of these is exposed as a Python type in the
berkeleydb.db module. The database objects can use various access methods:
btree, hash, recno, queue and heap. Complete support of Oracle Berkeley DB
distributed transactions. Complete support for Oracle Berkeley DB Replication
Manager. Complete support for Oracle Berkeley DB Base Replication.

%package -n     python3-%{pypi_name}-devel
Summary:        %{summary}
Requires:       python3-%{pypi_name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-%{pypi_name}-devel
This module provides a nearly complete wrapping of the Oracle/Sleepycat C API
for the Database Environment, Database, Cursor, Log Cursor, Sequence and
Transaction objects, and each of these is exposed as a Python type in the
berkeleydb.db module. The database objects can use various access methods:
btree, hash, recno, queue and heap. Complete support of Oracle Berkeley DB
distributed transactions. Complete support for Oracle Berkeley DB Replication
Manager. Complete support for Oracle Berkeley DB Base Replication.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{pypi_version}

%build
%pyproject_wheel

%install
%pyproject_install

chrpath --delete $RPM_BUILD_ROOT%{python3_sitearch}/berkeleydb/_berkeleydb.cpython-*-linux-gnu*so

sed -i /env\ python/d $RPM_BUILD_ROOT%{python3_sitearch}/berkeleydb/dbshelve.py

%files -n python3-%{pypi_name}
%license LICENSE.txt licenses.txt
%doc README.txt
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{pypi_version}.dist-info

%files -n python3-%{pypi_name}-devel
%{_includedir}/python%{python3_version}/berkeleydb/

%changelog
%autochangelog
