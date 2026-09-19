%global source0_hash bd299a4689f6770d9fa84fd1486d99d1b6b7f3e4adf855838378a01ea3cd55d1

%global pypi_name pytest-metadata

Name:          python-%{pypi_name}
Version:       3.1.1
Release:       %autorelease
Summary:       A plugin for accessing test session metadata
License:       MPL-2.0
URL:           https://github.com/pytest-dev/%{pypi_name}
Source0:       %url/archive/%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-pip
BuildRequires: python3-setuptools

%global _description %{expand:
pytest-metadata is a plugin for pytest that provides access to test
session metadata.
}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files pytest_metadata

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
