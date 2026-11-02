%global source0_hash 628095e1ef656bbe9034cf5bfa3c220880a16cd0ceea25b17cd2198ea3503e03
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: setup
Version: 2.15.1
Release: 2%{?dist}
Summary: Base system configuration files
License: LicenseRef-Fedora-Public-Domain
URL: https://pagure.io/setup
BuildArch: noarch
Source0: COPYING
Source1: aliases
Source2: bashrc
Source3: csh.cshrc
Source4: csh.login
Source5: ethertypes
Source6: filesystems
Source7: host.conf
Source8: hosts
Source9: inputrc
Source10: networks
Source11: printcap
Source12: profile
Source13: protocols
Source14: services
Source15: shells
Source16: lang.csh
Source17: lang.sh
Source18: uidgid
Source19: setup.sysusers.conf

BuildRequires: oreon-rpm-macros
BuildRequires: bash
BuildRequires: systemd

%description
passwd, group, profile, and the other base configuration files.

%prep
%oreon_sha256
mkdir -p etc/profile.d docs
cp %{SOURCE1} %{SOURCE2} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} %{SOURCE15} etc/
cp %{SOURCE3} %{SOURCE4} etc/
cp %{SOURCE16} %{SOURCE17} etc/profile.d/
cp %{SOURCE0} %{SOURCE18} docs/
touch etc/exports etc/motd etc/subgid etc/subuid etc/fstab

%build
systemd-sysusers --root=./ %{SOURCE19}
chmod 0400 etc/shadow etc/gshadow
rm -f etc/.pwd.lock

%install
mkdir -p %{buildroot}/etc %{buildroot}/usr/lib/sysusers.d
cp -a etc/. %{buildroot}/etc/
install -m 0644 %{SOURCE19} %{buildroot}/usr/lib/sysusers.d/setup.conf

%files
%license docs/COPYING
%doc docs/uidgid
%verify(not md5 size mtime) %config(noreplace) /etc/passwd
%verify(not md5 size mtime) %config(noreplace) /etc/group
%verify(not md5 size mtime) %attr(0000,root,root) %config(noreplace,missingok) /etc/shadow
%verify(not md5 size mtime) %attr(0000,root,root) %config(noreplace,missingok) /etc/gshadow
%verify(not md5 size mtime) %config(noreplace) /etc/subuid
%verify(not md5 size mtime) %config(noreplace) /etc/subgid
%config(noreplace) /etc/services
%verify(not md5 size mtime) %config(noreplace) /etc/exports
%config(noreplace) /etc/aliases
%config(noreplace) /etc/filesystems
%config(noreplace) /etc/host.conf
%verify(not md5 size mtime) %config(noreplace) /etc/hosts
%verify(not md5 size mtime) %config(noreplace) /etc/motd
%config(noreplace) /etc/printcap
%verify(not md5 size mtime) %config(noreplace) /etc/inputrc
%config(noreplace) /etc/bashrc
%config(noreplace) /etc/profile
%config(noreplace) /etc/protocols
%config(noreplace) /etc/ethertypes
%config(noreplace) /etc/csh.login
%config(noreplace) /etc/csh.cshrc
%config(noreplace) /etc/networks
%dir /etc/profile.d
/etc/profile.d/lang.csh
/etc/profile.d/lang.sh
%config(noreplace) /etc/shells
%ghost %verify(not md5 size mtime) %config(noreplace,missingok) /etc/fstab
/usr/lib/sysusers.d/setup.conf
