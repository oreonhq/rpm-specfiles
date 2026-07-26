%global source0_hash 3efa13b335a00a8de1d345ae41ec78dd11c9f8807f522d39850f2dd828681540

%global pypi_name pytzdata

%global _description %{expand:
The Olson timezone database for Python.

This package contains the python bindings to the database provided by
the tzdata package as installed (version %{version} or later).}

Name: python-%{pypi_name}
Version: 2020.1
Release: %autorelease

License: MIT
Summary: Timezone database for Python
URL: https://github.com/sdispater/%{pypi_name}
Source0: %{pypi_source}
BuildArch: noarch

# Cleo was updated to 1.0.0a5 because the latest version of poetry needed it.
# It changed the way how some modules are imported and this patch should fix it.
Patch1: %{pypi_name}-cleo-imports-fix.patch

# Set mandatory name attribute in Command class to make pytzdata
# compatible with cleo 2.0.0+.
Patch2: %{pypi_name}-cleo-2.0.0-compatibility.patch

Patch3: 0001-reduce-poetry-build-dependency-to-core.patch
Patch4: 0001-do-not-include-dev-commands-in-wheel.patch

BuildRequires: python3-devel
BuildRequires: tzdata >= %{version}

%description %_description

%package -n python3-%{pypi_name}
Summary: %{summary}
Requires: tzdata >= %{version}

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1
rm -r pytzdata/zoneinfo
sed -i "s|os.path.dirname(__file__)|'%{_datadir}'|" pytzdata/__init__.py

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
