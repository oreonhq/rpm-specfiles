%global source0_hash 35e038ea3afaacdf451046e87af876096cf1520efc04fc3f5b63ea22e0297175
Name:		gnome-phone-manager
Summary:        Gnome Phone Manager
Version: 	0_69
Release:        1%{?dist}
License: 	GPL-2.0-or-later
Source0:        http://ftp.gnome.org/pub/GNOME/sources/gnome-phone-manager/%{version}/%{name}-%{version}.tar.xz
URL: 		https://wiki.gnome.org/PhoneManager/
Patch03: gnome-phone-manager-0.68-eds.patch
Patch04: gnome-phone-manager-0.69-drop-plugin.patch
# oreon:deps
BuildRequires:  GConf2-devel
BuildRequires:  bluez-libs-devel
BuildRequires:  desktop-file-utils
BuildRequires:  evolution-data-server-devel
BuildRequires:  gettext
BuildRequires:  gnokii-devel
BuildRequires:  gnome-bluetooth-libs-devel
BuildRequires:  gnome-icon-theme-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gtk3-devel
BuildRequires:  gtkspell-devel
BuildRequires:  intltool
BuildRequires:  libcanberra-devel
BuildRequires:  make
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig(gnome-bluetooth-1.0)
BuildRequires:  telepathy-glib-devel
# /oreon:deps
%description
This program will connect to your mobile phone over a serial port,
either via a cable, infrared (IrDA) or Bluetooth connection.

For example it listens for text messages, and when they arrive,
displays them on the desktop. A visual indicator is displayed in
the notification area, if one is presently added to the panel.

%package telepathy
Summary: Telepathy connection manager to send and receive SMSes
%description telepathy
This program will connect to your mobile phone over a serial port,
either via a cable, infrared (IrDA) or Bluetooth connection.

This plugin to Telepathy allows you to send and receive messages using any
Instant Messaging application that uses Telepathy, such as Empathy.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

#%patch01 -p1 -b .no-g-thread-init
#%patch02 -p1 -b .bluetooth-api-change
%patch -P03 -p1 -b .eds
%patch -P4 -p0 -b .plugin

#rm ./libgsm/phonemgr-listener.lo
#rm ./libgsm/phonemgr-listener.o

%build

%configure
make %{?_smp_mflags}
%install
make DESTDIR=$RPM_BUILD_ROOT install
install -m0644 -D telepathy/sms.profile $RPM_BUILD_ROOT%{_datadir}/mission-control/profiles/sms.profile
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: https://bugzilla.gnome.org/show_bug.cgi?id=730849
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">gnome-phone-manager.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Control your mobile phone from your desktop</summary>
  <description>
    <p>
      Phone Manager allows you to control your mobile phone. It uses the
      gnokii backend that typically works with older Nokia devices. Phone
      manager allows you to send SMS messages, view the address book on your
      phone, and receive notifications on the desktop when a new SMS arrives.
    </p>
  </description>
  <url type="homepage">https://live.gnome.org/PhoneManager/</url>
  <screenshots>
    <screenshot type="default">https://wiki.gnome.org/PhoneManager?action=AttachFile&amp;do=get&amp;target=prefs-2.png</screenshot>
  </screenshots>
</application>
EOF
rm $RPM_BUILD_ROOT%{_libdir}/gnome-bluetooth/plugins/libphonemgr.a
rm $RPM_BUILD_ROOT%{_libdir}/gnome-bluetooth/plugins/libphonemgr.la
%find_lang %{name}
desktop-file-install \
  --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --add-category X-Fedora \
  $RPM_BUILD_ROOT%{_datadir}/applications/gnome-phone-manager.desktop
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
        %{_sysconfdir}/gconf/schemas/gnome-phone-manager.schemas 	\
	>& /dev/null || :
%pre

if [ "$1" -gt 1 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule 				\
        %{_sysconfdir}/gconf/schemas/gnome-phone-manager.schemas 	\
	>& /dev/null || :
fi
%preun

if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule 				\
        %{_sysconfdir}/gconf/schemas/gnome-phone-manager.schemas 	\
	>& /dev/null || :
fi
%files -f %{oreon_filedir}/main.list
%files -n gnome-phone-manager-telepathy -f %{oreon_filedir}/gnome-phone-manager-telepathy.list

%changelog

%autochangelog
