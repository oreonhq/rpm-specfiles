%global source0_hash 7fc2cc40e1699bf706b5cfcf0255650fc4623b99edbc72c5ad026cea2587a3d6
%undefine __cmake_in_source_build
%global _changelog_trimtime %(date +%s -d "1 year ago")
%global _python_bytecompile_extra 0
%global enable_installed_tests 0
%global tnef_support 0
%define glib2_version 2.66
%define gtk3_version 3.22
%define gnome_autoar_version 0.1.1
%define gnome_desktop_version 2.91.3
%define intltool_version 0.35.5
%define libgweather_version 3.91
%define geocode_glib_version 3.26.3
%define sqlite_version 3.7.17
%define libsoup_version 3.1.1
%define webkit2gtk_version 2.34.0
%define last_anjal_version 0.3.2-3
%define last_libgal2_version 2:2.5.3-2
%define last_evo_nm_version 3.5.0
%define last_evo_perl_version 3.21.90
%define ldap_support 1
%define libnotify_support 1
%define libpst_support 1
%{!?with_docs: %global with_docs 1}
%if 0%{?flatpak}
%global with_docs 0
%endif
%define evo_plugin_dir %{_libdir}/evolution/plugins
%global major_minor_version %(echo %{version} | cut -d "." -f 1-2)
Name: evolution
Version: 3.62.0
Release:        1%{?dist}
Summary:        Mail and calendar client for GNOME
License: GPL-2.0-or-later AND GFDL-1.3-or-later
URL: https://gitlab.gnome.org/GNOME/evolution/-/wikis/home
Source0:        http://download.gnome.org/sources/%{name}/%{major_minor_version}/%{name}-%{version}.tar.xz
Source1: flatpak-evolution-fix-service-names.sh
Source2: flatpak-evolution-wrapper.sh.in
Patch100: configurable-dbus-prefix.patch
Provides: bundled(libgnomecanvas) = 2.30.0
Obsoletes: anjal <= %{last_anjal_version}
Obsoletes: libgal2 <= %{last_libgal2_version}
Obsoletes: evolution-NetworkManager < %{last_evo_nm_version}
Obsoletes: evolution-perl < %{last_evo_perl_version}
Obsoletes: evolution-rss < 3.45.2
%if !%{enable_installed_tests}
Obsoletes: evolution-tests <= 3.31.1
%endif
%global eds_version %{version}
%if ! 0%{?flatpak}
Requires: %{_bindir}/killall
Requires: gvfs
%endif
Requires: evolution-data-server >= %{eds_version}
Requires: gspell
Requires: highlight
Requires: %{name}-langpacks = %{version}-%{release}
%if ! 0%{?flatpak}
%endif
%if %{ldap_support}
%endif
%if %{libnotify_support}
%endif
%if %{libpst_support}
%endif
# oreon:deps
BuildRequires:  /usr/bin/killall
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  highlight
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  openldap-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(camel-1.2)
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(gail-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gnome-autoar-0)
BuildRequires:  pkgconfig(gnome-autoar-gtk-0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gspell-1)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gweather4)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libcmark)
BuildRequires:  pkgconfig(libebackend-1.2)
BuildRequires:  pkgconfig(libebook-1.2)
BuildRequires:  pkgconfig(libecal-2.0)
BuildRequires:  pkgconfig(libedataserver-1.2)
BuildRequires:  pkgconfig(libedataserverui-1.2)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpst)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libytnef)
BuildRequires:  pkgconfig(nspr)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(webkit2gtk-web-extension-4.1)
BuildRequires:  yelp-tools
# /oreon:deps
%description
Evolution is the GNOME mailer, calendar, contact manager and
communications tool.  The components which make up Evolution
are tightly integrated with one another and act as a seamless
personal information-management tool.

%package devel
Summary: Development files for building against %{name}
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig(camel-1.2) >= %{eds_version}
Requires: pkgconfig(enchant-2)
Requires: pkgconfig(gtk+-3.0) >= %{gtk3_version}
Requires: pkgconfig(gspell-1)
Requires: pkgconfig(gweather4) >= %{libgweather_version}
Requires: pkgconfig(libebackend-1.2) >= %{eds_version}
Requires: pkgconfig(libebook-1.2) >= %{eds_version}
Requires: pkgconfig(libecal-2.0) >= %{eds_version}
Requires: pkgconfig(libedataserver-1.2) >= %{eds_version}
Requires: pkgconfig(libsoup-3.0) >= %{libsoup_version}
Requires: pkgconfig(libxml-2.0)
Obsoletes: libgal2-devel <= %{last_libgal2_version}
%description devel
Development files needed for building things which link against %{name}.

