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
Summary:        GNOME base library
Name: libgnome
Version: 2.32.1
Release:        1%{?dist}
URL: http://www.gnome.org
Source0:        http://download.gnome.org/sources/libgnome/2.32/%{name}-%{version}.tar.bz2
Source1: desktop_gnome_peripherals_monitor.schemas
License: LicenseRef-Callaway-LGPLv2+
Requires(pre): utempter
Requires(post): GConf2
Requires(pre): GConf2
Requires(preun): GConf2
Patch1: default-background.patch
Patch2: libgnome-2.11.1-scoreloc.patch
Patch3: libgnome-2.7.2-default-cursor.patch
Patch4: libgnome-2.8.0-default-browser.patch
Patch6: libgnome-2.19.1-default-settings.patch
Patch7: libgnome-2.22.0-default-sound-effects.patch
Patch8: im-setting.patch
Patch9: libgnome-2.24.1-default-noblink.patch
Patch10: 0001-Don-t-use-G_DISABLE_DEPRECATED.patch
Patch11: 0001-gnome-config.h-Fix-invalid-UTF-8-in-header.patch
# oreon:deps
BuildRequires:  GConf2-devel
BuildRequires:  ORBit2-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gnome-common
BuildRequires:  gnome-vfs2-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libbonobo-devel
BuildRequires:  libcanberra-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  make
BuildRequires:  popt-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties
rm -rf $RPM_BUILD_ROOT%{_datadir}/pixmaps
%find_lang %{po_package}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%{?ldconfig}
%gconf_schema_upgrade %{schemalist}
%pre

%gconf_schema_prepare %{schemalist}
%preun

%gconf_schema_remove %{schemalist}
%ldconfig_postun
%files -f %{oreon_filedir}/main.list
%files -n libgnome-devel -f %{oreon_filedir}/libgnome-devel.list

%changelog

%autochangelog
