%global source0_hash e58ca61c9d7963892ef9aef8d0b82f88b7e9e9be7a35b137ee1aa2d82030eabd
ExcludeArch:    %{ix86}
Name:    kstars
Summary:        Desktop Planetarium
Version: 3.8.4.1
Release:        1%{?dist}
Epoch:   1
License: GPL-2.0-or-later
URL:     http://edu.kde.org/kstars
%global kf5_dl_bug %(echo %{version} | cut -d. -f3)
%if 0%{?kf5_dl_bug} >= 50
%global kf5_dl_stable unstable
%else
%global kf5_dl_stable stable
%endif
Source0:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
Patch102: a0a11a9250d8072f0d7dd083dad90cdd8a459020.patch
Patch101: kstars-2.9.6-fix-compilerflag-exceptions.patch
Requires:  libindi 
Suggests:  astrometry
Obsoletes: kdeedu-kstars < 4.7.0-10
Obsoletes: kdeedu-kstars-libs < 4.7.0-10
Provides:  kdeedu-kstars = %{epoch}:%{version}-%{release}
# oreon:deps
BuildRequires:  LibRaw-devel
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Bookmarks)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DNSSD)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6Plotting)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Qt6DataVisualization)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebSockets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  libcurl-devel
BuildRequires:  libnova-devel
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libindi)
BuildRequires:  pkgconfig(libxisf)
BuildRequires:  pkgconfig(opencv)
BuildRequires:  pkgconfig(wcslib)
BuildRequires:  stellarsolver-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
KStars is a Desktop Planetarium.  It provides an accurate graphical
simulation of the night sky, from any location on Earth, at any date and
time.  The display includes up to 100 million stars, 13,000 deep-sky objects,
all 8 planets, the Sun and Moon, and thousands of comets and asteroids.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

# installs into the wrong location
sed -i 's/${DATA_INSTALL_DIR}/${KSTARS_DATADIR}/'  kstars/data/fr/CMakeLists.txt
sed -i 's/${DATA_INSTALL_DIR}/${KSTARS_DATADIR}/'  kstars/data/nds/CMakeLists.txt

%build

%{cmake_kf6} \
   -DBUILD_WITH_QT6:BOOL=ON
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
rm -fv %{buildroot}%{_kf6_libdir}/libhtmesh.a
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kstars.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
