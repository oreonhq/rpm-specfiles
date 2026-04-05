Name:    korganizer
Summary: Personal Organizer
Version: 25.12.3
Release:	2%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/pim/%{name}

Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: libappstream-glib
BuildRequires: perl-generators
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6UiTools)

BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Holidays)
BuildRequires: cmake(KF6UserFeedback)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6TextTemplate)

BuildRequires: cmake(KPim6Akonadi)
BuildRequires: cmake(KF6Contacts)
BuildRequires: cmake(KF6CalendarCore)
BuildRequires: cmake(KPim6AkonadiContactWidgets)
BuildRequires: cmake(KPim6IdentityManagementCore)
BuildRequires: cmake(KPim6MailTransport)
BuildRequires: cmake(KPim6CalendarUtils)
BuildRequires: cmake(KPim6LdapWidgets)
BuildRequires: cmake(KPim6AkonadiCalendar)
BuildRequires: cmake(KPim6KontactInterface)
BuildRequires: cmake(KPim6Mime)
BuildRequires: cmake(KPim6AkonadiNotes)
BuildRequires: cmake(KPim6PimCommonAkonadi)
BuildRequires: cmake(KPim6Libkdepim)
BuildRequires: cmake(KPim6IncidenceEditor)
BuildRequires: cmake(KPim6CalendarSupport)
BuildRequires: cmake(KPim6EventViews)

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: kdepim-runtime

%description
KOrganizer is the calendar and scheduling component of the Kontact suite.
You can write journal entries, schedule appointments, events, and to-dos.

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-html


%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/korganizer-import.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/korganizer-view.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml

%files -f %{name}.lang
%license LICENSES/*
%{_datadir}/dbus-1/interfaces/org.kde.Korganizer.*.xml
%{_datadir}/dbus-1/interfaces/org.kde.korganizer.*.xml
%{_datadir}/dbus-1/services/org.kde.korganizer.service
%{_kf6_bindir}/korganizer
%{_kf6_datadir}/applications/korganizer-import.desktop
%{_kf6_datadir}/applications/korganizer-view.desktop
%{_kf6_datadir}/applications/org.kde.korganizer.desktop
%{_kf6_datadir}/config.kcfg/korganizer.kcfg
%{_kf6_datadir}/icons/hicolor/*
%{_kf6_datadir}/korganizer/
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_metainfodir}/org.kde.korganizer.appdata.xml

%files libs
%{_kf6_libdir}/libkorganizer_interfaces.so.*
%{_kf6_libdir}/libkorganizer_core.so.*
%{_kf6_libdir}/libkorganizerprivate.so.*
%{_kf6_qtplugindir}/pim6/kcms/korganizer/*
%{_kf6_qtplugindir}/pim6/kcms/summary/*
%{_kf6_qtplugindir}/korganizerpart.so
# Kontact integration
%{_kf6_qtplugindir}/pim6/kontact/kontact_korganizerplugin.so
%{_kf6_qtplugindir}/pim6/kontact/kontact_todoplugin.so
%{_kf6_qtplugindir}/pim6/kontact/kontact_journalplugin.so
%{_kf6_qtplugindir}/pim6/kontact/kontact_specialdatesplugin.so
%{_kf6_qtplugindir}/pim6/korganizer/


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
