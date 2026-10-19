%global source0_hash b4d8915a526e626b0b14a2925907554b722d3b8e3e3781570fc35791712af323
Name:           python-sentry-sdk
Version:        2.69.2
Release:        1%{?dist}
Summary:        Python client for Sentry _https://sentry.io_
License:        MIT
URL:            https://docs.sentry.io/platforms/python/
Source0:        https://files.pythonhosted.org/packages/source/s/sentry_sdk/sentry_sdk-%{version}.tar.gz
BuildArch:      noarch
Patch0:         0001-Downstream-only-unpin-virtualenv.patch
Patch1:         0002-Add-django.contrib.admin-to-INSTALLED_APPS-to-fix-te.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sentry-sdk = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sentry-sdk
Summary:        Python client for Sentry _https://sentry.io_
%description -n python3-sentry-sdk

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir sentry_sdk-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sentry-sdk usr/lib/python3*/site-packages/sentry_sdk* usr/lib64/python3*/site-packages/sentry_sdk* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sentry_sdk* usr/lib64/python3*/site-packages/sentry_sdk* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sentry-sdk -f %{oreon_filedir}/python3-sentry-sdk.list

%changelog

%autochangelog
