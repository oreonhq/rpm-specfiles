%global source0_hash c11ad4c429a983493ba10014c7af9831a455c2c0eea91c1cefff74530e480277
Name:           python-boto3
Version:        1.43.106
Release:        1%{?dist}
Summary:        The AWS SDK for Python _Boto3_
License:        Apache-2.0
URL:            https://github.com/boto/boto3
Source0:        https://files.pythonhosted.org/packages/source/b/boto3/boto3-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-boto3 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-boto3
Summary:        The AWS SDK for Python _Boto3_
%description -n python3-boto3

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir boto3-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-boto3 usr/lib/python3*/site-packages/boto3* usr/lib64/python3*/site-packages/boto3* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/boto3* usr/lib64/python3*/site-packages/boto3* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-boto3 -f %{oreon_filedir}/python3-boto3.list

%changelog

%autochangelog
