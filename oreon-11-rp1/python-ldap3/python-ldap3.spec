%global source0_hash d7482a10dabd90e8d3ca3dc9288af3e5c8e9547f5f17f676db1e983cafdd78b9

%global pypi_name ldap3

Name:           python-%{pypi_name}
Version:        2.9.1
Release:        16%{?dist}
Summary:        Strictly RFC 4511 conforming LDAP V3 pure Python client

License:        LGPL-3.0-or-later
URL:            https://github.com/cannatag/ldap3
# The PyPI tarball is missing several files needed for running the test suite.
Source:         %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
ldap3 is a strictly RFC 4510 conforming LDAP V3 pure Python client library.

%description %{_description}

%package     -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
# Needed for the import check of ldap3.protocol.sasl.kerberos
BuildRequires:  python3-gssapi

%description -n python3-%{pypi_name} %{_description}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1

# Remove bundled ordereddict, which was only needed on Python < 2.7 anyways.
rm -vf %{pypi_name}/utils/ordDict.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
# The upstream test coverage isn't great, so we are going to do both an import
# check and run what tests we can.
%pyproject_check_import
SERVER='NONE' %{py3_test_envvars} %{python3} -m unittest discover -s test

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
