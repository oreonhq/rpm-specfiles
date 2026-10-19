%global source0_hash a48b5e6db21062bc6258548e6a3e4363043d40128f0e6b796774a59b6a7dbe82
Name:           python-ansible-pylibssh
Version:        1.4.0
Release:        1%{?dist}
Summary:        Python bindings for libssh client specific to Ansible use case
License:        ...
URL:            https://github.com/ansible/pylibssh
Source0:        https://files.pythonhosted.org/packages/source/a/ansible_pylibssh/ansible_pylibssh-%{version}.tar.gz
Patch0:         python-ansible-pylibssh-nocov.patch
Patch1:         python-ansible-pylibssh-debug.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 45
BuildRequires:  python3dist(setuptools-scm) >= 7.0.0
Requires:       python3-ansible-pylibssh = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-ansible-pylibssh
Summary:        Python bindings for libssh client specific to Ansible use case
%description -n python3-ansible-pylibssh

%prep
%global oreon_srcdir ansible_pylibssh-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ansible-pylibssh usr/lib/python3*/site-packages/ansible_pylibssh* usr/lib64/python3*/site-packages/ansible_pylibssh* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ansible_pylibssh* usr/lib64/python3*/site-packages/ansible_pylibssh* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ansible-pylibssh -f %{oreon_filedir}/python3-ansible-pylibssh.list

%changelog

%autochangelog
