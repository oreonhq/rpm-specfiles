%global source0_hash 2d05b306a62a71be61fd7cf664a66fa2d558ad11db5d737f2c16079c9a27e8ed

Name:		backupninja
Version:	1.2.2
Release:	10%{?dist}
Summary:	Lightweight, extensible backup system

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		https://0xacab.org/liberate/backupninja
Source0:	https://0xacab.org/liberate/backupninja/-/archive/backupninja-%{version}/backupninja-backupninja-%{version}.tar.gz#/backupninja-%{version}.tar.gz

Patch0:		backupninja-1.2.1-redhat.patch
Patch1:		backupninja-1.2.1-duplicity.patch
Patch2:		backupninja-1.2.1-extbackup.patch

BuildArch:	noarch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	make

Requires:	cronie
Requires:	gawk
Requires:	logrotate
Requires:	rdiff-backup

%description
Backupninja allows you to coordinate system backup by dropping a few simple
configuration files into /etc/backup.d/. Most programs you might use for making
backups don't have their own configuration file format. Backupninja provides
a centralized way to configure and schedule many different backup utilities.

It allows for secure, remote, incremental file system backup (via rdiff-backup),
compressed incremental data, backup system and hardware info, encrypted remote
backups (via duplicity), safe backup of MySQL/PostgreSQL databases, subversion
or trac repositories, burn CD/DVDs or create ISOs, incremental rsync with
hard-linking.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n backupninja-backupninja-%{version}
%patch -P0 -p1 -b .redhat
%patch -P1 -p1 -b .dupver
%patch -P2 -p1 -b .extbck

%build
# prepare build script
./autogen.sh

# put all script 'libs' into one dir
%configure --libdir=%{_libexecdir}

%make_build

%install
%make_install
mkdir -p -m 0750 %{buildroot}/%{_sysconfdir}/backup.d

%files
%{_sbindir}/backupninja
%{_sbindir}/ninjahelper
%{_libexecdir}/backupninja
%doc AUTHORS CHANGELOG.md FAQ.md README.md TODO
%license COPYING
%config(noreplace) %{_sysconfdir}/backupninja.conf
%config(noreplace) %{_sysconfdir}/cron.d/backupninja
%config(noreplace) %{_sysconfdir}/logrotate.d/backupninja
%dir %attr(0750,root,root )%{_sysconfdir}/backup.d
%{_datadir}/backupninja
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*

%changelog
%autochangelog
