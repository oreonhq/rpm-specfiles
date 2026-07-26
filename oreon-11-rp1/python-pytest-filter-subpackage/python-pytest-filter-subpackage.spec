%global source0_hash 3f468f1b36518128869b95deab661ba45ed6293854329fef14da4c8cac78af56

%global srcname pytest-filter-subpackage
%global modname pytest_filter_subpackage
%global sum Pytest plugin for filtering based on sub-packages

Name:           python-%{srcname}
Version:        0.2.0
Release:        %autorelease
Summary:        %{sum}

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
This package contains a simple plugin for the pytest framework that provides
a shortcut to testing all code and documentation for a given sub-package.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{sum}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

# Remove egg files from source
rm -rf %{pythonicname}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.rst
%doc README.rst CHANGES.rst

%changelog
%autochangelog
