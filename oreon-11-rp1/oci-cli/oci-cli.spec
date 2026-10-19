%global source0_hash 52e8f81154bda612b97961ab4c53f684afa7a420714dec3bbf47b9efe91b5b13
%bcond_with     tests
Name:           oci-cli
Version:        3.93.0
Release:        1%{?dist}
Summary:        Command Line Interface for Oracle Cloud Infrastructure
License:        UPL-1.0
URL:            https://github.com/oracle/oci-cli
Source0:        https://github.com/oracle/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-oci-cli = %{version}-%{release}
# /oreon:deps
%description

# Awaiting a fix for python-cx-oracle
# https://src.fedoraproject.org/rpms/python-cx-oracle/pull-request/1
# %%pyproject_extras_subpkg -n %%{name} db

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

# Remove upper limits and pinned dependencies.
sed -i -e 's/,[<=]\+[0-9\.]\+//' -e 's/==/>=/' setup.py

# Ignore the version of certifi.
sed -i -e 's/certifi>=[0-9\.]*/certifi/' setup.py

# Work around a versioning bug when trying to find terminaltables.
sed -i 's/terminaltables>=[0-9\.]\+/terminaltables/' setup.py

%build

%pyproject_wheel
%install
%pyproject_install
rm -f %{buildroot}/%{_bindir}/create_backup_from_onprem
%oreon_autofiles main

%check

%pyproject_check_import -e 'oci_cli.scripts.database.dbaas' -e 'services.*'
%if %{with tests}
%pytest
%endif
%license LICENSE.txt THIRD_PARTY_LICENSES.txt
%doc CHANGELOG.rst COMMON_ISSUES.rst README.rst
%{_bindir}/oci
%files

%changelog

%autochangelog
