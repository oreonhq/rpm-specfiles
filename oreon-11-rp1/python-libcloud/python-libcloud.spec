%global source0_hash b65eaa5ac32b28a0f9555e6a223dba39e73b99b682cd849624587ce7bc251661
Name:           python-apache-libcloud
Version:        3.9.1
Release:        1%{?dist}
Summary:        A standard Python library that abstracts away differences among multiple cloud provider APIs. For more information and documentation, please see https://libcloud.apache.org
License:        ...
URL:            https://libcloud.apache.org
Source0:        https://files.pythonhosted.org/packages/source/a/apache_libcloud/apache_libcloud-%{version}.tar.gz
BuildArch:      noarch
Patch0:         000-remove-linter-deps.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) < 80.11
BuildRequires:  python3dist(setuptools) >= 75.3
BuildRequires:  python3dist(wheel) >= 0.45.1
Requires:       python3-apache-libcloud = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-apache-libcloud
Summary:        A standard Python library that abstracts away differences among multiple cloud provider APIs. For more information and documentation, please see https://libcloud.apache.org
# oreon:reqs
Requires:       python3dist(requests) >= 2.26.0
# /oreon:reqs
%description -n python3-apache-libcloud

%prep
%global oreon_srcdir apache_libcloud-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-apache-libcloud usr/lib/python3*/site-packages/apache_libcloud* usr/lib64/python3*/site-packages/apache_libcloud* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/apache_libcloud* usr/lib64/python3*/site-packages/apache_libcloud* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-apache-libcloud -f %{oreon_filedir}/python3-apache-libcloud.list

%changelog

%autochangelog
