%global source0_hash 0013877c6bd23c2dbe42ad7c70a053d0e449be66736574e37867c49c5f905a4f

%{?mingw_package_header}

%global bin_version 3.0.0
# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-gtk3
# Drop Source2 on next update!
Version:        3.24.51
Release:        2%{?dist}
Summary:        MinGW Windows GTK+ library

License:        LGPL-2.0-or-later
URL:            http://www.gtk.org
Source0:        https://download.gnome.org/sources/gtk/%{release_version}/gtk-%{version}.tar.xz
# wine /usr/i686-w64-mingw32/sys-root/mingw/bin/gtk-query-immodules-3.0.exe | sed -e 's@Z:/usr/i686-w64-mingw32/sys-root/mingw@..@' -e 's@/usr/i686-w64-mingw32/sys-root/mingw@..@' > gtk.immodules
Source1:        gtk.immodules

BuildArch:      noarch

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ninja-build

BuildRequires:  mingw32-filesystem >= 98
BuildRequires:  mingw64-filesystem >= 98
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils

BuildRequires:  mingw32-atk
BuildRequires:  mingw64-atk
BuildRequires:  mingw32-cairo
BuildRequires:  mingw64-cairo
BuildRequires:  mingw32-gdk-pixbuf
BuildRequires:  mingw64-gdk-pixbuf
BuildRequires:  mingw32-gettext
BuildRequires:  mingw64-gettext
BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-glib2
BuildRequires:  mingw32-libepoxy
BuildRequires:  mingw64-libepoxy
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw32-pango
BuildRequires:  mingw64-pango
BuildRequires:  mingw32-pixman
BuildRequires:  mingw64-pixman
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-zlib

# Native one for msgfmt
BuildRequires:  gettext
# Native one for glib-genmarshal
BuildRequires:  glib2-devel
# Native one for gtk-update-icon-cache
BuildRequires:  gtk-update-icon-cache
# Native one for gdk-pixbuf-csource
BuildRequires:  gdk-pixbuf2-devel
# Native one for /usr/bin/perl
BuildRequires:  perl-interpreter

%description
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

This package contains the MinGW Windows cross compiled GTK+ 3 library.

%package -n mingw32-gtk3
Summary:        MinGW Windows GTK+ library
Requires:       mingw32-adwaita-icon-theme
# split out in a subpackage
Requires:       mingw32-gtk-update-icon-cache

%description -n mingw32-gtk3
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

This package contains the MinGW Windows cross compiled GTK+ 3 library.

%package -n mingw32-gtk-update-icon-cache
Summary: Icon theme caching utility

%description -n mingw32-gtk-update-icon-cache
GTK+ can use the cache files created by gtk-update-icon-cache to avoid a lot of
system call and disk seek overhead when the application starts. Since the
format of the cache files allows them to be mmap()ed shared between multiple
applications, the overall memory consumption is reduced as well.

This package contains the MinGW Windows cross compiled gtk-update-icon-cache.

%package -n mingw64-gtk3
Summary:        MinGW Windows GTK+ library
Requires:       mingw64-adwaita-icon-theme
# split out in a subpackage
Requires:       mingw64-gtk-update-icon-cache

%description -n mingw64-gtk3
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

This package contains the MinGW Windows cross compiled GTK+ 3 library.

%package -n mingw64-gtk-update-icon-cache
Summary: Icon theme caching utility

%description -n mingw64-gtk-update-icon-cache
GTK+ can use the cache files created by gtk-update-icon-cache to avoid a lot of
system call and disk seek overhead when the application starts. Since the
format of the cache files allows them to be mmap()ed shared between multiple
applications, the overall memory consumption is reduced as well.

This package contains the MinGW Windows cross compiled gtk-update-icon-cache.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n gtk-%{version}

%build
%mingw_meson -Dintrospection=false -Dbuiltin_immodules=no
%mingw_ninja

%install
%mingw_ninja_install

rm -f %{buildroot}/%{mingw32_libdir}/charset.alias
rm -f %{buildroot}/%{mingw64_libdir}/charset.alias

# Remove manpages which duplicate those in Fedora native.
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}

# Remove documentation too.
rm -rf %{buildroot}%{mingw32_datadir}/gtk-doc
rm -rf %{buildroot}%{mingw64_datadir}/gtk-doc

