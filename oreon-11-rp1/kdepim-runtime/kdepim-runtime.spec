%global source0_hash 498744228f225176624fafbab283815b6872351f6d15bb935e2d02c1a644dd43

Name:    kdepim-runtime
Summary: KDE PIM Runtime Environment
Epoch:   1
Version: 26.04.3
Release: 1%{?dist}

License: AGPL-3.0-or-later AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND LGPL-3.0-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/pim/%{name}

Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

## upstream patches

# nuke ill-advised -devel pkg
Obsoletes:      kdepim-runtime-devel < 1:4.7.90-3

Obsoletes:      akonadi-google < 0.4
Provides:       akonadi-google = %{version}-%{release}
Obsoletes:      akonadi-google-calendar < 0.4
Provides:       akonadi-google-calendar = %{version}-%{release}
Obsoletes:      akonadi-google-contacts < 0.4
Provides:       akonadi-google-contacts = %{version}-%{release}
Obsoletes:      akonadi-google-tasks < 0.4
Provides:       akonadi-google-tasks = %{version}-%{release}

Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qca-qt6)

BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6NetworkAuth)
BuildRequires:  cmake(Qt6Keychain)

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6DAV)
BuildRequires:  cmake(KF6TextCustomEditor)
BuildRequires:  cmake(KF6Wallet)

BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KPim6AkonadiMime)
BuildRequires:  cmake(KPim6AkonadiNotes)
BuildRequires:  cmake(KPim6MailTransport)
BuildRequires:  cmake(KPim6IdentityManagementWidgets)
BuildRequires:  cmake(KPim6PimCommonAkonadi)
BuildRequires:  cmake(KPim6PimCommonActivities)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KPim6CalendarUtils)
BuildRequires:  cmake(KPim6Mbox)
BuildRequires:  cmake(KPim6IMAP)
BuildRequires:  cmake(KPim6AkonadiNotes)
BuildRequires:  cmake(KPim6AkonadiCalendar)
BuildRequires:  cmake(KPim6GAPI)
BuildRequires:  cmake(KPim6LdapWidgets)
BuildRequires:  cmake(KPim6Libkdepim)
BuildRequires:  cmake(KF6TextTemplate)

# --- Optional
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6TextToSpeech)
# Disabling for now, it makes kdepim-runtime fail building
# BuildRequires:  cmake(Libkolabxml)

%description
%{summary}.

%package libs
Summary: %{name} runtime libraries
# some plugins moved here 16.04.0-1
Obsoletes: kdepim-runtime < 1:16.04
Obsoletes: kf5-kmailtransport-akonadi < 23.08.0
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: akonadi-server%{?_isa} >= %{version}
%description libs
%{summary}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n kdepim-runtime-%{version}%{?pre} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html

%check
desktop-file-validate %{buildroot}/%{_kf6_datadir}/applications/org.kde.akonadi_contacts_resource.desktop
desktop-file-validate %{buildroot}/%{_kf6_datadir}/applications/org.kde.akonadi_davgroupware_resource.desktop
desktop-file-validate %{buildroot}/%{_kf6_datadir}/applications/org.kde.akonadi_vcarddir_resource.desktop
desktop-file-validate %{buildroot}/%{_kf6_datadir}/applications/org.kde.akonadi_imap_resource.desktop
desktop-file-validate %{buildroot}/%{_kf6_datadir}/applications/org.kde.akonadi_openxchange_resource.desktop
desktop-file-validate %{buildroot}/%{_kf6_datadir}/applications/org.kde.akonadi_google_resource.desktop
desktop-file-validate %{buildroot}/%{_kf6_datadir}/applications/org.kde.akonadi_vcard_resource.desktop


%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/akonadi_*
%{_kf6_bindir}/gidmigrator
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_datadir}/akonadi/agents/*
%{_kf6_datadir}/akonadi/firstrun/*
%{_kf6_datadir}/knotifications6/*
%{_kf6_datadir}/mime/packages/kdepim-mime.xml
%{_kf6_datadir}/icons/hicolor/*/apps/*
%{_kf6_datadir}/dbus-1/interfaces/*.xml
%{_kf6_datadir}/applications/org.kde.akonadi_*.desktop
%{_datadir}/akonadi/davgroupware-providers/*

%files libs
%{_kf6_libdir}/libakonadi-singlefileresource-widget.so.*
%{_kf6_libdir}/libakonadi-filestore.so.*
%{_kf6_libdir}/libfolderarchivesettings.so.*
%{_kf6_libdir}/libakonadi-singlefileresource.so.*
%{_kf6_libdir}/libkmindexreader.so.*
%{_kf6_libdir}/libmaildir.so.*
%{_kf6_libdir}/libnewmailnotifier.so.*
%{_kf6_plugindir}/kio/akonadi.so
%{_kf6_qtplugindir}/pim6/akonadi/config/
%{_kf6_qtplugindir}/pim6/kcms/common/kcm_ldap.so
%{_kf6_qtplugindir}/pim6/mailtransport/mailtransport_akonadiplugin.so


%changelog
%autochangelog

