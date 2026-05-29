%global source0_hash 1912b91803ab09a5eed34d364bf09fe3a2a9c96751fde03a4e0cfa51a04d784c

%define libxml2_version 2.4.12
%define glib2_version 2.25.9
%define dbus_version 1.0.1
%define dbus_glib_version 0.74

%if !0%{?flatpak}
%define defaults_service 1
%endif

Name:    GConf2
Version: 3.2.6
Release: 49%{?dist}
Summary: A process-transparent configuration system
# COPYING:                                  GPL-2.0 text
# defaults/gconf-defaults-main.c:           GPL-2.0-or-later
# gsettings/gconfsettingsbackend-module.c:  LGPL-2.0-or-later
## Unbundled and not in any binary package
# aclocal.m4:                   FSFULLRWD AND FSFULLR AND
#                               GPL-2.0-or-later WITH Libtool-exception AND
#                               GPL-2.0-or-later WITH Autoconf-exception-generic AND
#                               GPL-1.0-or-later WITH Autoconf-exception-generic
# config.guess:                 GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# config.sub:                   GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# configure:                    FSFUL AND GPL-2.0-or-later WITH Libtool-exception
# depcomp:                      GPL-2.0-or-later WITH Autoconf-exception-generic
# gsettings/Makefile.in:        FSFULLRWD
# install-sh:                   X11 AND LicenseRef-Fedora-Public-Domain
# ltmain.sh:                    GPL-2.0-or-later WITH Libtool-exception
# missing:                      GPL-2.0-or-later WITH Autoconf-exception-generic
# po/Makefile.in.in:            "This file may be copied and used freely without restrictions."
## Not used at all
# INSTALL:                      FSFAP
License: LGPL-2.0-or-later AND GPL-2.0-or-later
SourceLicense: %{license} AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-2.0-or-later WITH Autoconf-exception-generic AND GPL-2.0-or-later WITH Libtool-exception AND GPL-1.0-or-later WITH Autoconf-exception-generic AND FSFULLRWD AND FSFULLR AND FSFUL AND FSFAP AND X11 AND LicenseRef-Fedora-Public-Domain
URL:     https://gitlab.gnome.org/Archive/gconf/
Source0:        https://download.gnome.org/sources/GConf/3.2/GConf-3.2.6.tar.xz
Source1: macros.gconf2

# http://bugzilla.gnome.org/show_bug.cgi?id=568845
Patch0: GConf-gettext.patch

# https://bugzilla.gnome.org/show_bug.cgi?id=671490
Patch1: drop-spew.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1197773
Patch2: gconf-3.2.6-gconf-engine_key_is_writable.patch

# Since gettext 0.25, one needs to execute autopoint (excplicitly or implictly
# by autoreconf) and that requires pinning to a version with
# AM_GNU_GETTEXT_VERSION() macro in configure.ac, bug #2366708.
# gettext 0.21 is available since EPEL9.
Patch3: GConf-3.2.6-Use-gettext-0.21.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=755992
Patch99: workaround-crash.patch
Patch100: pkill-hack.patch

BuildRequires: autoconf >= 2.60
BuildRequires: automake >= 1.9
BuildRequires: libtool
BuildRequires: gettext-devel >= 0.21
BuildRequires: gtk-doc >= 0.9
BuildRequires: intltool
BuildRequires: make
BuildRequires: pkgconfig(dbus-glib-1) >= 0.8
BuildRequires: pkgconfig(gobject-introspection-1.0) >= 0.6.7
BuildRequires: pkgconfig(libxml-2.0) >= %{libxml2_version}
%if 0%{?defaults_service}
BuildRequires: pkgconfig(polkit-gobject-1) >= 0.92
%endif
# we need to do python shebang mangling using pathfix.py
BuildRequires: python3-devel

%if 0%{?defaults_service}
Requires: dbus
%endif
# for patch100
Requires: /usr/bin/pkill
Conflicts: GConf2-dbus

Provides: GConf2-gtk = 3.2.6-6
Obsoletes: GConf2-gtk < 3.2.6-6

%description
GConf is a process-transparent configuration database API used to
store user preferences. It has pluggable backends and features to
support workgroup administration.

