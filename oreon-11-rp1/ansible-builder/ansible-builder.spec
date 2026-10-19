%global source0_hash 9d88bc15acc7d31056d0c51914a6102dac8e5ad73f9f2d35ba98378c89714ed2
%bcond tests 1
Name:           ansible-builder
Version:        3.1.1
Release:        1%{?dist}
Summary:        A tool for building Ansible Execution Environments
License:        Apache-2.0
URL:            https://ansible.readthedocs.io/projects/builder/en/stable/
Source0:        https://files.pythonhosted.org/packages/source/a/ansible_builder/ansible_builder-%{version}.tar.gz
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) <= 70.0.0
BuildRequires:  python3dist(setuptools) >= 45
BuildRequires:  python3dist(setuptools-scm[toml]) <= 8.1.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2
Requires:       python3-ansible-builder = %{version}-%{release}
# /oreon:deps
%description
Using Ansible content that depends on non-default dependencies can be tricky.
Packages must be installed on each node, play nicely with other software
installed on the host system, and be kept in sync.

To help simplify this process, we have introduced the concept of Execution
Environments, which you can create with Ansible Builder.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n ansible_builder-%{version}
# Remove setuptools version upper version pins.
# They're not needed in Fedora.
grep -q setuptools pyproject.toml
tomcli-set pyproject.toml lists replace build-system.requires \
    '(setuptools.*), <=.+' '\1'

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%if %{with tests}
%pytest -n auto test/unit
%endif
%files

%changelog

%autochangelog
