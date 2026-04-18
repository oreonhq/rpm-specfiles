Name:           kwrited
Version:        6.6.3
Release:        2%{?dist}
Summary:        KDE daemon for wall and write messages
License:        GPL-2.0-or-later
URL:            https://invent.kde.org/plasma/kwrited
Source0:        https://download.kde.org/stable/plasma/%{version}/kwrited-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  ninja-build
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Pty)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)

Requires:       kf6-filesystem

%description
%{summary}.


%prep
%autosetup -n kwrited-%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install


%files
%license LICENSES/*
%{_kf6_bindir}/kwrited
%{_sysconfdir}/xdg/autostart/kwrited-autostart.desktop
%{_kf6_datadir}/knotifications6/kwrited.notifyrc


%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.3-2
- Add kwrited for Plasma workspace
