%global source0_hash 79fde304101ef127626cd6a75ea843b3f7fe6759b0c789b342042ad6091e3b9e

%global srcname ns1-python

Name:           python-%{srcname}
Version:        0.17.1
Release:        %autorelease
Summary:        Python SDK for the NS1 DNS platform

License:        MIT
URL:            https://github.com/ns1/ns1-python
Source:         %{pypi_source}

Patch0001:      https://github.com/ns1/ns1-python/pull/75.patch#/0001-Fixup-compatibility-with-Python-3.10.patch

BuildArch:      noarch

%global _description %{expand:
This package provides a python SDK for accessing the NS1 DNS platform
and includes both a simple NS1 REST API wrapper as well as a higher level
interface for managing zones, records, data feeds, and more.
It supports synchronous and asynchronous transports.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Recommends:     python%{python3_version}dist(requests)
Suggests:       python%{python3_version}dist(twisted)

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1
rm -vrf *.egg-info
# Tests are not distributed on PyPI
sed -i -e '/setup_requires/,+3d' setup.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/ns1_python-*.egg-info/
%{python3_sitelib}/ns1/

%changelog
%autochangelog
