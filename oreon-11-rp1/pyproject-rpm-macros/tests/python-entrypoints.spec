%global source0_hash c70dd71abe5a8c85e55e12c19bd91ccfeec11a6e99044204511f9ed547d48451

%global pypi_name entrypoints
Name:           python-%{pypi_name}
Version:        0.3
Release:        0%{?dist}
Summary:        Discover and load entry points from installed packages
License:        MIT
URL:            https://entrypoints.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/e/entrypoints/entrypoints-0.3.tar.gz

BuildArch:      noarch

%description
This package contains one .py module
Building this tests the flit(_core) build backend.
This package also has no explicit BuildRequires for python or the macros,
testing the minimal implementation of %%pyproject_buildrequires
from pyproject-srpm-macros.


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{summary}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n %{pypi_name}-%{version}
%if 0%{?rhel}
# force the flit-core build backend, as that is available rather than full flit
sed -i 's/"flit/"flit_core/' pyproject.toml
%endif


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# the license is not marked as License-File, hence -L
%pyproject_save_files entrypoints -L


%check
# Internal check: Top level __pycache__ is never owned
grep -E '/__pycache__$' %{pyproject_files} && exit 1 || true
grep -E '/__pycache__/$' %{pyproject_files} && exit 1 || true
grep -F '/__pycache__/' %{pyproject_files}


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE
