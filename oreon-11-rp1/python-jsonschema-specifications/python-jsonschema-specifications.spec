%global source0_hash 0f38b83639958ce1152d02a7f062902c41c8fd20d558b0c34344292d417ae272

%global pypi_name jsonschema-specifications
%global pkg_name jsonschema_specifications
%global with_tests 1

# Some documentation reqs are not yet packaged for EPEL
%if ! 0%{?rhel}
%global with_doc 1
%endif

%global common_description %{expand:
JSON support files from the JSON Schema Specifications (metaschemas,
vocabularies, etc.), packaged for runtime access from Python as a
referencing-based Schema Registry.}

Name:           python-%{pypi_name}
Summary:        JSON Schema meta-schemas and vocabularies, exposed as a Registry
Version:        2024.10.1
Release:        7%{?dist}
License:        MIT
URL:            https://github.com/python-jsonschema/jsonschema-specifications
Source0:        https://files.pythonhosted.org/packages/source/j/jsonschema_specifications/jsonschema_specifications-2024.10.1.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%description %{common_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%description -n python3-%{pypi_name} %{common_description}

%if 0%{?with_tests}
%package  -n    python3-%{pypi_name}-tests
Summary:        Tests for the JSON Schema specifications
Requires:       python3-%{pypi_name} = %{version}-%{release}

BuildRequires:  python3dist(pytest)
Requires:       python3dist(pytest)

%description -n python3-%{pypi_name}-tests
Tests for the JSON Schema specifications
%endif

%if 0%{?with_doc}
%package  -n    python3-%{pypi_name}-doc
Summary:        Documentation for the JSON Schema specifications
Group:          Documentation

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-copybutton)
BuildRequires:  python3dist(sphinxext-opengraph)
BuildRequires:  python3dist(sphinxcontrib-spelling)

%description -n python3-%{pypi_name}-doc
Documentation for the JSON Schema specifications
%endif


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{pkg_name}-%{version}

sed -i "/^file:.*/d" docs/requirements.in
sed -i "/^pygments-github-lexers/d" docs/requirements.in
sed -i "s/^pyenchant.*/pyenchant/" docs/requirements.in

%generate_buildrequires
%if 0%{?with_doc}
%pyproject_buildrequires docs/requirements.in
%else
%pyproject_buildrequires
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pkg_name}

%if 0%{?with_doc}
# generate html docs
export PYTHONPATH="%{buildroot}/%{python3_sitelib}"
sphinx-build-3 -b html docs docs/build/html
# remove the sphinx-build-3 leftovers
rm -rf docs/build/html/.{doctrees,buildinfo}
%endif

%if 0%{?with_tests}
%check
%pytest
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license COPYING
%doc README.rst
%exclude %{python3_sitelib}/%{pkg_name}/tests

%if 0%{?with_tests}
%files -n python3-%{pypi_name}-tests
%license COPYING
%{python3_sitelib}/%{pkg_name}/tests
%endif

%if 0%{?with_doc}
%files -n python3-%{pypi_name}-doc
%doc docs/build/html
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2024.10.1-7
- Prepare for Oreon 11 (RP1)
