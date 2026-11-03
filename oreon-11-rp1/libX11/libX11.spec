%global source0_hash bbc78c46217174655c2b32b138ad119f3ac15f50808b4d0b3a2677a4b1afc950
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libX11
Version: 1.8.14
Release: 3%{?dist}
Summary: X11 client library
License: MIT
URL: https://www.x.org/
Source0: https://www.x.org/releases/individual/lib/libX11-%{version}.tar.xz
Source1: libX11-%{version}.tar.xz.sig
Source2: libX11-key.asc

BuildRequires: oreon-rpm-macros
BuildRequires: gnupg2
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: xorgproto
BuildRequires: xtrans
BuildRequires: libXau-devel >= 1.0.12
BuildRequires: libxcb-devel >= 1.17.0
BuildRequires: pkgconf
Requires: libX11-common = %{version}-%{release}

%description
X11 client library

%package devel
Summary: X11 client library
Requires: libX11%{?_isa} = %{version}-%{release}
Requires: libX11-xcb%{?_isa} = %{version}-%{release}

%description devel
X11 client library

%package common
Summary: Common data for libX11
BuildArch: noarch
Obsoletes: libX11 < 1.8.14-2

%description common
Locale data and error database shared by libX11.

%package xcb
Summary: XCB interoperability library for libX11
Requires: libX11%{?_isa} = %{version}-%{release}

%description xcb
libX11-xcb lets Xlib and XCB share one display connection.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n libX11-%{version} -p1

%build
%oreon_configure --disable-static
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
mkdir -p %{buildroot}%{_localstatedir}/cache/libX11/compose
rm -rf %{buildroot}%{_docdir}

%ldconfig_scriptlets
%ldconfig_scriptlets xcb

%files
%license COPYING
%{_libdir}/libX11.so.6
%{_libdir}/libX11.so.6.*

%files common
%license COPYING
%{_datadir}/X11/XErrorDB
%{_datadir}/X11/Xcms.txt
%{_datadir}/X11/locale/
%dir %{_localstatedir}/cache/libX11
%dir %{_localstatedir}/cache/libX11/compose

%files xcb
%license COPYING
%{_libdir}/libX11-xcb.so.1
%{_libdir}/libX11-xcb.so.1.*

%files devel
%{_includedir}/X11/*.h
%{_includedir}/X11/extensions/XKBgeom.h
%{_libdir}/libX11.so
%{_libdir}/libX11-xcb.so
%{_libdir}/pkgconfig/x11.pc
%{_libdir}/pkgconfig/x11-xcb.pc
%{_mandir}/man3/*.3*
%{_mandir}/man5/Compose.5*
%{_mandir}/man5/XCompose.5*
