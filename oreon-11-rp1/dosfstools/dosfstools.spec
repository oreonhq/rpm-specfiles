%global source0_hash 64926eebf90092dca21b14259a5301b7b98e7b1943e8a201c7d726084809b527

Name: dosfstools
Version: 4.2
Release: 18%{?dist}
Summary: Utilities for making and checking MS-DOS FAT filesystems on Linux
License: GPL-3.0-or-later
Source0: https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
URL: https://github.com/dosfstools/dosfstools

BuildRequires: gcc
BuildRequires: make
# For tests
BuildRequires: xxd
# rhbz#2021638
Recommends: glibc-gconv-extra

%if "%{_sbindir}" == "%{_bindir}"
# Compat symlinks for Requires in other packages.
# We rely on filesystem to create the symlinks for us.
Requires:       filesystem(unmerged-sbin-symlinks)
Provides:       /usr/sbin/mkfs.vfat
%endif

%description
The dosfstools package includes the mkdosfs and dosfsck utilities,
which respectively make and check MS-DOS FAT filesystems on hard
drives or on floppies.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
%configure --enable-compat-symlinks
%make_build CFLAGS="%{optflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -fno-strict-aliasing"

%install
%make_install PREFIX=%{_prefix}

# license file is in the licenses dir, drop ancient/duplicate docs
rm -f %{buildroot}%{_docdir}/%{name}/*

%check
make check

%files
%license COPYING
%doc NEWS README
%{_sbindir}/*
%{_mandir}/man8/*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.2-18
- Prepare for Oreon 11 (RP1)
