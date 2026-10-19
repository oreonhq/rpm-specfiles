%global source0_hash 69c60a188c9c629a0e947dfafd89acdc8b7d8d404a6b5eb0ad258fef29362501
Name:           python-wadllib
Version:        2.1.0
Release:        1%{?dist}
Summary:        Navigate HTTP resources using WADL files as guides.
License:        ...
URL:            https://code.launchpad.net/wadllib
Source0:        https://files.pythonhosted.org/packages/source/w/wadllib/wadllib-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-wadllib = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-wadllib
Summary:        Navigate HTTP resources using WADL files as guides.
%description -n python3-wadllib

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir wadllib-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-wadllib usr/lib/python3*/site-packages/wadllib* usr/lib64/python3*/site-packages/wadllib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/wadllib* usr/lib64/python3*/site-packages/wadllib* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-wadllib -f %{oreon_filedir}/python3-wadllib.list

%changelog

%autochangelog
