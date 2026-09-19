%global source0_hash 83f686fe3ea699b7e67d1c7b4f9aee4930b6b87fb2f5267a221785672d08092b

#
# spec file for package lbdb
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2011 Red Hat, Inc
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugzilla.redhat.com
#

Name:           lbdb
Summary:        Address Database for mutt
Version:        0.41
Release:        23%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Url:            http://www.spinnaker.de/lbdb/
Source:         http://www.spinnaker.de/debian/lbdb_%{version}.tar.gz
# change default modules list
Patch0: 0001-Change-default-methods.patch
# fix path of evolution-addressbook-export
Patch1: 0002-Look-up-evolution-addressbook-export-in-libexec-rath.patch
# fix hostname lookup if multiple domains are listed in resolv.conf
Patch2: 0003-Fix-hostname-lookup-if-multiple-domains-are-listed-i.patch

BuildRequires:  gcc
BuildRequires: /usr/bin/pod2man
BuildRequires:  abook
BuildRequires:  gnupg2
BuildRequires:  finger
BuildRequires:  perl-generators
BuildRequires: make
Requires:       perl(Net::LDAP)
Requires:       perl(Getopt::Long)

%description
The Little Brother's Database (lbdb) consists of a set of small tools
that collect mail addresses from several sources and offer these
addresses to the external query feature of the Mutt mail reader.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n lbdb-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
# lbdb uses libdir in most of its helper programs to find the absolute path
# to these binaries, that's why it's forcefully set to %_libexecdir/lbdb.
# Another option would be to s/libdir/libexecdir in the helpers, but there
# are about 15 programs to patch, so this approach is easier.
%configure --libdir=%{_libexecdir}/lbdb --with-evolution-addressbook-export=auto --with-gpg=/usr/bin/gpg2
make %{?_smp_mflags}

%install
BUILD_ROOT=${RPM_BUILD_ROOT} make \
        install_prefix=${RPM_BUILD_ROOT} \
        sysconfdir=%{_sysconfdir} \
        mandir=%{_mandir} \
        libdir=%{_libexecdir}/lbdb \
        install

%files
%doc README COPYING INSTALL TODO
%config(noreplace) %{_sysconfdir}/*
%{_bindir}/*
%{_libexecdir}/lbdb/*
%dir %{_libexecdir}/lbdb
%doc %{_mandir}/man?/*

%changelog
%autochangelog
