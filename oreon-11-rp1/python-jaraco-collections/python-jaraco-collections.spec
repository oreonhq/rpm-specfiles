%global source0_hash 0e4829409d39ad18a40aa6754fee2767f4d9730c4ba66dc9df89f1d2756994c2

# doc dependecies are not packaged
%bcond_with docs

Name:           python-jaraco-collections
Version:        5.1.0
Release:        %autorelease
Summary:        Collection objects similar to those in stdlib by jaraco

License:        MIT
URL:            https://github.com/jaraco/jaraco.collections
Source0:        %{pypi_source jaraco_collections}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
%{summary}

%package -n     python3-jaraco-collections
Summary:        %{summary}

%description -n python3-jaraco-collections
%{summary}

%package -n python-jaraco-collections-doc
Summary:        jaraco.collections documentation

%description -n python-jaraco-collections-doc
Documentation for jaraco.collections

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n jaraco_collections-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test%{?with_docs:,doc}

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

%files -n python3-jaraco-collections -f %{pyproject_files}
%doc README.rst

%if %{with docs}
%files -n python-jaraco-collections-doc
%doc html
%license LICENSE
%endif

%changelog
%autochangelog
