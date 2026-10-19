%global source0_hash 605d79fa2ec2f02905492e5ea13d903c2d842d0b4c915a57f7bf02ab9f3c91dd
Name:           python-djangorestframework
Version:        3.18.1
Release:        1%{?dist}
Summary:        Web APIs for Django, made easy.
License:        BSD-3-Clause
URL:            https://www.django-rest-framework.org
Source0:        https://files.pythonhosted.org/packages/source/d/djangorestframework/djangorestframework-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-djangorestframework = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-djangorestframework
Summary:        Web APIs for Django, made easy.
# oreon:reqs
Requires:       python3dist(django) >= 5.2
# /oreon:reqs
%description -n python3-djangorestframework

%prep
%global oreon_srcdir djangorestframework-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-djangorestframework usr/lib/python3*/site-packages/djangorestframework* usr/lib64/python3*/site-packages/djangorestframework* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/djangorestframework* usr/lib64/python3*/site-packages/djangorestframework* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-djangorestframework -f %{oreon_filedir}/python3-djangorestframework.list

%changelog

%autochangelog
