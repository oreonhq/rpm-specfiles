%global source0_hash 4b14d942e338cdc36c1b37067c19f77359f1d967cd56661e018cef83205ca192

%bcond_without  use_qt6
%bcond_with     bundle_lxqtwallet
%bcond_without  bundle_tcplay
%global srcname zuluCrypt

Name:           zulucrypt
Version:        7.1.0
Release:        4%{?dist}
Summary:        Qt GUI front end to cryptsetup

# More details available in the copyright file in the source tarball.
# Major license is GPLv2+ (but GPLv3+ for some files)
# BSD for zuluwallet and dependencies lxqt_wallet and tcplay (at least tcplay is always bundled)
# CRC32 for a file in tcplay
# generic-xts for a part of tcplay
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND BSD-2-clause AND BSD-3-clause AND generic-xts AND LicenseRef-Fedora-UltraPermissive
URL:            https://mhogomchungu.github.io/zuluCrypt
Source0:        https://github.com/mhogomchungu/zuluCrypt/archive/%{version}/%{name}-%{version}.tar.gz

# polkit policy stolen from Debian, https://github.com/marciosouza20/zulucrypt
Source10:      zulucrypt-gui.policy
Source11:      zulumount-gui.policy

BuildRequires:  gcc gcc-c++

BuildRequires:  kf5-rpm-macros

# These are only needed for building the lxqt-wallet bundled library
%if %{with bundle_lxqtwallet}
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5Notifications)
%endif

%if %{with use_qt6}
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Widgets)
%else
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
%endif

BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(devmapper)
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(ossp-uuid)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(libcryptsetup)

BuildRequires:  libgcrypt-devel

BuildRequires:  desktop-file-utils

# upstream: 'extended the "personal" copy of the library in incompatible ways'
%if %{with bundle_tcplay}
Provides:       bundled(tcplay) = 2.0
%else
#BuildRequires:  tcplay-devel >= 2.0
%endif

# NB: LXQT version 4.0.0 is only built with QT6
%if %{with bundle_lxqtwallet}
# Version 6.2.0 bundles lxqt-wallet 3.2.2
Provides:       bundled(lxqt-wallet) = 3.2.0
%else
BuildRequires:  pkgconfig(lxqt-wallet) >= 4.0.0
%endif

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-console%{?_isa} = %{version}-%{release}

# ownership of top folders we place files in
Requires:       polkit
Requires:       hicolor-icon-theme
Requires:       shared-mime-info

# optional support for ecryptfs
%if %{?fedora}
Suggests:       ecryptfs-simple
%endif

%description
zuluCrypt is a front end to cryptsetup. It makes it easier to use cryptsetup
by providing a Qt-based GUI and a simpler to use CLI frontend to cryptsetup.
It does the same thing truecrypt does but without licensing problems or
requiring a user to setup sudo for it or presenting root's password.
This package contains the applications.

%package console
Summary:        Console tools of %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description console
This package contains the console (CLI) frontends of zuluCrypt. Those got
split into an own subpackage to provide possible independence from Qt as some
minimum.

%package libs
Summary:        Library for %{name}

%description libs
This package contains libraries that provide higher level access to
cryptsetup API and provide mounting/unmounting API to easy opening and
closing of volume.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains development files and libraries
necessary to build programs around zuluCrypt.

%package doc
Summary:        Additional documentation files for %{name}
BuildArch:      noarch

%description doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

# Documentation later with %%doc
mv 'ABOUT ME' AUTHORS
sed -i /docs/d CMakeLists.txt
# Drop rpath, https://fedoraproject.org/wiki/Packaging:Guidelines#Beware_of_Rpath
# better use CMAKE_SKIP_INSTALL_RPATH=ON, https://fedorahosted.org/fpc/ticket/641
#find . -name CMakeLists.txt |xargs sed -i /INSTALL_RPATH/d
# Handle zuluSafe as a GUI application, binary needs Qt
sed -i -r 's:(zuluSafe)-cli:\1:g' CMakeLists.txt zuluSafe/CMakeLists.txt zuluSafe-cli.1
mv zuluSafe-cli.1 zuluSafe.1

%if %{without bundle_lxqtwallet}
rm -rf %{srcname}-gui/lxqt_wallet
%endif
%if %{without bundle_tcplay}
rm -rf external_libraries/tc-play
#sed -i -r 's:(STATIC_TCPLAY ").*":\1false":' CMakeLists.txt
%endif

%build
%{cmake_kf5} \
 -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name} \
 -DCMAKE_SKIP_INSTALL_RPATH=ON \
 -DREUSEMOUNTPOINT=false \
 -DUDEVSUPPORT=true \
 -DNOGUI=false \
%if %{with use_qt6}
 -DBUILD_WITH_QT6=true \
%else
 -DQT5=true \
%endif
 -DHOMEMOUNTPREFIX=false \
 -DNOGNOME=false \
 -DNOKDE=false \
 -DUSE_POLKIT=true \
 %{nil}
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt --all-name
%if 0%{?rhel}
# Explicitly create folders in epel, install does not know target option
#mkdir -p %{buildroot}%{_datadir}/polkit-1/actions
%endif
install -p -m0644 -t %{buildroot}%{_datadir}/polkit-1/actions -D %{SOURCE10} %{SOURCE11}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/zulu*.desktop

%ldconfig_scriptlets libs

%files -f %{name}.lang
%{_bindir}/zuluCrypt-gui
%{_bindir}/zuluMount-gui
%{_bindir}/zuluPolkit
%{_bindir}/zuluSafe
# Specific GUI plugins stored to libdir, need Qt
%{_libdir}/%{srcname}/
%{_datadir}/applications/zulu*.desktop
%{_datadir}/icons/hicolor/*/apps/zulu*.png
%{_datadir}/icons/zulu*.png
%{_datadir}/pixmaps/zulu*.png
%{_mandir}/man1/zulu*-gui.1*
%{_mandir}/man1/zuluSafe.1*
%{_datadir}/polkit-1/actions/*.policy
%{_datadir}/mime/packages/*.xml
# find_lang does not care about subfolders
%dir %{_datadir}/%{srcname}
%dir %{_datadir}/%{srcname}/translations
%dir %{_datadir}/%{srcname}/translations/zulu*-gui

%files console
%{_bindir}/zuluCrypt-cli
%{_bindir}/zuluMount-cli
%{_mandir}/man1/zulu*-cli.1*

%files libs
%license COPYING GPLv* LICENSE
%doc AUTHORS *README* TODO changelog
%{_libdir}/lib%{srcname}*.so.*

%files devel
%{_includedir}/%{srcname}/
%{_libdir}/lib%{srcname}*.so
%{_libdir}/pkgconfig/libzulu*.pc

%files doc
%license COPYING GPLv* LICENSE
%doc docs/*.pdf
%doc docs/README docs/*.jpg

%changelog
%autochangelog
