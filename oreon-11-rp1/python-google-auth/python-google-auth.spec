%global source0_hash 55e30cf15e737de92c5323d78cda8a83fcd57e7ffbaf900c4600039fd60a80fd
Name:           python-google-auth
Version:        2.58.0
Release:        1%{?dist}
Summary:        Google Authentication Library
License:        ...
URL:            https://github.com/googleapis/google-cloud-python/tree/main/packages/google-auth
Source0:        https://files.pythonhosted.org/packages/source/g/google_auth/google_auth-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-google-auth = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-google-auth
Summary:        Google Authentication Library
%description -n python3-google-auth

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir google_auth-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-google-auth usr/lib/python3*/site-packages/google_auth* usr/lib64/python3*/site-packages/google_auth* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/google_auth* usr/lib64/python3*/site-packages/google_auth* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-google-auth -f %{oreon_filedir}/python3-google-auth.list

%changelog

%autochangelog
