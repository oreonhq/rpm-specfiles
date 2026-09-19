%global source0_hash 2f0d6b8465b487d514c58ff39c1006be52ae63c4439770af594764aec75ed566

%global githash 79d751a

Name:		ansible-openstack-modules
Version:	0
Release:	20140926git%{githash}%{?dist}
Summary:	Unofficial Ansible modules for managing Openstack

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		https://github.com/openstack-ansible/openstack-ansible-modules
# git clone https://github.com/openstack-ansible/openstack-ansible-modules.git
# cd openstack-ansible-modules
# git archive --format=tar %%{githash} | gzip > %%{name}-%%{githash}.tar.gz
Source0:	ansible-openstack-modules-%{githash}.tar.gz
BuildArch:      noarch

Requires:	ansible

%description
Unofficial Ansible modules for managing and deployment of OpenStack. Contains
all the necesary Neutron networking modules and also some Cinder, Glance,
Keystone and Nova modules missing in the official modules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

%build

%install
mkdir -p %{buildroot}%{_datadir}/ansible/ansible-openstack-modules
cp -a cinder* glance* keystone* neutron* nova* %{buildroot}%{_datadir}/ansible/ansible-openstack-modules/

%files
%doc LICENSE README.md
%{_datadir}/ansible/ansible-openstack-modules

%changelog
%autochangelog
