%global source0_hash 64926eebf90092dca21b14259a5301b7b98e7b1943e8a201c7d726084809b527
Name: dosfstools
Version: 4.2
Release:        1%{?dist}
Summary:        Utilities for making and checking MS-DOS FAT filesystems on Linux
License: GPL-3.0-or-later
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
URL: https://github.com/dosfstools/dosfstools
Recommends: glibc-gconv-extra
%if "%{_sbindir}" == "%{_bindir}"
Requires:       filesystem(unmerged-sbin-symlinks)
Provides:       /usr/sbin/mkfs.vfat
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  xxd
# /oreon:deps
%description
The dosfstools package includes the mkdosfs and dosfsck utilities,
which respectively make and check MS-DOS FAT filesystems on hard
drives or on floppies.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --enable-compat-symlinks
%make_build CFLAGS="%{optflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -fno-strict-aliasing"
%install
%make_install PREFIX=%{_prefix}
rm -f %{buildroot}%{_docdir}/%{name}/*
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.2-18
- Prepare for Oreon 11 (RP1)
