%global source0_hash 7fffae1407a2fad8d33319b20c4839ea066a76776b79c312f93d43641c0df4ac

%global modname pyongc

Name:           python-%{modname}
Version:        1.2.0
Release:        %autorelease
Summary:        A python interface for accessing OpenNGC database data
# Code license is MIT, database is CC-BY-SA-4.0
License:        MIT AND CC-BY-SA-4.0
URL:            https://pypi.python.org/pypi/PyOngc
Source:         %{pypi_source pyongc}

BuildArch:      noarch
BuildRequires:  python3-devel

# For tests
BuildRequires:  python3dist(pytest)

%global _description %{expand:
PyOngc provides a python module to access astronomical data about
NGC and IC objects from the OpenNGC database.}

%description %_description

%package -n     python3-%{modname}
Summary:        %{summary}

%description -n python3-%{modname} %_description

%pyproject_extras_subpkg -n python3-pyongc data

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x data

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname} -l

%check
%pyproject_check_import
%pytest tests

%files -n python3-%{modname} -f %{pyproject_files}
%doc README.rst
%{_bindir}/ongc

%changelog
%autochangelog
