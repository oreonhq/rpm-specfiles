%global source0_hash 70d7ae368b1522dcaced130dd3fa49e552a794c80c819c92700cb0776ab5d385

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    ksystemlog
Summary: System Log Viewer for KDE
Version: 25.12.3
Release: 1%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://apps.kde.org/ksystemlog/
Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstreamable patches

## downstream patches
# fix ksystemlog to find log files in fedora locations
Patch1: ksystemlog-21.12.2-fedora.patch

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: cmake(Qt6Network)

BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6Crash)

BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(audit)

%description
This program is developed for beginner users, who don't know how to find
information about their Linux system, and don't know where log files are.

It is also of course designed for advanced users, who quickly want to understand
problems of their machine with a more powerful and graphical tool than tail -f
and less commands.

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
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.ksystemlog.appdata.xml

%files -f %{name}.lang
%license LICENSES
%{_kf6_bindir}/ksystemlog
%{_kf6_datadir}/applications/org.kde.ksystemlog.desktop
%{_kf6_datadir}/qlogging-categories6/ksystemlog.categories
%{_kf6_metainfodir}/org.kde.ksystemlog.appdata.xml

%changelog
%autochangelog
