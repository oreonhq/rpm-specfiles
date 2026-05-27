%global source0_hash none

%undefine __cmake_in_source_build


# 
ExcludeArch: %{ix86}

Name:    kmplot
Summary: Mathematical Function Plotter 
Version: 26.04.1
Release: 1%{?dist}

License: GPL-2.0-or-later
URL:     https://cgit.kde.org/%{name}.git
Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gettext
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: kf6-rpm-macros
BuildRequires: extra-cmake-modules

BuildRequires: git
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6TextWidgets)

# when split occurred
Conflicts: kdeedu-math < 4.7.0-10

%description
%{summary}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1


%build
%cmake_kf6 \
	-DQT_MAJOR_VERSION=6

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html --with-man --with-qt


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop


%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_datadir}/config.kcfg/%{name}.kcfg
%{_kf6_plugindir}/parts/%{name}part.so
%{_datadir}/dbus-1/interfaces/org.kde.%{name}.*.xml
%{_mandir}/man1/kmplot.*


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.04.1-1
- Import
