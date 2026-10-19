%global source0_hash 18646c024a771751111ba8bab5209ab089a02ccdfeb9787cbda94558dc372804
Name:           python-boxsdk
Version:        10.15.0
Release:        1%{?dist}
Summary:        Official Box Python SDK
License:        ...
URL:            https://github.com/box/box-python-sdk.git
Source0:        https://files.pythonhosted.org/packages/source/b/boxsdk/boxsdk-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-boxsdk = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-boxsdk
Summary:        Official Box Python SDK
%description -n python3-boxsdk

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir boxsdk-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-boxsdk usr/lib/python3*/site-packages/boxsdk* usr/lib64/python3*/site-packages/boxsdk* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/boxsdk* usr/lib64/python3*/site-packages/boxsdk* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-boxsdk -f %{oreon_filedir}/python3-boxsdk.list

%changelog

%autochangelog
