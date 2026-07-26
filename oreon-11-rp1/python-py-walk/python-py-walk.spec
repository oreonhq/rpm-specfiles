%global source0_hash a1b28d6079f27203fa3098b69a98572675b3ff5bd02286c43e6dacd66615f879

Name:           python-py-walk
Version:        0.3.3
Release:        %autorelease
Summary:        Filter filesystem paths based on gitignore-like patterns

License:        MIT
URL:            https://github.com/pacha/py-walk
Source:         %{pypi_source py_walk}

BuildArch:      noarch
BuildRequires:  python3-devel
# Test requirements
BuildRequires:  git-core

%global _description %{expand:
Python library to filter filesystem paths based on gitignore-like patterns}

%description %_description

%package -n     python3-py-walk
Summary:        %{summary}

%description -n python3-py-walk %_description

#%%pyproject_extras_subpkg -n python3-py-walk,tests 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n py_walk-%{version}

%generate_buildrequires
%pyproject_buildrequires -x tests

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l py_walk

%check
%pyproject_check_import
%pytest tests

%files -n python3-py-walk -f %{pyproject_files}

%changelog
%autochangelog
