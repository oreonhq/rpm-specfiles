# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 9e907499a6087406601c1559a90f6551ef557ef4642371355929c6ed12188dee
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# kstars FTB on i686
ExcludeArch:    %{ix86}

Name:    kstars
Summary: Desktop Planetarium
Version: 3.8.0
Release: 5%{?dist}

# We have to use epoch now, KStars is no longer part of KDE Applications and
# uses its own (lower) version now
# https://community.kde.org/Applications/17.12_Release_Notes#Tarballs_that_we_do_not_ship_anymore
Epoch:   1

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://edu.kde.org/kstars
%global kf5_dl_bug %(echo %{version} | cut -d. -f3)
%if 0%{?kf5_dl_bug} >= 50
%global kf5_dl_stable unstable
%else
%global kf5_dl_stable stable
%endif

Source0: https://download.kde.org/%{kf5_dl_stable}/%{name}/%{version}/%{name}-%{version}.tar.xz

## upstream patches


## Fedora specific patches
# https://bugs.kde.org/show_bug.cgi?id=512890
Patch102: a0a11a9250d8072f0d7dd083dad90cdd8a459020.patch
Patch101: kstars-2.9.6-fix-compilerflag-exceptions.patch

BuildRequires: desktop-file-utils
BuildRequires: kf6-rpm-macros
BuildRequires: extra-cmake-modules
BuildRequires: gettext

BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6OpenGL)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6DataVisualization)
BuildRequires: cmake(Qt6WebSockets)
BuildRequires: cmake(Qt6Keychain)

BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Bookmarks)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6DNSSD)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6NotifyConfig)
BuildRequires: cmake(KF6Plotting)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6TextEditor)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)

BuildRequires: libappstream-glib
BuildRequires: libnova-devel
BuildRequires: LibRaw-devel
BuildRequires: libcurl-devel
BuildRequires: pkgconfig(cfitsio)
BuildRequires: pkgconfig(eigen3)
BuildRequires: pkgconfig(gsl)
BuildRequires: pkgconfig(wcslib)
BuildRequires: zlib-devel
BuildRequires: pkgconfig(libindi) >= 1.5.0
BuildRequires: pkgconfig(libxisf)
BuildRequires: pkgconfig(opencv)
BuildRequires: stellarsolver-devel >= 1.9

%if 0%{?fedora}
BuildRequires: xplanet
%endif

# Require libindi to enable Ekos properly
Requires:  libindi 
# astrometry is useful for astrophotography with KStars, not required for
# usage as planetarium
Suggests:  astrometry
%if 0%{?fedora}
Requires:  xplanet
%endif


# when split occurred
Obsoletes: kdeedu-kstars < 4.7.0-10
Obsoletes: kdeedu-kstars-libs < 4.7.0-10
Provides:  kdeedu-kstars = %{epoch}:%{version}-%{release}

%description
KStars is a Desktop Planetarium.  It provides an accurate graphical
simulation of the night sky, from any location on Earth, at any date and
time.  The display includes up to 100 million stars, 13,000 deep-sky objects,
all 8 planets, the Sun and Moon, and thousands of comets and asteroids.


%prep
%oreon_verify_sources
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

## unpackaged files
rm -fv %{buildroot}%{_kf6_libdir}/libhtmesh.a

%check
# primarily care about validation on fedora only
# (ie, generally, if fedora is ok, then so is epel7)
%if 0%{?fedora}
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kstars.appdata.xml
%endif
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kstars.desktop


%if 0%{?rhel} && 0%{?rhel} < 8
%post
touch --no-create %{_kf6_datadir}/icons/hicolor  &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_kf6_datadir}/icons/hicolor &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
touch --no-create %{_kf6_datadir}/icons/hicolor &> /dev/null || :
gtk-update-icon-cache %{_kf6_datadir}/icons/hicolor &> /dev/null || :
fi
%endif

%files -f %{name}.lang
%license LICENSES/*
%doc AUTHORS ChangeLog README.* TODO
%{_kf6_bindir}/kstars
%{_kf6_metainfodir}/org.kde.kstars.appdata.xml
%{_kf6_datadir}/applications/org.kde.kstars.desktop
%{_kf6_datadir}/config.kcfg/kstars.kcfg
%{_kf6_datadir}/knotifications6/kstars.notifyrc
%{_kf6_datadir}/sounds/KDE-KStars-*
%{_kf6_datadir}/kstars/
%{_kf6_datadir}/icons/hicolor/*/*/*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.8.0-5
- Prepare for Oreon 11 (RP1)
