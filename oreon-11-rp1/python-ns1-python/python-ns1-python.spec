%global source0_hash cd3db956d1503542e6cd21237d6f61ebbf6888545ebedb8ea2265905fc90aa1a
Name:           python-ns1-python
Version:        0.29.0
Release:        1%{?dist}
Summary:        Python SDK for the NS1 DNS platform
License:        MIT
URL:            https://github.com/ns1/ns1-python
Source0:        https://files.pythonhosted.org/packages/source/n/ns1_python/ns1_python-%{version}.tar.gz
BuildArch:      noarch
Patch0001:      https://github.com/ns1/ns1-python/pull/75.patch#/0001-Fixup-compatibility-with-Python-3.10.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ns1-python = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-ns1-python
Summary:        Python SDK for the NS1 DNS platform
%description -n python3-ns1-python

%prep
%global oreon_srcdir ns1_python-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ns1-python usr/lib/python3*/site-packages/ns1_python* usr/lib64/python3*/site-packages/ns1_python* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ns1_python* usr/lib64/python3*/site-packages/ns1_python* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ns1-python -f %{oreon_filedir}/python3-ns1-python.list

%changelog

%autochangelog
