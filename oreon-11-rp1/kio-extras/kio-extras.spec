%global source0_hash 3adb4f9189b4b91d57b78d0a894868d8382451134bcfcc4f235027f23db13b3d
%global stable_kf6 stable
Name:    kio-extras
Version: 26.08.0
Release:        1%{?dist}
Summary:        Additional components to increase the functionality of KIO Framework
License: GPL-2.0-or-later
URL:     https://invent.kde.org/network/kio-extras
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Supplements:    kf6-kio-core
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  cmake(KDSoap)
BuildRequires:  cmake(KDSoapWSDiscoveryClient)
BuildRequires:  cmake(KExiv2Qt6)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DNSSD)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(OpenEXR)
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(PlasmaActivitiesStats)
BuildRequires:  cmake(QCoro6)
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  extra-cmake-modules
BuildRequires:  gperf
BuildRequires:  kf6-rpm-macros
BuildRequires:  libjpeg-devel
BuildRequires:  libmtp-devel
BuildRequires:  libsmbclient-devel
BuildRequires:  libssh-devel
BuildRequires:  openexr-devel
BuildRequires:  perl-generators
BuildRequires:  phonon-qt6-devel
BuildRequires:  pkgconfig(libimobiledevice-1.0)
BuildRequires:  pkgconfig(libplist-2.0)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  taglib-devel
# /oreon:deps
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
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_kf6 -DLIBSSH_LIBRARIES="$(pkg-config --libs libssh)"
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kio-extras-info -f %{oreon_filedir}/kio-extras-info.list
%files -n kio-extras-devel -f %{oreon_filedir}/kio-extras-devel.list
