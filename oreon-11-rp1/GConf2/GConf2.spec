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
Release:        49%{?dist}
Summary:        A process-transparent configuration system
License: LGPL-2.0-or-later AND GPL-2.0-or-later
SourceLicense: %{license} AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-2.0-or-later WITH Autoconf-exception-generic AND GPL-2.0-or-later WITH Libtool-exception AND GPL-1.0-or-later WITH Autoconf-exception-generic AND FSFULLRWD AND FSFULLR AND FSFUL AND FSFAP AND X11 AND LicenseRef-Fedora-Public-Domain
URL:     https://gitlab.gnome.org/Archive/gconf/
Source0:        https://download.gnome.org/sources/GConf/3.2/GConf-%{version}.tar.xz
Source1: macros.gconf2
Patch0: GConf-gettext.patch
Patch1: drop-spew.patch
Patch2: gconf-3.2.6-gconf-engine_key_is_writable.patch
Patch3: GConf-3.2.6-Use-gettext-0.21.patch
Patch99: workaround-crash.patch
Patch100: pkill-hack.patch
%if 0%{?defaults_service}
%endif
%if 0%{?defaults_service}
Requires: dbus
%endif
Requires: /usr/bin/pkill
Conflicts: GConf2-dbus
Provides: GConf2-gtk = 3.2.6-6
Obsoletes: GConf2-gtk < 3.2.6-6
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  python3-devel
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles GConf2-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%{?ldconfig}
if [ $1 -gt 1 ]; then
    if ! grep -q -F gconf.xml.system %{_sysconfdir}/gconf/2/path; then
        sed -i -e 's@xml:readwrite:$(HOME)/.gconf@&\n\n# Location for system-wide settings.\nxml:readonly:/etc/gconf/gconf.xml.system@' %{_sysconfdir}/gconf/2/path
    fi
fi
%ldconfig_postun
%files -f %{oreon_filedir}/main.list
%files -n GConf2-devel -f %{oreon_filedir}/GConf2-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.2.6-49
- Prepare for Oreon 11 (RP1)
