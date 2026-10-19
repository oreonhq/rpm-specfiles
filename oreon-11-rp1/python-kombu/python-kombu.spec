%global source0_hash 8060497058066c6f5aed7c26d7cd0d3b574990b09de842a8c5aaed0b92cc5a55
Name:           python-kombu
Version:        5.6.2
Release:        1%{?dist}
Summary:        Messaging library for Python.
License:        BSD-3-Clause
URL:            https://github.com/celery/kombu
Source0:        https://files.pythonhosted.org/packages/source/k/kombu/kombu-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-kombu = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-kombu
Summary:        Messaging library for Python.
%description -n python3-kombu

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir kombu-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-kombu usr/lib/python3*/site-packages/kombu* usr/lib64/python3*/site-packages/kombu* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/kombu* usr/lib64/python3*/site-packages/kombu* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-kombu -f %{oreon_filedir}/python3-kombu.list

%changelog

%autochangelog
