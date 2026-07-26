%global source0_hash 1a7f7490774c87f2052d146d1e0e64518d32e6848184a18654e8d0bb57883242

Summary: X.Org X11 libXfont runtime library
Name: libXfont
Version: 1.5.4
Release: 21%{?dist}
License: MIT
URL: http://www.x.org

Source0: http://www.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires: autoconf automake libtool
BuildRequires: pkgconfig(fontsproto)
BuildRequires: xorg-x11-util-macros
BuildRequires: xorg-x11-xtrans-devel >= 1.0.3-3
BuildRequires: libfontenc-devel
BuildRequires: freetype-devel

%description
X.Org X11 libXfont runtime library

%package devel
Summary: X.Org X11 libXfont development package
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libfontenc-devel%{?_isa}

%description devel
X.Org X11 libXfont development package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
autoreconf -v --install --force
export CFLAGS="$RPM_OPT_FLAGS -Os"
%configure --disable-static
make %{?_smp_mflags}  

%install
%make_install

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_post
%ldconfig_postun

%files
%doc AUTHORS COPYING README ChangeLog
%{_libdir}/libXfont.so.1
%{_libdir}/libXfont.so.1.4.1

%files devel
%{_includedir}/X11/fonts/bdfint.h
%{_includedir}/X11/fonts/bitmap.h
%{_includedir}/X11/fonts/bufio.h
%{_includedir}/X11/fonts/fntfil.h
%{_includedir}/X11/fonts/fntfilio.h
%{_includedir}/X11/fonts/fntfilst.h
%{_includedir}/X11/fonts/fontconf.h
%{_includedir}/X11/fonts/fontencc.h
%{_includedir}/X11/fonts/fontmisc.h
%{_includedir}/X11/fonts/fontshow.h
%{_includedir}/X11/fonts/fontutil.h
%{_includedir}/X11/fonts/fontxlfd.h
%{_includedir}/X11/fonts/pcf.h
%{_includedir}/X11/fonts/ft.h
%{_includedir}/X11/fonts/ftfuncs.h
%{_libdir}/libXfont.so
%{_libdir}/pkgconfig/xfont.pc

%changelog
%autochangelog
