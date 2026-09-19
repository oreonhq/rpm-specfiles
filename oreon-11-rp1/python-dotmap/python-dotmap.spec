%global source0_hash 5821a7933f075fb47563417c0e92e0b7c031158b4c9a6a7e56163479b658b368

%bcond_without tests

%global pypi_name dotmap

%global _description %{expand:
DotMap is a dot-access dict subclass that has dynamic hierarchy
creation (autovivification), can be initialized with keys, easily
initializes from dict, easily converts to dict, is ordered by insertion.
The key feature is exactly what you want: dot-access.}

Name:           python-%{pypi_name}
Version:        1.3.30
Release:        16%{?dist}
Summary:        Dot access dictionary with dynamic hierarchy creation and ordered iteration

License:        MIT
URL:            https://github.com/drgrib/%{pypi_name}
Source0:        %{pypi_source dotmap}

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  make
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files dotmap

%check
%if %{with tests}
python3 -m unittest
%endif

%files -n python3-dotmap -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
%autochangelog
