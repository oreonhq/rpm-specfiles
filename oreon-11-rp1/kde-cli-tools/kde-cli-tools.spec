%global source1_hash 94c6118e6edec4aa2e6f095022490735ae7611847b73cef775dfea43c097541a
%global source0_hash 18f3c421b305003caf73f9e9fbec09fbf30f472dbe81fec328046cca7883a31d
%global stable_kf6 stable
Name:    kde-cli-tools
Version:        6.7.5
Release:        1%{?dist}
Summary:        Tools based on KDE Frameworks 5 to better interact with the system
License: Artistic-2.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig
Requires:       libkworkspace6%{?_isa} >= %{version}
Requires:       kdesu = 1:%{version}-%{release}
Conflicts: kde-runtime < 17.08.3-23
# oreon:deps
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Su)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  plasma-workspace-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
# /oreon:deps
%description
Provides several KDE and Plasma specific command line tools to allow
better interaction with the system.

%package -n kdesu
Summary: Runs a program with elevated privileges
Epoch: 1
Conflicts: kde-runtime < 14.12.3-2
Conflicts: kde-runtime-docs < 14.12.3-2
%description -n kdesu
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang kdeclitools_qt --with-qt --with-kde --all-name
ln -s %{_kf6_libexecdir}/kdesu %{buildroot}%{_bindir}/kdesu
%oreon_autofiles kdesu usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n kdesu -f %{oreon_filedir}/kdesu.list

%changelog

%autochangelog
