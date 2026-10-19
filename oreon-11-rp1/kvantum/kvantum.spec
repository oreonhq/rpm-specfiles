%global source2_hash 7d0bd6933af334b2a61f9e25496f6be2f34c26a881619819e0cfc7e3db691682
%global source0_hash 7aa9099345e48048ebdad768f583944ac042f87b216fa0b26a169c7e05425047
%global _vpath_srcdir Kvantum
%bcond  qt5           1
Name:           kvantum
Version:        1.1.8
Release:        1%{?dist}
Summary:        SVG-based theme engine for Qt, KDE and LXQt
License:        GPL-3.0-or-later
URL:            https://github.com/tsujan/Kvantum
Source0:        https://github.com/tsujan/%{_vpath_srcdir}/releases/download/V%{version}/%{_vpath_srcdir}-%{version}.tar.xz
Source1:        %{url}/releases/download/V%{version}/Kvantum-%{version}.tar.xz.asc
Source2:        https://github.com/tsujan.gpg
%if %{with qt5}
%endif
Requires:       hicolor-icon-theme
Requires:       %{name}-data = %{version}-%{release}
Requires:       qt6qml(org.kde.desktop)
%if %{with qt5}
Recommends:     (%{name}-qt5 if qt5-qtbase-gui)
%endif
Provides:  kvantum-qt6 = %{version}-%{release}
Obsoletes: kvantum-qt6 < 1.1.0
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  kde-filesystem
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
# /oreon:deps
%description
Kvantum is an SVG-based theme engine for Qt, tuned to KDE and LXQt, with an
emphasis on elegance, usability and practicality.

Kvantum has a default dark theme, which is inspired by the default theme of
Enlightenment. Creation of realistic themes like that for KDE was the first
reason to make Kvantum but it goes far beyond its default theme: you could
make themes with very different looks and feels for it, whether they be
photorealistic or cartoonish, 3D or flat, embellished or minimalistic, or
something in between, and Kvantum will let you control almost every aspect of
Qt widgets.

Kvantum also comes with many other themes that are installed as root and can
be selected and activated by using Kvantum Manager.

%if %{with qt5}
%package qt5
Summary:   SVG-based theme engine for Qt5
Requires:  %{name}-data = %{version}-%{release}
%description qt5
Kvantum is an SVG-based theme engine for Qt, tuned to KDE and LXQt, with an
emphasis on elegance, usability and practicality.

This package contains the Qt5 integration plugin.
%endif

%package data
Summary:    SVG-based theme engine for Qt5, KDE and LXQt
BuildArch:  noarch
%description data
Kvantum is an SVG-based theme engine for Qt, tuned to KDE and LXQt, with an
emphasis on elegance, usability and practicality.

This package contains the data needed Kvantum.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n Kvantum-%{version}

%build

%if %{with qt5}
%global _vpath_builddir %{_target_platform}-qt5
%cmake -DENABLE_QT5:BOOL=ON
%cmake_build
%endif
%global _vpath_builddir %{_target_platform}-qt6
%cmake \
    -DENABLE_QT5:BOOL=OFF \
%cmake_build
%install
%if %{with qt5}
%global _vpath_builddir %{_target_platform}-qt5
%cmake_install
%endif
%global _vpath_builddir %{_target_platform}-qt6
%cmake_install
sed -i "s|LXQt|X-LXQt|" %{buildroot}%{_datadir}/applications/kvantummanager.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/kvantummanager.desktop
%find_lang %{name} --all-name --with-qt
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n kvantum-qt5 -f %{oreon_filedir}/kvantum-qt5.list
%files -n kvantum-data -f %{oreon_filedir}/kvantum-data.list

%changelog

%autochangelog
