%global source0_hash c53935393cc080665ce5e8bd79d3ce2eece4abad9efd2eafa21ae7ac4399e909

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:           isoimagewriter
Version:        25.12.3
Release:        1%{?dist}
Summary:        KDE ISO Image Writer, a tool to write a .iso file to a USB disk

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://apps.kde.org/isoimagewriter/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# General build time stuff
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib

# Libs
BuildRequires:  cmake(Gpgmepp)
BuildRequires:  cmake(QGpgmeQt6)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6NetworkPrivate)
BuildRequires:  cmake(Qt6DBusPrivate)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6TestPrivate)
BuildRequires:  cmake(Qt6CorePrivate)
BuildRequires:  cmake(Qt6WidgetsPrivate)
BuildRequires:  pkgconfig(libudev)

# KF5
BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6Solid)

%description
The KDE ISO Image Writer is a tool to write a .iso file to a USB disk.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

%check
appstream-util validate-relax --nonet \
    %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml

desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%license LICENSES/*
%{_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/org.kde.%{name}.*
%{_kf6_datadir}/%{name}
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml

%changelog
%autochangelog
