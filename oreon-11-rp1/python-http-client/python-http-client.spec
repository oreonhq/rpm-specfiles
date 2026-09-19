%global source0_hash 4b87ce2dbebae18e21453ac1b8c7ea31ef3139c94decc85ff5a07d4203671c56

%global srcname http-client
%global desc Quickly and easily access any RESTful or RESTful-like API.

Name:           python-%{srcname}
Version:        3.3.7
Release:        16%{?dist}
Summary:        HTTP REST client, simplified for Python
License:        MIT
URL:            https://github.com/sendgrid/%{name}
Source0:        %{url}/archive/%{version}.tar.gz

BuildArch:      noarch

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n python3-%{srcname}
%{desc}
This is a Python 3 version of the package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
# test_daterange.py tests the presence of the current year
# in the license file and breaks every January
%pytest --ignore=tests/test_daterange.py

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst CHANGELOG.md USAGE.md
%{python3_sitelib}/python_http_client/
%{python3_sitelib}/python_http_client-%{version}.dist-info/
%exclude %{python3_sitelib}/tests

%changelog
%autochangelog
