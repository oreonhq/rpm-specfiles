%global source0_hash 2ed3d5dadf9e8aef2ef1f3cdfa3cf9abae99c9eac5a2db0267f17a9dae3a66e1

%global srcname rxjson

Name:             python-%{srcname}
Summary:          JSON RX Schema validation tool
Version:          0.3
Release:          29%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:          GPL-2.0-or-later
URL:              https://pypi.python.org/pypi/rxjson
Source0:          %{pypi_source %{srcname} %{version} zip}

BuildArch:        noarch

%global _description\
JSON RX Schema validation tool.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-d2to1

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
rm -vrf *.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc README.rst
%{python3_sitelib}/%{srcname}*

%changelog
%autochangelog
