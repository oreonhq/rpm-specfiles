%global source0_hash 3190199592f87f47ffbf4da8a9ad7d208df0ab0089e744a5da540af507a23818
Name:           python-pytest-localftpserver
Version:        1.6.0
Release:        1%{?dist}
Summary:        A PyTest plugin which provides an FTP fixture for your tests
License:        MIT
URL:            https://github.com/oz123/pytest-localftpserver
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_localftpserver/pytest_localftpserver-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 67.0.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2
Requires:       python3-pytest-localftpserver = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-localftpserver
Summary:        A PyTest plugin which provides an FTP fixture for your tests
# oreon:reqs
Requires:       python3dist(pyftpdlib) >= 1.2.0
# /oreon:reqs
%description -n python3-pytest-localftpserver

%prep
%global oreon_srcdir pytest_localftpserver-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-localftpserver usr/lib/python3*/site-packages/pytest_localftpserver* usr/lib64/python3*/site-packages/pytest_localftpserver* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_localftpserver* usr/lib64/python3*/site-packages/pytest_localftpserver* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-localftpserver -f %{oreon_filedir}/python3-pytest-localftpserver.list

%changelog

%autochangelog
