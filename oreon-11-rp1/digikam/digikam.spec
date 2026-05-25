%bcond_with build_with_qt6
%if 0%{?fedora} > 39 || 0%{?rhel} > 9 || 0%{?oreon}
%bcond_without build_with_qt6
ExclusiveArch: %{qt6_qtwebengine_arches}
%else
ExclusiveArch: %{qt5_qtwebengine_arches}
%endif

# use ninja or not
%global ninja 1

#global beta rc

Name:    digikam
Summary: A digital camera accessing & photo management application
Version: 9.0.0
Release: 5%{?beta}%{?dist}

License: GPL-2.0-or-later
URL:     http://www.digikam.org/
%if 0%{?beta:1}
Source0: http://download.kde.org/unstable/digikam/digikam-%{version}-%{beta}.tar.xz
%else
Source0: http://download.kde.org/stable/digikam/%{version}/digiKam-%{version}.tar.xz
%endif

# rawhide s390x is borked recently
#ExcludeArch: s390x

# digiKam not listed as a media handler for pictures in Nautilus (#516447)
# TODO: upstream me
Source10: digikam-import.desktop

## upstream patches
Patch0: https://invent.kde.org/graphics/digikam/-/commit/9dd5e992b71b6a855fc419114344d4bd181bc08f.patch

## upstreamable patches

%if 0%{?ninja}
BuildRequires: ninja-build
%endif

BuildRequires: boost-devel
BuildRequires: eigen3-devel
BuildRequires: desktop-file-utils
BuildRequires: doxygen
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: gcc-c++
BuildRequires: ImageMagick-devel
BuildRequires: ImageMagick-c++-devel >= 6.7
BuildRequires: libjpeg-devel
BuildRequires: libtiff-devel
BuildRequires: perl-generators
BuildRequires: pkgconfig(exiv2) >= 0.26
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(jasper)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(libjxl)
BuildRequires: pkgconfig(libgphoto2_port) pkgconfig(libusb-1.0) pkgconfig(libusb)
BuildRequires: pkgconfig(libpng) >= 1.2.7
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(x11) pkgconfig(xproto)
%if %{with build_with_qt6}
BuildRequires: cmake(Qt6NetworkAuth)
BuildRequires: cmake(Qt6OpenGL)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6StateMachine)
BuildRequires: cmake(Qt6WebEngineWidgets)
BuildRequires: cmake(KSaneCore6)
BuildRequires: cmake(KSaneWidgets6)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6FileMetaData)
BuildRequires: cmake(KF6CalendarCore)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6NotifyConfig)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(KF6ThreadWeaver)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6Bookmarks)
BuildRequires: kf6-rpm-macros
BuildRequires: qt6-qtbase-private-devel
%else
BuildRequires: pkgconfig(Qt5NetworkAuth)
BuildRequires: pkgconfig(Qt5OpenGL)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: pkgconfig(Qt5XmlPatterns)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5WebEngine)
BuildRequires: cmake(KSaneCore)
BuildRequires: kf5-libksane-devel >= 16.03
BuildRequires: kf5-kcalendarcore-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-kfilemetadata-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kitemmodels-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kservice-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-karchive-devel
BuildRequires: kf5-threadweaver-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-knotifyconfig-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-solid-devel
BuildRequires: kf5-sonnet-devel
BuildRequires: kf5-kitemviews-devel
BuildRequires: kf5-kbookmarks-devel
BuildRequires: kf5-rpm-macros
%endif

## not actually checked-for or used -- rex
## rely on explicit cmake build options instead
#BuildRequires: mariadb-devel mariadb-server
## DNG converter
BuildRequires: expat-devel
## htmlexport plugin
BuildRequires: pkgconfig(libxslt)
## RemoveRedeye
BuildRequires: pkgconfig(opencv) >= 3.3
# Panorama plugin requires flex and bison
BuildRequires: flex
BuildRequires: bison
%if 0%{?fedora} || 0%{?rhel} > 8 || 0%{?oreon}
BuildRequires: pkgconfig(libheif)
BuildRequires: pkgconfig(lqr-1)
# MediaPlayer dependencies
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavdevice)
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libswscale)
BuildRequires: pkgconfig(libva)
BuildRequires: pkgconfig(xext)
%endif
BuildRequires: pkgconfig(lensfun) >= 0.2.6
BuildRequires: pkgconfig(libpgf) >= 6.12.24

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

Recommends: perl-Image-ExifTool
# expoblending assistant
Recommends: hugin-base
#Recommends: kf5-kipi-plugins
# thumbnailers, better default access to mtp-enabled devices
Recommends: kio-extras
%if %{with build_with_qt6}
Recommends: qt6-qtbase-mysql%{?_isa}
Recommends: qt6-qtimageformats%{?_isa}
%else
Recommends: qt5-qtbase-mysql%{?_isa}
Recommends: qt5-qtimageformats%{?_isa}
%endif

# core/libs/rawengine/libraw/
Provides: bundled(LibRaw) = 0.22.0

# no more DocBook documentation
# Sphinx documentation is published in a dedicated web site
# https://docs.digikam.org/en/index.html
Provides: %{name}-doc = %{version}-%{release}
Obsoletes: %{name}-doc < 8.0.0-3

%description
digiKam is an easy to use and powerful digital photo management application,
which makes importing, organizing and manipulating digital photos a "snap".
An easy to use interface is provided to connect to your digital camera,
preview the images and download and/or delete them.

