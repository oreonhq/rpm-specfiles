%global source0_hash f0b3b8871d6f4e4edd7e47763b18144a32c215f735569be44c49a70e04893519
%bcond docs 0
%bcond tests 0
%global py3_shebang_flags %(echo %{py3_shebang_flags} | sed 's|s||')
%global __brp_mangle_shebangs_exclude_from ^%{python3_sitelib}/ansible_collections/[^/]+/[^/]+/roles/[^/]+/(files|templates)/.*$
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}%{__brp_mangle_shebangs_exclude_from}
Name:           ansible
Summary:        Curated set of Ansible collections included in addition to ansible-core
Version:        14.4.0
%global uversion %{version_no_tilde %{quote:%nil}}
Release:        1%{?dist}
License:        GPL-3.0-or-later AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT AND MPL-2.0 AND PSF-2.0
Source0:        https://files.pythonhosted.org/packages/source/a/ansible/ansible-%{version}.tar.gz
Source1:        ansible-prep.sh
Source2:        ansible-install-licenses.sh
Url:            https://ansible.com
BuildArch:      noarch
%if %{with tests}
%endif
%if %{with docs}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ansible = %{version}-%{release}
# /oreon:deps
%description
Ansible is a radically simple model-driven configuration management,
multi-node deployment, and remote task execution system. Ansible works
over SSH and does not require any software or daemons to be installed
on remote nodes. Extension modules can be written in any language and
are transferred to managed machines automatically.

This package provides a curated set of Ansible collections included in addition
to ansible-core.

%prep

%autosetup -N -n %{name}-%{uversion}

# Relax ansible-core dependency to avoid FTI bugs on EPEL
#
# This is necessary, because the EPEL ansible maintainers don't have control
# over ansible-core in RHEL, and it's difficult to time updates across
# repositories. I have tried to stick to upstream's version constraints, but
# that's apparently not working too well. This change gives us a grace period
# to properly release and test new ansible major versions after RHEL rebases
# ansible-core. The lower version constraints can stay in place.

sed "s|ansible-core ~=|ansible-core >=|" setup.cfg > setup.cfg.bak
# Verify
set -o pipefail
grep -B1 "ansible-core >=" setup.cfg.bak | grep -F 'install_requires ='

# ansible-prep.sh
%{S:1}

(
mkdir licenses docs
cd ansible_collections
# ansible-license-install.sh
%{S:2} \
    "$(readlink -f ../licenses)" \
    "$(readlink -f ../docs)" \
)

%build

%py3_shebang_fix ansible_collections
%pyproject_wheel
%install
%pyproject_install
mkdir -p %{buildroot}%{_licensedir}/ansible %{buildroot}%{_docdir}/ansible
mv licenses %{buildroot}%{_licensedir}/ansible/ansible_collections
mv docs %{buildroot}%{_pkgdocdir}/ansible_collections
%oreon_autofiles main

%check

%if %{with tests}
%endif
%files

%changelog

%autochangelog
