%global source0_hash 2d05b306a62a71be61fd7cf664a66fa2d558ad11db5d737f2c16079c9a27e8ed
Name:		backupninja
Version:	1.2.2
Release:        10%{?dist}
Summary:        Lightweight, extensible backup system
License:	GPL-2.0-only
URL:		https://0xacab.org/liberate/backupninja
Source0:        https://0xacab.org/liberate/backupninja/-/archive/backupninja-%{version}/backupninja-backupninja-%{version}.tar.gz#/backupninja-%{version}.tar.gz
Patch0:		backupninja-1.2.1-redhat.patch
Patch1:		backupninja-1.2.1-duplicity.patch
Patch2:		backupninja-1.2.1-extbackup.patch
BuildArch:	noarch
Requires:	cronie
Requires:	gawk
Requires:	logrotate
Requires:	rdiff-backup
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
# /oreon:deps
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

./autogen.sh
%configure --libdir=%{_libexecdir}
%make_build
%install
%make_install
mkdir -p -m 0750 %{buildroot}/%{_sysconfdir}/backup.d
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
