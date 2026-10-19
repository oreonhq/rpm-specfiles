%global source2_hash 17f50c051df19926b09872abe99d51a211e54c87b840c674433084da2464cd7b
%global source1_hash 1b896e2053d775e9c9e072fa0fcc41180b8322591d5aecb99afc75aeca4ce2ec
%global source0_hash 8d80e78d1c59b4a06df3bb55427fb9fcdec14109f3793cf39ab7ea6aa10c286b
Name:    hotspot
Version: 1.6.0
Release:        1%{?dist}
Summary:        The Linux perf GUI for performance analysis
License: GPL-2.0-or-later
URL:     https://github.com/KDAB/hotspot
Source0:        https://github.com/KDAB/%{name}/releases/download/v%{version}/%{name}-v%{version}.tar.gz
Source1: https://github.com/KDAB/hotspot/releases/download/v%{version}/hotspot-perfparser-v%{version}.tar.gz
Source2: https://github.com/KDAB/hotspot/releases/download/v%{version}/hotspot-PrefixTickLabels-v%{version}.tar.gz
Patch: https://github.com/KDAB/hotspot/pull/694.patch
Recommends:     binutils
Requires:       hicolor-icon-theme
Provides:       bundled(hotspot-perfparser)
Provides:       bundled(hotspot-PrefixTickLabels)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KDDockWidgets-qt6)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6ThreadWeaver)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KGraphViewerPart)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  desktop-file-utils
BuildRequires:  elfutils-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  librustc_demangle-devel
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(qcustomplot-qt6)
BuildRequires:  rust-zstd-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
