%global source0_hash 9bd9143dee2d810ac816ff25e9d41cf37415bdf11ba4385d82c8cf5c1cad3fc2

%bcond_with docs
%bcond_without tests

%global pypi_name nashpy
%global pretty_name Nashpy

%global _description %{expand:
This library implements the following algorithms for Nash equilibria
on 2 player games: Support enumeration, Best response polytope vertex
enumeration, Lemke Howson algorithm.}

Name:           python-%{pypi_name}
Version:        0.0.43
Release:        %autorelease
Summary:        A library to compute equilibria of 2 player normal form games

License:        MIT
URL:            https://github.com/drvinceknight/%{pretty_name}
Source0:        %{url}/archive/v%{version}/%{pretty_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with docs}
# For documentation
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
#missing for now
#BuildRequires:  python3dist(sphinx-togglebutton)
%endif

%if %{with tests}
# For tests
# See testenv.deps in tox.ini, but note that it is mostly linters etc.,
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(pytest-subtests)
BuildRequires:  python3dist(pytest-randomly)
%endif

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%if %{with docs}
%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pretty_name}-%{version}

%generate_buildrequires	
%pyproject_buildrequires

%build
%pyproject_wheel

%if %{with docs}
# Generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
%pyproject_save_files nashpy

%check	
%if %{with tests}
%pytest --ignore-glob='benchmarks/*' -v
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGES.md CITATION.md paper paper.bib

%if %{with docs}
%files doc
%license LICENSE
%doc html/
%endif

%changelog
%autochangelog
