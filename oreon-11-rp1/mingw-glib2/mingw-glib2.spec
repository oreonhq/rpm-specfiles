%global source0_hash none

%{?mingw_package_header}

Name:           mingw-glib2
Version:        2.87.3
Release:        1%{?dist}
Summary:        MinGW Windows GLib2 library

License:        LGPL-2.0-or-later
URL:            http://www.gtk.org
# first two digits of version
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')
Source0:        http://download.gnome.org/sources/glib/%{release_version}/glib-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gcc-c++

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-libffi
BuildRequires:  mingw32-pcre2
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-libffi
BuildRequires:  mingw64-pcre2
BuildRequires:  mingw64-zlib

# Native version required for msgfmt use in build
BuildRequires:  gettext
# Native version required for glib-genmarshal
BuildRequires:  glib2-devel >= 2.45.3
BuildRequires:  python3-devel

# Prefer the use of GCC constructors over DllMain
# This prevents having to depend on DllMain in static libraries
# http://lists.fedoraproject.org/pipermail/mingw/2013-March/006429.html
# http://lists.fedoraproject.org/pipermail/mingw/2013-March/006469.html
# https://bugzilla.gnome.org/show_bug.cgi?id=698118
#Patch5:         glib-prefer-constructors-over-DllMain.patch

%description
MinGW Windows Glib2 library.

# Win32
%package -n mingw32-glib2
Summary:        MinGW Windows Glib2 library for the win32 target
# glib-genmarshal and glib-mkenums are written in Python
Requires:       python3

%description -n mingw32-glib2
MinGW Windows Glib2 library.

%package -n mingw32-glib2-static
Summary:        Static version of the MinGW Windows GLib2 library
Requires:       mingw32-glib2 = %{version}-%{release}
Requires:       mingw32-gettext-static

%description -n mingw32-glib2-static
Static version of the MinGW Windows GLib2 library.

# Win64
%package -n mingw64-glib2
Summary:        MinGW Windows Glib2 library for the win64 target
# glib-genmarshal and glib-mkenums are written in Python
Requires:       python3

%description -n mingw64-glib2
MinGW Windows Glib2 library.

%package -n mingw64-glib2-static
Summary:        Static version of the MinGW Windows GLib2 library
Requires:       mingw64-glib2 = %{version}-%{release}
Requires:       mingw64-gettext-static

%description -n mingw64-glib2-static
Static version of the MinGW Windows GLib2 library.


%{?mingw_debug_package}


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n glib-%{version}

%build
export MINGW_BUILDDIR_SUFFIX=static
%mingw_meson --default-library=static
%mingw_ninja
export MINGW_BUILDDIR_SUFFIX=shared
%mingw_meson --default-library=shared
%mingw_ninja

%install
export MINGW_BUILDDIR_SUFFIX=static
%mingw_ninja_install
export MINGW_BUILDDIR_SUFFIX=shared
%mingw_ninja_install

# There's a small difference in the file glibconfig.h between the
# shared and the static build:
#
#diff -ur shared/usr/i686-pc-mingw32/sys-root/mingw/lib/glib-2.0/include/glibconfig.h static/usr/i686-pc-mingw32/sys-root/mingw/lib/glib-2.0/include/glibconfig.h
#--- shared/usr/i686-pc-mingw32/sys-root/mingw/lib/glib-2.0/include/glibconfig.h	2009-02-20 17:34:35.735677022 +0100
#+++ static/usr/i686-pc-mingw32/sys-root/mingw/lib/glib-2.0/include/glibconfig.h	2009-02-20 17:33:35.498932269 +0100
#@@ -92,7 +92,8 @@
# 
# #define G_OS_WIN32
# #define G_PLATFORM_WIN32
#-
#+#define GLIB_STATIC_COMPILATION 1
#+#define GOBJECT_STATIC_COMPILATION 1
# 
# #define G_VA_COPY	va_copy
#
# However, we can't merge this change as it is situation-dependent...
#
# Developers using the static build of GLib need to add -DGLIB_STATIC_COMPILATION
# and -DGOBJECT_STATIC_COMPILATION to their CFLAGS to avoid compile failures

# Drop the folder which was temporary used for installing the static bits
rm -f %{buildroot}/%{mingw32_libdir}/charset.alias
rm -f %{buildroot}/%{mingw64_libdir}/charset.alias

# Drop the GDB helper files as we can't use the native Fedora GDB to debug Win32 programs
rm -rf %{buildroot}%{mingw32_datadir}/gdb
rm -rf %{buildroot}%{mingw64_datadir}/gdb

