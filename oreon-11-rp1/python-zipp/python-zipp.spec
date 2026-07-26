%global source0_hash a07157588a12518c9d4034df3fbbee09c814741a33ff63c05fa29d26a2404166

%global pypi_name zipp

Name:           python-%{pypi_name}
Version:        3.23.0
Release:        %autorelease
Summary:        Backport of pathlib-compatible object wrapper for zip files

# SPDX
License:        MIT
URL:            https://github.com/jaraco/zipp
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
# Not using test dependencies because the list
# is full of linters and static code checkers
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(jaraco-functools)
BuildRequires:  python3dist(jaraco-test)

%description
A pathlib-compatible Zipfile object wrapper. A backport of the Path object.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
A pathlib-compatible Zipfile object wrapper. A backport of the Path object.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# jaraco.itertools and func_timeout are not available in Fedora yet
sed -i "/import jaraco.itertools/d" tests/test_path.py
# coherent.licensed is not available in Fedora yet
sed -i "/coherent.licensed/d" pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
# Skipped test needs jaraco.itertools
%pytest -k "not test_joinpath_constant_time"

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
