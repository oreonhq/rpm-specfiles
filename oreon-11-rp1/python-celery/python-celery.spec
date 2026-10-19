%global source0_hash 177006bd2054b882e9f01be59abd8529e88879ef50d7918a7050c5a9f4e12912
Name:           python-celery
Version:        5.6.3
Release:        1%{?dist}
Summary:        Distributed Task Queue.
License:        BSD-3-Clause
URL:            https://docs.celeryq.dev/en/stable/
Source0:        https://files.pythonhosted.org/packages/source/c/celery/celery-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-celery = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-celery
Summary:        Distributed Task Queue.
%description -n python3-celery

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir celery-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-celery usr/lib/python3*/site-packages/celery* usr/lib64/python3*/site-packages/celery* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/celery* usr/lib64/python3*/site-packages/celery* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-celery -f %{oreon_filedir}/python3-celery.list

%changelog

%autochangelog
