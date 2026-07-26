%global source0_hash add8643c32f738014d252d2bdebb478623b04802e8396d5903905db36474d3ff

%global pypi_name mysqlclient
%bcond_with mysqldb

Name:           python-%{pypi_name}
Version:        2.2.5
Release:        7%{?dist}
Summary:        MySQL/mariaDB database connector for Python

License:        GPL-2.0-only
URL:            https://github.com/PyMySQL/mysqlclient
Source0:        %{pypi_source}

BuildRequires:  gcc
BuildRequires:  mariadb-connector-c-devel

%description
MySQLdb is an interface to the popular MySQL database server that provides
the Python database API.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Provides: python3-mysql = %{version}-%{release}
Obsoletes: python3-mysql < 2.0.0-1

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with mysqldb}
BuildRequires:  python3-pytest
%endif

%description -n python3-%{pypi_name}
MySQLdb is an interface to the popular MySQL database server that provides
the Python database API.

%package -n python-%{pypi_name}-doc
Summary:        Documentation for %{name}

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
%description -n python-%{pypi_name}-doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 doc html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%if %{with mysqldb}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests
%endif

%files -n python3-%{pypi_name}
%doc README.md HISTORY.rst
%license LICENSE
%{python3_sitearch}/MySQLdb/
%{python3_sitearch}/%{pypi_name}-%{version}-py*.egg-info/

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
%autochangelog
