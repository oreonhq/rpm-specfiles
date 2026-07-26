%global source0_hash none

%global centos_git_common_url https://git.centos.org/centos-git-common
%global centos_git_common_commit 28b610e9fb79594c49bc64c7c331d0aaab382e7e

Name:           centos-packager
Version:        0.7.0
Release:        19%{?dist}
Summary:        Tools and files necessary for building CentOS packages
Group:          Applications/Productivity

License:        GPL-2.0-or-later
URL:            https://git.centos.org/centos/centos-packager
Source0:        cbs-koji.conf
Source1:        COPYING
Source2:        centos-cert
Source5:        %{centos_git_common_url}/raw/%{centos_git_common_commit}/f/get_sources.sh

Requires:       koji
Requires:       rpm-build rpmdevtools rpmlint
Requires:       mock curl openssh-clients
Requires:       redhat-rpm-config
Requires:       bc
Requires:       krb5-workstation
Requires:       openssl
Requires:       fasjson-client python3-fasjson-client

BuildArch:      noarch

%description
Tools to help set up a CentOS packaging environment and interact with the
Community Build System (CBS).

%prep
cp %{SOURCE1} .

%build
# Nothing here

%install
mkdir -p %{buildroot}%{_sysconfdir}/koji.conf.d
install -p -m 0644 %{SOURCE0} %{buildroot}%{_sysconfdir}/koji.conf.d/cbs-koji.conf

mkdir -p %{buildroot}/%{_bindir}
ln -s koji %{buildroot}%{_bindir}/cbs
install -p -m 0755 %{SOURCE2} %{buildroot}%{_bindir}/centos-cert
install -p -m 0755 %{SOURCE3} %{buildroot}%{_bindir}/centos-lookaside-upload
install -p -m 0755 %{SOURCE4} %{buildroot}%{_bindir}/centos-lookaside-upload-sig
install -p -m 0755 %{SOURCE5} %{buildroot}%{_bindir}/centos-get-sources

%files
%license COPYING
%config(noreplace) %{_sysconfdir}/koji.conf.d/cbs-koji.conf
%{_bindir}/cbs
%{_bindir}/centos-cert
%{_bindir}/centos-lookaside-upload
%{_bindir}/centos-lookaside-upload-sig
%{_bindir}/centos-get-sources

%changelog
%autochangelog
