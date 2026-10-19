%global source0_hash e194a359c2a9fb596f04ad64b5dc247af2c4d5fdc6528492692bce83df6fb183
%global make_flags bindir=%{_bindir} mandir="%{_mandir}" prefix="%{_prefix}" \\\
CC=%{__cc} CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" ENABLE_MAN=1
Name:           cc1541
Version:        4.1
Release:        9%{?dist}
Summary:        Tool for creating Commodore Floppy disk images in D64, G64, D71 or D81 format
License:        MIT
URL:            https://bitbucket.org/PTV_Claus/%{name}
Source0:        https://bitbucket.org/PTV_Claus/%{name}/downloads/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
This is %{name} v%{version}, a tool for creating Commodore 1541
Floppy disk images in D64, G64, D71 or D81 format with custom
sector interleaving etc.   Also supports extended tracks 35-40
using either SPEED DOS or DOLPHIN DOS BAM-formatting.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build all test_cc1541 %{make_flags}
%install
%make_install %{make_flags}
%oreon_autofiles main

%check

%make_build check %{make_flags}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
