%global source0_hash 3adb4f9189b4b91d57b78d0a894868d8382451134bcfcc4f235027f23db13b3d
%if !0%{?bootstrap}
%endif
Name:    kio-extras-kf5
Version: 26.08.0
Release:        1%{?dist}
Summary:        Additional components to increase the functionality of KIO Framework
License: GPL-2.0-or-later
URL:     https://invent.kde.org/network/kio-extras
%global srcname kio-extras
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{srcname}-%{version}.tar.xz
%if 0%{?tests}
%endif
Recommends: qt5-qtimageformats%{?_isa}
Recommends: (icoutils if wine-core)
Supplements: kf5-kio-core
# oreon:deps
BuildRequires:  OpenEXR-devel
BuildRequires:  bzip2-devel
BuildRequires:  cmake(KDSoap)
BuildRequires:  cmake(KF5ActivitiesStats)
BuildRequires:  cmake(KF5KExiv2)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  dbus-x11
BuildRequires:  extra-cmake-modules
BuildRequires:  gperf
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
BuildRequires:  libjpeg-devel
BuildRequires:  libmtp-devel
BuildRequires:  libsmbclient-devel
BuildRequires:  libssh-devel
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
BuildRequires:  qt6-qtbase-devel
BuildRequires:  taglib-devel
BuildRequires:  time
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  zlib-devel
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

%autosetup -p1 -n %{srcname}-%{version}

%build

%cmake_kf5 \
  -DLIBSSH_LIBRARIES="$(pkg-config --libs libssh)" \
  %{?tests:-DBUILD_TESTING:BOOL=ON}
%cmake_build
%install
%cmake_install
%find_lang %{srcname} --all-name --with-html
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a dbus-launch --exit-with-session \
time make test -C %{_target_platform} ARGS="--output-on-failure --timeout 10" ||:
%endif
%files -f %{oreon_filedir}/main.list
%files -n kio-extras-kf5-info -f %{oreon_filedir}/kio-extras-kf5-info.list
%files -n kio-extras-kf5-devel -f %{oreon_filedir}/kio-extras-kf5-devel.list

%changelog

%autochangelog
