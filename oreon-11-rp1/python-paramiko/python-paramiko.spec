%global source0_hash 36763b5b95c2a0dcfdf1abc48e48156ee425b21efe2f0e787c2dd5a95c0e5e79
Name:           python-paramiko
Version:        5.0.0
Release:        1%{?dist}
Summary:        SSH2 protocol library
License:        LGPL-2.1
URL:            https://github.com/paramiko/paramiko
Source0:        https://files.pythonhosted.org/packages/source/p/paramiko/paramiko-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-paramiko = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-paramiko
Summary:        SSH2 protocol library
# oreon:reqs
Requires:       python3dist(bcrypt) >= 3.2
Requires:       python3dist(cryptography) >= 3.3
Requires:       python3dist(invoke) >= 2.0
Requires:       python3dist(pynacl) >= 1.5
# /oreon:reqs
%description -n python3-paramiko

%prep
%global oreon_srcdir paramiko-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-paramiko usr/lib/python3*/site-packages/paramiko* usr/lib64/python3*/site-packages/paramiko* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/paramiko* usr/lib64/python3*/site-packages/paramiko* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-paramiko -f %{oreon_filedir}/python3-paramiko.list

%changelog

%autochangelog
