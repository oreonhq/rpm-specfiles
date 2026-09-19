%global source0_hash 3413c6a1213684ccebed70bc7ec11c5f19eff38dde07e8998e729df8b7668693

%bcond check 0
%global pypi_name aspy.yaml

Name:           python-%{pypi_name}
Version:        1.3.0
Release:        28%{?dist}
Summary:        Few extensions to PyYAML

License:        MIT
URL:            https://github.com/asottile/aspy.yaml
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with check}
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3-pytest
%endif

%description
A few extensions to PyYAML.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l aspy

%if %{with check}
%check
%pyproject_check_import

%{python3} -m pytest -v
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
