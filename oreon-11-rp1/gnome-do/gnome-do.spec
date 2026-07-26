%global source0_hash 282343285c818f2bb8198e7876f9ec895327415c8ddadc20c299fbe2c8deedfb

%global			debug_package %{nil}

Name:			gnome-do
Version:		0.95.3
Release:		32%{?dist}
Summary:		Quick launch and search

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:		GPL-3.0-or-later
URL:			http://do.cooperteam.net/
Source0:		http://launchpad.net/do/trunk/%{version}/+download/gnome-do-%{version}.tar.gz
Patch0:			fix-build.patch

BuildRequires:		mono-devel, mono-addins-devel
BuildRequires:		nunit2-devel
BuildRequires:		desktop-file-utils
BuildRequires:		dbus-sharp-devel
BuildRequires:		dbus-sharp-glib-devel
BuildRequires:		GConf2-devel
BuildRequires:		gtk-sharp2-devel, notify-sharp-devel
BuildRequires:		gnome-sharp-devel, gnome-desktop-sharp-devel >= 2.26
BuildRequires:		gnome-keyring-sharp-devel
BuildRequires:		gettext
BuildRequires:		perl-XML-Parser
BuildRequires:		intltool
BuildRequires:		gtk2-devel
BuildRequires:		desktop-file-utils
BuildRequires:		gio-sharp-devel
BuildRequires:		gkeyfile-sharp-devel
BuildRequires:		autoconf automake libtool
BuildRequires: make

Requires(pre):		GConf2
Requires(post):		GConf2
Requires(preun):	GConf2

Requires:		mono(NDesk.DBus.GLib) = 1.0.0.0
Requires:		gnome-keyring-sharp, gnome-desktop-sharp, findutils
Requires:		gnome-desktop3, pkgconfig
Requires:		gio-sharp, gkeyfile-sharp

# Mono only available on these:
ExclusiveArch: %mono_arches

# nunit2 fails to build on armv7hl. Mono crashes. see bug 1923663
# it is too much work to switch to nunit (version 3) at the moment.
ExcludeArch:		armv7hl

%description
GNOME Do (Do) is an intelligent launcher tool that makes performing
common tasks on your computer simple and efficient. Do not only allows
you to search for items in your desktop environment
(e.g. applications, contacts, bookmarks, files, music), it also allows
you to specify actions to perform on search results (e.g. run, open,
email, chat, play).

%package devel
Summary:		Development files for GNOME Do
Requires:		%{name} = %{version}-%{release}
Requires:		pkgconfig

%description devel
Development files for GNOME Do

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

sed -i "s#gmcs#mcs#g" configure*
sed -i "s#gmcs#mcs#g" m4/shamrock/mono.m4

sed -i "s#dbus-sharp-1.0#dbus-sharp-2.0#g" configure.ac
sed -i "s#dbus-sharp-glib-1.0#dbus-sharp-glib-2.0#g" configure.ac
%build
NOCONFIGURE=1 autoreconf -vif
%configure
make %{?_smp_mflags}

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%make_install

desktop-file-install	\
	--dir $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart	\
	--add-only-show-in=GNOME				\
	$RPM_BUILD_ROOT%{_datadir}/applications/gnome-do.desktop
desktop-file-install --delete-original	\
	--dir $RPM_BUILD_ROOT%{_datadir}/applications	\
	--remove-category Application	\
	$RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

#own this dir:
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/

%find_lang %{name}

%pre
if [ "$1" -gt 1 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/%{name}.schemas >/dev/null || :
fi

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
  %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :

%preun
if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
fi

%files -f %{name}.lang
%doc AUTHORS COPYING COPYRIGHT
%{_bindir}/gnome-do
%{_libdir}/gnome-do/
%{_datadir}/gnome-do/
%config(noreplace) %{_sysconfdir}/xdg/autostart/gnome-do.desktop
%config(noreplace) %{_sysconfdir}/gconf/schemas/*
%{_datadir}/icons/hicolor/*/apps/gnome-do.*
%{_datadir}/applications/*

%files devel
%{_libdir}/pkgconfig/*

%changelog
%autochangelog
