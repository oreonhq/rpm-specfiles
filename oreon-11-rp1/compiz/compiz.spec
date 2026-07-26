%global source0_hash e87018b2d6c9ab3da87d910b117a7ae35f64328eea485e6c2a532501b361144c

%bcond_with bootstrap

%global    core_plugins    blur clone cube decoration fade ini inotify minimize move place png regex resize rotate scale screenshot switcher water wobbly zoom fs obs commands wall annotate svg matecompat

# List of plugins passed to ./configure.  The order is important

%global    plugins         core,dbus,decoration,fade,minimize,move,obs,place,png,resize,scale,screenshot,svg,switcher,wall

Name:           compiz
# Automatically converted from old format: GPLv2+ and LGPLv2+ and MIT - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT
Version:        0.8.18
Release:        20%{?dist}
Epoch:          1
Summary:        OpenGL window and compositing manager

URL:            https://gitlab.com/compiz/compiz-core
Source0:        %{url}/-/archive/v%{version}/compiz-core-v%{version}.tar.bz2

# fedora specific
Patch0:        compiz-0.8.18-fedora-logo.patch
# FTBFS fix, this can be dropped with compiz > 0.8.18
Patch1:        compiz-0.8.18-rsvg2-2.52-fix.patch
# https://gitlab.com/compiz/compiz-core/-/merge_requests/177
Patch2:        compiz-0.8.18-gcc-14-fix.patch
# https://gitlab.com/compiz/compiz-core/-/commit/10050cb679a582fd9beb921c3e88288e10613987
Patch3:        compiz-0.8.18-libxml-2.12-fix.patch

BuildRequires: libX11-devel
BuildRequires: libdrm-devel
BuildRequires: libXcursor-devel
BuildRequires: libXfixes-devel
BuildRequires: libXrandr-devel
BuildRequires: libXrender-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXdamage-devel
BuildRequires: libXext-devel
BuildRequires: libXt-devel
BuildRequires: libSM-devel
BuildRequires: libICE-devel
BuildRequires: libXmu-devel
BuildRequires: desktop-file-utils
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: librsvg2-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: fuse-devel
BuildRequires: cairo-devel
BuildRequires: libtool
BuildRequires: libjpeg-turbo-devel
BuildRequires: libxslt-devel
BuildRequires: marco-devel
BuildRequires: glib2-devel
BuildRequires: libwnck3-devel
%if %{without bootstrap}
BuildRequires: libcompizconfig-devel
%endif
BuildRequires: dbus-devel
BuildRequires: dbus-glib-devel
BuildRequires: automake
BuildRequires: make

Requires:      glx-utils

# obsolete old subpackges
Obsoletes: %{name}-xfce < %{epoch}:%{version}-%{release}
Obsoletes: %{name}-lxde < %{epoch}:%{version}-%{release}
Obsoletes: %{name}-mate < %{epoch}:%{version}-%{release}
%if 0%{?fedora} < 25
Provides:  compiz-mate = %{epoch}:%{version}-%{release}
%endif

%description
Compiz is one of the first OpenGL-accelerated compositing window
managers for the X Window System. The integration allows it to perform
compositing effects in window management, such as a minimization
effect and a cube work space. Compiz is an OpenGL compositing manager
that use Compiz use EXT_texture_from_pixmap OpenGL extension for
binding redirected top-level windows to texture objects.

%package devel
Summary: Development packages for compiz
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: pkgconfig
Requires: libXcomposite-devel libXfixes-devel libXdamage-devel libXrandr-devel
Requires: libXinerama-devel libICE-devel libSM-devel libxml2-devel
Requires: libxslt-devel startup-notification-devel

%description devel
The compiz-devel package includes the header files,
and developer docs for the compiz package.
Install compiz-devel if you want to develop plugins for the compiz
windows and compositing manager.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n compiz-core-v%{version}

%build
./autogen.sh
%configure \
    --with-gtk=3.0 \
    --enable-librsvg \
    --enable-gtk \
    --enable-marco \
    --enable-menu-entries \
    --with-default-plugins=%{plugins}

make %{?_smp_mflags} V=1

%install
%{make_install}

desktop-file-install                              \
    --delete-original                             \
    --dir=%{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/*.desktop

find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

%find_lang %{name}

cat %{name}.lang > core-files.txt

for f in %{core_plugins}; do
  echo %{_libdir}/compiz/lib$f.so
  echo %{_datadir}/compiz/$f.xml
done >> core-files.txt

# placeholder for local icons
mkdir -p %{buildroot}%{_datadir}/compiz/icons/hicolor/{scalable/{apps,\
categories},22x22/{categories,devices,mimetypes}}

%ldconfig_scriptlets

%files -f core-files.txt
%doc AUTHORS COPYING.GPL COPYING.LGPL README.md TODO NEWS
%{_bindir}/compiz
%{_bindir}/compiz-decorator
%{_bindir}/gtk-window-decorator
%{_libdir}/libdecoration.so.*
%dir %{_libdir}/compiz
%{_libdir}/compiz/libdbus.so
%{_libdir}/compiz/libglib.so
%dir %{_datadir}/compiz
%{_datadir}/compiz/*.png
%{_datadir}/compiz/icons
%{_datadir}/compiz/core.xml
%{_datadir}/compiz/dbus.xml
%{_datadir}/compiz/glib.xml
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/applications/compiz.desktop
%{_datadir}/applications/compiz-start.desktop
%{_datadir}/glib-2.0/schemas/org.compiz-0.gwd.gschema.xml

%files devel
%{_libdir}/pkgconfig/compiz.pc
%{_libdir}/pkgconfig/libdecoration.pc
%{_libdir}/pkgconfig/compiz-cube.pc
%{_libdir}/pkgconfig/compiz-scale.pc
%{_includedir}/compiz/
%{_libdir}/libdecoration.so

%changelog
%autochangelog
