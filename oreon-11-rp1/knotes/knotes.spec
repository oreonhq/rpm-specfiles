%global source0_hash 4e6da68e1ccfd5a2fcaf038a6438bef7b671446b05a3e739787b63689016d592

Name:    knotes
Summary: Popup notes
Version: 24.05.2
Release: 6%{?dist}

# Automatically converted from old format: GPLv2 and GFDL - review is highly recommended.
License: GPL-2.0-only AND LicenseRef-Callaway-GFDL
URL:     https://www.kde.org/applications/utilities/knotes/

Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

Patch0:  kmime-headers.patch

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: libappstream-glib
BuildRequires: perl-generators

BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6Test)

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DNSSD)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6NotifyConfig)
BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6TextAutoCorrectionWidgets)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6TextTemplate)

BuildRequires: cmake(KPim6Akonadi)
BuildRequires: cmake(KPim6AkonadiNotes)
BuildRequires: cmake(KPim6CalendarUtils)
BuildRequires: cmake(KPim6KontactInterface)
BuildRequires: cmake(KPim6Mime)
BuildRequires: cmake(KPim6PimCommonAkonadi)
BuildRequires: cmake(KPim6GrantleeTheme)
BuildRequires: cmake(KF6TextUtils)
BuildRequires: cmake(KF6TextCustomEditor)
BuildRequires: cmake(KPim6AkonadiSearch)
BuildRequires: cmake(KPim6Libkdepim)

# akonadi_notes_agent moved here
Conflicts: kmail < 16.12

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
KNotes is a program that lets you write the computer equivalent of sticky
notes. The notes are saved automatically when you exit the program, and
they display when you open the program.

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n knotes-%{version} -p1

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
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml

%files -f %{name}.lang
%license LICENSES/*
%{_datadir}/dbus-1/interfaces/org.kde.KNotes.xml
%{_datadir}/dbus-1/interfaces/org.kde.kontact.KNotes.xml
%{_kf6_bindir}/akonadi_notes_agent
%{_kf6_bindir}/knotes
%{_kf6_datadir}/akonadi/agents/notesagent.desktop
%{_kf6_datadir}/applications/org.kde.knotes.desktop
%{_kf6_datadir}/config.kcfg/knotesglobalconfig.kcfg
%{_kf6_datadir}/config.kcfg/notesagentsettings.kcfg
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/knotes/
%{_kf6_datadir}/knotifications6/akonadi_notes_agent.notifyrc
%{_kf6_datadir}/knsrcfiles/knotes_printing_theme.knsrc
%{_kf6_datadir}/kxmlgui5/knotes/
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_metainfodir}/org.kde.knotes.appdata.xml

%files libs
%{_kf6_libdir}/libknotesprivate.so.*
%{_kf6_libdir}/libnotesharedprivate.so.*
%{_kf6_qtplugindir}/pim6/kontact/kontact_knotesplugin.so
%{_kf6_qtplugindir}/pim6/kcms/knotes/*
%{_kf6_qtplugindir}/pim6/kcms/summary/*

%changelog
%autochangelog
