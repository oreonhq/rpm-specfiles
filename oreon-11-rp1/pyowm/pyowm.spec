%global source0_hash a1ddefe7c3d79ab81f0c3cd84fb53a40dc7e5bdcd20c1cea491e5ad5d45c8eec

%global pypi_name pyowm
# needs api key for tests
%global with_tests 0

Name:           pyowm
Version:        3.5.0
Release:        1%{?dist}
Summary:        A Python wrapper around the OpenWeatherMap web API

License:        MIT
URL:            https://github.com/csparpa/pyowm
Source0:        https://github.com/csparpa/pyowm/archive/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if 0%{?with_tests}
BuildRequires:  python3-pytest
%endif

%description
PyOWM is a client Python wrapper library for the OpenWeatherMap web API.
It allows quick and easy consumption of OWM weather data from Python
applications via a simple object model and in a human-friendly fashion.

%package     -n python3-%{pypi_name}
Summary: A Python wrapper around the OpenWeatherMap web API
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires: python3-requests
Requires: python3-coverage

%description -n python3-%{pypi_name}
PyOWM is a client Python wrapper library for the OpenWeatherMap web API.
It allows quick and easy consumption of OWM weather data from Python
applications via a simple object model and in a human-friendly fashion.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

# Strip out #!/usr/bin/env python
sed -i -e '1{\@^#!/usr/bin/env python@d}' %{buildroot}%{python3_sitelib}/%{pypi_name}/*.py

%check
%if %{with_tests}
%{__python3} setup.py test
%endif

%files -n python3-%{pypi_name}
%doc README.md CONTRIBUTORS.md
%license LICENSE
%{python3_sitelib}/*

%changelog
%autochangelog
