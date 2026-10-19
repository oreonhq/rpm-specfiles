%global source0_hash d28e0073fd1dd637c8b95947bc864b5625eca9f8f2db1538145e33b2a1cd4b92
Name:           python-maxminddb
Version:        3.2.0
Release:        1%{?dist}
Summary:        Reader for the MaxMind DB format
License:        Apache-2.0
URL:            https://www.maxmind.com/en/home
Source0:        https://files.pythonhosted.org/packages/source/m/maxminddb/maxminddb-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-maxminddb = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-maxminddb
Summary:        Reader for the MaxMind DB format
%description -n python3-maxminddb

%prep
%global oreon_srcdir maxminddb-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-maxminddb usr/lib/python3*/site-packages/maxminddb* usr/lib64/python3*/site-packages/maxminddb* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/maxminddb* usr/lib64/python3*/site-packages/maxminddb* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-maxminddb -f %{oreon_filedir}/python3-maxminddb.list

%changelog

%autochangelog
