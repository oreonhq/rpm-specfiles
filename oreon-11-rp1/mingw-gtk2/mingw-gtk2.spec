%global source0_hash ac2ac757f5942d318a311a54b0c80b5ef295f299c2a73c632f6bfb1ff49cc6da

%{?mingw_package_header}

Name:           mingw-gtk2
Version:        2.24.33
Release:        17%{?dist}
Summary:        MinGW Windows Gtk2 library

License:        LGPL-2.0-or-later
URL:            http://www.gtk.org
Source0:        http://download.gnome.org/sources/gtk+/2.24/gtk+-%{version}.tar.xz
BuildArch:      noarch

# wine %{mingw32_bindir}/gtk-query-immodules-2.0.exe > gtk.immodules
Source1:        gtk.immodules

Patch1:         system-python.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=583273
Patch2:         icon-padding.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=599618
Patch3:         tooltip-positioning.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=611313
Patch4:         window-dragging.patch
# Fix use of extended buttons in gtkstatusicon.
Patch5:         mingw32-gtk2-2.15.0-xbuttons.patch
# Enable building a static library of GTK
Patch6:         mingw32-gtk2-enable_static_build.patch
# Fix incompatible pointer types
Patch7:         gtk-incompat-pointer-type.patch
# Avoid implicit function declaration
Patch8:         gtk-implicit-decl.patch
# Assorted build fixes
Patch10:        gtk2-c99.patch
Patch11:        gtk2-c89.patch
Patch12:        gtk2-c89-2.patch
Patch13:        gtk2-c89-3.patch
Patch14:        gtk2-c89-4.patch
Patch15:        gtk2-c89-5.patch
Patch16:        gtk2-c89-6.patch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-atk
BuildRequires:  mingw32-cairo
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-pango
BuildRequires:  mingw32-gdk-pixbuf
BuildRequires:  mingw32-pixman
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-atk
BuildRequires:  mingw64-cairo
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-pango
BuildRequires:  mingw64-gdk-pixbuf
BuildRequires:  mingw64-pixman
BuildRequires:  mingw64-zlib

BuildRequires:  pkgconfig

# Native one for msgfmt
BuildRequires:  gettext
# Native one for glib-genmarsjal
BuildRequires:  glib2-devel
# Native one for gtk-update-icon-cache
BuildRequires:  gtk-update-icon-cache
# Native one for gdk-pixbuf-csource
BuildRequires:  gtk2-devel
# Packages needed for regenerating configure
BuildRequires:  gtk-doc
BuildRequires:  gobject-introspection-devel

# Needed for the patch
BuildRequires:  autoconf automake libtool

%description
MinGW Windows Gtk2 library.

# Win32
%package -n mingw32-gtk2
Summary:        MinGW Windows Gtk2 library
# built as a subpackage of mingw-gtk3
Requires:       mingw32-gtk-update-icon-cache

%description -n mingw32-gtk2
MinGW Windows Gtk2 library.

%package -n mingw32-gtk2-static
Summary:        Static version of the MinGW Windows Gtk2 library
Requires:       mingw32-gtk2 = %{version}-%{release}

%description -n mingw32-gtk2-static
Static version of the MinGW Windows Gtk2 library.

# Win64
%package -n mingw64-gtk2
Summary:        MinGW Windows Gtk2 library
# built as a subpackage of mingw-gtk3
Requires:       mingw64-gtk-update-icon-cache

%description -n mingw64-gtk2
MinGW Windows Gtk2 library.

%package -n mingw64-gtk2-static
Summary:        Static version of the MinGW Windows Gtk2 library
Requires:       mingw64-gtk2 = %{version}-%{release}

%description -n mingw64-gtk2-static
Static version of the MinGW Windows Gtk2 library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n gtk+-%{version}

%build

export MINGW32_CFLAGS='%mingw32_cflags -fno-strict-aliasing -std=gnu99'
export MINGW64_CFLAGS='%mingw64_cflags -fno-strict-aliasing -std=gnu99'
%mingw_configure --disable-cups --enable-static

# The pre-generated gtk.def file can't be used for MinGW-W64
# Force a regeneration of this file by removing the bundled copy
rm -f gtk/gtk.def

