%global source0_hash 051801ee3d9704bb254332e7a317c228a510a5b83ff0304937011148b0212311

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:           massif-visualizer
Summary:        Visualizer for Massif heap memory profiler data files
Version:        25.12.3
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/massif_visualizer/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

Requires:       kf6-filesystem

BuildRequires:  kf6-rpm-macros
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  libappstream-glib
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KChart6)

BuildRequires:  cmake(KGraphViewerPart) >= 2.5.0

BuildRequires:  shared-mime-info

%description
Massif Visualizer is a tool that visualizes massif data.

You run your application in Valgrind with "--tool=massif" and then open the
generated "massif.out.<pid>" in the visualizer. Gzip or Bzip2 compressed massif
files can also be opened transparently.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/*.appdata.xml
%find_lang %{name} --with-kde

%files -f %{name}.lang
%{_kf6_bindir}/massif-visualizer
%{_kf6_datadir}/mime/packages/massif.xml
%{_kf6_datadir}/applications/org.kde.massif-visualizer.desktop
%{_kf6_datadir}/config.kcfg/massif-visualizer-settings.kcfg
%{_kf6_datadir}/icons/hicolor
%{_kf6_datadir}/massif-visualizer/icons/hicolor/22x22/actions/shortentemplates.png
%{_kf6_metainfodir}/org.kde.massif-visualizer.appdata.xml
%license COPYING
%doc AUTHORS

%changelog
%autochangelog
