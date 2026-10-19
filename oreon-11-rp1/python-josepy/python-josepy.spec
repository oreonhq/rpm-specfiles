%global source0_hash 74c033151337c854f83efe5305a291686cef723b4b970c43cfe7270cf4a677a9
Name:           python-josepy
Version:        2.2.0
Release:        1%{?dist}
Summary:        JOSE protocol implementation in Python
License:        Apache-2.0
URL:            https://github.com/certbot/josepy
Source0:        https://files.pythonhosted.org/packages/source/j/josepy/josepy-%{version}.tar.gz
BuildArch:      noarch
Patch1:         python-josepy-support-py314.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 2.2.0
Requires:       python3-josepy = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-josepy
Summary:        JOSE protocol implementation in Python
%description -n python3-josepy

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir josepy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-josepy usr/lib/python3*/site-packages/josepy* usr/lib64/python3*/site-packages/josepy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/josepy* usr/lib64/python3*/site-packages/josepy* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-josepy -f %{oreon_filedir}/python3-josepy.list

%changelog

%autochangelog
