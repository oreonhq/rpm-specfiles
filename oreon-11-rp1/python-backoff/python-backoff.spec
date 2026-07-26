%global source0_hash 7b92e74aac38ec49e97ac899c96c882496c7b09cf4235e8da205e62b2c6c001d

%global desc This module provides function decorators which can be used to wrap \
a function such that it will be retried until some condition is met. \
It is meant to be of use when accessing unreliable resources with the \
potential for intermittent failures i.e. network resources and external \
APIs. Somewhat more generally, it may also be of use for dynamically \
polling resources for externally generated content.
%global srcname backoff

Name:      python-%{srcname}
Version:   2.2.1
Release:   14%{?dist}
BuildArch: noarch

License: MIT
Summary: Python library providing function decorators for configurable backoff and retry
URL:     https://github.com/litl/backoff
Source0: %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires: pyproject-rpm-macros

%description
%{desc}

%package -n python3-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{srcname}
%license LICENSE
%doc CHANGELOG.md README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.dist-info/

%changelog
%autochangelog
