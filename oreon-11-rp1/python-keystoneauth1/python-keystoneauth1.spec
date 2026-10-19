%global source0_hash 82359acc20c754fcb22818e090e2fea647e4c5c1137a6addb4984e9fba708ab3
Name:           python-keystoneauth1
Version:        5.17.0
Release:        1%{?dist}
Summary:        Authentication Library for OpenStack Identity
License:        Apache-2.0
URL:            https://opendev.org/openstack/keystoneauth/
Source0:        https://files.pythonhosted.org/packages/source/k/keystoneauth1/keystoneauth1-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr) >= 6.1.1
Requires:       python3-keystoneauth1 = %{version}-%{release}
# /oreon:deps
%package -n       python3-keystoneauth1+kerberos
Summary:        Metapackage for python3-keystoneauth1 kerberos extras
Requires:       python3-keystoneauth1 = %{version}-%{release}
Requires:       python3dist(requests-kerberos) >= 0.8.0
Provides:       python3dist(keystoneauth1[kerberos]) = %{version}-%{release}

%description -n python3-keystoneauth1+kerberos
Metapackage for python3-keystoneauth1 kerberos extras.

%package -n       python3-keystoneauth1+saml2
Summary:        Metapackage for python3-keystoneauth1 saml2 extras
Requires:       python3-keystoneauth1 = %{version}-%{release}
Requires:       python3dist(lxml) >= 4.2.0
Provides:       python3dist(keystoneauth1[saml2]) = %{version}-%{release}

%description -n python3-keystoneauth1+saml2
Metapackage for python3-keystoneauth1 saml2 extras.

%package -n       python3-keystoneauth1+oauth1
Summary:        Metapackage for python3-keystoneauth1 oauth1 extras
Requires:       python3-keystoneauth1 = %{version}-%{release}
Requires:       python3dist(oauthlib) >= 0.6.2
Provides:       python3dist(keystoneauth1[oauth1]) = %{version}-%{release}

%description -n python3-keystoneauth1+oauth1
Metapackage for python3-keystoneauth1 oauth1 extras.

%package -n       python3-keystoneauth1+betamax
Summary:        Metapackage for python3-keystoneauth1 betamax extras
Requires:       python3-keystoneauth1 = %{version}-%{release}
Requires:       python3dist(betamax) >= 0.7.0
Requires:       python3dist(fixtures) >= 3.0.0
Requires:       python3dist(pyyaml) >= 3.13
Provides:       python3dist(keystoneauth1[betamax]) = %{version}-%{release}

%description -n python3-keystoneauth1+betamax
Metapackage for python3-keystoneauth1 betamax extras.

%description

%package -n     python3-keystoneauth1
Summary:        Authentication Library for OpenStack Identity
%description -n python3-keystoneauth1

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir keystoneauth1-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-keystoneauth1 usr/lib/python3*/site-packages/keystoneauth1* usr/lib64/python3*/site-packages/keystoneauth1* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/keystoneauth1* usr/lib64/python3*/site-packages/keystoneauth1* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-keystoneauth1 -f %{oreon_filedir}/python3-keystoneauth1.list

%changelog

%autochangelog
