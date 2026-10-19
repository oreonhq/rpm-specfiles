%global source0_hash 75737f16e5e5f003101baf519612e06e1785bb8cba0e576783deef52a142c81a
%global archive_name ansible-lint
%global lib_name ansiblelint
Name:           %{archive_name}
Epoch:          1
Version:        26.9.0
Release:        1%{?dist}
Summary:        Best practices checker for Ansible
License:        GPL-3.0-only
URL:            https://github.com/ansible/ansible-lint
Source0:        https://github.com/ansible/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 65.3.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 7.0.5
Requires:       python3-ansible-lint = %{version}-%{release}
# /oreon:deps
%description
Checks playbooks for practices and behavior that could potentially be improved.

%package -n python3-%{archive_name}
Summary:        Best practices checker for Ansible
Obsoletes:      python2-%{archive_name} < 3.4.23-6
Provides:       %{archive_name} = %{version}-%{release}
Requires:       /usr/bin/ansible
%description  -n python3-%{archive_name}
Python3 module for ansible-lint.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{archive_name}-%{version}

# Fedora's ansible-core is 2.18.9 version currently
sed -i '37d' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
ln -sr %{buildroot}%{_bindir}/%{name}{,-3}
%oreon_autofiles main usr/lib/python3*/site-packages/ansible_lint* usr/lib64/python3*/site-packages/ansible_lint* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-ansible-lint -f %{oreon_filedir}/python3-ansible-lint.list

%changelog

%autochangelog
