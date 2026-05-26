Name:           gcompris-qt
Version:        26.1
Release:        1%{?dist}
Summary:        Educational software suite for children aged 2 to 10

License:        AGPL-3.0-only
URL:            http://gcompris.net
Source0:        https://download.kde.org/stable/gcompris/qt/src/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/gcompris/qt/src/%{name}-%{version}.tar.xz.sig
# Download from https://collaborate.kde.org/s/8GpWjyHg5xBTQFS
Source2:        0x63d7264c05687d7e.asc
# oreon url source checksums begin
%global source0_sha256 c389b863b29f012ccc1b3eef740982ff6c7654c13a2e343397ee466124f31339
%global source0_file gcompris-qt-26.1.tar.xz
# oreon url source checksums end

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Sensors)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickControls2Basic)
BuildRequires:  cmake(Qt6QuickTemplates2)
BuildRequires:  cmake(Qt6Graphs)
BuildRequires:  cmake(Qt6Quick3D)
BuildRequires:  cmake(Qt6QmlWorkerScript)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  wayland-devel
BuildRequires:  openssl-devel
BuildRequires:  kf6-kdoctools-devel
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
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
# see REUSE.toml for disambiguation
License:        GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND MPL-2.0 AND LicenseRef-Public-Domain AND CC0-1.0 AND CC-BY-SA-4.0 AND CC-BY-4.0 AND CC-BY-3.0 AND GFDL-1.2-or-later AND OFL-1.1 AND Unlicense
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description activities
This package contains the bundle of activities for %{name}.
More than 100 activities are available.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/gcompris-qt-26.1.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "c389b863b29f012ccc1b3eef740982ff6c7654c13a2e343397ee466124f31339" || { echo "oreon: Source0 SHA256 mismatch for gcompris-qt-26.1.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' \
  --data='%{SOURCE0}'
%autosetup


%build
# qml-box2d in not available in Fedora
%cmake_kf6 \
  -DQML_BOX2D_MODULE=disabled \
  -DBUILD_SERVER=OFF
%cmake_build


%install
%cmake_install

# Validate desktop file
desktop-file-validate \
   %{buildroot}%{_datadir}/applications/org.kde.gcompris.desktop

# Validate AppData file
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.gcompris.appdata.xml

%find_lang %{name} --all-name --with-qt --with-html


%files -f %{name}.lang
%{_kf6_bindir}/%{name}
%dir %{_kf6_datadir}/%{name}
%{_kf6_metainfodir}/org.kde.gcompris.appdata.xml
%{_kf6_datadir}/applications/org.kde.gcompris.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%license LICENSES/AGPL-3.0-only.txt LICENSES/GPL-3.0-or-later.txt
%doc README 

%files activities
%{_kf6_datadir}/%{name}/rcc
%license LICENSES/AGPL-3.0-only.txt LICENSES/GPL-3.0-or-later.txt


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.1-1
- Import
