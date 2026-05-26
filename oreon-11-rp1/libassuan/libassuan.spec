Name:    libassuan
Summary: GnuPG IPC library
Version: 2.5.7
Release: 5%{?dist}

# The library is LGPLv2+, the documentation GPLv3+
License: GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Source0: https://gnupg.org/ftp/gcrypt/libassuan/libassuan-%{version}.tar.bz2
Source1: https://gnupg.org/ftp/gcrypt/libassuan/libassuan-%{version}.tar.bz2.sig
URL:     https://www.gnupg.org/

Patch1:  libassuan-2.5.2-multilib.patch
Patch2:  libassuan-2.5.5-coverity.patch
# oreon url source checksums begin
%global source0_sha256 0103081ffc27838a2e50479153ca105e873d3d65d8a9593282e9c94c7e6afb76
%global source0_file libassuan-2.5.7.tar.bz2
# oreon url source checksums end

BuildRequires: gcc
BuildRequires: gawk
BuildRequires: libgpg-error-devel >= 1.8
BuildRequires: make

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libassuan-2.5.7.tar.bz2; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "0103081ffc27838a2e50479153ca105e873d3d65d8a9593282e9c94c7e6afb76" || { echo "oreon: Source0 SHA256 mismatch for libassuan-2.5.7.tar.bz2" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q

%patch 1 -p1 -b .multilib
%patch 2 -p1 -b .coverity


%build
%configure \
  --includedir=%{_includedir}/libassuan2

%make_build


%install
%make_install

## Unpackaged files
rm -fv %{buildroot}%{_infodir}/dir
rm -fv %{buildroot}%{_libdir}/lib*.la


%check
make check


%ldconfig_scriptlets

%files
%license COPYING COPYING.LIB
%doc AUTHORS NEWS README
%{_libdir}/libassuan.so.0*

%files devel 
%{_bindir}/libassuan-config
%{_includedir}/libassuan2/
%{_libdir}/libassuan.so
%{_libdir}/pkgconfig/libassuan.pc
%{_datadir}/aclocal/libassuan.m4
%{_infodir}/assuan.info*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5.7-5
- Prepare for Oreon 11 (RP1)
