%global source0_hash 3eeb137319b608512b2d23c54ea8b52b511db806ffbd5fa730a394431d556f3f
Name:           rsync-bpc
Version:        3.1.3.2
Release:        1%{?dist}
Summary:        A customized fork of rsync that is used as part of BackupPC
License:        GPL-3.0-or-later
URL:            https://github.com/backuppc/rsync-bpc
Source0:        https://github.com/backuppc/rsync-bpc/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0:         rsync-bpc-rsync_h.patch
Patch1:         rsync-bpc-configure-c99.patch
Patch2:         rsync-bpc-gcc_15.patch
Provides:       bundled(rsync) = 3.1.3
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  popt-devel
# /oreon:deps
%description
Rsync-bpc is a customized version of rsync that is used as part of
BackupPC, an open source backup system.

The main change to rsync is adding a shim layer (in the subdirectory
backuppc, and in bpc_sysCalls.c) that emulates the system calls for
accessing the file system so that rsync can directly read/write files
in BackupPC's format.

Rsync-bpc is fully line-compatible with vanilla rsync, so it can talk
to rsync servers and clients.

Rsync-bpc serves no purpose outside of BackupPC.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
