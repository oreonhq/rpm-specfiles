%global source0_hash 9e25e61104bdbe73ccde056db920303ef8cf1ac632f3365e0bd099cc7fee71a1

Name:    hotspot
Version: 1.5.1
Release: 8%{?dist}
Summary: The Linux perf GUI for performance analysis

License: GPL-2.0-or-later
URL:     https://github.com/KDAB/hotspot

Source0: https://github.com/KDAB/%{name}/releases/download/v%{version}/%{name}-v%{version}.tar.gz
Source1: https://github.com/KDAB/hotspot/releases/download/v%{version}/hotspot-perfparser-v%{version}.tar.gz
Source2: https://github.com/KDAB/hotspot/releases/download/v%{version}/hotspot-PrefixTickLabels-v%{version}.tar.gz

# Fix build with Qt 6.9
Patch: https://github.com/KDAB/hotspot/pull/694.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(libelf)
BuildRequires:  elfutils-devel
BuildRequires:  rust-zstd-devel
BuildRequires:  librustc_demangle-devel

Recommends:     binutils
Requires:       hicolor-icon-theme
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  cmake(KF6ThreadWeaver)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KDDockWidgets-qt6)
BuildRequires:  pkgconfig(qcustomplot-qt6)
BuildRequires:  cmake(KGraphViewerPart)
BuildRequires:  cmake(Qt6Svg)

Provides:       bundled(hotspot-perfparser)
Provides:       bundled(hotspot-PrefixTickLabels)

%description
A standalone GUI for performance data. Attempting to provide a UI like
KCachegrind around Linux perf.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name} -a 1 -a 2
%autopatch -p1
mv perfparser/* 3rdparty/perfparser/
mv PrefixTickLabels/* 3rdparty/PrefixTickLabels/

%build
%cmake_kf6 -DQT6_BUILD=TRUE
%cmake_build

%install
%cmake_install
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/com.kdab.hotspot.desktop

%files
%license LICENSE.GPL.txt
%{_kf6_bindir}/hotspot
%{_kf6_datadir}/icons/hicolor/*/*/hotspot*
%{_libexecdir}/hotspot-perfparser
%{_kf6_datadir}/applications/com.kdab.hotspot.desktop
%{_kf6_metainfodir}/com.kdab.Hotspot.appdata.xml
%{_kf6_datadir}/knotifications6/hotspot.notifyrc

%changelog
%autochangelog
