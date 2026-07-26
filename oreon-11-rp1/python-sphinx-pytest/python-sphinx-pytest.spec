%global source0_hash 3c26f5c39ed8600eb4f554d07034f114952c101a011f7fcfeed72c28ffe12670

Name:           python-sphinx-pytest
Version:        0.2.0
Release:        11%{?dist}
Summary:        Helpful pytest fixtures for sphinx extensions

# SPDX
License:        MIT
URL:            https://github.com/sphinx-extensions2/sphinx-pytest
Source:         %{pypi_source sphinx_pytest}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Helpful pytest fixtures for sphinx extensions.
This extension provides pytest fixtures to "simulate" converting
some source text to docutils AST at different stages; before transforms,
after transforms, etc.}

%description %_description

%package -n     python3-sphinx-pytest
Summary:        %{summary}

%description -n python3-sphinx-pytest %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n sphinx_pytest-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinx_pytest

%check
%pytest

%files -n python3-sphinx-pytest -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
