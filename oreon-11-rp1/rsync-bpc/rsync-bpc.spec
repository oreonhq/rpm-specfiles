%global source0_hash 3eeb137319b608512b2d23c54ea8b52b511db806ffbd5fa730a394431d556f3f

Name:           rsync-bpc
Version:        3.1.3.0
Release:        16%{?dist}
Summary:        A customized fork of rsync that is used as part of BackupPC

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/backuppc/rsync-bpc
Source0:        https://github.com/backuppc/rsync-bpc/releases/download/%{version}/%{name}-%{version}.tar.gz

# Fix for building on CentOS 6 in COPR
Patch0:         rsync-bpc-rsync_h.patch
Patch1:         rsync-bpc-configure-c99.patch
Patch2:         rsync-bpc-gcc_15.patch

BuildRequires:  gcc
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  make
BuildRequires:  popt-devel
BuildRequires:  perl

Provides:       bundled(rsync) = 3.1.3

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

%autosetup -p1 -n %{name}-%{version}

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc NEWS README
%{_bindir}/rsync_bpc

%changelog
%autochangelog
