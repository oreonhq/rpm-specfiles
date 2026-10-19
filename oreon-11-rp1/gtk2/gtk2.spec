%global source0_hash ac2ac757f5942d318a311a54b0c80b5ef295f299c2a73c632f6bfb1ff49cc6da
%global _changelog_trimtime %(date +%s -d "1 year ago")
%define glib2_base_version 2.28.0
%define glib2_version %{glib2_base_version}-1
%define pango_base_version 1.20.0
%define pango_version %{pango_base_version}-1
%define atk_base_version 1.29.4
%define atk_version %{atk_base_version}-2
%define cairo_base_version 1.6.0
%define cairo_version %{cairo_base_version}-1
%define xrandr_version 1.2.99.4-2
%define gobject_introspection_version 0.9.3
%define gir_repository_version 0.6.5-5
%define bin_version 2.10.0
%global __provides_exclude_from ^%{_libdir}/gtk-2.0
Summary:        GTK+ graphical user interface library
Name: gtk2
Version: 2.24.33
Release:        1%{?dist}
License: LicenseRef-Callaway-LGPLv2+
URL: http://www.gtk.org
Source0:        http://download.gnome.org/sources/gtk+/2.24/gtk+-%{version}.tar.xz
Source2: update-gtk-immodules
Source3: im-cedilla.conf
Source4: update-gtk-immodules.1
Patch2: icon-padding.patch
Patch8: tooltip-positioning.patch
Patch15: window-dragging.patch
Patch16: gtk2-c99.patch
Patch17: gtk2-c89.patch
Patch18: gtk2-c89-2.patch
Patch19: gtk2-c89-3.patch
Patch20: gtk2-c89-4.patch
Patch21: gtk2-c89-5.patch
Patch22: gtk2-c89-6.patch
Conflicts: gtk2-engines < 2.7.4-7
Conflicts: libgnomeui < 2.15.1cvs20060505-2
Conflicts: redhat-artwork < 0.243-1
Provides: gail = %{version}-%{release}
Obsoletes: gail < 2.13.0-1
Requires: hicolor-icon-theme
Requires: gtk-update-icon-cache
Requires: glib2 >= %{glib2_version}
Requires: atk >= %{atk_version}
Requires: pango >= %{pango_version}
Requires(post): libtiff >= 3.6.1
Requires: libXrandr >= %{xrandr_version}
Recommends: (adwaita-gtk2-theme if gnome-shell)
Recommends: libcanberra-gtk2%{?_isa}
Recommends: (ibus-gtk2 if ibus)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cups-devel
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  python3-devel
# /oreon:deps
%description
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

%package immodules
Summary: Input methods for GTK+
Requires: gtk2 = %{version}-%{release}
Requires: gtk-immodules-imsettings
%description immodules
The gtk2-immodules package contains standalone input methods that are shipped
as part of GTK+.

%package -n gtk-immodules-imsettings
Summary: IMSettings config files for GTK+ input methods
Conflicts: gtk2 < 2.24.33-12
BuildArch: noarch
%description -n gtk-immodules-imsettings
The gtk-immodules-imsettings package contains IMSettings configuration for the
standalone input methods that are shipped as part of GTK+.

%package immodule-xim
Summary: XIM support for GTK+
Requires: gtk2 = %{version}-%{release}
%description immodule-xim
The gtk2-immodule-xim package contains XIM support for GTK+.

%package devel
Summary: Development files for GTK+
Requires: gtk2 = %{version}-%{release}
Requires: pango-devel >= %{pango_version}
Requires: atk-devel >= %{atk_version}
Requires: glib2-devel >= %{glib2_version}
Requires: gdk-pixbuf2-devel
Requires: cairo-devel >= %{cairo_version}
Requires: libX11-devel, libXcursor-devel, libXinerama-devel
Requires: libXext-devel, libXi-devel, libXrandr-devel
Requires: libXfixes-devel, libXcomposite-devel
Requires: pkgconfig
Provides: gail-devel = %{version}-%{release}
Obsoletes: gail-devel < 2.13.0-1
%description devel
This package contains the libraries and header files that are needed
for writing applications with the GTK+ widget toolkit. If you plan
to develop applications with GTK+, consider installing the gtk2-devel-docs
package.

%package devel-docs
Summary: Developer documentation for GTK+
Requires: gtk2 = %{version}-%{release}
%description devel-docs
This package contains developer documentation for the GTK+ widget toolkit.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir gtk+-%{version}
%oreon_prep
%build

