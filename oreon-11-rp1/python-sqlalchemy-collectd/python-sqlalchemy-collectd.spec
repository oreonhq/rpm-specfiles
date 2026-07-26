%global source0_hash 261cb21e61de6877d0ab89cff2eef252fb0ba83e723c1770d4e42e679c355df3

%global pypi_name sqlalchemy-collectd

%bcond check 1

Name:           python-%{pypi_name}
Version:        0.0.8
Release:        10%{?dist}
Summary:        Send database connection pool stats to collectd

License:        MIT
URL:            https://github.com/sqlalchemy/%{pypi_name}
%global tag rel_%{gsub %{version} %%. _}
Source:         %{url}/archive/%{tag}/%{pypi_name}-%{tag}.tar.gz
BuildArch:      noarch

%global _description %{expand:
Send statistics on SQLAlchemy connection and transaction metrics used by Python
applications to the collectd service.

sqlalchemy-collectd works as a SQLAlchemy plugin invoked via the database URL,
so can be used in any SQLAlchemy application (1.1 or greater) that accepts
arbitrary connection URLs. The plugin is loaded using setuptools entrypoints
and no code changes to the application are required. There are no dependencies
on database backends or drivers.

sqlalchemy-collectd is oriented towards providing a unified view of
application-side database metrics in sprawling, many-host / many-process
environments that may make use of any number of topologically complicating
technologies such as database clusters, proxy servers, large numbers of client
applications, multi-process applications, and containers.}

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3-setuptools
Requires:       collectd-python

BuildRequires:  python3-devel
%if %{with check}
BuildRequires:  python3-pytest
%endif

%description -n python3-%{pypi_name} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pypi_name}-%{tag}
# https://fedoraproject.org/wiki/Changes/DeprecatePythonMock
# https://github.com/sqlalchemy/sqlalchemy-collectd/commit/f074fb09b9368213f9c1371a64c5aef4a1e73242
sed -r -i 's/^import mock$/from unittest &/' */tests/*.py */*/tests/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l sqlalchemy_collectd

%check
%if %{with check}
%pytest
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst examples/
%{_bindir}/connmon

%changelog
%autochangelog
