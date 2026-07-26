%global source0_hash 4b29e4a385fb96fd6b8ffee82f42d1f49f5e2275e4e7ee57f889fe3111eb82b4

%{?python_enable_dependency_generator}

%global srcname pytest-multihost
%global modulename pytest_multihost
%global srcversion 3.0
%global versionedname %{srcname}-%{srcversion}

Name: python-%{srcname}
Version: %{srcversion}
Release: 32%{?dist}
Summary: Utility for writing multi-host tests for pytest

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
URL:           https://github.com/encukou/pytest-multihost
Source0:       %{url}/archive/v%{srcversion}/%{versionedname}.tar.gz

BuildArch:     noarch

%description
Allows pytest tests to run commands on several machines.
The machines to run on are described on the command line, the tests
specify how many machines they need and commands/checks to run on them.

%package -n python3-%{srcname}
Summary: Utility for writing multi-host tests for pytest
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pytest
# These are not *strictly* required, but are part of the default workflow.
Recommends:    python%{python3_version}dist(pyyaml)
Recommends:    python%{python3_version}dist(paramiko)

%description -n python3-%{srcname}
Allows pytest tests to run commands on several machines.
The machines to run on are described on the command line, the tests
specify how many machines they need and commands/checks to run on them.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{versionedname}

%build
%py3_build

%check
# Do not run the test that needs passwordless SSH to localhost set up
%{__python3} -m pytest -m "not needs_ssh"

%install
%py3_install

%files -n python3-%{srcname}
%license COPYING
%doc README.rst
%{python3_sitelib}/%{modulename}-*.egg-info/
%{python3_sitelib}/%{modulename}/

%changelog
%autochangelog
