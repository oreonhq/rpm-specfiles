%global source0_hash f7c305a75cc4e3a331d248e996f25783ba784b88d5a9b9f73c53eacaa6d76985

%global pypi_name inject

%global pkg_description %{expand:Dependency injection the python way, the good way.

Key features:
  - Fast.
  - Thread-safe.
  - Simple to use.
  - Does not steal class constructors.
  - Does not try to manage your application object graph.
  - Transparently integrates into tests.
  - Supports type hinting in Python 3.5+.
  - Autoparams leveraging type annotations.
}
 
Name: python-%{pypi_name}
Summary: Dependency injection, the Python way
License: Apache-2.0

Version: 5.2.1
Release: 11%{?dist}

URL: https://github.com/ivankorobkov/python-%{pypi_name}
Source0: %pypi_source

# Fix tests failing on Python 3.14
Patch0: 0000-asyncio.patch

BuildRequires: python3-devel
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(pytest)

BuildArch: noarch

%description
%{pkg_description}

%package -n python3-%{pypi_name}
Summary: %{summary}
BuildArch: noarch

%description -n python3-%{pypi_name}
%{pkg_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGES.md README.md

%changelog
%autochangelog
