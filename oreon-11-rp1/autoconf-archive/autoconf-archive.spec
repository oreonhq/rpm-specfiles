# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 7bcd5d001916f3a50ed7436f4f700e3d2b1bade3ed803219c592d62502a57363
%global source1_hash 3355caad9664b41d39ea11a75de2666096b59d2bcb73d9a2b770ae445209541c
%global source2_hash 255185230570c689dfd98ed5e206ea06c00f7e97b9731e6844a2ab39c30b73a3
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           autoconf-archive
Version:        2024.10.16
Release:        1%{?dist}
Summary:        The Autoconf Macro Archive

License:        GPL-2.0-or-later WITH Autoconf-exception-macro AND GPL-3.0-or-later AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-3.0-or-later WITH Autoconf-exception-macro AND GFDL-1.3-or-later AND LGPL-3.0-or-later WITH Autoconf-exception-macro AND LGPL-2.1-or-later AND BSD-2-Clause AND BSD-3-Clause AND FSFAP AND FSFAP-no-warranty-disclaimer AND FSFULLR
URL:            https://www.gnu.org/software/autoconf-archive/
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        gpgkey-1A4F63A13A4649B632F65EE141BC28FE99089D72.gpg
BuildArch:      noarch
BuildRequires: oreon-rpm-macros
BuildRequires:  gnupg2
BuildRequires:  make
Requires:       autoconf

Patch: 0001-ax_check_gl.m4-properly-quote-m4_fatal.patch

%description
The GNU Autoconf Archive is a collection of more than 450 macros for
GNU Autoconf that have been contributed as free software by friendly
supporters of the cause from all over the Internet.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
rm -frv %{buildroot}%{_infodir}/dir
rm -frv %{buildroot}%{_datadir}/doc/%{name}

%files
%doc AUTHORS NEWS README TODO
%license COPYING*
%{_datadir}/aclocal/*.m4
%{_infodir}/autoconf-archive.info*

%changelog
%autochangelog
