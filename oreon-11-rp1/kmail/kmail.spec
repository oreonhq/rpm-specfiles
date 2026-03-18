Name:    kmail
Summary: Mail client
Version: 25.12.3
Release: 1%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://www.kde.org/applications/internet/kmail

Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

## upstream patches (lookaside cache)

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: libappstream-glib
BuildRequires: perl-generators
BuildRequires: cmake(Gpgmepp)
BuildRequires: cmake(QGpgmeQt6)

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Bookmarks)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6NotifyConfig)
BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6Contacts)
BuildRequires: cmake(KF6CalendarCore)
BuildRequires: cmake(KF6StatusNotifierItem)

BuildRequires: cmake(KPim6Akonadi)
BuildRequires: cmake(KPim6AkonadiContactWidgets)
BuildRequires: cmake(KPim6AkonadiMime)
BuildRequires: cmake(KPim6CalendarUtils)
BuildRequires: cmake(KPim6IdentityManagementCore)
BuildRequires: cmake(KPim6LdapWidgets)
BuildRequires: cmake(KPim6MailTransport)
BuildRequires: cmake(KPim6TextEdit)
BuildRequires: cmake(KPim6KontactInterface)
BuildRequires: cmake(KPim6Mime)
BuildRequires: cmake(KPim6Gravatar)
BuildRequires: cmake(KPim6Libkdepim)
BuildRequires: cmake(KPim6Libkleo)
BuildRequires: cmake(KPim6KSieveUi)
BuildRequires: cmake(KPim6MailCommon)
BuildRequires: cmake(KPim6MessageCore)
BuildRequires: cmake(KPim6MessageComposer)
BuildRequires: cmake(KPim6MessageList)
BuildRequires: cmake(KPim6MessageViewer)
BuildRequires: cmake(KPim6PimCommonAkonadi)
BuildRequires: cmake(KPim6TemplateParser)
BuildRequires: cmake(KPim6Tnef)
BuildRequires: cmake(KPim6MailTransportDBusService)
BuildRequires: cmake(KPim6AkonadiSearch)
BuildRequires: cmake(KF6TextEditTextToSpeech)
BuildRequires: cmake(KF6TextAutoCorrectionWidgets)
BuildRequires: cmake(KF6TextUtils)
BuildRequires: cmake(KF6TextCustomEditor)
BuildRequires: cmake(KF6TextTemplate)
BuildRequires: cmake(Qt6Keychain)
BuildRequires: pkgconfig(cups)
BuildRequires: cmake(KF6UserFeedback)

Obsoletes: pim-storage-service-manager < 17.03

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

## runtime deps
Requires: akonadi-import-wizard
Requires: grantlee-editor
Requires: kdepim-runtime
Requires: kmail-account-wizard
Requires: pim-data-exporter
Requires: pim-sieve-editor

%description
%{summary}.

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html

%check
for f in %{buildroot}%{_kf6_datadir}/applications/*.desktop ; do
  desktop-file-validate $f
done
for f in %{buildroot}%{_kf6_metainfodir}/*.appdata.xml ; do
appstream-util validate-relax --nonet $f
done


%files -f %{name}.lang
%license LICENSES/*
%{_datadir}/dbus-1/interfaces/org.kde.kmail.*.xml
%{_datadir}/dbus-1/services/org.kde.kmail.service
%{_kf6_bindir}/kmail
%{_kf6_bindir}/kmail-refresh-settings
%{_kf6_datadir}/applications/kmail_view.desktop
%{_kf6_datadir}/applications/org.kde.kmail-refresh-settings.desktop
%{_kf6_datadir}/applications/org.kde.kmail2.desktop
%{_kf6_datadir}/config.kcfg/kmail.kcfg
%{_kf6_datadir}/icons/breeze-dark/*/*/*
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/kmail2/
%{_kf6_datadir}/knotifications6/kmail2.notifyrc
%{_kf6_datadir}/qlogging-categories6/*kmail.*
%{_kf6_metainfodir}/org.kde.kmail2.appdata.xml
%{_kf6_datadir}/akonadi/agents/*.desktop
%{_kf6_bindir}/akonadi_*_agent
%{_kf6_datadir}/config.kcfg/archivemailagentsettings.kcfg
%{_kf6_datadir}/knotifications6/akonadi_archivemail_agent.notifyrc
%{_kf6_datadir}/knotifications6/akonadi_followupreminder_agent.notifyrc
%{_kf6_datadir}/knotifications6/akonadi_mailfilter_agent.notifyrc
%{_kf6_datadir}/knotifications6/akonadi_mailmerge_agent.notifyrc
%{_kf6_datadir}/knotifications6/akonadi_sendlater_agent.notifyrc
%{_kf6_bindir}/ktnef
%{_kf6_datadir}/applications/org.kde.ktnef.desktop

%files libs
%{_kf6_libdir}/libkmailprivate.so.*
%{_kf6_qtplugindir}/pim6/kcms/kmail/*
%{_kf6_qtplugindir}/pim6/kcms/summary/*
%{_kf6_qtplugindir}/kmailpart.so
%dir %{_kf6_qtplugindir}/pim6/kontact/
%{_kf6_qtplugindir}/pim6/kontact/kontact_kmailplugin.so
%{_kf6_qtplugindir}/pim6/kontact/kontact_summaryplugin.so
%{_kf6_qtplugindir}/pim6/akonadi/config/
%{_kf6_libdir}/libmailfilteragentprivate.so.*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
