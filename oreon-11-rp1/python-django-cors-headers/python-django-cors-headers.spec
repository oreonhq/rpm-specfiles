%global source0_hash 96069c4aaacace786a34ee7894ff680780ec2644e4268b31181044410fecd12e

%global srcname django-cors-headers

Name:           python-%{srcname}
Version:        3.7.0
Release:        19%{?dist}
Summary:        Django application for handling the server headers required for CORS

License:        MIT
URL:            https://github.com/adamchainz/django-cors-headers
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
A Django App that adds Cross-Origin Resource Sharing (CORS) headers
to responses. This allows in-browser requests to your Django application
from other origins.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1
rm -vrf *.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst HISTORY.rst
%{python3_sitelib}/django_cors_headers-*.egg-info/
%{python3_sitelib}/corsheaders/

%changelog
%autochangelog
