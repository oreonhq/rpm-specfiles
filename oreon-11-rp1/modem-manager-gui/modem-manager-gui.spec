%global source0_hash 00c7054293e5e7832a7eeb7d9ba0d35745e95d2f7df27ab8f912302e2bb56fc5

Name:          modem-manager-gui
Summary:       Graphical interface for ModemManager
Summary(de):   Grafische Oberfläche für ModemManager
Summary(ru):   Графический интерфейс для демона ModemManager

Version:       0.0.20
Release:       18%{?dist}
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:       GPL-3.0-only

URL:           https://linuxonly.ru/page/modem-manager-gui
Source0:       http://download.tuxfamily.org/gsf/source/modem-manager-gui-%{version}.tar.gz

# Fix the NetworkManager dispatcher script location
Patch1: 0001-Move-the-NetworkManager-dispatcher-script-out-of-etc.patch

# Appdata XML validation fails
Patch2: 0002-add-missing-appdata-tags.patch

# There have been a couple of Meson releases since the last MMGUI release
# and some of the stuff used in build scripts has been deprecated since
Patch3: 0003-fix-deprecated-meson-functions.patch

# MMGUI crashes with some new versions of NetworkManager.
# Patch taken from Debian:
# https://salsa.debian.org/debian/modem-manager-gui/-/raw/master/debian/patches/fix_segfault_on_DNS_entries.patch
Patch4: 0004-fix-segfault-on-DNS-entries.patch

# Use meson for build? Otherwise, use make.
%global build_using_meson 1

# Enable/disable plugins.
%global with_connman 0
%global with_ofono   1
%global with_ppp     1

BuildRequires: gcc
BuildRequires: desktop-file-utils
BuildRequires: gdbm-devel >= 1.10
BuildRequires: gettext
BuildRequires: glib2-devel >= 2.32.1
BuildRequires: gtk3-devel >= 3.4.0
BuildRequires: gtkspell3-devel >= 3.0.3
BuildRequires: itstool >= 1.2.0
BuildRequires: libappindicator-gtk3-devel >= 0.4.92
BuildRequires: libappstream-glib
BuildRequires: libnotify-devel >= 0.7.5
BuildRequires: pkgconfig
BuildRequires: po4a > 0.45

%if %{build_using_meson}
BuildRequires: meson >= 0.38
%else
BuildRequires: make
%endif

%if %{with_ofono}
%global ofono_version 1.9
BuildRequires: ofono-devel >= %{ofono_version}
%endif

Requires: filesystem
Requires: hicolor-icon-theme
Requires: mobile-broadband-provider-info >= 1.20120614
Requires: yelp >= 3.10

Requires: %{name}-cm%{?_isa} = %{version}-%{release}
Suggests: %{name}-cm-NetworkManager%{?_isa} = %{version}-%{release}
Requires: %{name}-mm%{?_isa} = %{version}-%{release}
Suggests: %{name}-mm-ModemManager%{?_isa} = %{version}-%{release}

%description
This program is a simple graphical interface for Modem Manager 
daemon dbus interface.
Current features:
- View device information: Operator name, Mode, IMEI, IMSI,
  Signal level.
- Send and receive SMS messages with long massages 
  concatenation and store messages in database.
- Send USSD requests and read answers in GSM7 and UCS2 formats
  converted to system UTF8 charset.
- Scan available mobile networks.

%description -l de
Dieses Programm ist eine einfache grafische Oberfläche für
die DBus-Schnittstelle des ModemManager-Daemons.
Funktionen:
- Geräteinformationen anzeigen: Name des Netzanbieters, Modus,
  IMEI, IMSI, Signalstärke.
- SMS senden und empfangen, Verkettung langer Nachrichten,
  Speichern der Nachrichten in der Datenbank.
- USSD-Befehle in den Formaten GSM7 und UCS2 senden und
  Antworten empfangen, Umwandlung in den UTF-8-Zeichensatz.
- Nach verfügbaren Mobilnetzwerken suchen.

%description -l ru
Данная программа является простым графическим интерфейсом для
демона Modem Manager, использующим интерфейс dbus.
Текущие возможности:
- Просмотр информации об устройстве: имени оператора, режима работы,
  IMEI, IMSI и уровня сигнала.
