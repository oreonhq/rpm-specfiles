%global source0_hash d882ba51c5035cf8a8fb33240836075606d7629e456ac4bd0e80c0da381eef6d
Name:           python-ftputil
Version:        5.2.0
Release:        1%{?dist}
Summary:        High-level FTP client library _virtual file system and more_
License:        BSD-3-Clause
URL:            https://ftputil.sschwarzer.net/
Source0:        https://files.pythonhosted.org/packages/source/f/ftputil/ftputil-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ftputil = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-ftputil
Summary:        High-level FTP client library _virtual file system and more_
%description -n python3-ftputil

%prep
%global oreon_srcdir ftputil-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ftputil usr/lib/python3*/site-packages/ftputil* usr/lib64/python3*/site-packages/ftputil* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ftputil* usr/lib64/python3*/site-packages/ftputil* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ftputil -f %{oreon_filedir}/python3-ftputil.list

%changelog

%autochangelog
