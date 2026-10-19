%global source0_hash 15e270637586eabc56755ee5fcc81c48bdb46ba7ef7c0d5b1b64302d080cc60f
%global pypi_name pytest-xprocess
Name:           python-%{pypi_name}
Version:        1.0.2
Release:        1%{?dist}
Summary:        Pytest plugin to manage external processes across test runs
License:        MIT
URL:            https://github.com/pytest-dev/pytest-xprocess/
Source0:        https://files.pythonhosted.org/packages/source/p/python-pytest-xprocess/python-pytest-xprocess-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
# /oreon:deps
%description
Experimental py.test <>_ plugin for managing processes across test runs.Usage
install via:: pip install pytest-xprocessThis will provide a xprocess fixture
which helps you to ensure that one ore more longer-running processes are
present for your tests. You can use it to start and pre-configure test-specific
databases (Postgres, Couchdb, ...).Additionally there are two new command
line...

%package -n     python3-%{pypi_name}
Summary:        Pytest plugin to manage external processes across test runs
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3dist(psutil)
Requires:       python3dist(pytest)
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
Experimental py.test <>_ plugin for managing processes across test runs.Usage
install via:: pip install pytest-xprocessThis will provide a xprocess fixture
which helps you to ensure that one ore more longer-running processes are
present for your tests. You can use it to start and pre-configure test-specific
databases (Postgres, Couchdb, ...).Additionally there are two new command
line...

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Remove executable bit from README
chmod -x README.rst

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest
%files -f %{oreon_filedir}/main.list
%files -n python3-pytest-xprocess -f %{oreon_filedir}/python3-pytest-xprocess.list

%changelog

%autochangelog
