%global source0_hash ae352f2495889e65524c979932c909f4629a58e64290fb0c95333373225d3c0f

%define po_package libgnomeui-2.0

Summary: GNOME base GUI library
Name: libgnomeui
Version: 2.24.5
Release: 37%{?dist}
URL: http://www.gnome.org
Source0: http://download.gnome.org/sources/libgnomeui/2.24/%{name}-%{version}.tar.bz2

# https://bugzilla.gnome.org/show_bug.cgi?id=606437
Patch0: libgnomeui-2.23.4-disable-event-sounds.patch
Patch1: 0001-gnome-scores.h-Convert-to-UTF-8.patch

License: LGPL-2.0-or-later

BuildRequires: glib2-devel
BuildRequires: pango-devel
BuildRequires: gtk2-devel
BuildRequires: GConf2-devel
BuildRequires: gnome-vfs2-devel
BuildRequires: libgnomecanvas-devel
BuildRequires: libbonoboui-devel
BuildRequires: libxml2-devel
BuildRequires: libgnome-devel
BuildRequires: libart_lgpl-devel
BuildRequires: libglade2-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: libSM-devel
BuildRequires: fontconfig-devel
BuildRequires: gettext
BuildRequires: automake, autoconf, libtool
BuildRequires: intltool
BuildRequires: make

#Requires: yelp
#  This creates a chicken/egg problem with updating yelp:
#  https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=249000

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The libgnomeui package
includes GUI-related libraries that are needed to run GNOME. (The
libgnome package includes the library features that don\'t use the X
Window System.)

%package devel
Summary: Libraries and headers for libgnome
Requires: %{name} = %{version}-%{release}
Requires: libSM-devel
Requires: libICE-devel

%description devel
You should install the libgnomeui-devel package if you would like to
compile GNOME applications. You do not need to install
libgnomeui-devel if you just want to use the GNOME desktop
environment.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .disable-sound-events
%patch -P1 -p1

libtoolize --force --copy
autoreconf -i

%build
export CFLAGS="$CFLAGS -std=gnu17"
%configure --disable-gtk-doc --disable-static

sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' libtool

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang %{po_package}

%ldconfig_scriptlets

%files -f %{po_package}.lang
%doc COPYING.LIB NEWS ChangeLog
%{_libdir}/lib*.so.*
## FIXME questionable that libgnomeui still contains these
%{_datadir}/pixmaps/*
%{_libdir}/libglade/2.0/*.so

%files devel
%doc %{_datadir}/gtk-doc/html/libgnomeui
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%changelog
%autochangelog
