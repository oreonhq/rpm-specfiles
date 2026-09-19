%global source0_hash d1e7c7ffeb8c1339d2214e7b368a5abb3db6f836115fec4cedb8fc3c18193af4

Name:    pim-data-exporter
Summary: Pim Data Exporter
Version: 25.12.3
Release: 1%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/pim/%{name}

Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: libappstream-glib
BuildRequires: cmake(QGpgmeQt6)

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Test)

BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6TextTemplate)
BuildRequires: cmake(KF6IconThemes)

BuildRequires: cmake(KPim6Akonadi)
BuildRequires: cmake(KF6Contacts)
BuildRequires: cmake(KPim6IdentityManagementCore)
BuildRequires: cmake(KPim6MailCommon)
BuildRequires: cmake(KPim6MailTransport)
BuildRequires: cmake(KPim6Mime)
BuildRequires: cmake(KPim6PimCommonAkonadi)
BuildRequires: cmake(KF6CalendarCore)
BuildRequires: cmake(KPim6AkonadiNotes)
BuildRequires: cmake(KF6TextCustomEditor)
BuildRequires: cmake(KF6UserFeedback)
BuildRequires: cmake(KPim6Libkdepim)

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
%{summary}.

%package libs
Summary: Runtime libraries for %{name}
Conflicts: kdepim-libs < 7:16.12
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.pimdataexporter.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.pimdataexporter.appdata.xml

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/pimdataexporter
%{_kf6_bindir}/pimdataexporterconsole
%{_kf6_datadir}/applications/org.kde.pimdataexporter.desktop
%{_kf6_datadir}/config.kcfg/pimdataexporterglobalconfig.kcfg
%{_kf6_datadir}/qlogging-categories6/*pimdataexporter.*
%{_kf6_metainfodir}/org.kde.pimdataexporter.appdata.xml

%files libs
%{_kf6_libdir}/libpimdataexporterprivate.so.*

%changelog
%autochangelog
