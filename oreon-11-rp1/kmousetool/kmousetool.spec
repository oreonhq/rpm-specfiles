%global source0_hash 3eafbd2c38a2b767963824f081b8d22f55381b1b51fed3a17a44e4dc1c05a6de

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kmousetool
Version: 25.12.3
Release: 1%{?dist}
Summary: A program that clicks the mouse for you

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://apps.kde.org/kmousetool/
Source:  https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6DocTools)

BuildRequires: pkgconfig(xt)
BuildRequires: pkgconfig(xtst)

%description
A program for people whom it hurts to click the mouse.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html --with-man

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop ||:

%files -f %{name}.lang
%doc AUTHORS ChangeLog README TODO
%license LICENSES/*
%{_kf6_bindir}/kmousetool
%{_kf6_datadir}/kmousetool/
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_mandir}/man1/*.1*

%changelog
%autochangelog
