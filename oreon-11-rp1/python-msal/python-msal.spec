%global source0_hash 6ab7de335e6d7f5717e2c7e1dbf86e4dda2f6acf3c56773b78dc53ebc6395b5f
Name:           python-msal
Version:        1.39.0
Release:        1%{?dist}
Summary:        The Microsoft Authentication Library _MSAL_ for Python library enables your app to access the Microsoft Cloud by supporting authentication of users with Microsoft Azure Active Directory accounts _AAD_ and Microsoft Accounts _MSA_ using industry standard OAuth2 and OpenID Connect.
License:        MIT
URL:            https://github.com/AzureAD/microsoft-authentication-library-for-python/releases
Source0:        https://files.pythonhosted.org/packages/source/m/msal/msal-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-msal = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-msal
Summary:        The Microsoft Authentication Library _MSAL_ for Python library enables your app to access the Microsoft Cloud by supporting authentication of users with Microsoft Azure Active Directory accounts _AAD_ and Microsoft Accounts _MSA_ using industry standard OAuth2 and OpenID Connect.
%description -n python3-msal

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir msal-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-msal usr/lib/python3*/site-packages/msal* usr/lib64/python3*/site-packages/msal* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/msal* usr/lib64/python3*/site-packages/msal* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-msal -f %{oreon_filedir}/python3-msal.list

%changelog

%autochangelog
