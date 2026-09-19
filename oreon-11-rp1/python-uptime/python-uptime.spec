%global source0_hash 7c300254775b807ce46e3dcbcda30aa3b9a204b9c57a7ac1e79ee6dbe3942973

%global pypi_name uptime

Name:           python-%{pypi_name}
Version:        3.0.1
Release:        21%{?dist}
Summary:        Cross-platform uptime library

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/Cairnarvon/uptime
Source0:        %{pypi_source}

BuildRequires:  gcc

%description
This module provides a cross-platform way to retrieve system uptime and boot
time.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This module provides a cross-platform way to retrieve system uptime and boot
time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
sed -i -e '/^#!\//, 1d' src/__*.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license COPYING.txt
%doc README.txt
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
