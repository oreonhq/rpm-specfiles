%global source0_hash 47a024b51d0239c0dd8c8540c6c7f484be3b8fcf0b2d85c13825780d3b3f3acd

# Created by pyp2rpm-3.3.2
%global pkg_name jaraco-classes
%global pypi_name jaraco.classes
# waiting on jaraco-packaging and rst-linker to build docs
%bcond_with doc

Name:           python-jaraco-classes
Version:        3.4.0
Release:        %autorelease
Summary:        Utility functions for Python class constructs

License:        MIT
URL:            https://github.com/jaraco/jaraco.classes
Source0:        %{pypi_source jaraco.classes}
BuildArch:      noarch
 
%description
Utility functions for Python class constructs.

%package -n python3-jaraco-classes
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-jaraco-classes
Utility functions for Python class constructs.

%if %{with docs}
%package -n python-jaraco-classes-doc
Summary:        jaraco-classes documentation

BuildRequires:  python3dist(pytest-checkdocs)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(jaraco-packaging) >= 3.2
BuildRequires:  python3dist(rst-linker) >= 1.9

%description -n python-jaraco-classes-doc
Documentation for jaraco-classes
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n jaraco.classes-%{version}
# Remove dev-only dependencies. Upstream later split the `test` dependencies out of it
# https://github.com/jaraco/skeleton/issues/138
sed -E -i '/pytest-/d' setup.cfg

%generate_buildrequires
%pyproject_buildrequires -x testing

%build
%pyproject_wheel
%if %{with docs}
# generate html docs 
%{python3} -m sphinx docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
%pyproject_save_files -l jaraco

%check
%pytest

%files -n python3-jaraco-classes -f %{pyproject_files}
%doc README.rst

%if %{with docs}
%files -n python-jaraco-classes-doc
%doc html
%license LICENSE
%endif

%changelog
%autochangelog
