%global source0_hash 3083db359ba02c539cecbae06763101f72e11ae9fe4a426d772cd733bfc042d9

%bcond_without tests
%bcond_without docs
%global pypi_name interrogate

%global _description %{expand:
interrogate checks your code base for missing docstrings.
Documentation should be as important as code itself. And it should 
live within code. Python standardized docstrings, allowing for developers 
to navigate libraries as simply as calling help() on objects, and with 
powerful tools like Sphinx, pydoc, and Docutils to automatically generate 
HTML, LaTeX, PDFs, etc.}

Name:           python-%{pypi_name}
Version:        1.7.0
Release:        8%{?dist}
Summary:        Interrogate a codebase for docstring coverage

License:        MIT
URL:            https://github.com/econchick/interrogate
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-mock)
%endif

%if %{with docs}
BuildRequires:  python3dist(sphinx)
%endif

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%package -n python-%{pypi_name}-doc
Summary:  %{summary}

%description -n python-%{pypi_name}-doc
Documentation for interrogate

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest tests/

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/interrogate

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
%autochangelog
