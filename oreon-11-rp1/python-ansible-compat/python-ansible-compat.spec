%global source0_hash 1254bd1db72dcc93b74774f54b81e272260d3cd34ba5d595d42ca2dd9c46f7de
Name:           python-ansible-compat
Version:        26.8.0
Release:        1%{?dist}
Summary:        Ansible compatibility goodies
License:        MIT
URL:            https://github.com/ansible/ansible-compat
Source0:        https://files.pythonhosted.org/packages/source/a/ansible_compat/ansible_compat-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 65.3.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 7.0.5
Requires:       python3-ansible-compat = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-ansible-compat
Summary:        Ansible compatibility goodies
# oreon:reqs
Requires:       python3dist(ansible-core) >= 2.16.19
Requires:       python3dist(jsonschema) >= 4.6.0
Requires:       python3dist(packaging) >= 22.0
Requires:       python3dist(pyyaml) >= 6.0.1
Requires:       python3dist(subprocess-tee) >= 0.4.1
# /oreon:reqs
%description -n python3-ansible-compat

%prep
%global oreon_srcdir ansible_compat-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ansible-compat usr/lib/python3*/site-packages/ansible_compat* usr/lib64/python3*/site-packages/ansible_compat* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ansible_compat* usr/lib64/python3*/site-packages/ansible_compat* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ansible-compat -f %{oreon_filedir}/python3-ansible-compat.list

%changelog

%autochangelog
