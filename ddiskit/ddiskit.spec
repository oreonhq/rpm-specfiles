# Use the forge macros to simplify packaging.
# See https://fedoraproject.org/wiki/Forge-hosted_projects_packaging_automation 
%global forgeurl https://gitlab.com/redhat/centos-stream/src/dup/ddiskit
# When we no longer need to build against a git commit, 
# Simply remove the commit variable and update the Version
# Then forge will pick up the release
%global commit d857c7726fd55e613bbd7af6c842ddfc80a9fdc8

Name:           ddiskit
Version:        3.6

%forgemeta

Release:        33%{?dist}
Summary:        Tool for Red Hat Enterprise Linux Driver Update Disk creation

License:        GPL-3.0-only
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       rpm createrepo
Requires:       /usr/bin/mkisofs
Suggests:       quilt git
Recommends:     kernel-devel redhat-rpm-config rpm-build
Recommends:     mock

%description -n %{name}
Ddiskit is a little framework for simplifying creation of proper
Driver Update Disks (DUD) used for providing new or updated out-of-tree
kernel modules.

%prep
%forgesetup
# Fix build with setuptools 62.1
# https://github.com/orosp/ddiskit/issues/17
sed -i "8i packages=[]," setup.py

%build
%py3_build

%install
%py3_install
find %{buildroot} -size 0 -delete

%files -n %{name}
%doc README
%license COPYING
%{python3_sitelib}/ddiskit-*.egg-info
%{_bindir}/ddiskit
%{_mandir}/man1/ddiskit.1*
%{_datadir}/bash-completion/completions/ddiskit

%dir %{_datadir}/ddiskit
%dir %{_datadir}/ddiskit/keyrings
%dir %{_datadir}/ddiskit/keyrings/rh-release
%dir %{_datadir}/ddiskit/profiles
%dir %{_datadir}/ddiskit/templates
%{_datadir}/ddiskit/templates/spec
%{_datadir}/ddiskit/templates/config
%{_datadir}/ddiskit/profiles/*
%{_datadir}/ddiskit/keyrings/rh-release/*.key
%{_datadir}/ddiskit/ddiskit.config

%config(noreplace) /etc/ddiskit.config

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.6-33
- Prepare for Oreon 11 (RP1)
