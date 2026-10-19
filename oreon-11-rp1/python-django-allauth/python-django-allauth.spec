%global source0_hash 7ea5f0057f91fa25f9ca7814f84aed63a66096b43df073fbdf1ef0167bc92f1d
Name:           python-django-allauth
Version:        65.19.4
Release:        1%{?dist}
Summary:        Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party _social_ account authentication.
License:        MIT
URL:            https://allauth.org
Source0:        https://files.pythonhosted.org/packages/source/d/django_allauth/django_allauth-%{version}.tar.gz
BuildArch:      noarch
Patch:          django-allauth-relax-coverage-version.diff
Patch:          django-allauth-lower_pytest-asyncio_req.diff
Patch:          django-allauth-no-django-ninja.diff
Patch:          django-allauth-relax-xmlsec-version.diff
Patch:          django-allauth-relax-lxml-version.diff
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 75.3.0
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-django-allauth = %{version}-%{release}
# /oreon:deps
%package -n       python3-django-allauth+headless
Summary:        Metapackage for python3-django-allauth headless extras
Requires:       python3-django-allauth = %{version}-%{release}
Requires:       python3dist(pyjwt[crypto]) >= 2.0
Requires:       python3dist(pyjwt[crypto]) < 3
Provides:       python3dist(django-allauth[headless]) = %{version}-%{release}

%description -n python3-django-allauth+headless
Metapackage for python3-django-allauth headless extras.

%package -n       python3-django-allauth+headless-spec
Summary:        Metapackage for python3-django-allauth headless-spec extras
Requires:       python3-django-allauth = %{version}-%{release}
Requires:       python3dist(pyyaml) >= 6
Requires:       python3dist(pyyaml) < 7
Provides:       python3dist(django-allauth[headless-spec]) = %{version}-%{release}

%description -n python3-django-allauth+headless-spec
Metapackage for python3-django-allauth headless-spec extras.

%package -n       python3-django-allauth+idp-oidc
Summary:        Metapackage for python3-django-allauth idp-oidc extras
Requires:       python3-django-allauth = %{version}-%{release}
Requires:       python3dist(oauthlib) >= 3.3.0
Requires:       python3dist(oauthlib) < 4
Requires:       python3dist(pyjwt[crypto]) >= 2.0
Requires:       python3dist(pyjwt[crypto]) < 3
Provides:       python3dist(django-allauth[idp-oidc]) = %{version}-%{release}

%description -n python3-django-allauth+idp-oidc
Metapackage for python3-django-allauth idp-oidc extras.

%package -n       python3-django-allauth+mfa
Summary:        Metapackage for python3-django-allauth mfa extras
Requires:       python3-django-allauth = %{version}-%{release}
Requires:       python3dist(qrcode) >= 7.0.0
Requires:       python3dist(qrcode) < 9
Requires:       python3dist(fido2) >= 1.1.2
Requires:       python3dist(fido2) < 3
Provides:       python3dist(django-allauth[mfa]) = %{version}-%{release}

%description -n python3-django-allauth+mfa
Metapackage for python3-django-allauth mfa extras.

%package -n       python3-django-allauth+openid
Summary:        Metapackage for python3-django-allauth openid extras
Requires:       python3-django-allauth = %{version}-%{release}
Requires:       python3dist(python3-openid) >= 3.0.8
Requires:       python3dist(python3-openid) < 4
Provides:       python3dist(django-allauth[openid]) = %{version}-%{release}

%description -n python3-django-allauth+openid
Metapackage for python3-django-allauth openid extras.

%package -n       python3-django-allauth+saml
Summary:        Metapackage for python3-django-allauth saml extras
Requires:       python3-django-allauth = %{version}-%{release}
Requires:       python3dist(python3-saml) >= 1.15.0
Requires:       python3dist(python3-saml) < 2.0.0
Provides:       python3dist(django-allauth[saml]) = %{version}-%{release}

%description -n python3-django-allauth+saml
Metapackage for python3-django-allauth saml extras.

%package -n       python3-django-allauth+steam
Summary:        Metapackage for python3-django-allauth steam extras
Requires:       python3-django-allauth = %{version}-%{release}
Requires:       python3dist(python3-openid) >= 3.0.8
Requires:       python3dist(python3-openid) < 4
Provides:       python3dist(django-allauth[steam]) = %{version}-%{release}

%description -n python3-django-allauth+steam
Metapackage for python3-django-allauth steam extras.

%package -n       python3-django-allauth+socialaccount
Summary:        Metapackage for python3-django-allauth socialaccount extras
Requires:       python3-django-allauth = %{version}-%{release}
Requires:       python3dist(oauthlib) >= 3.3.0
Requires:       python3dist(oauthlib) < 4
Requires:       python3dist(requests) >= 2.0.0
Requires:       python3dist(requests) < 3
Requires:       python3dist(pyjwt[crypto]) >= 2.0
Requires:       python3dist(pyjwt[crypto]) < 3
Provides:       python3dist(django-allauth[socialaccount]) = %{version}-%{release}

%description -n python3-django-allauth+socialaccount
Metapackage for python3-django-allauth socialaccount extras.

%description

%package -n     python3-django-allauth
Summary:        Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party _social_ account authentication.
# oreon:reqs
Requires:       python3dist(asgiref) >= 3.8.1
Requires:       python3dist(django) >= 4.2.16
# /oreon:reqs
%description -n python3-django-allauth

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir django_allauth-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-django-allauth usr/lib/python3*/site-packages/django_allauth* usr/lib64/python3*/site-packages/django_allauth* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/django_allauth* usr/lib64/python3*/site-packages/django_allauth* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-django-allauth -f %{oreon_filedir}/python3-django-allauth.list

%changelog

%autochangelog
