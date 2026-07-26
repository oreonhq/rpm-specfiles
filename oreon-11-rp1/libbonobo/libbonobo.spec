%global source0_hash 9160d4f277646400d3bb6b4fa73636cc6d1a865a32b9d0760e1e9e6ee624976b

%define libxml2_version 2.4.21
%define orbit2_version 2.7.5

%define po_package libbonobo-2.0

Summary: Bonobo component system
Name: libbonobo
Version: 2.32.1
Release: 34%{?dist}
URL: http://ftp.gnome.org
Source0: http://download.gnome.org/sources/libbonobo/2.32/%{name}-%{version}.tar.bz2
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
# bonobo-activation-server, bonobo-activation-sysconf and bonobo-slay are GPL
# libbonobo and libbonobo-activation are LGPLv2+
BuildRequires: libxml2-devel >= %{libxml2_version}
BuildRequires: ORBit2-devel >= %{orbit2_version}
BuildRequires: intltool >= 0.14-1
BuildRequires: automake autoconf libtool
BuildRequires: gtk-doc
BuildRequires: flex, bison, zlib-devel, popt-devel
BuildRequires: dbus-glib-devel
BuildRequires: gettext
BuildRequires: make

Patch0: libbonobo-multishlib.patch
Patch1: libbonobo-2.32.1-srcdir-macro.patch
Patch2: 0001-Remove-use-of-G_DISABLE_DEPRECATED.patch
Patch3: libbonobo-2.32.1-c23.patch

%description
Bonobo is a component system based on CORBA, used by the GNOME desktop.

%package devel
Summary: Libraries and headers for libbonobo
Requires:  %name = %{version}-%{release}
Requires:  ORBit2-devel >= %{orbit2_version}
Requires:  libxml2-devel >= %{libxml2_version}
Requires:  popt-devel

%description devel
Bonobo is a component system based on CORBA, used by the GNOME desktop.

This package contains header files used to compile programs that
use Bonobo.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%ifarch ppc64 s390x x86_64
%patch -P0 -p1 -b .multishlib
%endif

%patch -P1 -p0 -b .srcmacro
%patch -P2 -p1
%patch -P3 -p1 -b .c23

# Add ACLOCAL_PATH for gettext 0.25 (ref: bug 2366708)
export ACLOCAL_PATH=%{_datadir}/gettext/m4/
autoreconf -i -f

%build
%configure --disable-gtk-doc

make

%install
make install DESTDIR=$RPM_BUILD_ROOT

## just kill this wherever it lives
rm -f $RPM_BUILD_ROOT%{_libdir}/bonobo-2.0/samples/bonobo-echo-2
rm -f $RPM_BUILD_ROOT%{_prefix}/lib/bonobo-2.0/samples/bonobo-echo-2

## kill other stuff
rm $RPM_BUILD_ROOT%{_bindir}/echo-client-2
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm $RPM_BUILD_ROOT%{_libdir}/*.a
rm $RPM_BUILD_ROOT%{_libdir}/bonobo/monikers/*.*a
rm $RPM_BUILD_ROOT%{_libdir}/orbit-2.0/*.*a
rm $RPM_BUILD_ROOT%{_bindir}/bonobo-slay

for serverfile in $RPM_BUILD_ROOT%{_libdir}/bonobo/servers/*.server; do
    sed -i -e 's|location *= *"/usr/lib\(64\)*/|location="/usr/$LIB/|' $serverfile
done

# noarch packages install to /usr/lib/bonobo/servers
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/bonobo/servers

%find_lang %{po_package}

%ldconfig_scriptlets

%files -f %{po_package}.lang

%doc AUTHORS COPYING NEWS README doc/NAMESPACE

%{_libdir}/lib*.so.*
%{_libdir}/bonobo
%{_libdir}/orbit-2.0/*.so*
%{_bindir}/*
%{_libexecdir}/*
%{_sbindir}/*
%dir %{_prefix}/lib/bonobo/servers
%dir %{_prefix}/lib/bonobo
%dir %{_sysconfdir}/bonobo-activation
%config %{_sysconfdir}/bonobo-activation/*
%{_datadir}/man/man*/*

%files devel

%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/idl/*
%{_datadir}/gtk-doc/html/libbonobo
%{_datadir}/gtk-doc/html/bonobo-activation

%changelog
%autochangelog
