%global source0_hash none

%global _hardened_build 1
#global snapshot 0
%global OWNER Drive-Trust-Alliance
%global PROJECT sedutil
%global commit 5bbe4ff75b9416926d157a755d9760f7ff4e3904
%global commitdate 20241211
%global gittag %{version}
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		sedutil
Version:	1.49.13
Release:	3%{?dist}
Summary:	Tools to manage the activation and use of self encrypting drives

# Everything is GPLv3+ except:
# - Common/pbkdf2/* which is CC0, a bundled copy of Cifra: https://github.com/ctz/cifra
License:	GPL-3.0-or-later AND CC0-1.0 AND BSD-4-Clause-UC AND Unlicense
URL:		https://github.com/%{OWNER}/%{PROJECT}/wiki
Source0:	https://github.com/%{OWNER}/%{PROJECT}/archive/%{gittag}/%{name}-%{gittag}.tar.gz

# sedutil does not work on big-endian architectures
# Common/DtaEndianFixup.h:37:2: error: #error This code does not support big endian architectures
ExcludeArch:	ppc ppc64 s390 s390x

BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	ncurses-devel
BuildRequires:	autoconf automake
BuildRequires:	systemd-devel
BuildRequires:	libnvme-devel

# This package uses a bundled copy of Cifra:
# https://github.com/ctz/cifra/commit/319fdb764cd12e12b8296358cfcd640346c4d0dd
Provides:	bundled(cifra)

# Replaces msed, but doesn't provide a compatible CLI command
Obsoletes:	msed <= 0.23-0.20

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

%files
%doc README.md Common/Copyright.txt Common/ReadMe.txt linux/PSIDRevert_LINUX.txt
%license Common/LICENSE.txt
%{_sbindir}/sedutil-cli
%{_mandir}/man8/sedutil-cli.8*
%{_sbindir}/linuxpba
%{_libexecdir}/linuxpba

%changelog
%autochangelog
