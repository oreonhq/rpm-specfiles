# RHEL does not include the test dependencies
%bcond tests %{undefined rhel}

%global distname requests-oauthlib
%global modname requests_oauthlib

Name:               python-requests-oauthlib
Version:            2.0.0
Release:            1%{?dist}
Summary:            OAuthlib authentication support for Requests.

License:            ISC
URL:                http://pypi.python.org/pypi/requests-oauthlib
Source0:            https://github.com/requests/requests-oauthlib/archive/v%{version}/requests-oauthlib-%{version}.tar.gz
# Updated tests to support oauthlib 3.3.0 wrt expires_at
Patch0:             https://github.com/requests/requests-oauthlib/commit/b1dd93c5d024500b6236dea06734d6e6482c3565.patch

BuildArch:          noarch

%description
This project provides first-class OAuth library support for python-request.

%package -n python3-%{distname}
%{?python_provide:%python_provide python3-%{distname}}
Summary:            OAuthlib authentication support for Requests.

BuildRequires:      python3-devel
%if %{with tests}
BuildRequires:      python3-pytest
BuildRequires:      python3-pytest-mock
BuildRequires:      python3-requests-mock
BuildRequires:      python3-selenium, selenium-manager
%endif

%description -n python3-%{distname}
This project provides first-class OAuth library support for python-request.

%prep
%autosetup -n %{distname}-%{version} -p1
# Requires python-selenium fix from unmerged https://src.fedoraproject.org/rpms/python-selenium/pull-request/9
# Furthermore then throws error on insisting on only chrome-146 but fedora has 148
rm tests/examples/test_native_spa_pkce_auth0.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{modname}

%check
%if %{with tests}
%pytest -k "not testCanPostBinaryData and not test_content_type_override and not test_url_is_native_str"
%else
%pyproject_check_import
%endif

%files -n python3-%{distname} -f %{pyproject_files}
%doc README.rst HISTORY.rst requirements.txt AUTHORS.rst

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.0-1
- Import