# Remove unneeded files
rm -f %{buildroot}%{mingw32_libdir}/*.def
rm -f %{buildroot}%{mingw64_libdir}/*.def

# Remove files used only for tests.
rm -f %{buildroot}%{mingw32_bindir}/libgtkreftestprivate-0.dll
rm -f %{buildroot}%{mingw64_bindir}/libgtkreftestprivate-0.dll
rm -f %{buildroot}%{mingw32_libdir}/libgtkreftestprivate.dll.a
rm -f %{buildroot}%{mingw64_libdir}/libgtkreftestprivate.dll.a

rm -f %{buildroot}%{mingw32_libdir}/*.la
rm -f %{buildroot}%{mingw64_libdir}/*.la
rm -f %{buildroot}%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/*.dll.a
rm -f %{buildroot}%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/*.dll.a
rm -f %{buildroot}%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/*.la
rm -f %{buildroot}%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/*.la

# Remove desktop files and corresponding icons as they aren't useful for win32
rm -f %{buildroot}%{mingw32_datadir}/applications/*.desktop
rm -f %{buildroot}%{mingw64_datadir}/applications/*.desktop
rm -f %{buildroot}%{mingw32_datadir}/icons/hicolor/*/apps/*.png
rm -f %{buildroot}%{mingw64_datadir}/icons/hicolor/*/apps/*.png

# Install the gtk.immodules file
mkdir -p %{buildroot}%{mingw32_sysconfdir}/gtk-3.0/
mkdir -p %{buildroot}%{mingw64_sysconfdir}/gtk-3.0/
install -m 0644 %{SOURCE1} %{buildroot}%{mingw32_sysconfdir}/gtk-3.0/
install -m 0644 %{SOURCE1} %{buildroot}%{mingw64_sysconfdir}/gtk-3.0/

%mingw_find_lang %{name} --all-name

%postun -n mingw32-gtk3
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{mingw32_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans -n mingw32-gtk3
/usr/bin/glib-compile-schemas %{mingw32_datadir}/glib-2.0/schemas &> /dev/null || :

%postun -n mingw64-gtk3
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{mingw64_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans -n mingw64-gtk3
/usr/bin/glib-compile-schemas %{mingw64_datadir}/glib-2.0/schemas &> /dev/null || :

%files -n mingw32-gtk3 -f mingw32-%{name}.lang
%license COPYING
%{mingw32_bindir}/gtk3-demo-application.exe
%{mingw32_bindir}/gtk3-demo.exe
%{mingw32_bindir}/gtk3-icon-browser.exe
%{mingw32_bindir}/gtk3-widget-factory.exe
%{mingw32_bindir}/gtk-builder-tool.exe
%{mingw32_bindir}/gtk-encode-symbolic-svg.exe
%{mingw32_bindir}/gtk-launch.exe
%{mingw32_bindir}/gtk-query-immodules-3.0.exe
%{mingw32_bindir}/gtk-query-settings.exe
%{mingw32_bindir}/libgdk-3-0.dll
%{mingw32_bindir}/libgailutil-3-0.dll
%{mingw32_bindir}/libgtk-3-0.dll
%{mingw32_sysconfdir}/gtk-3.0/
%{mingw32_includedir}/gtk-3.0/
%{mingw32_includedir}/gail-3.0/
%dir %{mingw32_libdir}/gtk-3.0
%dir %{mingw32_libdir}/gtk-3.0/%{bin_version}
%dir %{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules
%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/im-am-et.dll
%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/im-cedilla.dll
%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/im-cyrillic-translit.dll
%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/im-ime.dll
%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/im-inuktitut.dll
%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/im-ipa.dll
%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/im-multipress.dll
%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/im-thai.dll
%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/im-ti-er.dll
%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/im-ti-et.dll
%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/im-viqr.dll
%{mingw32_libdir}/libgailutil-3.dll.a
%{mingw32_libdir}/libgdk-3.dll.a
%{mingw32_libdir}/libgtk-3.dll.a
%{mingw32_libdir}/pkgconfig/gail-3.0.pc
%{mingw32_libdir}/pkgconfig/gdk-3.0.pc
%{mingw32_libdir}/pkgconfig/gdk-win32-3.0.pc
%{mingw32_libdir}/pkgconfig/gtk+-3.0.pc
%{mingw32_libdir}/pkgconfig/gtk+-win32-3.0.pc
%{mingw32_datadir}/aclocal/gtk-3.0.m4
%{mingw32_datadir}/gettext/
%{mingw32_datadir}/glib-2.0/schemas/org.gtk.Demo.gschema.xml
%{mingw32_datadir}/glib-2.0/schemas/org.gtk.exampleapp.gschema.xml
%{mingw32_datadir}/glib-2.0/schemas/org.gtk.Settings.ColorChooser.gschema.xml
%{mingw32_datadir}/glib-2.0/schemas/org.gtk.Settings.Debug.gschema.xml
%{mingw32_datadir}/glib-2.0/schemas/org.gtk.Settings.EmojiChooser.gschema.xml
%{mingw32_datadir}/glib-2.0/schemas/org.gtk.Settings.FileChooser.gschema.xml
%{mingw32_datadir}/gtk-3.0/
%{mingw32_datadir}/themes/*

%files -n mingw32-gtk-update-icon-cache
%license COPYING
%{mingw32_bindir}/gtk-update-icon-cache.exe

%files -n mingw64-gtk3 -f mingw64-%{name}.lang
%license COPYING
%{mingw64_bindir}/gtk3-demo-application.exe
%{mingw64_bindir}/gtk3-demo.exe
%{mingw64_bindir}/gtk3-icon-browser.exe
%{mingw64_bindir}/gtk3-widget-factory.exe
%{mingw64_bindir}/gtk-builder-tool.exe
%{mingw64_bindir}/gtk-encode-symbolic-svg.exe
%{mingw64_bindir}/gtk-launch.exe
%{mingw64_bindir}/gtk-query-immodules-3.0.exe
%{mingw64_bindir}/gtk-query-settings.exe
%{mingw64_bindir}/libgdk-3-0.dll
%{mingw64_bindir}/libgailutil-3-0.dll
%{mingw64_bindir}/libgtk-3-0.dll
%{mingw64_sysconfdir}/gtk-3.0/
%{mingw64_includedir}/gtk-3.0/
%{mingw64_includedir}/gail-3.0/
%dir %{mingw64_libdir}/gtk-3.0
%dir %{mingw64_libdir}/gtk-3.0/%{bin_version}
%dir %{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules
%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/im-am-et.dll
%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/im-cedilla.dll
%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/im-cyrillic-translit.dll
%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/im-ime.dll
%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/im-inuktitut.dll
%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/im-ipa.dll
%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/im-multipress.dll
%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/im-thai.dll
%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/im-ti-er.dll
%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/im-ti-et.dll
%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/im-viqr.dll
%{mingw64_libdir}/libgailutil-3.dll.a
%{mingw64_libdir}/libgdk-3.dll.a
%{mingw64_libdir}/libgtk-3.dll.a
%{mingw64_libdir}/pkgconfig/gail-3.0.pc
%{mingw64_libdir}/pkgconfig/gdk-3.0.pc
%{mingw64_libdir}/pkgconfig/gdk-win32-3.0.pc
%{mingw64_libdir}/pkgconfig/gtk+-3.0.pc
%{mingw64_libdir}/pkgconfig/gtk+-win32-3.0.pc
%{mingw64_datadir}/aclocal/gtk-3.0.m4
%{mingw64_datadir}/gettext/
%{mingw64_datadir}/glib-2.0/schemas/org.gtk.Demo.gschema.xml
%{mingw64_datadir}/glib-2.0/schemas/org.gtk.exampleapp.gschema.xml
%{mingw64_datadir}/glib-2.0/schemas/org.gtk.Settings.ColorChooser.gschema.xml
%{mingw64_datadir}/glib-2.0/schemas/org.gtk.Settings.Debug.gschema.xml
%{mingw64_datadir}/glib-2.0/schemas/org.gtk.Settings.EmojiChooser.gschema.xml
%{mingw64_datadir}/glib-2.0/schemas/org.gtk.Settings.FileChooser.gschema.xml
%{mingw64_datadir}/gtk-3.0/
%{mingw64_datadir}/themes/*

%files -n mingw64-gtk-update-icon-cache
%license COPYING
%{mingw64_bindir}/gtk-update-icon-cache.exe

%changelog
%autochangelog
