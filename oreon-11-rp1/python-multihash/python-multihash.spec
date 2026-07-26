%global source0_hash b97511a87b7091f8b37a3d74ccb4a898e133529e7c5e431f9a27f78248a75e60

%global pypi_name multihash

Name:          python-%{pypi_name}
Version:       2.0.1
Release:       %autorelease
BuildArch:     noarch
Summary:       Multihash implementation in Python
License:       MIT
URL:           https://github.com/multiformats/py-%{pypi_name}
VCS:           git:%{url}.git
Source0:       %{pypi_source py-%{pypi_name}}

# Downstream-only: remove pytest-runner dependency
# We can’t send this upstream because the project is archived.
# https://fedoraproject.org/wiki/Changes/DeprecatePythonPytestRunner
Patch:         0001-Downstream-only-remove-pytest-runner-dependency.patch

BuildRequires: python3-pytest
BuildSystem:   pyproject
BuildOption(prep):    -n py-%{pypi_name}-%{version}
BuildOption(install): -l %{pypi_name}

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}.

%description -n python3-%{pypi_name}
%{summary}.

%check -a
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc AUTHORS.rst HISTORY.rst README.rst

%changelog
%autochangelog
