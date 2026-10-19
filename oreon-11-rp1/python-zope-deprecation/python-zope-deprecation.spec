%global source0_hash 18727ebda8e63a6d4bd28a290e8b46852e9f14473debb5cc40a0a2dccfadf15f
Name:           python-zope-deprecation
Version:        6.0
Release:        1%{?dist}
Summary:        Zope Deprecation Infrastructure
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/zope.deprecation
Source0:        https://files.pythonhosted.org/packages/source/z/zope_deprecation/zope_deprecation-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) == 78.1.1
Requires:       python3-zope-deprecation = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-zope-deprecation
Summary:        Zope Deprecation Infrastructure
%description -n python3-zope-deprecation

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir zope_deprecation-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-zope-deprecation usr/lib/python3*/site-packages/zope_deprecation* usr/lib64/python3*/site-packages/zope_deprecation* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/zope_deprecation* usr/lib64/python3*/site-packages/zope_deprecation* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-zope-deprecation -f %{oreon_filedir}/python3-zope-deprecation.list

%changelog

%autochangelog
