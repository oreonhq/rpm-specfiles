%global source0_hash 1e8b678473fef38a972d3e4c5f6fa898558abe7ba46bd56b8429cc484483bf7b
Name:           python-social-auth-core
Version:        5.1.0
Release:        1%{?dist}
Summary:        Python social authentication made simple.
License:        BSD-3-Clause
URL:            https://github.com/python-social-auth/social-core
Source0:        https://files.pythonhosted.org/packages/source/s/social_auth_core/social_auth_core-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 78.0.2
Requires:       python3-social-auth-core = %{version}-%{release}
# /oreon:deps
%package -n       python3-social-auth-core+all
Summary:        Metapackage for python3-social-auth-core all extras
Requires:       python3-social-auth-core = %{version}-%{release}
Provides:       python3dist(social-auth-core[all]) = %{version}-%{release}

%description -n python3-social-auth-core+all
Metapackage for python3-social-auth-core all extras.

%package -n       python3-social-auth-core+allpy3
Summary:        Metapackage for python3-social-auth-core allpy3 extras
Requires:       python3-social-auth-core = %{version}-%{release}
Provides:       python3dist(social-auth-core[allpy3]) = %{version}-%{release}

%description -n python3-social-auth-core+allpy3
Metapackage for python3-social-auth-core allpy3 extras.

%package -n       python3-social-auth-core+dev
Summary:        Metapackage for python3-social-auth-core dev extras
Requires:       python3-social-auth-core = %{version}-%{release}
Requires:       python3dist(coverage) == 7.15.3
Requires:       python3dist(flake8) == 7.3.0
Requires:       python3dist(google-auth-stubs) == 0.3.0
Requires:       python3dist(mypy) == 2.3.0
Requires:       python3dist(pyright) == 1.1.411
Requires:       python3dist(pytest-cov) == 7.1.0
Requires:       python3dist(pytest-github-actions-annotate-failures) == 0.4.2
Requires:       python3dist(pytest-profiling) == 1.8.1
Requires:       python3dist(pytest-xdist) == 3.8.0
Requires:       python3dist(pytest) == 9.1.1
Requires:       python3dist(responses) == 0.26.2
Requires:       python3dist(ty) == 0.0.69
Requires:       python3dist(types-defusedxml) == 0.7.0.20260504
Requires:       python3dist(types-oauthlib) == 3.3.0.20260724
Requires:       python3dist(types-requests-oauthlib) == 2.0.0.20260610
Requires:       python3dist(types-requests) == 2.33.0.20260712
Provides:       python3dist(social-auth-core[dev]) = %{version}-%{release}

%description -n python3-social-auth-core+dev
Metapackage for python3-social-auth-core dev extras.

%package -n       python3-social-auth-core+google-onetap
Summary:        Metapackage for python3-social-auth-core google-onetap extras
Requires:       python3-social-auth-core = %{version}-%{release}
Requires:       python3dist(google-auth) >= 2.40.0
Requires:       python3dist(google-auth) < 2.57
Provides:       python3dist(social-auth-core[google-onetap]) = %{version}-%{release}

%description -n python3-social-auth-core+google-onetap
Metapackage for python3-social-auth-core google-onetap extras.

%package -n       python3-social-auth-core+saml
Summary:        Metapackage for python3-social-auth-core saml extras
Requires:       python3-social-auth-core = %{version}-%{release}
Requires:       python3dist(python3-saml) >= 1.16.0
Provides:       python3dist(social-auth-core[saml]) = %{version}-%{release}

%description -n python3-social-auth-core+saml
Metapackage for python3-social-auth-core saml extras.

%package -n       python3-social-auth-core+shopify
Summary:        Metapackage for python3-social-auth-core shopify extras
Requires:       python3-social-auth-core = %{version}-%{release}
Provides:       python3dist(social-auth-core[shopify]) = %{version}-%{release}

%description -n python3-social-auth-core+shopify
Metapackage for python3-social-auth-core shopify extras.

%description

%package -n     python3-social-auth-core
Summary:        Python social authentication made simple.
# oreon:reqs
Requires:       python3dist(cryptography) >= 46.0.7
Requires:       python3dist(defusedxml) >= 0.7.1
Requires:       python3dist(oauthlib) >= 3.3.1
Requires:       python3dist(pyjwt[crypto]) >= 2.13.0
Requires:       python3dist(python3-openid) >= 3.2.0
Requires:       python3dist(requests) >= 2.34.0
Requires:       python3dist(requests-oauthlib) >= 2.0.0
# /oreon:reqs
%description -n python3-social-auth-core

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir social_auth_core-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-social-auth-core usr/lib/python3*/site-packages/social_auth_core* usr/lib64/python3*/site-packages/social_auth_core* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/social_auth_core* usr/lib64/python3*/site-packages/social_auth_core* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-social-auth-core -f %{oreon_filedir}/python3-social-auth-core.list

%changelog

%autochangelog
