%global source0_hash 50057fd5ad5fcf047f542dfc6747a896e7ef982f1b5f8500daf51f3abd609962

%global pypi_name dropbox
Name:           python-%{pypi_name}
Version:        12.0.2
Release:        12%{?dist}
Summary:        Official Dropbox REST API Client
License:        MIT

URL:            https://www.dropbox.com/developers/core/sdks
Source0:        %pypi_source
# Remove pytest-runner / setup.py test support
# https://github.com/dropbox/dropbox-sdk-python/pull/523
# Without changes to requirements.txt, which is not in the PyPI sdist
Patch:          dropbox-12.0.2-no-pytest-runner.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
A Python library for Dropbox's HTTP-based Core and Datastore APIs.

%package -n python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-requests
Requires:       python3-six
Requires:       python3-urllib3

%description -n python3-%{pypi_name}
A Python library for Dropbox's HTTP-based Core and Datastore APIs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
%autochangelog
