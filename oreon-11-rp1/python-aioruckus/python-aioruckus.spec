%global source0_hash f6d2223710a70d1bf5270c13c7188444d5fedc4d069b9b23dd58e5cc3c1e9593

%global srcname aioruckus

# Tests are disabled as they require a live deployment to test against
%bcond_with tests

Name:           python-%{srcname}
Version:        0.37
Release:        %autorelease
Summary:        Interact with Ruckus Unleashed and ZoneDirector devices

License:        0BSD
URL:            https://github.com/ms264556/aioruckus
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
%endif

%global _description %{expand:
This package provides a Python API which interacts with Ruckus Unleashed and
ZoneDirector devices via their AJAX Web Service interface. Configuration
information can also be queried from Ruckus Unleashed and ZoneDirector backup
files.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%if %{with tests}
%pytest
%else
%pyproject_check_import
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
