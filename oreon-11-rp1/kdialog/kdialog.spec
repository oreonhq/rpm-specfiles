%global stable_kf6 stable

Name:    kdialog
Summary: Nice dialog boxes from shell scripts
Version: 25.12.3
Release: 1%{?dist}

# Automatically converted from old format: GPLv2+ and GFDL - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:     https://www.kde.org/

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6DBusAddons)

BuildRequires: cmake(Qt6DBus)

%description
KDialog can be used to show nice dialog boxes from shell scripts.


%prep
%autosetup -p1


%build
%cmake_kf6

%cmake_build


%install
%cmake_install

%find_lang %{name} --with-html --with-man


%files -f %{name}.lang
%license COPYING*
%{_kf6_bindir}/kdialog
%{_kf6_bindir}/kdialog_progress_helper
%{_kf6_datadir}/dbus-1/interfaces/org.kde.kdialog.ProgressDialog.xml
%{_kf6_datadir}/applications/org.kde.kdialog.desktop
%{_kf6_metainfodir}/org.kde.kdialog.metainfo.xml


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
