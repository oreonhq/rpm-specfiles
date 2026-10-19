%global source0_hash 1684c4e06446e9f7d93a39729fa0ba56f07a4007560080fdad7d0e2076a3615f
Summary:        Printer Application Framework (PAPPL)
Name: pappl
Version: 1.4.12
Release:        1%{?dist}
License: Apache-2.0 WITH LLVM-exception
Source0:        https://github.com/michaelrsweet/pappl/releases/download/v%{version}/pappl-%{version}.tar.gz
Url: https://www.msweet.org/pappl
Patch001: 0001-List-raw-sockets-during-printers-subcommand-if-avail.patch
Patch002: pappl-max-vendors.patch
# oreon:deps
BuildRequires:  avahi-devel
BuildRequires:  cups-devel
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  glibc-devel
BuildRequires:  gnutls-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libusbx-devel
BuildRequires:  make
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CPPFLAGS="$CPPFLAGS -D_FILE_OFFSET_BITS=64"
%configure --enable-libjpeg\
  --enable-libpng\
  --enable-libusb\
  --disable-static\
  --with-dnssd=avahi\
  --with-tls=gnutls\
  --with-dsoflags="$DSOFLAGS -Wl,-z,now,--as-needed"
%make_build
%install
%make_install BUILDROOT=%{buildroot}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n pappl-devel -f %{oreon_filedir}/pappl-devel.list

%changelog

%autochangelog