%package langpacks
Summary: Translations for %{name}
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
%description langpacks
This package contains translations for %{name}.

%package bogofilter
Summary: Bogofilter plugin for Evolution
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: bogofilter
%description bogofilter
This package contains the plugin to filter junk mail using Bogofilter.

%package spamassassin
Summary: SpamAssassin plugin for Evolution
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: spamassassin
%description spamassassin
This package contains the plugin to filter junk mail using SpamAssassin.

%if %{libpst_support}
%package pst
Summary: PST importer plugin for Evolution
Requires: %{name}%{?_isa} = %{version}-%{release}
%description pst
This package contains the plugin to import Microsoft Personal Storage Table
(PST) files used by Microsoft Outlook and Microsoft Exchange.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -S gendiff -N

# General patches
# %%autopatch -p1 -m 0 -M 99

# Flatpak-specific patches
%if 0%{?flatpak}
%autopatch -p1 -m 100 -M 199
%endif

# Remove the welcome email from Novell
for inbox in src/mail/default/*/Inbox; do
  echo -n "" > $inbox
done

%if 0%{?flatpak}
mv data/org.gnome.Evolution.desktop.in.in data/org.gnome.Evolution.desktop.in.i
cat data/org.gnome.Evolution.desktop.in.i | sed -e "s/Icon=evolution/Icon=org.gnome.Evolution/" >data/org.gnome.Evolution.desktop.in.in
%endif

%build

%if %{ldap_support}
%define ldap_flags -DWITH_OPENLDAP=ON
%else
%define ldap_flags -DWITH_OPENLDAP=OFF
%endif
%define ssl_flags -DENABLE_SMIME=ON
if ! pkg-config --exists nss; then
  echo "Unable to find suitable version of mozilla nss to use!"
  exit 1
fi
%define gtkdoc_flags -DENABLE_GTK_DOC=OFF -DWITH_HELP=OFF
%define tests_flags -DENABLE_INSTALLED_TESTS=OFF
%global tnef_flags -DENABLE_YTNEF=ON
%if 0%{?flatpak}
%global temp_home "-DTEMP_HOME=1"
%else
%global temp_home ""
%endif
CFLAGS="$RPM_OPT_FLAGS -fPIC -DLDAP_DEPRECATED -Wno-sign-compare -Wno-deprecated-declarations %temp_home"
export CFLAGS
%cmake -DENABLE_MAINTAINER_MODE=OFF \
	-DVERSION_SUBSTRING=" (%{version}-%{release})" \
	%ldap_flags %ssl_flags %gtkdoc_flags %tests_flags %tnef_flags \
	-DENABLE_PLUGINS=all \
	%if 0%{?flatpak}
	"-DWITH_WMCLASS_OVERRIDE=evolution.bin" \
	%endif
	-DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \
	-DLIB_INSTALL_DIR:PATH=%{_libdir} \
	-DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \
	-DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \
	%if "%{?_lib}" == "lib64"
		-DLIB_SUFFIX=64 \
	%endif
	%{nil}
%cmake_build
%install
%cmake_install
%if 0%{?flatpak}
%{S:1} <%{S:2} >flatpak-evolution-wrapper.sh
chmod a+x flatpak-evolution-wrapper.sh
mv $RPM_BUILD_ROOT%{_bindir}/evolution $RPM_BUILD_ROOT%{_bindir}/evolution.bin
cp flatpak-evolution-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/evolution
%endif
%find_lang evolution --all-name --with-gnome
grep "%{_datadir}/locale" evolution.lang > translations.lang
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n evolution-devel -f %{oreon_filedir}/evolution-devel.list
%files -n evolution-langpacks -f %{oreon_filedir}/evolution-langpacks.list
%files -n evolution-bogofilter -f %{oreon_filedir}/evolution-bogofilter.list
%files -n evolution-spamassassin -f %{oreon_filedir}/evolution-spamassassin.list
%files -n evolution-pst -f %{oreon_filedir}/evolution-pst.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.60.0-1
- Prepare for Oreon 11 (RP1)
