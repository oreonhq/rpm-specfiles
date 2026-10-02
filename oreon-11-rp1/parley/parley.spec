%global source0_hash f75ad6da8d9b867ed24d7275333902269983d094d06a32971d6c929cd6523306

%global stable_kf6 stable
%global majmin_ver_kf6 26.03


Name:    parley
Summary: Vocabulary Trainer
Version: 26.08.1
Release: 1%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://apps.kde.org/parley/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6WebEngineWidgets)

BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Notifications)

BuildRequires: libkeduvocdocument-devel >= %{majmin_ver_kf6}
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libxslt)

Recommends: translate-shell

%description
%{summary}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1


%build
%cmake_kf6

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html --with-man

## unpackaged files


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop


%files -f %{name}.lang
%license LICENSES/*
#doc README
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/knsrcfiles/%{name}*.knsrc
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}*
%{_kf6_datadir}/icons/oxygen/*/*/*
%{_kf6_datadir}/%{name}/
%{_kf6_datadir}/config.kcfg/*.kcfg


%changelog
%autochangelog
