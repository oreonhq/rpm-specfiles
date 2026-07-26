%global source0_hash 29485cb18f1d51c2900d90a45c2e989424185051d0fc5c057185156e0408a3a4

%global forgeurl https://github.com/cmadamsgit/ks-install
%global commit 72db7819e3ed40c7f00bd6cd709335970a5ba9c5
# forgemeta getting a date mismatch at 20230506 vs 07
%global date 20230507
%forgemeta

Name:		ks-install
Summary:	Take a Fedora/CentOS/RHEL kickstart file and make a VM
Version:	0
Release:	0.12%{?dist}
URL:		%{forgeurl}
Source:		%{forgesource}
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
BuildArch:	noarch
BuildRequires:	perl-generators perl-podlators
Requires:	virt-install
Recommends:	swtpm-tools

%description
Take a Fedora/CentOS/RHEL kickstart file and make a VM

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build
pod2man ks-libvirt > ks-libvirt.1
touch --reference=ks-libvirt ks-libvirt.1

%install
install -D -m0755 ks-libvirt %{buildroot}%{_bindir}/ks-libvirt
install -D -m0644 ks-libvirt.1 %{buildroot}%{_mandir}/man1/ks-libvirt.1

%files
%license LICENSE
%doc examples
%{_bindir}/*
%{_mandir}/man*/*

%changelog
%autochangelog
