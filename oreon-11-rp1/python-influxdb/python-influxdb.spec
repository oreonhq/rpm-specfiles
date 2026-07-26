%global source0_hash 3ba558432d4c64293ada0deccf76527777e76750e99176d3b9dbc5a72bd4163b

%global pypi_name influxdb

Name:           python-%{pypi_name}
Version:        5.2.0
Release:        28%{?dist}
Summary:        InfluxDB client

License:        MIT
URL:            https://github.com/influxdb/influxdb-python
Source0:        https://pypi.python.org/packages/e1/af/94faea244de2a73b7a0087637660db2d638edaae58f22d3f0d0d219ad8b7/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%description
InfluxDB Python is a client for interacting with InfluxDB. 

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-requests
Requires:       python3-dateutil
Requires:       python3-pytz
Requires:       python3-six

%description -n python3-%{pypi_name}
InfluxDB Python is a client for interacting with InfluxDB.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py*egg-info

%changelog
%autochangelog
