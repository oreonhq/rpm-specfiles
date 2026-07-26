%global source0_hash 3f5f85b507d56c09944b394c94551fa27d6fc5ca21ec033e4ebd98ac47417e68

Name:           bkhive
Version:        1.1.1
Release:        35%{?dist}
Summary:        Dump the syskey bootkey from a Windows system hive

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://ophcrack.sourceforge.net/
Source0:        http://downloads.sourceforge.net/ophcrack/%{name}-%{version}.tar.gz

#Patch adds possibility to install with current user and not only root
Patch0:         %{name}-install.patch

BuildRequires:  gcc
BuildRequires:  make
%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
This tool is designed to recover the syskey bootkey from a Windows NT/2K/XP
system hive. Then we can decrypt the SAM file with the syskey and dump
password hashes.

Syskey is a Windows feature that adds an additional encryption layer to the
password hashes stored in the SAM database.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

%build
%set_build_flags
%make_build CFLAGS="$CFLAGS"

%install
OWNER=`id -un`
GROUP=`id -gn`

make install DESTDIR=%{buildroot} BINDIR=%{_bindir} MANDIR=%{_mandir}/man1/ OWNER=${OWNER} GROUP=${GROUP}

%files
%license COPYING
%doc AUTHORS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
