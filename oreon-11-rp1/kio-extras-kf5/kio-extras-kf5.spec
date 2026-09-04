%global source0_hash a9aaf58f3b802c8341bba1ceb95054f915059ea447f59ffc7b933cca71b12ac9

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
#global tests 1
%endif

Name:    kio-extras-kf5
Version: 26.08.0
Release: 1%{?dist}
Summary: Additional components to increase the functionality of KIO Framework

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://invent.kde.org/network/kio-extras

%global srcname %{name}

Source0: http://download.kde.org/%{stable_kf5}/release-service/%{version}/src/%{srcname}-%{version}.tar.xz

## upstramable patches

## upstream patches

BuildRequires:  bzip2-devel
BuildRequires:  gperf

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kactivities-devel
BuildRequires:  kf5-karchive-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-kdnssd-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-khtml-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kpty-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-solid-devel
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(KF5ActivitiesStats)
BuildRequires:  cmake(KF5KExiv2)

BuildRequires:  cmake(KDSoap) >= 1.9
BuildRequires:  libjpeg-devel
BuildRequires:  libmtp-devel
BuildRequires:  libsmbclient-devel
BuildRequires:  libssh-devel
%if 0%{?fedora} > 33
# As of 2.5.x openexr is cmake based.
BuildRequires:  cmake(OpenEXR)
%else
BuildRequires:  OpenEXR-devel
%endif
BuildRequires:  openslp-devel
BuildRequires:  perl-generators
BuildRequires:  phonon-qt5-devel
BuildRequires:  pkgconfig(libimobiledevice-1.0)
BuildRequires:  pkgconfig(libplist-2.0)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  taglib-devel > 1.11
BuildRequires:  zlib-devel

%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: time
BuildRequires: xorg-x11-server-Xvfb
%endif

# helpful for  imagethumbnail plugin
Recommends: qt5-qtimageformats%{?_isa}
# .exe/.ico previews, will limit dep to only if wine-core is installed for now -- rdieter
Recommends: (icoutils if wine-core)

Supplements: kf5-kio-core

%description
%{summary}.

%package info
Summary: Info kioslave
%description info
Kioslave for reading info pages.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%cmake_kf5 \
  -DLIBSSH_LIBRARIES="$(pkg-config --libs libssh)" \
  %{?tests:-DBUILD_TESTING:BOOL=ON}

%cmake_build

%install
%cmake_install

%find_lang %{srcname} --all-name --with-html

%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a dbus-launch --exit-with-session \
time make test -C %{_target_platform} ARGS="--output-on-failure --timeout 10" ||:
%endif

%files -f %{srcname}.lang
%dir %{_kf5_plugindir}/kded
%dir %{_kf5_plugindir}/kio/
%dir %{_kf5_plugindir}/kiod/

%license LICENSES/*

%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_datadir}/kservicetypes5/thumbcreator.desktop
%{_kf5_datadir}/qlogging-categories5/kio-extras*

%{_kf5_libdir}/libkioarchive.so.5{,.*}

%{_kf5_libexecdir}/smbnotifier

%{_kf5_plugindir}/kded/filenamesearchmodule.so
%{_kf5_plugindir}/kded/recentdocumentsnotifier.so
%{_kf5_plugindir}/kded/smbwatcher.so
%{_kf5_plugindir}/kfileitemaction/kactivitymanagerd_fileitem_linking_plugin.so
%{_kf5_plugindir}/kfileitemaction/forgetfileitemaction.so
%{_kf5_plugindir}/kio/activities.so
%{_kf5_plugindir}/kio/afc.so
%{_kf5_plugindir}/kio/archive.so
%{_kf5_plugindir}/kio/filter.so
%{_kf5_plugindir}/kio/fish.so
%{_kf5_plugindir}/kio/kio_filenamesearch.so
%{_kf5_plugindir}/kio/man.so
%{_kf5_plugindir}/kio/mtp.so
%{_kf5_plugindir}/kio/nfs.so
%{_kf5_plugindir}/kio/recentdocuments.so
%{_kf5_plugindir}/kio/recentlyused.so
%{_kf5_plugindir}/kio/sftp.so
%{_kf5_plugindir}/kio/smb.so
%{_kf5_plugindir}/kio/thumbnail.so
%{_kf5_plugindir}/kiod/kmtpd.so
%{_kf5_plugindir}/thumbcreator/*.so

%{_kf5_qtplugindir}/kfileaudiopreview.so

%files info
%{_kf5_plugindir}/kio/info.so

%files devel
%{_includedir}/KioArchive/*.h
# no soname symlink? --rex
#{_kf5_libdir}/libkioarchive.so
%{_kf5_libdir}/cmake/KioArchive/

%changelog
* Fri Sep 04 2026 Brandon Lester <boostyconnect@oreonproject.org> - 26.08.0-1
- Latest upstream release

%autochangelog
