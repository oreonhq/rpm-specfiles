%global source0_hash eb14ebfc259780be0816f8cabe8617ed2fa35c22efcaa21dabaa472bd2f51de1

%global _description %{expand:
Library for checking syntax of reStructuredText and code blocks nested within
it.}

%global forgeurl https://github.com/rstcheck/rstcheck-core

Name:           python-rstcheck-core
Version:        1.2.2
Release:        %{autorelease}
Summary:        Checks syntax of reStructuredText and code blocks nested within it

%forgemeta

License:        MIT
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

%description %_description

%package -n python3-rstcheck-core
Summary:        %{summary}
BuildRequires:  python3-devel
# for tests
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  gcc gcc-c++

%description -n python3-rstcheck-core %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%forgeautosetup

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files rstcheck_core

%check
# https://github.com/rstcheck/rstcheck-core/issues/57
%{pytest} -k "not test_check_python_returns_error_on_syntax_warning"

%files -n python3-rstcheck-core -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
