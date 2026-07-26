%global source0_hash b22ca970efe24fcedff44f38075c5f34e0893f66abb419f3180ff92adf9e2a22

Summary: A program for X11 protocol tracing
Name: x11trace
Version: 1.3.1
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: http://xtrace.alioth.debian.org/

# Please set buildid below when building a private version of this rpm to
# differentiate it from the stock rpm.
#
# % global buildid .local

Release: 31%{?buildid}%{?dist}
Obsoletes: xtrace < 1.3.1-7

Source0: ftp://ftp.debian.org/debian/pool/main/x/xtrace/xtrace_%{version}.orig.tar.gz

# Bring the sources up to the head of the git master branch.
Patch1: x11trace-1.3.1-git-HEAD.patch

# AM_CONFIG_HEADER() is obsolete - use AC_CONFIG_HEADERS instead.
Patch2: x11trace-1.3.1-use-AC_CONFIG_HEADERS.patch

# Rename xtrace to x11trace
Patch3: x11trace-1.3.1-rename-to-x11trace.patch
Patch4: x11trace-1.3.1-rename-manpage.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires: automake autoconf
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: xorg-x11-proto-devel

%description
What strace is for system calls, x11trace is for X11 connections:
you hook it between one or more X11 clients and an X server and
it prints the requests going from client to server and the replies,
events and errors going the other way.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n xtrace-1.3.1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

%build
autoreconf -i
%configure

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"

%files
%doc AUTHORS COPYING NEWS README
%{_bindir}/*
%{_datadir}/x11trace
%{_mandir}/man1/*

%changelog
%autochangelog
