%global source0_hash 247ccc7bcc4277e2fc63a753c367d0ca10efe3b4916f60a44d9ca2da403c4fe5

Name:           kunifiedpush
Version:        26.04.3
Release:        2%{?dist}
Summary:        UnifiedPush client library and distributor daemon
License:        BSD-2-Clause AND CC0-1.0 AND BSD-3-Clause AND LGPL-2.0-or-later
URL:            https://invent.kde.org/libraries/kunifiedpush

Source :        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  desktop-file-utils
# Qt dependencies
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebSockets)
BuildRequires:  cmake(Qt6DBus)
# KF dependencies
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6Crash)

BuildRequires:  openssl-devel

%description
%{summary}.

%package devel
Summary:        %{name} development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Required headers to build components based
on %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6 -DKDE_INSTALL_SYSTEMDUSERUNITDIR=%{_userunitdir}
%cmake_build

%install
%cmake_install
%find_lang kcm_push_notifications

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/kcm_push_notifications.desktop

%files -f kcm_push_notifications.lang
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKUnifiedPush.so.%{version}
%{_kf6_libdir}/libKUnifiedPush.so.1
%{_bindir}/kunifiedpush-distributor
%{_sysconfdir}/xdg/autostart/org.kde.kunifiedpush-distributor.desktop
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_push_notifications.so
%{_kf6_datadir}/applications/kcm_push_notifications.desktop
%{_sysconfdir}/xdg/KDE/kunifiedpush-distributor.conf
%{_kf6_datadir}/qlogging-categories6/org_kde_kunifiedpush.categories
%{_userunitdir}/graphical-session.target.wants/kunifiedpush-distributor.service
%{_userunitdir}/kunifiedpush-distributor.service

%files devel
%{_kf6_libdir}/libKUnifiedPush.so
%{_includedir}/KUnifiedPush/
%{_kf6_libdir}/cmake/KUnifiedPush/

%changelog
%autochangelog

