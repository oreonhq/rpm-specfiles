%global source0_hash fc3fce98865f6784c9cd0a56a20644fc6098f21c8c33834a8d9fe383c17e554b

Name:           python-jupyter-events
Version:        0.12.0
Release:        %autorelease
Summary:        Jupyter Event System library
License:        BSD-3-Clause
URL:            https://jupyter.org
Source:         %{pypi_source jupyter_events}
BuildArch:      noarch
BuildRequires:  python3-devel
# Manual test deps - upstream contains coverage, pre-commit, …
BuildRequires:  python3-click
BuildRequires:  python3-rich
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-console-scripts

%global _description %{expand:
An event system for Jupyter Applications and extensions.}

%description %_description

%package -n     python3-jupyter-events
Summary:        %{summary}

%description -n python3-jupyter-events %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n jupyter_events-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files jupyter_events

%check
# For now ignore DeprecationWarnings coming from python-pytest-asyncio 0.26
%pytest -W ignore::DeprecationWarning

%files -n python3-jupyter-events -f %{pyproject_files}
%doc README.md
%{_bindir}/jupyter-events

%changelog
%autochangelog
