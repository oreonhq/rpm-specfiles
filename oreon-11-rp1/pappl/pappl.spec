%global source0_hash 50fec863a28a3c39af639de29d58bf8cefdafa258b66e3c0dfbe2097801dc9db

#
# RPM spec file for the Printer Application Framework
#
# Copyright © 2020-2021 by Michael R Sweet
#
# Licensed under Apache License v2.0.  See the file "LICENSE" for more
# information.
#

Summary: Printer Application Framework (PAPPL)
Name: pappl
Version: 1.4.9
Release: 4%{?dist}
License: Apache-2.0 WITH LLVM-exception
Source:        https://github.com/michaelrsweet/pappl/releases/download/v1.4.9/pappl-1.4.9.tar.gz
Url: https://www.msweet.org/pappl


# Add listing raw sockets
# https://github.com/michaelrsweet/pappl/pull/341
Patch001: 0001-List-raw-sockets-during-printers-subcommand-if-avail.patch
# raise MAX_VENDOR https://sourceforge.net/p/gimp-print/mailman/gimp-print-devel/thread/e24b2385-6576-a949-a40d-3786c8067520%40gmail.com/#msg37353830
# downstream only, Mike does not want to merge the change
Patch002: pappl-max-vendors.patch


BuildRequires: avahi-devel
BuildRequires: cups-devel
BuildRequires: gcc
BuildRequires: git-core
BuildRequires: glibc-devel
BuildRequires: gnutls-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libpng-devel
BuildRequires: libusbx-devel
BuildRequires: make
BuildRequires: pkgconfig
BuildRequires: pam-devel
BuildRequires: zlib-devel

%description
PAPPL is a simple C-based framework/library for developing CUPS Printer
Applications, which are the recommended replacement for printer drivers.

PAPPL supports JPEG, PNG, PWG Raster, Apple Raster, and "raw" printing to
printers connected via USB and network (AppSocket/JetDirect) connections.
PAPPL provides access to the printer via its embedded IPP Everywhere™ service,
either local to the computer or on your whole network, which can then be
discovered and used by any application.

PAPPL is licensed under the Apache License Version 2.0 with an exception
to allow linking against GPL2/LGPL2 software (like older versions of CUPS),
so it can be used freely in any project you'd like.

%package devel
Summary: PAPPL - development environment
Requires: %{name}%{?_isa} = %{version}-%{release}

BuildRequires: avahi-devel

%description devel
This package provides the PAPPL headers and development environment.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -S git

%build
#need this to enable build with '-D_TIME_BITS=64' flag
export CPPFLAGS="$CPPFLAGS -D_FILE_OFFSET_BITS=64"
%configure --enable-libjpeg\
  --enable-libpng\
  --enable-libusb\
  --disable-static\
  --with-dnssd=avahi\
  --with-tls=gnutls\
  --with-dsoflags="$DSOFLAGS -Wl,-z,now,--as-needed"
# add --enable-libpam once there is a new version - cosmetic issue, libpam is used when
# found in buildroot, which is taken care of by BuilrRequires for pam-devel
%make_build

%install
%make_install BUILDROOT=%{buildroot}

%check
make test

%files
%dir %{_datadir}/pappl
%{_datadir}/pappl/*
%doc *.md
%{_libdir}/libpappl.so.*
%license LICENSE NOTICE

%files devel
%{_bindir}/pappl-makeresheader
%{_docdir}/pappl/*.png
%{_docdir}/pappl/*.html
%dir %{_includedir}/pappl
%{_includedir}/pappl/*.h
%{_libdir}/libpappl.so
%{_libdir}/pkgconfig/pappl.pc
%{_mandir}/man1/pappl.1.gz
%{_mandir}/man1/pappl-makeresheader.1.gz
%{_mandir}/man3/pappl-client.3.gz
%{_mandir}/man3/pappl-device.3.gz
%{_mandir}/man3/pappl-job.3.gz
%{_mandir}/man3/pappl-log.3.gz
%{_mandir}/man3/pappl-mainloop.3.gz
%{_mandir}/man3/pappl-printer.3.gz
%{_mandir}/man3/pappl-resource.3.gz
%{_mandir}/man3/pappl-system.3.gz

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.9-4
- Prepare for Oreon 11 (RP1)
