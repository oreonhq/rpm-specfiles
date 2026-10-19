%global source0_hash 3f2b260bf9bd4c2b6857f697a1d7e8edc26fa569282b77027e849dfe1e48580a
Name:           python-scp
Version:        0.16.1
Release:        1%{?dist}
Summary:        scp module for paramiko
License:        LGPL-2.1-or-later
URL:            https://github.com/jbardin/scp.py
Source0:        https://files.pythonhosted.org/packages/source/s/scp/scp-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-scp = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-scp
Summary:        scp module for paramiko
%description -n python3-scp

%prep
%global oreon_srcdir scp-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-scp usr/lib/python3*/site-packages/scp* usr/lib64/python3*/site-packages/scp* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/scp* usr/lib64/python3*/site-packages/scp* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-scp -f %{oreon_filedir}/python3-scp.list

%changelog

%autochangelog