# Remove the gtk-doc documentation and manpages which duplicate Fedora native
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw32_datadir}/gtk-doc

rm -rf %{buildroot}%{mingw64_mandir}
rm -rf %{buildroot}%{mingw64_datadir}/gtk-doc

# Bash-completion files aren't interesting for mingw
rm -rf %{buildroot}%{mingw32_datadir}/bash-completion
rm -rf %{buildroot}%{mingw64_datadir}/bash-completion

# The .def files are also of no use to other binaries
rm -f %{buildroot}%{mingw32_libdir}/*.def
rm -f %{buildroot}%{mingw64_libdir}/*.def

# The gdbus-codegen pieces are already in the native glib2 package
rm -f %{buildroot}%{mingw32_bindir}/gdbus-codegen
rm -rf %{buildroot}%{mingw32_libdir}/gdbus-2.0
sed -i 's|gdbus_codegen=.*|gdbus_codegen=%{_bindir}/gdbus-codegen|g' %{buildroot}%{mingw32_libdir}/pkgconfig/gio-2.0.pc

rm -f %{buildroot}%{mingw64_bindir}/gdbus-codegen
rm -rf %{buildroot}%{mingw64_libdir}/gdbus-2.0
sed -i 's|gdbus_codegen=.*|gdbus_codegen=%{_bindir}/gdbus-codegen|g' %{buildroot}%{mingw64_libdir}/pkgconfig/gio-2.0.pc

# Delete installed tests
rm -rf %{buildroot}%{mingw32_libexecdir}/installed-tests/
rm -rf %{buildroot}%{mingw64_libexecdir}/installed-tests/

# Drop all .la files
find %{buildroot} -name "*.la" -delete

%mingw_find_lang glib20

# Manually invoke the python byte compile macro for each path that needs byte
# compilation.
%py_byte_compile %{__python3} %{buildroot}%{mingw32_datadir}/glib-2.0/gdb
%py_byte_compile %{__python3} %{buildroot}%{mingw32_datadir}/glib-2.0/codegen
%py_byte_compile %{__python3} %{buildroot}%{mingw64_datadir}/glib-2.0/gdb
%py_byte_compile %{__python3} %{buildroot}%{mingw64_datadir}/glib-2.0/codegen


# Win32
%files -n mingw32-glib2 -f mingw32-glib20.lang
%license LICENSES/LGPL-2.1-or-later.txt
%{mingw32_bindir}/gdbus.exe
%{mingw32_bindir}/gi-compile-repository.exe
%{mingw32_bindir}/gi-decompile-typelib.exe
%{mingw32_bindir}/gi-inspect-typelib.exe
%{mingw32_bindir}/gio.exe
%{mingw32_bindir}/gio-querymodules.exe
%{mingw32_bindir}/glib-compile-resources.exe
%{mingw32_bindir}/glib-compile-schemas.exe
%{mingw32_bindir}/glib-genmarshal
%{mingw32_bindir}/glib-gettextize
%{mingw32_bindir}/glib-mkenums
%{mingw32_bindir}/gobject-query.exe
%{mingw32_bindir}/gresource.exe
%{mingw32_bindir}/gsettings.exe
%{mingw32_bindir}/gspawn-win32-helper-console.exe
%{mingw32_bindir}/gspawn-win32-helper.exe
%{mingw32_bindir}/gtester-report
%{mingw32_bindir}/libgio-2.0-0.dll
%{mingw32_bindir}/libglib-2.0-0.dll
%{mingw32_bindir}/libgmodule-2.0-0.dll
%{mingw32_bindir}/libgobject-2.0-0.dll
%{mingw32_bindir}/libgirepository-2.0-0.dll
%{mingw32_bindir}/libgthread-2.0-0.dll
%{mingw32_includedir}/glib-2.0/
%{mingw32_includedir}/gio-win32-2.0/
%{mingw32_libdir}/glib-2.0/
%{mingw32_libdir}/libgio-2.0.dll.a
%{mingw32_libdir}/libglib-2.0.dll.a
%{mingw32_libdir}/libgmodule-2.0.dll.a
%{mingw32_libdir}/libgobject-2.0.dll.a
%{mingw32_libdir}/libgirepository-2.0.dll.a
%{mingw32_libdir}/libgthread-2.0.dll.a
%{mingw32_libdir}/pkgconfig/gio-2.0.pc
%{mingw32_libdir}/pkgconfig/gio-windows-2.0.pc
%{mingw32_libdir}/pkgconfig/girepository-2.0.pc
%{mingw32_libdir}/pkgconfig/glib-2.0.pc
%{mingw32_libdir}/pkgconfig/gmodule-2.0.pc
%{mingw32_libdir}/pkgconfig/gmodule-export-2.0.pc
%{mingw32_libdir}/pkgconfig/gmodule-no-export-2.0.pc
%{mingw32_libdir}/pkgconfig/gobject-2.0.pc
%{mingw32_libdir}/pkgconfig/gthread-2.0.pc
%{mingw32_datadir}/aclocal/glib-2.0.m4
%{mingw32_datadir}/aclocal/glib-gettext.m4
%{mingw32_datadir}/aclocal/gsettings.m4
%{mingw32_datadir}/gettext/its/
%{mingw32_datadir}/glib-2.0/

%files -n mingw32-glib2-static
%{mingw32_libdir}/libgio-2.0.a
%{mingw32_libdir}/libgirepository-2.0.a
%{mingw32_libdir}/libglib-2.0.a
%{mingw32_libdir}/libgmodule-2.0.a
%{mingw32_libdir}/libgobject-2.0.a
%{mingw32_libdir}/libgthread-2.0.a

# Win64
%files -n mingw64-glib2 -f mingw64-glib20.lang
%license LICENSES/LGPL-2.1-or-later.txt
%{mingw64_bindir}/gdbus.exe
%{mingw64_bindir}/gi-compile-repository.exe
%{mingw64_bindir}/gi-decompile-typelib.exe
%{mingw64_bindir}/gi-inspect-typelib.exe
%{mingw64_bindir}/gio.exe
%{mingw64_bindir}/gio-querymodules.exe
%{mingw64_bindir}/glib-compile-resources.exe
%{mingw64_bindir}/glib-compile-schemas.exe
%{mingw64_bindir}/glib-genmarshal
%{mingw64_bindir}/glib-gettextize
%{mingw64_bindir}/glib-mkenums
%{mingw64_bindir}/gobject-query.exe
%{mingw64_bindir}/gresource.exe
%{mingw64_bindir}/gsettings.exe
%{mingw64_bindir}/gspawn-win64-helper-console.exe
%{mingw64_bindir}/gspawn-win64-helper.exe
%{mingw64_bindir}/gtester-report
%{mingw64_bindir}/libgio-2.0-0.dll
%{mingw64_bindir}/libglib-2.0-0.dll
%{mingw64_bindir}/libgmodule-2.0-0.dll
%{mingw64_bindir}/libgobject-2.0-0.dll
%{mingw64_bindir}/libgirepository-2.0-0.dll
%{mingw64_bindir}/libgthread-2.0-0.dll
%{mingw64_includedir}/glib-2.0/
%{mingw64_includedir}/gio-win32-2.0/
%{mingw64_libdir}/glib-2.0/
%{mingw64_libdir}/libgio-2.0.dll.a
%{mingw64_libdir}/libglib-2.0.dll.a
%{mingw64_libdir}/libgmodule-2.0.dll.a
%{mingw64_libdir}/libgobject-2.0.dll.a
%{mingw64_libdir}/libgirepository-2.0.dll.a
%{mingw64_libdir}/libgthread-2.0.dll.a
%{mingw64_libdir}/pkgconfig/gio-2.0.pc
%{mingw64_libdir}/pkgconfig/gio-windows-2.0.pc
%{mingw64_libdir}/pkgconfig/girepository-2.0.pc
%{mingw64_libdir}/pkgconfig/glib-2.0.pc
%{mingw64_libdir}/pkgconfig/gmodule-2.0.pc
%{mingw64_libdir}/pkgconfig/gmodule-export-2.0.pc
%{mingw64_libdir}/pkgconfig/gmodule-no-export-2.0.pc
%{mingw64_libdir}/pkgconfig/gobject-2.0.pc
%{mingw64_libdir}/pkgconfig/gthread-2.0.pc
%{mingw64_datadir}/aclocal/glib-2.0.m4
%{mingw64_datadir}/aclocal/glib-gettext.m4
%{mingw64_datadir}/aclocal/gsettings.m4
%{mingw64_datadir}/gettext/its/
%{mingw64_datadir}/glib-2.0/

%files -n mingw64-glib2-static
%{mingw64_libdir}/libgio-2.0.a
%{mingw64_libdir}/libgirepository-2.0.a
%{mingw64_libdir}/libglib-2.0.a
%{mingw64_libdir}/libgmodule-2.0.a
%{mingw64_libdir}/libgobject-2.0.a
%{mingw64_libdir}/libgthread-2.0.a


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.87.3-1
- Prepare for Oreon 11 (RP1)
