%global source0_hash 9c1e3679ee17e74e69bd1f8854f7ac67513294d09c0d837d2db26f1b1a6782b0

%define version 47
# disable the dependecy extractor, it would add
# Require: /usr/share/migrationtools/migrate_common.ph
%global __perl_requires /usr/bin/tail -n 0

Name:           migrationtools
Version:        %{version}
Release:        39%{?dist}
Summary:        Migration scripts for LDAP

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.padl.com/OSS/MigrationTools.html
Source0:        http://www.padl.com/download/MigrationTools-%{version}.tar.gz
Source1:        migration-tools.txt
BuildArch:      noarch
Requires:       perl-interpreter, ldif2ldbm

Patch1: MigrationTools-38-instdir.patch
Patch2: MigrationTools-36-mktemp.patch
Patch3: MigrationTools-27-simple.patch
Patch4: MigrationTools-26-suffix.patch
Patch5: MigrationTools-46-schema.patch
Patch6: MigrationTools-45-noaliases.patch
Patch7: MigrationTools-46-ddp.patch
Patch8: MigrationTools-46-unique-hosts.patch

%description
The MigrationTools are a set of Perl scripts for migrating users, groups,
aliases, hosts, netgroups, networks, protocols, RPCs, and services from 
existing nameservices (flat files, NIS, and NetInfo) to LDAP.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MigrationTools-47

%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1

%build
# nothing to build
cp %SOURCE1 .

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
install -m 755 migrate_* $RPM_BUILD_ROOT/%{_datadir}/%{name}

%files
%attr(0755,root,root) %dir /%{_datadir}/%{name}
%attr(0644,root,root) /%{_datadir}/%{name}/*.ph
%attr(0755,root,root) /%{_datadir}/%{name}/*.pl
%attr(0755,root,root) /%{_datadir}/%{name}/*.sh
%doc README
%doc migration-tools.txt

%changelog
%autochangelog
