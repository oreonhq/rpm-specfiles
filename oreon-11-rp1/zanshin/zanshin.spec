%global stable_kf6 stable
%global source0_hash 4df387da010b1875f73052849634df03bed453b62d0a01e8131d37ba5865cbd2
ExcludeArch: %{ix86}
Name:           zanshin
Version:        25.12.3
Release:        1%{?dist}
Summary:        Todo/action management software
License:        CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND MIT
URL:            http://zanshin.kde.org/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}
Provides: zanshin-frontend = %{version}-%{release}
Requires: zanshin-common = %{version}-%{release}
Obsoletes: renku < %{version}
Provides: zanshin = %{version}-%{release}
Requires: kdepim-runtime
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Runner)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6AkonadiCalendar)
BuildRequires:  cmake(KPim6IdentityManagementCore)
BuildRequires:  cmake(KPim6KontactInterface)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
# /oreon:deps
%description
Zanshin Todo is a powerful yet simple application for managing your day to day
actions. It helps you organize and reduce the cognitive pressure of what one has
to do in his job and personal life. You'll never forget anything anymore,
getting your mind like water.

%package common
Summary: common files for %{name}
Requires: zanshin-frontend = %{version}-%{release}
BuildArch: noarch
%description common
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop
%files -f %{oreon_filedir}/main.list
%files -n zanshin-common -f %{oreon_filedir}/zanshin-common.list

%changelog

%autochangelog
