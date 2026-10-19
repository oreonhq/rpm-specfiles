%global source0_hash ccd4677ca5ee509de3dc4cf2e4c4c192ccc6ed33f614f89ba24fea0d883e8917
%global gitcommit_full 5bfa8fa9c880db2374c75d2d25107da3926b8f29
%global gitcommit %(c=%{gitcommit_full}; echo ${c:0:7})
%global date 20220606
Name:           fancontrol-gui
Version:        0.8
Release:        1%{?dist}
Summary:        GUI for fancontrol
License:        GPL-2.0-or-later
URL:            https://github.com/Maldela/fancontrol-gui
Source0:        https://github.com/Maldela/%{name}/tarball/%{gitcommit_full}
Requires:       lm_sensors
Requires:       hicolor-icon-theme
Requires:       dbus-common
Requires:       polkit
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF5Auth)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Package)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib
# /oreon:deps
%description
GUI for fancontrol which is part of lm_sensors.
It uses the KAuth module of the KDE Frameworks 5 to write the
generated config file. Furthermore it communicates with systemd
via dbus to control the fancontrol service.

%package        kcm
Summary:        KCM for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       plasma-settings
Requires:       kf5-filesystem
Requires:       kf5-kcmutils
%description    kcm
KCM for %{name}.

%package        plasmoid
Summary:        Plasmoid for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       plasma-workspace
Requires:       kf5-filesystem
%description    plasmoid
Plasmoid for %{name}.

%prep

%autosetup -n Maldela-%{name}-%{gitcommit}

%build

%cmake_kf5 -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_KCM=on -DBUILD_PLASMOID=on
%cmake_build
%install
%cmake_install
%find_lang fancontrol_kcm --all-name
sed -i '/icon/d' %{buildroot}%{_metainfodir}/org.kde.fancontrol.gui.appdata.xml
sed -i '/icon/d' %{buildroot}%{_metainfodir}/org.kde.fancontrol.kcm.appdata.xml
sed -i '/icon/d' %{buildroot}%{_metainfodir}/org.kde.fancontrol.plasmoid.appdata.xml
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.fancontrol.gui.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.kde.fancontrol.*.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n fancontrol-gui-kcm -f %{oreon_filedir}/fancontrol-gui-kcm.list
%files -n fancontrol-gui-plasmoid -f %{oreon_filedir}/fancontrol-gui-plasmoid.list

%changelog

%autochangelog
