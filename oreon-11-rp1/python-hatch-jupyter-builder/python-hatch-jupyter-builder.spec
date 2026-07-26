%global source0_hash 79278198d124c646b799c5e8dca8504aed9dcaaa88d071a09eb0b5c2009a58ad

Name:           python-hatch-jupyter-builder
Version:        0.9.1
Release:        6%{?dist}
Summary:        A hatch plugin to help build Jupyter packages
License:        BSD-3-Clause
URL:            https://pypi.org/project/hatch-jupyter-builder/
Source:         %{pypi_source hatch_jupyter_builder}

BuildArch:      noarch
BuildRequires:  python3-devel
# Test deps, upstream contains pre-commit, pytest-cov etc.
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  (python3-tomli if python3 < 3.11)

%global _description %{expand:
This provides a build hook plugin for Hatch that adds
a build step for use with Jupyter packages.}

%description %_description

%package -n     python3-hatch-jupyter-builder
Summary:        %{summary}

%description -n python3-hatch-jupyter-builder %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n hatch_jupyter_builder-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files hatch_jupyter_builder

%check
# Skipped tests installs from internet
%pytest -k "not test_hatch_build"

%files -n python3-hatch-jupyter-builder -f %{pyproject_files}
%doc README.md
%{_bindir}/hatch-jupyter-builder

%changelog
%autochangelog