digiKam built-in image editor makes the common photo correction a simple task.

%package libs
Summary: Runtime libraries for %{name}
# not *strictly* required, but nice -- rdieter
# see also https://bugzilla.redhat.com/show_bug.cgi?id=1973495
Recommends: %{name} = %{version}-%{release}
%description libs
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
This package contains the libraries, include files and other resources
needed to develop applications using %{name}.


%prep
%autosetup -n %{name}-%{version}%{?beta:-%{beta}} -p1

%build
%if %{with build_with_qt6}
%cmake_kf6 \
  -DBUILD_WITH_QT6:BOOL=ON \
%else
%cmake_kf5 \
%endif
  %{?ninja:-G Ninja} \
  -DENABLE_APPSTYLES:BOOL=ON \
  -DENABLE_KFILEMETADATASUPPORT:BOOL=ON \
%if 0%{?rhel} && 0%{?rhel} < 9 || 0%{?oreon}
  -DENABLE_MEDIAPLAYER:BOOL=OFF \
%endif
  -DENABLE_MYSQLSUPPORT:BOOL=ON \
  -DENABLE_INTERNALMYSQL:BOOL=ON

%cmake_build


%install
%cmake_install

desktop-file-install --vendor="" \
  --dir=%{buildroot}%{_datadir}/applications/ \
  %{SOURCE10}

%find_lang %{name}


%check
for i in %{buildroot}%{_datadir}/applications/*.desktop ; do
desktop-file-validate $i ||:
done

%if 0%{?rhel} && 0%{?rhel} < 8 || 0%{?oreon}
%post
touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/hicolor &> /dev/null
  gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
  update-desktop-database -q &> /dev/null
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
update-desktop-database -q &> /dev/null
%endif


%ldconfig_scriptlets libs


%if %{with build_with_qt6}
%files -f %{name}.lang
%doc AUTHORS ChangeLog
%doc NEWS README.md
%license LICENSES/GPL-2.0-or-later.txt
%{_kf6_bindir}/digikam
%{_kf6_bindir}/digitaglinktree
%{_kf6_bindir}/cleanup_digikamdb
%{_kf6_bindir}/showfoto
%{_kf6_datadir}/kxmlgui5/digikam/
%{_kf6_datadir}/kxmlgui5/showfoto/
%{_kf6_datadir}/knotifications6/digikam.notifyrc
%{_kf6_datadir}/digikam/
%{_kf6_datadir}/showfoto/
%{_kf6_datadir}/solid/actions/digikam*.desktop
%{_kf6_metainfodir}/org.kde.digikam.appdata.xml
%{_kf6_metainfodir}/org.kde.showfoto.appdata.xml
%{_kf6_datadir}/applications/digikam-import.desktop
%{_kf6_datadir}/applications/org.kde.digikam.desktop
%{_kf6_datadir}/applications/org.kde.showfoto.desktop
%{_mandir}/man1/digitaglinktree.1*
%{_mandir}/man1/cleanup_digikamdb.1*
%{_kf6_datadir}/icons/hicolor/*/*/*

%files libs
%{_kf6_libdir}/libdigikamcore.so.*
%{_kf6_libdir}/libdigikamdatabase.so.*
%{_kf6_libdir}/libdigikamgui.so.*
%{_kf6_qtplugindir}/digikam/

%files devel
%{_kf6_libdir}/libdigikamcore.so
%{_kf6_libdir}/libdigikamdatabase.so
%{_kf6_libdir}/libdigikamgui.so
%{_kf6_libdir}/cmake/Digikam*/
%{_includedir}/digikam/

%else
%files -f %{name}.lang
%doc AUTHORS ChangeLog
%doc NEWS README.md
%license LICENSES/GPL-2.0-or-later.txt
%{_kf5_bindir}/digikam
%{_kf5_bindir}/digitaglinktree
%{_kf5_bindir}/cleanup_digikamdb
%{_kf5_bindir}/showfoto
%{_kf5_datadir}/kxmlgui5/digikam/
%{_kf5_datadir}/kxmlgui5/showfoto/
%{_kf5_datadir}/knotifications5/digikam.notifyrc
%{_kf5_datadir}/digikam/
%{_kf5_datadir}/showfoto/
%{_kf5_datadir}/solid/actions/digikam*.desktop
%{_kf5_metainfodir}/org.kde.digikam.appdata.xml
%{_kf5_metainfodir}/org.kde.showfoto.appdata.xml
%{_kf5_datadir}/applications/digikam-import.desktop
%{_kf5_datadir}/applications/org.kde.digikam.desktop
%{_kf5_datadir}/applications/org.kde.showfoto.desktop
%{_mandir}/man1/digitaglinktree.1*
%{_mandir}/man1/cleanup_digikamdb.1*
%{_kf5_datadir}/icons/hicolor/*/*/*

%files libs
%{_kf5_libdir}/libdigikamcore.so.*
%{_kf5_libdir}/libdigikamdatabase.so.*
%{_kf5_libdir}/libdigikamgui.so.*
%{_kf5_qtplugindir}/digikam/

%files devel
%{_kf5_libdir}/libdigikamcore.so
%{_kf5_libdir}/libdigikamdatabase.so
%{_kf5_libdir}/libdigikamgui.so
%{_kf5_libdir}/cmake/Digikam*/
%{_includedir}/digikam/
%endif


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9.0.0-5
- Import
