%global source0_hash bc9d22d6d252b920ec9cdf18e00b7655a6189b3f34f42e58d5bb152957289840

Summary: Tools for reading and writing Macintosh HFS volumes
Name: hfsutils
Version: 3.2.6
Release: 53%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source: ftp://ftp.mars.org/pub/hfs/%{name}-%{version}.tar.gz
Patch0: hfsutils-3.2.6-errno.patch
Patch1: hfsutils-3.2.6-largefile.patch
Patch2: hfsutils-3.2.6-configure-c99.patch
Patch3: hfsutils-3.2.6-include-c99.patch
URL: http://www.mars.org/home/rob/proj/hfs/
BuildRequires: libXft-devel tcl-devel tk-devel gcc
BuildRequires: make

%package devel
Summary: A C library for reading and writing Macintosh HFS volumes
Provides: %{name}-static = %{version}-%{release}

%package x11
Summary: A Tk-based front end for browsing and copying files

%description
HFS (Hierarchical File System) is the native volume format found on
modern Macintosh computers.  Hfsutils provides utilities for accessing
HFS volumes from Linux and UNIX systems.  Hfsutils contains several
command-line programs which are comparable to mtools.

%description -n hfsutils-devel
The hfsutils-devel package provides a C library for low-level access
to Macintosh volumes. HFS (Hierarchical File System) is the native
volume format found on modern Macintosh computers.  The C library can
be linked with other programs to allow them to manipulate Macintosh
files in their native format.  Other HFS accessing utilities, which
are comparable to mtools, are included in the hfsutils package.

%description -n hfsutils-x11
The hfsutils-x11 package includes a Tk-based front end for browsing
and copying files, and a Tcl package and interface for scriptable access
to volumes.  A C library for low-level access to volumes is included in the
hfsutils-devel package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
CFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64 -DUSE_INTERP_RESULT -Wno-incompatible-pointer-types -Wno-deprecated-declarations -Wno-deprecated-declarations -Wno-pointer-sign -Wno-unused-but-set-variable -Wno-int-to-pointer-cast"
%{configure} --with-tcl=%{_libdir}  --with-tk=%{_libdir}
make
make hfsck/hfsck

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_includedir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}
make	BINDEST=$RPM_BUILD_ROOT%{_bindir} \
	LIBDEST=$RPM_BUILD_ROOT%{_libdir} \
	INCDEST=$RPM_BUILD_ROOT%{_includedir} \
	MANDEST=$RPM_BUILD_ROOT%{_mandir} \
	INSTALL="install -p" \
	install install_lib
install -p -m 0755 hfsck/hfsck $RPM_BUILD_ROOT/%{_bindir}

%files
%doc CHANGES CREDITS README TODO
%license COPYING COPYRIGHT
%{_bindir}/hattrib
%{_bindir}/hcd
%{_bindir}/hcopy
%{_bindir}/hdel
%{_bindir}/hdir
%{_bindir}/hformat
%{_bindir}/hfs
%{_bindir}/hfssh
%{_bindir}/hls
%{_bindir}/hmkdir
%{_bindir}/hmount
%{_bindir}/hpwd
%{_bindir}/hrename
%{_bindir}/hrmdir
%{_bindir}/humount
%{_bindir}/hvol
%{_bindir}/hfsck
%{_mandir}/man1/hattrib.1.*
%{_mandir}/man1/hcd.1.*
%{_mandir}/man1/hcopy.1.*
%{_mandir}/man1/hdel.1.*
%{_mandir}/man1/hdir.1.*
%{_mandir}/man1/hformat.1.*
%{_mandir}/man1/hfs.1.*
%{_mandir}/man1/hfssh.1.*
%{_mandir}/man1/hfsutils.1.*
%{_mandir}/man1/hls.1.*
%{_mandir}/man1/hmkdir.1.*
%{_mandir}/man1/hmount.1.*
%{_mandir}/man1/hpwd.1.*
%{_mandir}/man1/hrename.1.*
%{_mandir}/man1/hrmdir.1.*
%{_mandir}/man1/humount.1.*
%{_mandir}/man1/hvol.1.*

%files -n hfsutils-x11
%{_bindir}/xhfs
%{_mandir}/man1/xhfs.1.*

%files -n hfsutils-devel
%{_libdir}/libhfs.a
%{_libdir}/librsrc.a
%{_includedir}/hfs.h
%{_includedir}/rsrc.h

%changelog
%autochangelog
