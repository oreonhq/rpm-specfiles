%global source0_hash c739895fe20851bdba53f246d0599aa389bc1a1cba48db2ecac0130576dc1b0e

%global srcname pytest-fixture-config
%global sum Simple configuration objects for Py.test fixtures

Name:           python-%{srcname}
Version:        1.8.0
Release:        8%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-six

%description
Simple configuration objects for Py.test fixtures.
Allows you to skip tests when their required config variables aren't set.

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Simple configuration objects for Py.test fixtures.
Allows you to skip tests when their required config variables aren't set.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l pytest_fixture_config

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGES.md

%changelog
%autochangelog
