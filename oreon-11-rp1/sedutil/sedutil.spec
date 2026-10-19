%global source0_hash 32683065331c7c61b07355b0eb443cabcf3433f4613b68552e43c466d0024f2d
%global _hardened_build 1
%global OWNER Drive-Trust-Alliance
%global PROJECT sedutil
%global commit 5bbe4ff75b9416926d157a755d9760f7ff4e3904
%global commitdate 20241211
%global gittag %{version}
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:		sedutil
Version:	1.49.13
Release:        3%{?dist}
Summary:        Tools to manage the activation and use of self encrypting drives
License:	GPL-3.0-or-later AND CC0-1.0 AND BSD-4-Clause-UC AND Unlicense
URL:		https://github.com/%{OWNER}/%{PROJECT}/wiki
Source0:        https://github.com/%{OWNER}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
ExcludeArch:	ppc ppc64 s390 s390x
Provides:	bundled(cifra)
Obsoletes:	msed <= 0.23-0.20
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libnvme-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  systemd-devel
# /oreon:deps
%description
The Drive Trust Alliance software (sedutil) is an Open Source (GPLv3)
effort to make Self Encrypting Drive technology freely available to
everyone. It is a combination of the two known available Open Source
code bases today: msed and OpalTool.

sedutil is a Self-Encrypting Drive (SED) management program and
Pre-Boot Authorization (PBA) image that will allow the activation and
use of self encrypting drives that comply with the Trusted Computing
Group Opal 2.0 SSC.

This package provides the sedutil-cli and linuxpba binaries, but not
the PBA image itself.

%prep

%autosetup
# Adjust the GitVersion.sh script to just use the git tag from the
# checkout so we don't need a full git tree or the git tool itself.
sed -i -e's/tarball/%{gittag}/' Customizations.OpenSource/linux/CLI/GitVersion.sh
sed -i -e's/tarball/%{gittag}/' linux/GitVersionPBA.sh

%build

autoreconf -iv
%configure
%make_build
%install
%make_install
mkdir -p %{buildroot}%{_libexecdir}/linuxpba
ln -sr %{buildroot}%{_sbindir}/linuxpba %{buildroot}%{_libexecdir}/linuxpba
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