export CFLAGS='%optflags -fno-strict-aliasing -std=gnu99'
(if ! test -x configure; then NOCONFIGURE=1 ./autogen.sh; CONFIGFLAGS=--enable-gtk-doc; fi;
 %configure $CONFIGFLAGS \
	--enable-man		\
	--with-xinput=xfree	\
	--enable-debug		\
)
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
make %{?_smp_mflags}
awk '/^Overview of Changes/ { seen+=1 }
{ if (seen < 2) print }
{ if (seen == 2) { print "For older news, see http://git.gnome.org/cgit/gtk+/plain/NEWS"; exit } }' NEWS > tmp; mv tmp NEWS
%install
case "%{_host}" in
  *linux) host="%{_host}-gnu"
  ;;
  *) host="%{_host}"
  ;;
esac
host=`echo $host | sed "s/^ppc/powerpc/"`
compile_host=`grep 'host_triplet =' gtk/Makefile | sed "s/.* = //"`
if test "x$compile_host" != "x$host" ; then
  echo 1>&2 "Host mismatch: compile='$compile_host', spec file='$host'" && exit 1
fi
make install DESTDIR=$RPM_BUILD_ROOT        \
             RUN_QUERY_IMMODULES_TEST=false
echo ".so man1/gtk-query-immodules-2.0.1" > $RPM_BUILD_ROOT%{_mandir}/man1/gtk-query-immodules-2.0-%{__isa_bits}.1
gzip -c %{SOURCE4} > $RPM_BUILD_ROOT%{_mandir}/man1/update-gtk-immodules.1.gz
%find_lang gtk20
%find_lang gtk20-properties
mkdir -p tmpdocs
cp -aR docs/tutorial/html tmpdocs/tutorial
cp -aR docs/faq/html tmpdocs/faq
for dir in examples/* ; do
  if [ -d $dir ] ; then
     mkdir -p tmpdocs/$dir
     for file in $dir/* ; do
       install -m 0644 $file tmpdocs/$dir
     done
  fi
done
case "$host" in
  alpha*|ia64*|ppc64*|powerpc64*|s390x*|x86_64*|aarch64*|mips64*)
   mv $RPM_BUILD_ROOT%{_bindir}/gtk-query-immodules-2.0 $RPM_BUILD_ROOT%{_bindir}/gtk-query-immodules-2.0-64
   ;;
  *)
   mv $RPM_BUILD_ROOT%{_bindir}/gtk-query-immodules-2.0 $RPM_BUILD_ROOT%{_bindir}/gtk-query-immodules-2.0-32
   ;;
esac
cp %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/update-gtk-immodules
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinput.d
cp %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinput.d
%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -pn -i %{__python3} $RPM_BUILD_ROOT%{_bindir}/gtk-builder-convert
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/*.la
rm $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/%{bin_version}/*/*.la
rm $RPM_BUILD_ROOT%{_bindir}/gtk-update-icon-cache
rm $RPM_BUILD_ROOT%{_mandir}/man1/gtk-update-icon-cache.1*
touch $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/%{bin_version}/immodules.cache
mkdir -p $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/modules
mkdir -p $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/immodules
mkdir -p $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/%{bin_version}/filesystems
%transfiletriggerin -- %{_libdir}/gtk-2.0/immodules/ %{_libdir}/gtk-2.0/%{bin_version}/immodules/
%{_bindir}/gtk-query-immodules-2.0-%{__isa_bits} --update-cache
%transfiletriggerpostun -- %{_libdir}/gtk-2.0/immodules/ %{_libdir}/gtk-2.0/%{bin_version}/immodules/
%{_bindir}/gtk-query-immodules-2.0-%{__isa_bits} --update-cache
%ldconfig_scriptlets
%oreon_autofiles gtk-immodules-imsettings usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gtk2-immodules -f %{oreon_filedir}/gtk2-immodules.list
%files -n gtk-immodules-imsettings -f %{oreon_filedir}/gtk-immodules-imsettings.list
%files -n gtk2-immodule-xim -f %{oreon_filedir}/gtk2-immodule-xim.list
%files -n gtk2-devel -f %{oreon_filedir}/gtk2-devel.list
%files -n gtk2-devel-docs -f %{oreon_filedir}/gtk2-devel-docs.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.24.33-25
- Prepare for Oreon 11 (RP1)
