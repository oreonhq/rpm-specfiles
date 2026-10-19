%global source0_hash df60cf57b12d559a68767557933e355fd34a862e0443279d3e6613ee35807394
%global framework incidenceeditor
ExcludeArch: %{ix86}
Name:    kf5-%{framework}
Version: 23.08.5
Release:        1%{?dist}
Summary:        KDE PIM library for creating and editing calendar incidences
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://invent.kde.org/pim/%{framework}
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/stable/release-service/%{version}/src/%{framework}-%{version}.tar.xz
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}
%global majmin_ver %{version}
Obsoletes:      kdepim-libs < 7:16.04.0
Conflicts:      kdepim-libs < 7:16.04.0
# oreon:deps
BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KGantt)
BuildRequires:  cmake(KPim5Akonadi)
BuildRequires:  cmake(KPim5AkonadiMime)
BuildRequires:  cmake(KPim5CalendarSupport)
BuildRequires:  cmake(KPim5CalendarUtils)
BuildRequires:  cmake(KPim5EventViews)
BuildRequires:  cmake(KPim5Ldap)
BuildRequires:  cmake(KPim5Libkdepim)
BuildRequires:  cmake(KPim5MailTransport)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-akonadi-mime-devel
BuildRequires:  kf5-akonadi-server-devel
BuildRequires:  kf5-eventviews-devel
BuildRequires:  kf5-kcalendarcore-devel
BuildRequires:  kf5-kcalendarutils-devel
BuildRequires:  kf5-kmailtransport-devel
BuildRequires:  kf5-libkdepim-devel
BuildRequires:  kf5-pimcommon-devel
BuildRequires:  kf5-rpm-macros
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-incidenceeditor-devel -f %{oreon_filedir}/kf5-incidenceeditor-devel.list

%changelog

%autochangelog
