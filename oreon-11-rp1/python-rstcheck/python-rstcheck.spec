%global source0_hash 3bb933abc457254fd6dc5268368dc3d36079a1921ee71a59a87356898254ec6d

%global forgeurl https://github.com/rstcheck/rstcheck

Name:       python-rstcheck
Version:    6.2.5
Release:    %autorelease
Summary:    Checks syntax of reStructuredText and code blocks nested within it
%forgemeta

License:    MIT
URL:        %forgeurl
Source0:    %forgesource

BuildArch:  noarch
%description
Checks syntax of reStructuredText and code blocks nested within it.

%package -n python3-rstcheck
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
Summary:        %{summary}

%description -n python3-rstcheck
Checks syntax of reStructuredText and code blocks nested within it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%forgesetup

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install

%pyproject_save_files rstcheck

%check
# intermittently fails to find some data files for tests
# TODO: needs debugging
%pytest -v -k "not test_all_good_examples and not test_all_bad_examples[test_file2] and not test_all_bad_examples_recurively and not test_error_without_config_file and not test_file_1_is_bad_without_config"

%files -n python3-rstcheck -f %{pyproject_files}
%doc README.rst AUTHORS.rst
%{_bindir}/rstcheck

%changelog
%autochangelog
