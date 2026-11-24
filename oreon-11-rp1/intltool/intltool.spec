# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 67c74d94196b153b774ab9f89b2fa6c6ba79352407037c8c14d5aeb334e959cd
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: intltool
Summary: Utility for internationalizing various kinds of data files
Version: 0.51.0
Release: %{autorelease}
License: GPL-2.0-or-later WITH Autoconf-exception-generic
Source0:        https://launchpad.net/intltool/trunk/%{version}/+download/intltool-%{version}.tar.gz
URL: https://launchpad.net/intltool
BuildArch: noarch
Requires: patch
Requires: automake
Requires: gettext-devel
Requires: perl(Getopt::Long)
Requires: perl(XML::Parser)
BuildRequires: oreon-rpm-macros
BuildRequires: perl-generators
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(XML::Parser)
BuildRequires: gettext
BuildRequires: make

Patch: intltool-perl5.26-regex-fixes.patch
Patch: intltool-merge-Create-cache-file-atomically.patch
Patch: intltool_distcheck-fix.patch
Patch: intltool-cache-race.patch

%description
This tool automatically extracts translatable strings from oaf, glade,
bonobo ui, nautilus theme, .desktop, and other data files and puts
them in the po files.

%prep
%oreon_sha256
%autosetup -p1

%build
%configure

%make_build

%install
%make_install

%check
if ! make check; then
    find . -type f -name 'test-suite.log' | while read trs; do
	echo "BEGIN " ${trs}; cat ${trs} 1>&2;
    done
    echo  "Exiting abnormally due to make check failure above" 1>&2
    exit 1
fi

%files
%doc AUTHORS README
%license COPYING
%{_bindir}/intltool*
%{_datadir}/intltool
%{_datadir}/aclocal/intltool.m4
%{_mandir}/man8/intltool*.8*

%changelog
%autochangelog
