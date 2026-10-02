%global source0_hash b96194c68ef67ac3127cf353f026b5b69d35c7d5e204bd89d1155c74f2fe073a

Name:           xwaylandvideobridge
Version:        0.5.3
Release:        1%{?dist}
Summary:        Utility to allow streaming Wayland windows to X applications

License:        (GPL-2.0-only or GPL-3.0-only) and LGPL-2.0-or-later and BSD-3-Clause
URL:            https://invent.kde.org/system/xwaylandvideobridge
Source0:        https://download.kde.org/stable/%{name}/src/%{name}-%{version}.tar.xz

Patch0:         xwaylandvideobridge-fix-build-against-qt-6-10.patch

BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  cmake >= 3.16
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-record)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  cmake(KPipeWire) >= 6.0.0

Requires:       hicolor-icon-theme

%description
By design, X11 applications can't access window or screen contents
for wayland clients. This is fine in principle, but it breaks screen
sharing in tools like Discord, MS Teams, Skype, etc and more.

This tool allows us to share specific windows to X11 clients,
but within the control of the user at all times.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version} -p1


%build
%cmake_kf6 \
    -DQT_MAJOR_VERSION=6
%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop


%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/qlogging-categories6/%{name}.categories
%{_sysconfdir}/xdg/autostart/org.kde.%{name}.desktop


%changelog
%autochangelog
