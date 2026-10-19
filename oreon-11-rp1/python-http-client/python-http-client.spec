%global source0_hash 4b87ce2dbebae18e21453ac1b8c7ea31ef3139c94decc85ff5a07d4203671c56
%global srcname http-client
%global desc Quickly and easily access any RESTful or RESTful-like API.
Name:           python-%{srcname}
Version:        3.3.7
Release:        16%{?dist}
Summary:        HTTP REST client, simplified for Python
License:        MIT
URL:            https://github.com/sendgrid/%{name}
Source0:        https://github.com/sendgrid/%{name}/archive/%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-http-client = %{version}-%{release}
# /oreon:deps
%description
%{desc}

%package -n python3-%{srcname}
Summary:        HTTP REST client, simplified for Python
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%description -n python3-%{srcname}
%{desc}
This is a Python 3 version of the package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/http_client* usr/lib64/python3*/site-packages/http_client* usr/bin/*

%check

%pytest --ignore=tests/test_daterange.py
%files
%files -n python3-http-client -f %{oreon_filedir}/python3-http-client.list

%changelog

%autochangelog
