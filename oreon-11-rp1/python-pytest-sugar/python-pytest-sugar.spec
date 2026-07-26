%global source0_hash 73b8b65163ebf10f9f671efab9eed3d56f20d2ca68bda83fa64740a92c08f65d

%global _description %{expand:
pytest-sugar is a plugin for pytest that shows failures and errors instantly
and shows a progress bar.}

Name:           python-pytest-sugar
Version:        1.1.1
Release:        %autorelease
Summary:        Change the default look and feel of pytest

# SPDX
License:        BSD-3-Clause
URL:            https://pypi.org/project/pytest-sugar
Source:         %{pypi_source pytest-sugar}

BuildArch:      noarch

%description %_description

%package -n python3-pytest-sugar
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

%description -n python3-pytest-sugar %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pytest-sugar-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pytest_sugar

%check
PYTHONPATH=. %{pytest} -v -s

%files -n python3-pytest-sugar -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
