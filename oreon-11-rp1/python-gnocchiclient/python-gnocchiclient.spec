%global source0_hash 6ede1913b730a17e96f076ce831411ead447dbb6a2db9b103c50262a8c718477
Name:           python-gnocchiclient
Version:        7.2.0
Release:        1%{?dist}
Summary:        Python client library for Gnocchi
License:        ...
URL:            http://gnocchi.osci.io/gnocchiclient
Source0:        https://files.pythonhosted.org/packages/source/g/gnocchiclient/gnocchiclient-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-gnocchiclient = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-gnocchiclient
Summary:        Python client library for Gnocchi
%description -n python3-gnocchiclient

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir gnocchiclient-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-gnocchiclient usr/lib/python3*/site-packages/gnocchiclient* usr/lib64/python3*/site-packages/gnocchiclient* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/gnocchiclient* usr/lib64/python3*/site-packages/gnocchiclient* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-gnocchiclient -f %{oreon_filedir}/python3-gnocchiclient.list

%changelog

%autochangelog
