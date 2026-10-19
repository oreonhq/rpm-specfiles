%global source2_hash 2eae0f8247d2cc46063e51836f94f6cd962091976fd86dc64377b5617c0f0298
%global source1_hash eeea49f016246f2e89b26925305f4a71cbc5394bde6c4f23d7e1011ea3c1e2c7
%global source0_hash f876239f39397f554006f4218a3c229627e2af4317a8765ecf9462f0058dfcb4
Name:           gcompris-qt
Version:        26.2
Release:        1%{?dist}
Summary:        Educational software suite for children aged 2 to 10
License:        AGPL-3.0-only
URL:            http://gcompris.net
Source0:        https://download.kde.org/stable/gcompris/qt/src/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/gcompris/qt/src/%{name}-%{version}.tar.xz.sig
Source2:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x63D7264C05687D7E#/0x63d7264c05687d7e.asc
Requires:       qt6-qtmultimedia
Requires:       qt6-qtdeclarative
Requires:       qt6-qtsvg
Requires:       qt6-qtimageformats
Requires:       qt6-qtgraphs
Requires:       qt6-qtsensors
Requires:       qt6-qtwayland
Requires:       hicolor-icon-theme
Requires:       %{name}-activities = %{version}-%{release}
Obsoletes:      gcompris <= 15.10-16
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Graphs)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlWorkerScript)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Quick3D)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickControls2Basic)
BuildRequires:  cmake(Qt6QuickTemplates2)
BuildRequires:  cmake(Qt6Sensors)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  kf6-kdoctools-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  openssl-devel
BuildRequires:  wayland-devel
# /oreon:deps
%description
GCompris-Qt is an educational software suite comprising
of numerous activities for children aged 2 to 10. Some of the
activities are game orientated, but nonetheless still educational.

Currently, GCompris offers in excess of 100 activities. New
activities can be added, and an activity can implement its own game
scheme.

This version is a rewrite of GCompris using the QtQuick
technology.

%package activities
Summary:        Activity files for %{name}
License:        GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND MPL-2.0 AND LicenseRef-Public-Domain AND CC0-1.0 AND CC-BY-SA-4.0 AND CC-BY-4.0 AND CC-BY-3.0 AND GFDL-1.2-or-later AND OFL-1.1 AND Unlicense
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description activities
This package contains the bundle of activities for %{name}.
More than 100 activities are available.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' \
  --data='%{SOURCE0}'
%autosetup

%build

%cmake_kf6 \
  -DQML_BOX2D_MODULE=disabled \
  -DBUILD_SERVER=OFF
%cmake_build
%install
%cmake_install
desktop-file-validate \
   %{buildroot}%{_datadir}/applications/org.kde.gcompris.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.gcompris.appdata.xml
%find_lang %{name} --all-name --with-qt --with-html
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gcompris-qt-activities -f %{oreon_filedir}/gcompris-qt-activities.list

%changelog

%autochangelog
