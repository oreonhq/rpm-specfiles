%global source0_hash 1012f551382639d69e194eabfbe99342ede7c856b1cd6788287f9dfd4bd8d122
%define _legacy_common_support 1
Name:           fatsort
Version:        1.7.679
Release:        1%{?dist}
Summary:        FAT sorter for FAT16 and FAT32 filesystems
License:        GPL-2.0-or-later
URL:            https://fatsort.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  make
# /oreon:deps
%description
Fatsort is a utility written in C to sort FAT16 and FAT32 filesystems. It is
needed to sort files on cheap mp3 players that display files not sorted by
their name but by the order they appear in the file allocation table (FAT).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_OPT_FLAGS"
%install
%make_install SBINDIR=%{_sbindir} MANDIR=%{_mandir}/man1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
