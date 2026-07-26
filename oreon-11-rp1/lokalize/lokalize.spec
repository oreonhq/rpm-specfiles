%global source0_hash f62c5c1116d0fa8c7c3d24b1b642060bc3a0fddc6aa65218f375303de4191e8e

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    lokalize
Summary: Computer-aided translation system
Version: 25.12.3
Release: 1%{?dist}

License: BSD-3-Clause AND GFDL-1.2-or-later AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.1-or-later
URL:     https://invent.kde.org/sdk/%{name}

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Test)

BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KDDockWidgets-qt6)

BuildRequires: pkgconfig(hunspell)

## fixme
# aka python-unversioned-command
Requires: /usr/bin/python
Requires: python3-dbus
Requires: gettext
# odf2xliff
Requires: translate-toolkit
Recommends: poxml
Recommends: subversion

%description
Computer-aided translation system focusing on productivity and performance

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6 \
  -DBUILD_TESTING:BOOL=%{?tests}%{!?tests:0}

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

# Add Comment key to .desktop file
grep '^Comment=' %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop || \
desktop-file-install \
  --dir=%{buildroot}%{_kf6_datadir}/applications \
  --set-comment="%{summary}" \
  %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/qlogging-categories6/%{name}*
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_datadir}/%{name}/
%{_kf6_datadir}/knotifications6/%{name}.notifyrc
%{_kf6_datadir}/config.kcfg/%{name}.kcfg

%changelog
%autochangelog
