%global source0_hash 602659af30c565750fa01650e0a223d26355b5df98f2fbc30e3a6c593ed4e526

Name:           samdump2
Version:        3.0.0
Release:        32%{?dist}
Summary:        Retrieves syskey and extracts hashes from Windows 2k/NT/XP/Vista SAM

#MD5 RC4 DES functions are linked from openssl library
#Code of samdump2 is GPLv2+
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://sourceforge.net/projects/ophcrack/files/samdump2
Source0:        http://downloads.sourceforge.net/ophcrack/%{name}-%{version}.tar.bz2

Patch0:         %{name}-install.patch

# Patch from Debian to move from legacy openssl version to contemporary version
# Author: Joao Eriberto Mota Filho <eriberto@debian.org>
Patch1:         %{name}-openssl.patch

BuildRequires:  openssl-devel
BuildRequires:  make
BuildRequires:  gcc

%description
This tool is designed to recover the syskey bootkey from Windows NT/2K/XP/Vista
system hive and uses it to decrypt and dump password hashes from the SAM hive.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
make %{?_smp_mflags} CFLAGS="%{optflags}" LIBS="-lcrypto"

%install
rm -rf %{buildroot}

OWNER=`id -un`
GROUP=`id -gn`

make install DESTDIR=%{buildroot} BINDIR=%{_bindir} MANDIR=%{_mandir}/man1/ OWNER=${OWNER} GROUP=${GROUP}

%files
%doc AUTHORS COPYING README LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
