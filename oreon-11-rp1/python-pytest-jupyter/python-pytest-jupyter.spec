%global source0_hash a4e08ced44cfea1bce080090c626b8dc4f9d617fa5aafcd84b71405f503e9899

Name:           python-pytest-jupyter
Version:        0.11.0
Release:        %autorelease
Summary:        A pytest plugin for testing Jupyter libraries and extensions
# BSD for pytest-jupyter itself and
# MIT is for bundled parts of tornasync package
License:        BSD-3-Clause AND MIT
URL:            https://jupyter.org
Source:         %{pypi_source pytest_jupyter}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
A set of pytest plugins for Jupyter libraries and extensions.}

%description %_description

%package -n     python3-pytest-jupyter
Summary:        %{summary}

%description -n python3-pytest-jupyter %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pytest_jupyter-%{version}

%generate_buildrequires
%pyproject_buildrequires -x client

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_jupyter

%check
# No real tests now as there is a circular dependency
# between pytest_jupyter and jupyter_server.
# %%pytest
%pyproject_check_import

%files -n python3-pytest-jupyter -f %{pyproject_files}
%doc README.md

%pyproject_extras_subpkg -n python3-pytest-jupyter server
%pyproject_extras_subpkg -n python3-pytest-jupyter client

%changelog
%autochangelog
