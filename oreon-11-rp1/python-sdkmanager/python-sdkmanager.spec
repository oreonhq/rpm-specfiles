%global source0_hash 49063acd70f37826ae2e88a78fe774d394b0a56cbc538649f40369834e356c67
Name:           python-sdkmanager
Version:        0.7.1
Release:        1%{?dist}
Summary:        Android SDK Manager
License:        AGPL-3.0-or-later
URL:            https://gitlab.com/fdroid/sdkmanager
Source0:        https://files.pythonhosted.org/packages/source/s/sdkmanager/sdkmanager-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sdkmanager = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sdkmanager
Summary:        Android SDK Manager
%description -n python3-sdkmanager

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir sdkmanager-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sdkmanager usr/lib/python3*/site-packages/sdkmanager* usr/lib64/python3*/site-packages/sdkmanager* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sdkmanager* usr/lib64/python3*/site-packages/sdkmanager* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sdkmanager -f %{oreon_filedir}/python3-sdkmanager.list

%changelog

%autochangelog