%mingw_make_build

%install
%mingw_make_install

rm -f %{buildroot}/%{mingw32_libdir}/charset.alias
rm -f %{buildroot}/%{mingw64_libdir}/charset.alias

# Remove manpages which duplicate those in Fedora native.
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}

# Remove documentation too.
rm -rf %{buildroot}%{mingw32_datadir}/gtk-doc
rm -rf %{buildroot}%{mingw64_datadir}/gtk-doc

# The .def files are only used while compiling the libraries themselves
# (they contain a list of functions which need to be exported by the linker)
# so they serve no purpose for other libraries and applications
rm -f %{buildroot}%{mingw32_libdir}/*.def
rm -f %{buildroot}%{mingw64_libdir}/*.def

# Install the gtk.immodules file
mkdir -p %{buildroot}%{mingw32_sysconfdir}/gtk-2.0/
mkdir -p %{buildroot}%{mingw64_sysconfdir}/gtk-2.0/
install -m 0644 %{SOURCE1} %{buildroot}%{mingw32_sysconfdir}/gtk-2.0/
install -m 0644 %{SOURCE1} %{buildroot}%{mingw64_sysconfdir}/gtk-2.0/

# Drop all .la files
find %{buildroot} -name "*.la" -delete

# Drop the .dll.a files for all modules as nothing is supposed
# to link directly to these modules
rm -f %{buildroot}%{mingw32_libdir}/gtk-2.0/2.10.0/*/*.dll.a
rm -f %{buildroot}%{mingw64_libdir}/gtk-2.0/2.10.0/*/*.dll.a
rm -f %{buildroot}%{mingw32_libdir}/gtk-2.0/modules/*.dll.a
rm -f %{buildroot}%{mingw64_libdir}/gtk-2.0/modules/*.dll.a

# gtk-update-icon-cache.exe is now shipped in mingw-gtk3
rm -f %{buildroot}%{mingw32_bindir}/gtk-update-icon-cache.exe
rm -f %{buildroot}%{mingw64_bindir}/gtk-update-icon-cache.exe

%mingw_find_lang gtk2 --all-name

# Win32
%files -n mingw32-gtk2 -f mingw32-gtk2.lang
%license COPYING
%{mingw32_datadir}/themes/*
%{mingw32_bindir}/gtk-builder-convert
%{mingw32_bindir}/gtk-demo.exe
%{mingw32_bindir}/gtk-query-immodules-2.0.exe
%{mingw32_bindir}/libgailutil-18.dll
%{mingw32_bindir}/libgdk-win32-2.0-0.dll
%{mingw32_bindir}/libgtk-win32-2.0-0.dll
%dir %{mingw32_libdir}/gtk-2.0
%dir %{mingw32_libdir}/gtk-2.0/2.10.0
%dir %{mingw32_libdir}/gtk-2.0/2.10.0/engines
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libpixmap.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libwimp.dll
%dir %{mingw32_libdir}/gtk-2.0/2.10.0/immodules
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-am-et.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-cedilla.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-cyrillic-translit.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-ime.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-inuktitut.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-ipa.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-multipress.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-thai.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-ti-er.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-ti-et.dll
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-viqr.dll
%{mingw32_libdir}/gtk-2.0/include/
%dir %{mingw32_libdir}/gtk-2.0/modules
%{mingw32_libdir}/gtk-2.0/modules/libgail.dll
%{mingw32_libdir}/libgailutil.dll.a
%{mingw32_libdir}/libgdk-win32-2.0.dll.a
%{mingw32_libdir}/libgtk-win32-2.0.dll.a
%{mingw32_libdir}/pkgconfig/gail.pc
%{mingw32_libdir}/pkgconfig/gdk-2.0.pc
%{mingw32_libdir}/pkgconfig/gdk-win32-2.0.pc
%{mingw32_libdir}/pkgconfig/gtk+-2.0.pc
%{mingw32_libdir}/pkgconfig/gtk+-win32-2.0.pc
%{mingw32_includedir}/gtk-2.0/
%{mingw32_includedir}/gail-1.0/
%{mingw32_sysconfdir}/gtk-2.0/
%{mingw32_datadir}/aclocal/gtk-2.0.m4
%{mingw32_datadir}/gtk-2.0/

%files -n mingw32-gtk2-static
%{mingw32_libdir}/libgailutil.a
%{mingw32_libdir}/libgdk-win32-2.0.a
%{mingw32_libdir}/libgtk-win32-2.0.a
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libpixmap.a
%{mingw32_libdir}/gtk-2.0/2.10.0/engines/libwimp.a
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-am-et.a
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-cedilla.a
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-cyrillic-translit.a
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-ime.a
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-inuktitut.a
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-ipa.a
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-multipress.a
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-thai.a
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-ti-er.a
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-ti-et.a
%{mingw32_libdir}/gtk-2.0/2.10.0/immodules/im-viqr.a
%{mingw32_libdir}/gtk-2.0/modules/libgail.a

# Win64
%files -n mingw64-gtk2 -f mingw64-gtk2.lang
%license COPYING
%{mingw64_datadir}/themes/*
%{mingw64_bindir}/gtk-builder-convert
%{mingw64_bindir}/gtk-demo.exe
%{mingw64_bindir}/gtk-query-immodules-2.0.exe
%{mingw64_bindir}/libgailutil-18.dll
%{mingw64_bindir}/libgdk-win32-2.0-0.dll
%{mingw64_bindir}/libgtk-win32-2.0-0.dll
%dir %{mingw64_libdir}/gtk-2.0
%dir %{mingw64_libdir}/gtk-2.0/2.10.0
%dir %{mingw64_libdir}/gtk-2.0/2.10.0/engines
%{mingw64_libdir}/gtk-2.0/2.10.0/engines/libpixmap.dll
%{mingw64_libdir}/gtk-2.0/2.10.0/engines/libwimp.dll
%dir %{mingw64_libdir}/gtk-2.0/2.10.0/immodules
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-am-et.dll
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-cedilla.dll
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-cyrillic-translit.dll
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-ime.dll
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-inuktitut.dll
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-ipa.dll
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-multipress.dll
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-thai.dll
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-ti-er.dll
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-ti-et.dll
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-viqr.dll
%{mingw64_libdir}/gtk-2.0/include/
%dir %{mingw64_libdir}/gtk-2.0/modules
%{mingw64_libdir}/gtk-2.0/modules/libgail.dll
%{mingw64_libdir}/libgailutil.dll.a
%{mingw64_libdir}/libgdk-win32-2.0.dll.a
%{mingw64_libdir}/libgtk-win32-2.0.dll.a
%{mingw64_libdir}/pkgconfig/gail.pc
%{mingw64_libdir}/pkgconfig/gdk-2.0.pc
%{mingw64_libdir}/pkgconfig/gdk-win32-2.0.pc
%{mingw64_libdir}/pkgconfig/gtk+-2.0.pc
%{mingw64_libdir}/pkgconfig/gtk+-win32-2.0.pc
%{mingw64_includedir}/gtk-2.0/
%{mingw64_includedir}/gail-1.0/
%{mingw64_sysconfdir}/gtk-2.0/
%{mingw64_datadir}/aclocal/gtk-2.0.m4
%{mingw64_datadir}/gtk-2.0/

%files -n mingw64-gtk2-static
%{mingw64_libdir}/libgailutil.a
%{mingw64_libdir}/libgdk-win32-2.0.a
%{mingw64_libdir}/libgtk-win32-2.0.a
%{mingw64_libdir}/gtk-2.0/2.10.0/engines/libpixmap.a
%{mingw64_libdir}/gtk-2.0/2.10.0/engines/libwimp.a
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-am-et.a
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-cedilla.a
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-cyrillic-translit.a
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-ime.a
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-inuktitut.a
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-ipa.a
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-multipress.a
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-thai.a
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-ti-er.a
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-ti-et.a
%{mingw64_libdir}/gtk-2.0/2.10.0/immodules/im-viqr.a
%{mingw64_libdir}/gtk-2.0/modules/libgail.a

%changelog
%autochangelog
