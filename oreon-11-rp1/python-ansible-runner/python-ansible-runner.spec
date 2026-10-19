%global source0_hash 5f3025529bb968fdc3b627457dd8d418dbf9d53bc73735d50e69c28544d53031
Name:           python-ansible-runner
Version:        2.4.3
Release:        1%{?dist}
Summary:        _Consistent Ansible Python API and CLI with container and process isolation runtime capabilities_
License:        ...
URL:            https://github.com/ansible/ansible-runner
Source0:        https://files.pythonhosted.org/packages/source/a/ansible_runner/ansible_runner-%{version}.tar.gz
BuildArch:      noarch
Patch:          0001-Base64IO-set-write-buffer-before-doing-attr-check.patch
Patch:          0001-Python-3.14-compat-replace-codecs.open-with-open.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) <= 70.0.0
BuildRequires:  python3dist(setuptools) >= 45
BuildRequires:  python3dist(setuptools-scm[toml]) <= 8.1.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2
Requires:       python3-ansible-runner = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-ansible-runner
Summary:        _Consistent Ansible Python API and CLI with container and process isolation runtime capabilities_
%description -n python3-ansible-runner

%prep
%global oreon_srcdir ansible_runner-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ansible-runner usr/lib/python3*/site-packages/ansible_runner* usr/lib64/python3*/site-packages/ansible_runner* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ansible_runner* usr/lib64/python3*/site-packages/ansible_runner* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ansible-runner -f %{oreon_filedir}/python3-ansible-runner.list

%changelog

%autochangelog
