%global source0_hash 5a826ed84cc0afa202eb9e44381d7d762f7bdda8e0c23f9f79a7f1f44cf4a895

Name:           python-pytest-console-scripts
Version:        1.4.1
Release:        %autorelease
Summary:        Pytest plugin for testing console scripts
# SPDX
License:        MIT
URL:            https://github.com/kvas-it/pytest-console-scripts
Source:         %{pypi_source pytest-console-scripts}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Pytest-console-scripts is a pytest plugin for running python
scripts from within tests.}

%description %_description

%package -n     python3-pytest-console-scripts
Summary:        %{summary}
# https://github.com/kvas-it/pytest-console-scripts/issues/56
Requires:       python3-setuptools

%description -n python3-pytest-console-scripts %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pytest-console-scripts-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_console_scripts

%check
%tox

%files -n python3-pytest-console-scripts -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
