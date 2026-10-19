%global source1_hash 5aa3c5cea6f42bcb96be9e1dd922b33ccb05e2f0565e93674e85ddcf8cd78e86
%global source0_hash d2931cdad266e633510f9970e1a2f346055e351bb19f9b78912475b8074c36f6
Name:    libassuan
Summary:        GnuPG IPC library
Version: 3.0.2
Release:        1%{?dist}
License: GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Source0:        https://gnupg.org/ftp/gcrypt/libassuan/libassuan-%{version}.tar.bz2
Source1:        https://gnupg.org/ftp/gcrypt/libassuan/libassuan-%{version}.tar.bz2.sig
URL:     https://www.gnupg.org/
Patch1:  libassuan-2.5.2-multilib.patch
Patch2:  libassuan-2.5.5-coverity.patch
# oreon:deps
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  hostname
BuildRequires:  libgpg-error-devel
BuildRequires:  make
# /oreon:deps
%description
This is the IPC library used by GnuPG 2, GPGME and a few other
packages.

%package devel 
Summary: GnuPG IPC library 
Provides: libassuan2-devel = %{version}-%{release}
Provides: libassuan2-devel%{?_isa} = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
%description devel 
This is the IPC static library used by GnuPG 2, GPGME and a few other
packages.

This package contains files needed to develop applications using %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%patch 1 -p1 -b .multilib
%patch 2 -p1 -b .coverity
sed -i 's/^\([[:space:]]*\)fp =/\1FILE *fp =/' tests/fdpassing.c

%build

%configure \
  --includedir=%{_includedir}/libassuan2
%make_build
%install
%make_install
rm -fv %{buildroot}%{_infodir}/dir
rm -fv %{buildroot}%{_libdir}/lib*.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libassuan-devel -f %{oreon_filedir}/libassuan-devel.list

%changelog

%autochangelog
