%global source0_hash 455785712a32f0dba7947a314eb99065d902ac6c432947e9e699a44ca18c70a1

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    calendarsupport
Version: 25.12.3
Release: 1%{?dist}
Summary: KDE PIM library for calendar and event handling

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://invent.kde.org/pim/%{name}

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
# available only where kf6-pimcommon is
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake

BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6PrintSupport)

BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KPim6CalendarUtils)
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KPim6IdentityManagementCore)
BuildRequires:  cmake(KF6Holidays)
BuildRequires:  cmake(KPim6AkonadiCalendar)
BuildRequires:  cmake(KPim6AkonadiNotes)
BuildRequires:  cmake(KF6TextCustomEditor)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KPim6Mime)
Requires:       cmake(KPim6IdentityManagementCore)
Requires:       cmake(KPim6AkonadiCalendar)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6CalendarSupport.so.*

%files devel
%{_includedir}/KPim6/CalendarSupport/
%{_kf6_libdir}/cmake/KPim6CalendarSupport/
%{_kf6_libdir}/libKPim6CalendarSupport.so
%{_qt6_docdir}/*.tags
 
%files doc
%{_qt6_docdir}/*.qch

%changelog
%autochangelog
