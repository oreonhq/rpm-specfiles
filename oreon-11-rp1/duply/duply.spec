%global source0_hash 0d24a78df6dc81622e59a03ee21eddff41eaa43a17aa424ec866a9617e2bb4fd
Name:           duply
Version:        2.5.6
Release:        1%{?dist}
Summary:        Wrapper for duplicity
License:        GPL-2.0-only
URL:            http://duply.net/
Source0:        http://downloads.sourceforge.net/ftplicity/%{name}_%{version}.tgz
BuildArch:      noarch
Requires:       duplicity
# oreon:deps
BuildRequires:  txt2man
# /oreon:deps
%description
duply is a frontend for the mighty duplicity magic. It simplifies
running duplicity with cron or on command line by:

- keeping recurring settings in profiles per backup job
- automated import/export of keys between profile and keyring
- enabling batch operations e.g. backup_verify_purge
- executing pre/post scripts
- precondition checking for flawless duplicity operation

Since version 1.5.0 all duplicity backends are supported. Hence the
name changed from ftplicity to duply.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}_%{version}

%build

chmod +x %{name}
./%{name} txt2man > %{name}.1
%install
install -p -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -p -D -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}
sed -i "1c#!/bin/bash" %{buildroot}%{_bindir}/%{name}
mv gpl-2.0.txt LICENSE
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
