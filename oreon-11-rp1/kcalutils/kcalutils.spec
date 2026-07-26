%global source0_hash 8d54dfef43b7929c9d9b52ba2b6234f94537923e4ff94984611bf7489502a234

Name:    kcalutils
Version: 25.12.3
Release: 1%{?dist}
Summary: The KCalendarUtils Library

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{name}

Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF6TextEditTextToSpeech)

BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KPim6IdentityManagementCore)
BuildRequires:  cmake(Qt6Core)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons)
Requires:       cmake(KF6CalendarCore)
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

%autosetup -n %{name}-%{version} -p1

# Remove together with move-translations.patch once released
find ./po -type f -name libkcalutils5.po -execdir mv {} libkcalutils6.po \;

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6CalendarUtils.so.*
%{_kf6_qtplugindir}/kf6/ktexttemplate/kcalendar_grantlee_plugin.so

%files devel
%{_includedir}/KPim6/KCalUtils/
%{_kf6_libdir}/libKPim6CalendarUtils.so
%{_kf6_libdir}/cmake/KPim6CalendarUtils/
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch

%changelog
%autochangelog
