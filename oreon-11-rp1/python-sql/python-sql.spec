%global source0_hash 7e960b9427b9c61a22ec415cd64c26fca8de756612bfa6b0e7c9ea2aafc6d126

%global sum Python library to write SQL queries
%global module_name sql
%global srcname python_sql

Name:           python-%{module_name}
Version:        1.7.0
Release:        2%{?dist}
Summary:        %{sum}

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/%{name}
VCS:            hg:https://foss.heptapod.net/tryton/python-sql
Source0:        %{pypi_source %{srcname}}

BuildArch:      noarch
BuildRequires:  python3-devel

%description
%{name} is a library to write SQL queries in a pythonic way.

%package -n python3-%{module_name}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{module_name}
%{name} is a library to write SQL queries in a pythonic way.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

# remove upstream egg-info
rm -rf */*.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{module_name}

%check
%{py3_test_envvars} %{python3} -m unittest discover -s sql.tests

%files -n python3-%{module_name} -f %{pyproject_files}
%doc {CHANGELOG,README}
%exclude %{python3_sitelib}/*/tests

%changelog
%autochangelog
