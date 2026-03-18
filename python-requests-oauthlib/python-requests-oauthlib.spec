# RHEL does not include the test dependencies
%bcond tests %{undefined rhel}

%global distname requests-oauthlib
%global modname requests_oauthlib

Name:               python-requests-oauthlib
Version:            1.3.1
Release:            16%{?dist}
Summary:            OAuthlib authentication support for Requests.

License:            ISC
URL:                http://pypi.python.org/pypi/requests-oauthlib
Source0:            https://github.com/requests/requests-oauthlib/archive/v%{version}.tar.gz

BuildArch:          noarch

%description
This project provides first-class OAuth library support for python-request.

%package -n python3-%{distname}
%{?python_provide:%python_provide python3-%{distname}}
Summary:            OAuthlib authentication support for Requests.

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools

BuildRequires:      python3-oauthlib >= 0.6.2
BuildRequires:      python3-requests >= 2.0.0

%if %{with tests}
BuildRequires:      python3-pytest
BuildRequires:      python3-pytest-mock
BuildRequires:      python3-requests-mock
%endif

Requires:           python3-oauthlib
Requires:           python3-requests

%description -n python3-%{distname}
This project provides first-class OAuth library support for python-request.

%prep
%autosetup -n %{distname}-%{version} -p1

# Remove bundled egg-info in case it exists
rm -rf %{distname}.egg-info


%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
%pytest -k "not testCanPostBinaryData and not test_content_type_override and not test_url_is_native_str"
%else
%py3_check_import %{modname}
%endif

%files -n python3-%{distname}
%doc README.rst HISTORY.rst requirements.txt AUTHORS.rst
%license LICENSE
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.1-16
- Prepare for Oreon 11 (RP1)
