%global source0_hash 00c7054293e5e7832a7eeb7d9ba0d35745e95d2f7df27ab8f912302e2bb56fc5
Name:          modem-manager-gui
Summary:        Graphical interface for ModemManager
Summary(de):   Grafische Oberfläche für ModemManager
Summary(ru):   Графический интерфейс для демона ModemManager
Version:       0.0.20
Release:        1%{?dist}
License:       GPL-3.0-only
URL:           https://linuxonly.ru/page/modem-manager-gui
Source0:        http://download.tuxfamily.org/gsf/source/modem-manager-gui-%{version}.tar.gz
Patch1: 0001-Move-the-NetworkManager-dispatcher-script-out-of-etc.patch
Patch2: 0002-add-missing-appdata-tags.patch
Patch3: 0003-fix-deprecated-meson-functions.patch
Patch4: 0004-fix-segfault-on-DNS-entries.patch
%global build_using_meson 1
%global with_connman 0
%global with_ofono   1
%global with_ppp     1
%global ofono_version 1.9
Requires: filesystem
Requires: hicolor-icon-theme
Requires: mobile-broadband-provider-info >= 1.20120614
Requires: yelp >= 3.10
Requires: %{name}-cm%{?_isa} = %{version}-%{release}
Suggests: %{name}-cm-NetworkManager%{?_isa} = %{version}-%{release}
Requires: %{name}-mm%{?_isa} = %{version}-%{release}
Suggests: %{name}-mm-ModemManager%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gdbm-devel
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  gtkspell3-devel
BuildRequires:  itstool
BuildRequires:  libappindicator-gtk3-devel
BuildRequires:  libappstream-glib
BuildRequires:  libnotify-devel
BuildRequires:  meson
BuildRequires:  ofono-devel
BuildRequires:  pkgconfig
BuildRequires:  po4a
# /oreon:deps
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

%package cm-NetworkManager
Summary: Use NetworkManager to manage connections in %{name}
Requires: NetworkManager >= 1.20
Requires: python3
Provides: %{name}-cm%{?_isa}
%description cm-NetworkManager
Plugin for %{name} allowing to use NetworkManager
as the connection manager.

%package cm-pppd
Summary: Use pppd to manage connections in %{name}
Requires: ppp >= 2.4.5
Provides: %{name}-cm%{?_isa}
%description cm-pppd
Plugin for %{name} allowing to use pppd as the connection manager.

%package mm-ModemManager
Summary: Use ModemManager to manage modems in %{name}
Requires: ModemManager >= 0.7.0
Provides: %{name}-mm%{?_isa}
%description mm-ModemManager
Plugin for %{name} allowing to use ModemManager as the modem manager.

%package mm-ofono
Summary: Use ofono to manage modems in %{name}
Requires: ofono >= %{ofono_version}
Provides: %{name}-mm%{?_isa}
%description mm-ofono
Plugin for %{name} allowing to use ofono as the modem manager. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}
%oreon_prep
%build

    %meson
    %meson_build
%install
%global _smp_mflags -j1
    %meson_install
%find_lang %{name} --with-gnome
sed -e 's|/usr/bin/env python3|/usr/bin/python3|' \
    -i %{buildroot}%{_prefix}/lib/NetworkManager/dispatcher.d/95-mmgui-timestamp-notifier
rm %{buildroot}/%{_libdir}/%{name}/modules/libmodmm_mm06.so
%if !%{with_connman}
    find %{buildroot} -name '*connman*.so*' -printf 'Removed unused file: %p\n' -delete
%endif
%if !%{with_ofono}
    find %{buildroot} -name '*ofono*.so*' -printf 'Removed unused file: %p\n' -delete
%endif
%if !%{with_ppp}
    find %{buildroot} -name '*pppd*.so*' -printf 'Removed unused file: %p\n' -delete
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%check

appstream-util validate --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list
%files -n modem-manager-gui-cm-NetworkManager -f %{oreon_filedir}/modem-manager-gui-cm-NetworkManager.list
%files -n modem-manager-gui-cm-pppd -f %{oreon_filedir}/modem-manager-gui-cm-pppd.list
%files -n modem-manager-gui-mm-ModemManager -f %{oreon_filedir}/modem-manager-gui-mm-ModemManager.list
%files -n modem-manager-gui-mm-ofono -f %{oreon_filedir}/modem-manager-gui-mm-ofono.list

%changelog

%autochangelog
