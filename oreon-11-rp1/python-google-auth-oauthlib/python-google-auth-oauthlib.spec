%global source0_hash 1a83f5f2a8421dedadaa3caf25b3a710dddf85a33a63144be41c2fc79174b106
Name:           python-google-auth-oauthlib
Version:        1.4.1
Release:        1%{?dist}
Summary:        Google Authentication Library
License:        ...
URL:            https://github.com/googleapis/google-cloud-python/tree/main/packages/google-auth-oauthlib
Source0:        https://files.pythonhosted.org/packages/source/g/google_auth_oauthlib/google_auth_oauthlib-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-google-auth-oauthlib = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-google-auth-oauthlib
Summary:        Google Authentication Library
%description -n python3-google-auth-oauthlib

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir google_auth_oauthlib-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-google-auth-oauthlib usr/lib/python3*/site-packages/google_auth_oauthlib* usr/lib64/python3*/site-packages/google_auth_oauthlib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/google_auth_oauthlib* usr/lib64/python3*/site-packages/google_auth_oauthlib* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-google-auth-oauthlib -f %{oreon_filedir}/python3-google-auth-oauthlib.list

%changelog

%autochangelog