%package devel
Summary: Headers and libraries for GConf development
Requires: %{name}%{?_isa} = %{version}-%{release}
Conflicts: GConf2-dbus-devel

%description devel
GConf development package. Contains files needed for doing
development using GConf.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n GConf-%{version}
# Remove bundled and generated files
rm ABOUT-NLS aclocal.m4 backends/Makefile.in config.guess config.h.in \
    config.sub configure defaults/Makefile.in depcomp \
    doc/gconf/Makefile.in doc/Makefile.in examples/Makefile.in \
    gconf/Makefile.in gsettings/Makefile.in gtk-doc.make INSTALL install-sh \
    intltool-extract.in intltool-merge.in intltool-update.in ltmain.sh \
    Makefile.in missing po/Makefile.in.in tests/Makefile.in

%build
autoreconf -Im4 --force --install

%configure --disable-static \
      %{?defaults_service:--enable-defaults-service} \
      %{!?defaults_service:--disable-defaults-service} \
      --disable-orbit --without-openldap --disable-gsettings-backend

# drop unneeded direct library deps with --as-needed
# libtool doesn't make this easy, so we do it the hard way
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' -e 's/    if test "$export_dynamic" = yes && test -n "$export_dynamic_flag_spec"; then/      func_append compile_command " -Wl,-O1,--as-needed"\n      func_append finalize_command " -Wl,-O1,--as-needed"\n\0/' libtool

%make_build

%install
%make_install

mkdir -p %{buildroot}%{_sysconfdir}/gconf/schemas
mkdir -p %{buildroot}%{_sysconfdir}/gconf/gconf.xml.system
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d/
mkdir -p %{buildroot}%{_localstatedir}/lib/rpm-state/gconf
mkdir -p %{buildroot}%{_datadir}/GConf/gsettings

install -p -m 644 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/macros.d/

find %{buildroot} -name "*.la" -type f -delete

mkdir -p %{buildroot}%{_datadir}/GConf/gsettings

%find_lang %name

%post
%{?ldconfig}

if [ $1 -gt 1 ]; then
    if ! grep -q -F gconf.xml.system %{_sysconfdir}/gconf/2/path; then
        sed -i -e 's@xml:readwrite:$(HOME)/.gconf@&\n\n# Location for system-wide settings.\nxml:readonly:/etc/gconf/gconf.xml.system@' %{_sysconfdir}/gconf/2/path
    fi
fi

%ldconfig_postun

%files -f %{name}.lang
%license COPYING
%doc NEWS README
%config(noreplace) %{_sysconfdir}/gconf/2/path
%dir %{_sysconfdir}/gconf
%dir %{_sysconfdir}/gconf/2
%dir %{_sysconfdir}/gconf/gconf.xml.defaults
%dir %{_sysconfdir}/gconf/gconf.xml.mandatory
%dir %{_sysconfdir}/gconf/gconf.xml.system
%dir %{_sysconfdir}/gconf/schemas
%{_bindir}/gconf-merge-tree
%{_bindir}/gconftool-2
%{_libexecdir}/gconfd-2
%{_libdir}/libgconf-2.so.4{,.*}
%{_libdir}/GConf/2/*.so
%dir %{_datadir}/sgml
%{_datadir}/sgml/gconf
%{_datadir}/GConf
%{_mandir}/man1/gconftool-2.*
%dir %{_libdir}/GConf
%dir %{_libdir}/GConf/2
%{_rpmconfigdir}/macros.d/macros.gconf2
%if 0%{?defaults_service}
%{_sysconfdir}/dbus-1/system.d/org.gnome.GConf.Defaults.conf
%{_libexecdir}/gconf-defaults-mechanism
%{_datadir}/polkit-1/actions/org.gnome.gconf.defaults.policy
%{_datadir}/dbus-1/system-services/org.gnome.GConf.Defaults.service
%endif
%{_datadir}/dbus-1/services/org.gnome.GConf.service
%{_localstatedir}/lib/rpm-state/gconf/
%{_libdir}/girepository-1.0

%files devel
%{_libdir}/libgconf-2.so
%{_includedir}/gconf
%{_datadir}/aclocal/gconf-2.m4
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/gconf
%{_libdir}/pkgconfig/gconf-2.0.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GConf-2.0.gir

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.2.6-49
- Prepare for Oreon 11 (RP1)
