%global source0_hash 2137e904b1a65546be4ccb96730a391fcd5a85aab8a0632721feb5d7e39cfbce

%global pypi_name pymssql
%global _description %{expand:A simple database interface for Python that builds on top of FreeTDS to provide
a Python DB-API (PEP-249) interface to Microsoft SQL Server.}

Name:           python-%{pypi_name}
Version:        2.3.13
Release:        1%{?dist}
Summary:        DB-API interface to Microsoft SQL Server

License:        LGPL-2.0-or-later
URL:            http://pymssql.org/
Source0:        %{pypi_source}

BuildRequires:  freetds-devel
BuildRequires:  gcc
BuildRequires:  krb5-devel
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist cython}
# For easy patching of pyproject.toml
BuildRequires:  tomcli

# Testing is only possible after sqlalchemy is built and BuildRequires pymssql.
# This bcond allows to build this package without tests when necessary.
%bcond tests 1

%description
%{_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

# Drop unneeded dependencies not available in Fedora
tomcli set pyproject.toml arrays delitem "build-system.requires" "standard-distutils\b.*"
%{?with_tests:sed -i -E '/^\s*standard-distutils\b/d' dev/requirements-dev.txt}

%if 0%{?fedora} <= 43
# Drop version constraint on setuptools
tomcli set pyproject.toml arrays replace "build-system.requires" "(setuptools)\s*[><=]+.*" "\1"
sed -i -E 's/^(\s*setuptools)\s*[><=]+.*$/\1/' setup.cfg %{?with_tests:dev/requirements-dev.txt}

%if 0%{?fedora} < 43
# Drop version constraint on Cython
tomcli set pyproject.toml arrays replace "build-system.requires" "(Cython)\s*[><=]+.*" "\1"
sed -i -E 's/^(\s*cython)\s*[><=]+.*$/\1/' setup.cfg %{?with_tests:dev/requirements-dev.txt}
%endif
%endif

%generate_buildrequires
%pyproject_buildrequires -r %{?with_tests:dev/requirements-dev.txt}

%build
LINK_FREETDS_STATICALLY=no %pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import
%if 0%{?with_tests}
%pytest
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc ChangeLog.rst README.rst
%license LICENSE
# Remove useless header files and Cython sources
%exclude %{python3_sitearch}/%{pypi_name}/*.{h,pyx}

%changelog
%autochangelog
