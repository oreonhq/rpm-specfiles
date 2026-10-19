%global source0_hash 6b2a32f18d97e16e90827d7a819ffa8dbd8cc245fc4e1fa9d1095b54ef4bd999
Name:           python-httptools
Version:        0.8.0
Release:        1%{?dist}
Summary:        A collection of framework independent HTTP protocol utils.
License:        MIT
URL:            https://github.com/MagicStack/httptools
Source0:        https://files.pythonhosted.org/packages/source/h/httptools/httptools-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) <= 82.0.1
BuildRequires:  python3dist(setuptools) >= 80.9.0
Requires:       python3-httptools = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-httptools
Summary:        A collection of framework independent HTTP protocol utils.
%description -n python3-httptools

%prep
%global oreon_srcdir httptools-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-httptools usr/lib/python3*/site-packages/httptools* usr/lib64/python3*/site-packages/httptools* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/httptools* usr/lib64/python3*/site-packages/httptools* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-httptools -f %{oreon_filedir}/python3-httptools.list

%changelog

%autochangelog
