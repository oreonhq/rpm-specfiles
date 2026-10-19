%global source0_hash 366f4614f4544c5fb5d780c82f57af8f30492b44a68ed20750390aa81e20c2ea
Name:           python-elastic-transport
Version:        9.4.2
Release:        1%{?dist}
Summary:        Transport classes and utilities shared among Python Elastic client libraries
License:        ...
URL:            https://github.com/elastic/elastic-transport-python
Source0:        https://files.pythonhosted.org/packages/source/e/elastic_transport/elastic_transport-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-elastic-transport = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-elastic-transport
Summary:        Transport classes and utilities shared among Python Elastic client libraries
%description -n python3-elastic-transport

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir elastic_transport-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-elastic-transport usr/lib/python3*/site-packages/elastic_transport* usr/lib64/python3*/site-packages/elastic_transport* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/elastic_transport* usr/lib64/python3*/site-packages/elastic_transport* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-elastic-transport -f %{oreon_filedir}/python3-elastic-transport.list

%changelog

%autochangelog
