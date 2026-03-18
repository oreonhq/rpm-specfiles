Name: merkuro
Version: 25.12.3
Release: 1%{?dist}
Summary: A calendar application using Akonadi to sync with external services (Nextcloud, GMail, ...)

License: GPL-3.0-or-later
URL:     https://invent.kde.org/pim/%{name}

Source:  https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches

BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(QGpgmeQt6)
BuildRequires:  cmake(Plasma)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickTest)
BuildRequires:  cmake(Qt6Location)

BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6QQC2DesktopStyle)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6Holidays)

BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  gpgme-devel

BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6AkonadiCalendar)
BuildRequires:  cmake(KPim6AkonadiContactCore)
BuildRequires:  cmake(KPim6AkonadiMime)
BuildRequires:  cmake(KPim6CalendarUtils)
BuildRequires:  cmake(KPim6IdentityManagementQuick)
BuildRequires:  cmake(KPim6MailCommon)
BuildRequires:  cmake(KPim6MailTransport)
BuildRequires:  cmake(KPim6MimeTreeParserCore)
BuildRequires:  cmake(KPim6Mbox)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KPim6Libkdepim)
BuildRequires:  cmake(KPim6AkonadiSearch)

BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib



# kalendar has been renamed to merkuro
Obsoletes:	kalendar < 23.08
Provides:	kalendar = %{version}-%{release}
Provides:	kalendar%{?_isa} = %{version}-%{release}

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
# Package doesn't build on arches that qtwebengine is not built on.
ExclusiveArch:	%{qt6_qtwebengine_arches}


%description
Merkuro is a application suite designed to make handling your emails, \
calendars, contacts, and tasks simple. Merkuro handles local and \
remote accounts of your choice, keeping changes synchronised across \
your Plasma desktop or phone.


%prep
%autosetup -n %{name}-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-kde --with-man --all-name

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.%{name}.contact.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.%{name}.calendar.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.%{name}.mail.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.contact.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.calendar.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.mail.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.merkuro.metainfo.xml

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/merkuro-calendar
%{_kf6_bindir}/merkuro-contact
%{_kf6_bindir}/merkuro-mail
%{_kf6_qmldir}/org/kde/merkuro/*
%{_kf6_datadir}/plasma/plasmoids/org.kde.merkuro.contact.applet/
%{_kf6_datadir}/applications/org.kde.merkuro.calendar.desktop
%{_kf6_datadir}/applications/org.kde.merkuro.contact.desktop
%{_kf6_datadir}/applications/org.kde.merkuro.mail.desktop
%{_kf6_datadir}/applications/org.kde.merkuro.desktop
%{_kf6_datadir}/icons/hicolor/128x128/apps/org.kde.merkuro*.png
%{_kf6_datadir}/icons/hicolor/256x256/apps/org.kde.merkuro*.png
%{_kf6_datadir}/icons/hicolor/48x48/apps/org.kde.merkuro*.png
%{_kf6_datadir}/icons/hicolor/16x16/apps/org.kde.merkuro*.png
%{_kf6_datadir}/icons/hicolor/24x24/apps/org.kde.merkuro*.png
%{_kf6_datadir}/icons/hicolor/32x32/apps/org.kde.merkuro*.png
%{_kf6_metainfodir}/org.kde.merkuro.*.metainfo.xml
%{_kf6_datadir}/qlogging-categories6/merkuro.categories
%{_kf6_datadir}/qlogging-categories6/merkuro.contact.categories
%{_kf6_libdir}/libMerkuroComponents.so
%{_kf6_libdir}/libMerkuroComponents.so.{6,%{version}}
%{_kf6_libdir}/libmerkuro_contact.so
%{_kf6_libdir}/libmerkuro_contact.so.{6,%{version}}
%{_kf6_datadir}/knotifications6/merkuro.mail.notifyrc
%{_kf6_metainfodir}/org.kde.merkuro.metainfo.xml

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
