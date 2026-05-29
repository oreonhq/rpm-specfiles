%global source0_hash fa026f9bb0124f4d6c808f9aef4057aad65e7b35d8ff43951cef0abe06bb9a9a

%global tarball libX11
#global gitdate 20130524
#global gitversion a3bdd2b09

Summary: Core X11 protocol client library
Name: libX11
Version: 1.8.12
Release: 3%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
License: MIT AND X11
URL: http://www.x.org

%if 0%{?gitdate}
Source0:        https://www.x.org/archive/individual/lib/libX11-1.8.12.tar.xz
Source1:    make-git-snapshot.sh
Source2:    commitid
%else
Source0:        https://www.x.org/archive/individual/lib/libX11-1.8.12.tar.xz
%endif


Patch2: dont-forward-keycode-0.patch

BuildRequires: libtool
BuildRequires: make
BuildRequires: xorg-x11-util-macros >= 1.11
BuildRequires: pkgconfig(xproto) >= 7.0.15
BuildRequires: xorg-x11-xtrans-devel >= 1.0.3-4
BuildRequires: libxcb-devel >= 1.2
BuildRequires: pkgconfig(xau) pkgconfig(xdmcp)
BuildRequires: perl(Pod::Usage)

Requires: %{name}-common >= %{version}-%{release}

%description
Core X11 protocol client library.

%package common
Summary: Common data for libX11
BuildArch: noarch

%description common
libX11 common data

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-xcb = %{version}-%{release}

%description devel
X.Org X11 libX11 development package

%package xcb
Summary: XCB interop for libX11
Conflicts: %{name} < %{version}-%{release}

%description xcb
libX11/libxcb interoperability library

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build
autoreconf -v --install --force
%configure --disable-silent-rules --disable-static

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# create/own compose cache dir
mkdir -p $RPM_BUILD_ROOT/var/cache/libX11/compose

# We intentionally don't ship *.la files
find $RPM_BUILD_ROOT -type f -name '*.la' -delete

# FIXME: Don't install Xcms.txt - find out why upstream still ships this.
find $RPM_BUILD_ROOT -name 'Xcms.txt' -delete

# FIXME package these properly
rm -rf $RPM_BUILD_ROOT%{_docdir}

%check
make %{?_smp_mflags} check

%ldconfig_post
%ldconfig_postun

%files
%{_libdir}/libX11.so.6
%{_libdir}/libX11.so.6.4.0

%files xcb
%{_libdir}/libX11-xcb.so.1
%{_libdir}/libX11-xcb.so.1.0.0

%files common
%doc AUTHORS COPYING README.md
%{_datadir}/X11/locale/
%{_datadir}/X11/XErrorDB
%dir /var/cache/libX11
%dir /var/cache/libX11/compose

%files devel
%{_includedir}/X11/ImUtil.h
%{_includedir}/X11/XKBlib.h
%{_includedir}/X11/Xcms.h
%{_includedir}/X11/Xlib.h
%{_includedir}/X11/XlibConf.h
%{_includedir}/X11/Xlibint.h
%{_includedir}/X11/Xlib-xcb.h
%{_includedir}/X11/Xlocale.h
%{_includedir}/X11/Xregion.h
%{_includedir}/X11/Xresource.h
%{_includedir}/X11/Xutil.h
%{_includedir}/X11/cursorfont.h
%{_includedir}/X11/extensions/XKBgeom.h
%{_libdir}/libX11.so
%{_libdir}/libX11-xcb.so
%{_libdir}/pkgconfig/x11.pc
%{_libdir}/pkgconfig/x11-xcb.pc
%{_mandir}/man3/*.3*
%{_mandir}/man5/*.5*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8.12-3
- Prepare for Oreon 11 (RP1)
