%global source0_hash 15de008451739d29ecf8089f550f4c96c45ae06bc68e1e6821e267a5ef4ec176

%global pretty_name BatAlgorithm
%global extract_name buma-BatAlgorithm-d913e9d
%global new_name batalgorithm

%global _description %{expand:
Implementation of Bat Algorithm in Python.}

Name:           python-%{new_name}
Version:        0.3.1
Release:        19%{?dist}
Summary:        Bat Algorithm for optimization

License:        MIT
URL:            https://github.com/buma/BatAlgorithm
Source0:        %{url}/tarball/master/%{extract_name}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{new_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{new_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{extract_name}

%build
%py3_build

%install
%py3_install

%files -n python3-%{new_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pretty_name}-%{version}-py%{python3_version}.egg-info
%pycached %{python3_sitelib}/%{pretty_name}.py

%changelog
%autochangelog
