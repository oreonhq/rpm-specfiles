%global source0_hash b2c63916866485793b87398266dd7778548c1734923c272a94d84ee011b6f7a4

%global _default_patch_fuzz 2

%global po_package libgnome-2.0

%global schemalist \\\
	desktop_gnome_accessibility_keyboard \\\
	desktop_gnome_accessibility_startup \\\
	desktop_gnome_applications_at_mobility \\\
	desktop_gnome_applications_at_visual \\\
	desktop_gnome_applications_browser \\\
	desktop_gnome_applications_office \\\
	desktop_gnome_applications_terminal  \\\
	desktop_gnome_applications_window_manager \\\
	desktop_gnome_background \\\
	desktop_gnome_file_views \\\
	desktop_gnome_interface \\\
	desktop_gnome_lockdown \\\
	desktop_gnome_peripherals_keyboard \\\
	desktop_gnome_peripherals_monitor \\\
	desktop_gnome_peripherals_mouse \\\
	desktop_gnome_sound \\\
	desktop_gnome_thumbnail_cache \\\
	desktop_gnome_thumbnailers \\\
	desktop_gnome_typing_break

Summary: GNOME base library
Name: libgnome
Version: 2.32.1
Release: 35%{?dist}
URL: http://www.gnome.org
Source0: http://download.gnome.org/sources/libgnome/2.32/%{name}-%{version}.tar.bz2
Source1: desktop_gnome_peripherals_monitor.schemas
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+

# Added to avoid the warning messages about utmp group, bug #24171
# fixme, just libzvt?
Requires(pre): utempter
Requires(post): GConf2
Requires(pre): GConf2
Requires(preun): GConf2

BuildRequires: zlib-devel
BuildRequires: glib2-devel 
BuildRequires:  libbonobo-devel 
BuildRequires:  GConf2-devel 
BuildRequires:  gnome-vfs2-devel 
BuildRequires:  libxml2-devel 
BuildRequires:  ORBit2-devel 
BuildRequires:  libxslt-devel 
BuildRequires:  libcanberra-devel
BuildRequires:  intltool
BuildRequires:  gnome-common autoconf automake libtool
BuildRequires:  gettext
BuildRequires:  popt-devel
BuildRequires:  gtk-doc
BuildRequires: make

# make sure to update gnome-desktop requires when changing below patch
Patch1: default-background.patch

# https://bugzilla.gnome.org/show_bug.cgi?id=606436
Patch2: libgnome-2.11.1-scoreloc.patch

Patch3: libgnome-2.7.2-default-cursor.patch
Patch4: libgnome-2.8.0-default-browser.patch
Patch6: libgnome-2.19.1-default-settings.patch
Patch7: libgnome-2.22.0-default-sound-effects.patch

# backport from upstream svn
Patch8: im-setting.patch

Patch9: libgnome-2.24.1-default-noblink.patch

Patch10: 0001-Don-t-use-G_DISABLE_DEPRECATED.patch
Patch11: 0001-gnome-config.h-Fix-invalid-UTF-8-in-header.patch

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The libgnome package includes
non-GUI-related libraries that are needed to run GNOME. The libgnomeui
package contains X11-dependent GNOME library features.

%package devel
Summary: Libraries and headers for libgnome
Requires: %{name} = %{version}-%{release}

%description devel
You should install the libgnome-devel package if you would like to
compile GNOME applications. You do not need to install libgnome-devel
if you just want to use the GNOME desktop environment.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P1 -p1 -b .default-background
%patch -P2 -p1 -b .scoreloc
%patch -P3 -p1 -b .default-cursor
%patch -P4 -p1 -b .default-browser
%patch -P6 -p1 -b .default-settings
%patch -P7 -p1 -b .default-sound-effects
%patch -P8 -p1 -b .im-setting
%patch -P9 -p1 -b .default-noblink
%patch -P10 -p1
%patch -P11 -p1

%build
autoreconf -vfi
%configure --disable-gtk-doc --disable-static --disable-esd

make %{?_smp_mflags}

# strip unneeded translations from .mo files
# ideally intltool (ha!) would do that for us
# http://bugzilla.gnome.org/show_bug.cgi?id=474987
cd po
grep -v ".*[.]desktop[.]in[.]in$\|.*[.]server[.]in[.]in$" POTFILES.in > POTFILES.keep
mv POTFILES.keep POTFILES.in
intltool-update --pot
sed -ie 's|POT-Creation-Date.*|POT-Creation-Date: 2008-10-01 00:00-0400\\n"|g' %{po_package}.pot
for p in *.po; do
  msgmerge $p %{po_package}.pot > $p.out
  msgfmt -o `basename $p .po`.gmo $p.out
done

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas/

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

for serverfile in $RPM_BUILD_ROOT%{_libdir}/bonobo/servers/*.server; do
    sed -i -e 's|location *= *"/usr/lib\(64\)*/|location="/usr/$LIB/|' $serverfile
done

# http://bugzilla.gnome.org/show_bug.cgi?id=477846
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties
rm -rf $RPM_BUILD_ROOT%{_datadir}/pixmaps

%find_lang %{po_package}

%post
%{?ldconfig}
%gconf_schema_upgrade %{schemalist}

%pre
%gconf_schema_prepare %{schemalist}

%preun
%gconf_schema_remove %{schemalist}

%ldconfig_postun

%files -f %{po_package}.lang
%doc AUTHORS COPYING.LIB NEWS README
%{_bindir}/*
%{_libdir}/lib*.so.*
%{_libdir}/bonobo/monikers/*
%{_libdir}/bonobo/servers/*
%{_mandir}/man7/*
%{_sysconfdir}/gconf/schemas/*.schemas
%{_sysconfdir}/sound

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
# as per guidelines own this instead Requires:gtk-doc 
%{_datadir}/gtk-doc

%changelog
%autochangelog
