%global source0_hash d3dbeb0999ffd0e68aa4bd73f2ac698a18133fd11b3fc890e1366f18c8889fac

%global pypi_name social-auth-core
%global egginfo_name social_auth_core
# The Python module name is different from the package name published to PyPI.
%global module_name social_core

%global desc %{expand:
Python Social Auth aims to be an easy-to-setup social authentication and
authorization mechanism for Python projects supporting protocols like OAuth (1
and 2), OpenID and others.

The initial codebase is derived from django-social-auth with the idea of
generalizing the process to suit the different frameworks around, providing
the needed tools to bring support to new frameworks.

django-social-auth itself was a product of modified code from
django-twitter-oauth and django-openid-auth projects.

The project is now split into smaller modules to isolate and reduce
responsibilities and improve reusability.

Documentation: https://python-social-auth.readthedocs.io/en/latest/
Release notes: https://github.com/python-social-auth/%{module_name}/releases/tag/4.2.0
}

%global summary Python Social Auth is an easy to setup social authentication\/registration mechanism with support for several frameworks and auth providers.

Name:           python-%{pypi_name}
Version:        4.5.4
Release:        8%{?dist}
Summary:        %{summary}
License:        BSD-3-Clause
URL:            https://github.com/python-social-auth/social-core/
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

# Requirements for running social-core
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(oauthlib)
BuildRequires:  python3dist(requests-oauthlib)
BuildRequires:  python3dist(pyjwt) >= 2.7.0
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(defusedxml)
BuildRequires:  python3dist(python3-openid) >= 3.0.10
BuildRequires:  python3dist(python3-saml)

# Requirements for running tests
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(httpretty)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)

%description
%{desc}

%package -n python3-%{pypi_name}
Summary: %{summary}
%py_provides python3-%{pypi_name}

Requires:       python3dist(cryptography) >= 2.1.1
Requires:       python3dist(defusedxml)
Requires:       python3dist(oauthlib)
Requires:       python3dist(pyjwt) >= 2.7.0
Requires:       python3dist(python3-openid) >= 3.0.10
Requires:       python3dist(requests)
Requires:       python3dist(requests-oauthlib)

%description -n python3-%{pypi_name}
%{desc}
If you want social-core to work with azuread (the Azure Active Directory), this
is the package you need.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

rm -rf %{egginfo_name}.egg-info

%build
%py3_build

%install
%py3_install

rm -r %{buildroot}%{python3_sitelib}/%{module_name}/tests/

%check
%{pytest} %{module_name}/tests/

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md CHANGELOG.md
%{python3_sitelib}/%{module_name}/
%{python3_sitelib}/%{egginfo_name}-%{version}-py*.egg-info

%changelog
%autochangelog
