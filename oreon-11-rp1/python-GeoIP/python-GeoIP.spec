%global source0_hash a890da6a21574050692198f14b07aa4268a01371278dfc24f71cd9bc87ebf0e6

%global srcname GeoIP
%global sum Python bindings for the GeoIP geographical lookup libraries

Name:           python-GeoIP
Version:        1.3.2
Release:        36%{?dist}
Summary:        Python bindings for the GeoIP geographical lookup libraries

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.maxmind.com/download/geoip/api/python/
Source0:        http://pypi.python.org/packages/source/G/GeoIP/GeoIP-%{version}.tar.gz

BuildRequires:  gcc
# GeoIP 1.4.8 required by v1.2.7 of this package per README
BuildRequires:  GeoIP-devel >= 1.4.8
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
This package contains the Python bindings for the GeoIP API, allowing IP to
location lookups to country, city and organization level within Python code.

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This package contains the Python bindings for the GeoIP API, allowing IP to
location lookups to country, city and organization level within Python code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n GeoIP-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc README.rst examples/
%license LICENSE
%{python3_sitearch}/GeoIP*.so
%{python3_sitearch}/*egg-info

%changelog
%autochangelog
