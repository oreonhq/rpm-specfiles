%global source0_hash f75ad6da8d9b867ed24d7275333902269983d094d06a32971d6c929cd6523306
%global stable_kf6 stable
%global majmin_ver_kf6 26.03
Name:    parley
Summary:        Vocabulary Trainer
Version: 26.08.1
Release:        1%{?dist}
License: GPL-2.0-or-later
URL:     https://apps.kde.org/parley/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}
Recommends: translate-shell
# oreon:deps
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  libkeduvocdocument-devel
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html --with-man
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
