%global source0_hash 5a8f5cd6ae8fa8f29dada3808417a51c355e4e3077b1063152324d9406cd25e5

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    palapeli
Summary: A jigsaw puzzle game
Version: 25.12.3
Release: 1%{?dist}

# Automatically converted from old format: GPLv2+ and GFDL - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:     https://invent.kde.org/games/%{name}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: extra-cmake-modules
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6XmlGui)

%global majmin_ver %(echo %{version} | cut -d. -f1,2)
BuildRequires: libkdegames-devel >= %{majmin_ver}

BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Test)

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

# needs the qvoronoi executable from qhull
%if !0%{?bootstrap}
BuildRequires: qhull
%endif
Requires: qhull

Conflicts: kde-l10n < 17.08.3-2

%description
Palapeli is a single-player jigsaw puzzle game. The object of the
game is to assemble the given pieces to an image.

%package libs
Summary: Runtime libraries for %{name}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.

%package devel
Summary: Development files for %{name} 
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake_kf6

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%license LICENSES/*
%license src/pics/LICENSE
%doc slicers/goldberg/README
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/qlogging-categories6/%{name}*
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/%{name}/
%{_kf6_datadir}/knotifications6/%{name}*
%{_kf6_datadir}/mime/packages/%{name}*.xml
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_sysconfdir}/xdg/palapeli-collectionrc
%{_kf6_datadir}/kio/servicemenus/palapeli_servicemenu.desktop

%ldconfig_scriptlets libs

%files libs
%{_kf6_libdir}/libpala.so.*
%{_qt6_plugindir}/palapelislicers/
%{_kf6_plugindir}/thumbcreator/palathumbcreator.so

%files devel
%{_includedir}/Pala/
%{_kf6_libdir}/libpala.so
%{_kf6_libdir}/cmake/Pala/

%changelog
%autochangelog
