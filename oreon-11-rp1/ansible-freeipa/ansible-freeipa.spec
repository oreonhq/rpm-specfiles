%global source0_hash 8b9bbb3366c9b0959006fc7813017c8219eb50817c399e55bc6c8edb4a2b4214

# Turn off automatic python byte compilation because these are Ansible
# roles and the files are transferred to the node and compiled there with
# the python version used in the node
%define __brp_python_bytecompile %{nil}

%global python %{__python3}

%global collection_namespace freeipa
%global collection_name ansible_freeipa
%global ansible_collections_dir %{_datadir}/ansible/collections/ansible_collections

Summary: Roles and playbooks to deploy FreeIPA servers, replicas and clients
Name: ansible-freeipa
Version: 1.16.0
Release: 3%{?dist}
URL: https://github.com/freeipa/ansible-freeipa
License: GPL-3.0-or-later
Source:        https://github.com/freeipa/ansible-freeipa/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: noarch
Requires: ansible-core >= 2.14.0
BuildRequires: ansible-core >= 2.14.0
BuildRequires: python
Provides: ansible-collection-%{collection_namespace}-%{collection_name} = %{version}-%{release}
Provides: ansible-freeipa-tests
Obsoletes: ansible-freeipa-tests < 1.12.1-2
Provides: ansible-freeipa-collection
Obsoletes: ansible-freeipa-collection < 1.14.0

%description
Ansible collection %{collection_namespace}.%{collection_name} providing
roles to install and uninstall FreeIPA servers, replicas and clients, roles
for backups and SmartCard configuration, modules for management and also
playbooks for all roles and modules.

Note: The Ansible playbooks and roles require a configured Ansible environment
where the Ansible nodes are reachable and are properly set up to have an IP
address and a working package manager.

Features

- Server, replica and client deployment
- Cluster deployments: Server, replicas and clients in one playbook
- One-time-password (OTP) support for client installation
- Repair mode for clients
- Backup and restore, also to and from controller
- Smartcard setup for servers and clients
- Inventory plugin freeipa
- Modules for automembership rule management
- Modules for automount key management
- Modules for automount location management
- Modules for automount map management
- Modules for certificate management
- Modules for config management
- Modules for delegation management
- Modules for dns config management
- Modules for dns forwarder management
- Modules for dns record management
- Modules for dns zone management
- Modules for group management
- Modules for hbacrule management
- Modules for hbacsvc management
- Modules for hbacsvcgroup management
- Modules for host management
- Modules for hostgroup management
- Modules for idoverridegroup management
- Modules for idoverrideuser management
- Modules for idp management
- Modules for idrange management
- Modules for idview management
- Modules for location management
- Modules for netgroup management
- Modules for passkeyconfig management
- Modules for permission management
- Modules for privilege management
- Modules for pwpolicy management
- Modules for role management
- Modules for self service management
- Modules for server management
- Modules for service management
- Modules for service delegation rule management
- Modules for service delegation target management
- Modules for sudocmd management
- Modules for sudocmdgroup management
- Modules for sudorule management
- Modules for sysaccount management
- Modules for topology management
- Modules for trust management
- Modules for user management
- Modules for vault management

Supported FreeIPA Versions

FreeIPA versions 4.6 and up are supported by all roles.

The client role supports versions 4.4 and up, the server role is working with
versions 4.5 and up, the replica role is currently only working with versions
4.6 and up.

Supported Distributions

- RHEL/CentOS 7.4+
- Fedora 26+
- Ubuntu
- Debian 10+ (ipaclient only, no server or replica!)

Requirements

  Controller
  - Ansible version: 2.14+

  Node
  - Supported FreeIPA version (see above)
  - Supported distribution (needed for package installation only, see above)

Limitations

External signed CA is now supported. But the currently needed two step process
is an issue for the processing in a simple playbook.
Work is planned to have a new method to handle CSR for external signed CAs in
a separate step before starting the server installation.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
# Do not create backup files with patches

# Fix python modules and module utils:
# - Remove shebang
# - Remove execute flag
for i in roles/ipa*/library/*.py roles/ipa*/module_utils/*.py plugins/*/*.py;
do
    sed -i '1{/\/usr\/bin\/python*/d;}' $i
    sed -i '1{/\/usr\/bin\/env python*/d;}' $i
    chmod a-x $i
done

for i in utils/*.py utils/new_module utils/changelog utils/ansible-doc-test;
do
    sed -i '{s@/usr/bin/python*@%{python}@}' $i
    sed -i '{s@/usr/bin/env python*@%{python}@}' $i
done


%build

%install
# Create collection and install to %%{buildroot}%%{ansible_collections_dir}
# ansible-galaxy collection install creates ansible_collections directory
# automatically in given path, therefore /..
utils/build-galaxy-release.sh -o "%{version}" -p %{buildroot}%{ansible_collections_dir}/.. %{collection_namespace} %{collection_name}

cp %{buildroot}/%{ansible_collections_dir}/%{collection_namespace}/%{collection_name}/README.md .


%files
%license COPYING
%doc README.md
%dir %{ansible_collections_dir}/%{collection_namespace}
%{ansible_collections_dir}/%{collection_namespace}/%{collection_name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.16.0-3
- Prepare for Oreon 11 (RP1)