- Прием и отправка сообщений SMS с объединением длинных сообщений 
  и сохранением сообщений в базе данных.
- Отправка запросов USSD и прием ответов в кодировках GSM7 и UCS2
  с последующей конвертацией в системную кодировку UTF8.
- Сканирование доступных мобильных сетей.

%if %{with_connman}
%package cm-connman
Summary: Use connman to manage connections in %{name}
Requires: connman >= 1.12
Provides: %{name}-cm%{?_isa}
%description cm-connman
Plugin for %{name} allowing to use connman as the connection manager.
%endif

%package cm-NetworkManager
Summary: Use NetworkManager to manage connections in %{name}
Requires: NetworkManager >= 1.20
Requires: python3
Provides: %{name}-cm%{?_isa}
%description cm-NetworkManager
Plugin for %{name} allowing to use NetworkManager
as the connection manager.

%if %{with_ppp}
%package cm-pppd
Summary: Use pppd to manage connections in %{name}
Requires: ppp >= 2.4.5
Provides: %{name}-cm%{?_isa}
%description cm-pppd
Plugin for %{name} allowing to use pppd as the connection manager.
%endif

%package mm-ModemManager
Summary: Use ModemManager to manage modems in %{name}
Requires: ModemManager >= 0.7.0
Provides: %{name}-mm%{?_isa}
%description mm-ModemManager
Plugin for %{name} allowing to use ModemManager as the modem manager.

%if %{with_ofono}
%package mm-ofono
Summary: Use ofono to manage modems in %{name}
Requires: ofono >= %{ofono_version}
Provides: %{name}-mm%{?_isa}
%description mm-ofono
Plugin for %{name} allowing to use ofono as the modem manager. 
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name} -p1

%build
%if %{build_using_meson}
    %meson
    %meson_build
%else
    %configure
    %make_build
%endif

%install
# Override the system RPM macro to force a single-threaded install process.
# This is a workaround around bugs in /usr/bin/itstool, which cause it
# to behave non-deterministic during pararell builds.
%global _smp_mflags -j1

%if %{build_using_meson}
    %meson_install
%else
    %make_install
%endif

%find_lang %{name} --with-gnome

# Fix /usr/bin/env usage
sed -e 's|/usr/bin/env python3|/usr/bin/python3|' \
    -i %{buildroot}%{_prefix}/lib/NetworkManager/dispatcher.d/95-mmgui-timestamp-notifier

# Remove plugin for obsolete ModemManager version
rm %{buildroot}/%{_libdir}/%{name}/modules/libmodmm_mm06.so

%if !%{with_connman}
    find %{buildroot} -name '*connman*.so*' -printf 'Removed unused file: %p\n' -delete
%endif

%if !%{with_ofono}
    find %{buildroot} -name '*ofono*.so*' -printf 'Removed unused file: %p\n' -delete
%endif

%if !%{with_ppp}
    find %{buildroot} -name '*pppd*.so*' -printf 'Removed unused file: %p\n' -delete
%endif

%check
appstream-util validate --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS Changelog
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{name}-symbolic.svg
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/polkit-1/actions/ru.linuxonly.modem-manager-gui.policy
%{_datadir}/%{name}/
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/modules/
%{_mandir}/man1/%{name}.1.*
%{_mandir}/*/man1/%{name}.1.*

%if %{with_connman}
%files cm-connman
%{_libdir}/%{name}/modules/libmodcm_connman112.so
%endif

%files cm-NetworkManager
%{_libdir}/%{name}/modules/libmodcm_nm09.so
%{_prefix}/lib/NetworkManager/dispatcher.d/95-mmgui-timestamp-notifier

%if %{with_ppp}
%files cm-pppd
%{_libdir}/%{name}/modules/libmodcm_pppd245.so
%endif

%files mm-ModemManager
%{_libdir}/%{name}/modules/libmodmm_mm07.so

%if %{with_ofono}
%files mm-ofono
%{_libdir}/%{name}/modules/libmodmm_ofono109.so
%{_libdir}/ofono/plugins/libmmgui-ofono-history.so*
%endif

%changelog
%autochangelog
