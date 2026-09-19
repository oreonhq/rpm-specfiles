%global source0_hash 26ef9df924cd874a825d92d6bc01a5a869a4a28d2f2ebba61d3b5b19c60120f0

# To break circular dependency on poetry, when bootstrapping
# we don't BuildRequire runtime deps and we don't run tests.
%bcond bootstrap 0

Name:           python-poetry-plugin-export
Version:        1.10.0
Release:        %autorelease
Summary:        Poetry plugin to export the dependencies to various formats

# SPDX
License:        MIT
URL:            https://python-poetry.org/
Source:         %{pypi_source poetry_plugin_export}

BuildArch:      noarch
BuildRequires:  python3-devel
# Test dependencies are taken from [tool.poetry.dev-dependencies]
# in pyproject.toml file. poetry-plugin-export lists test dependencies
# in dependency groups instead of extras, since they are not extras
# pyproject-rpm-macros can't recognize them and we list them manually.
# They also mix in pre-commit and mypy and we don't need them.
%if %{without bootstrap}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-xdist
%endif

%global _description %{expand:
This package is a plugin that allows the export of locked packages to various
formats. This plugin provides the same features as the existing export command
of Poetry which it will eventually replace.
}

%description %_description

%package -n python3-poetry-plugin-export
Summary:        %{summary}

%description -n python3-poetry-plugin-export %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n poetry_plugin_export-%{version}

%generate_buildrequires
%pyproject_buildrequires %{?with_bootstrap: -R}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files poetry_plugin_export

%if %{without bootstrap}
%check
%pytest
%endif

%files -n python3-poetry-plugin-export -f %{pyproject_files}
%doc README.*
%license LICENSE

%changelog
%autochangelog
