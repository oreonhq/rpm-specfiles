%global source0_hash 59dcb51c272ad209d59bed5708a64a333083e86017d7fcdd67498eeab7784340
Name:           python-asgiref
Version:        3.12.1
Release:        1%{?dist}
Summary:        ASGI specs, helper code, and adapters
License:        BSD-3-Clause
URL:            https://asgi.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/a/asgiref/asgiref-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-asgiref = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-asgiref
Summary:        ASGI specs, helper code, and adapters
%description -n python3-asgiref

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir asgiref-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-asgiref usr/lib/python3*/site-packages/asgiref* usr/lib64/python3*/site-packages/asgiref* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/asgiref* usr/lib64/python3*/site-packages/asgiref* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-asgiref -f %{oreon_filedir}/python3-asgiref.list

%changelog

%autochangelog
