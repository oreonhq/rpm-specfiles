%global source0_hash 8073e265d82eee148795f4ac3f98e6b8a68b755d64a338e9c22f873041808008

%global pypi_name sphinx-tabs
%global python_module_name sphinx_tabs

Name:           python-sphinx-tabs
Version:        3.4.7
Release:        8%{?dist}
Summary:        Tabbed views for Sphinx
# SPDX
License:        MIT
URL:            https://github.com/executablebooks/sphinx-tabs
Source0:        https://github.com/executablebooks/%{pypi_name}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

# Open PR for Python Sphinx 8.1 issues with tests
# https://bugzilla.redhat.com/show_bug.cgi?id=2330154
Patch0:         https://patch-diff.githubusercontent.com/raw/executablebooks/sphinx-tabs/pull/200.patch
# Make tests pass with docutils 0.22+
Patch1:         https://github.com/executablebooks/sphinx-tabs/pull/207.patch
BuildArch:      noarch

%global _description %{expand:
Create tabbed content in Sphinx documentation when building HTML.}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
# Needed for testing
BuildRequires:  python3dist(beautifulsoup4)
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-regressions)
BuildRequires:  python3dist(sphinx)

%generate_buildrequires
%pyproject_buildrequires

%description %{_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{_description}

%package -n python3-%{pypi_name}-doc
Summary:        HTML documentation for %{pypi_name}
Requires:       python3-%{pypi_name}

%description -n python3-%{pypi_name}-doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%build
%pyproject_wheel

PYTHONPATH=$(pwd) sphinx-build -b html docs html_docs

%install
%pyproject_install
%pyproject_save_files %{python_module_name}

%check
# rinohtype extension to Sphinx is not yet packaged
%pytest -k 'not test_rinohtype_pdf'

%files -n  python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md README.md

%files -n python3-%{pypi_name}-doc
%doc html_docs/*

%changelog
%autochangelog
