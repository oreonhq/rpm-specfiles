%global framework incidenceeditor


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kf5-%{framework}
Version: 23.08.5
Release: 6%{?dist}
Summary: KDE PIM library for creating and editing calendar incidences

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://invent.kde.org/pim/%{framework}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
# available only where kf5-eventviews is
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}

BuildRequires:  extra-cmake-modules >= 5.23.0
BuildRequires:  kf5-rpm-macros >= 5.23.0

BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)

BuildRequires:  cmake(KGantt)

BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(KPim5Akonadi)
BuildRequires:  cmake(KPim5AkonadiMime)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KPim5CalendarSupport)
BuildRequires:  cmake(KPim5CalendarUtils)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KPim5EventViews)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KPim5Ldap)
BuildRequires:  cmake(KPim5Libkdepim)
BuildRequires:  cmake(KPim5MailTransport)

#global majmin_ver %(echo %{version} | cut -d. -f1,2)
%global majmin_ver %{version}
BuildRequires:  kf5-akonadi-mime-devel >= %{majmin_ver}
BuildRequires:  kf5-akonadi-server-devel >= %{majmin_ver}
BuildRequires:  kf5-eventviews-devel >= %{majmin_ver}
BuildRequires:  kf5-kcalendarcore-devel >= %{majmin_ver}
BuildRequires:  kf5-kcalendarutils-devel >= %{majmin_ver}
BuildRequires:  kf5-kmailtransport-devel >= %{majmin_ver}
BuildRequires:  kf5-libkdepim-devel >= %{majmin_ver}
BuildRequires:  kf5-pimcommon-devel >= %{majmin_ver}

Obsoletes:      kdepim-libs < 7:16.04.0
Conflicts:      kdepim-libs < 7:16.04.0

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF5CalendarCore)
Requires:       cmake(KPim5CalendarSupport)
Requires:       cmake(KPim5CalendarUtils)
Requires:       cmake(KPim5EventViews)
Requires:       cmake(KPim5MailTransport)
Requires:       cmake(KPim5Mime)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version}

# Rename translation files to avoid conflict with KF6
find ./po -type f -execdir mv {} libincidenceeditors5.po \;
sed -i "/TRANSLATION_DOMAIN/ s/libincidenceeditors/libincidenceeditors5/" src/CMakeLists.txt
sed -i "s/libincidenceeditors/libincidenceeditors5/" src/Messages.sh


%build
%cmake_kf5

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html


%ldconfig_scriptlets

%files -f %{name}.lang
%license LICENSES/*
%{_kf5_datadir}/qlogging-categories5/*%{framework}.*
%{_kf5_libdir}/libKPim5IncidenceEditor.so.*

%files devel
%{_kf5_archdatadir}/mkspecs/modules/qt_IncidenceEditor.pri
%{_includedir}/KPim5/IncidenceEditor/
%{_kf5_libdir}/cmake/KPim5IncidenceEditor/
%{_kf5_libdir}/libKPim5IncidenceEditor.so


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 23.08.5-6
- Prepare for Oreon 11 (RP1)
