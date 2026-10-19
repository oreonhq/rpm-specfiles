%global source0_hash 9d85ba25c159f15dc0e794366bcf5d2f401b6313004ee621409f35bb664ae368
%global framework kdewebkit
Name:    kf5-%{framework}
Version: 5.116.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 3 integration module for QtWebKit
License: LicenseRef-Callaway-LGPLv2+
URL:     https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
Patch0: revert_feature_summary_ecm.patch
# oreon:deps
BuildRequires:  cmake(Qt5UiPlugin)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kjobwidgets-devel
BuildRequires:  kf5-kparts-devel
BuildRequires:  kf5-kservice-devel
BuildRequires:  kf5-kwallet-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtwebkit-devel
# /oreon:deps
%description
KDE Frameworks 5 Tier 3 integration module for the HTML rendering engine WebKit.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtwebkit-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

%build

%cmake_kf5
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-kdewebkit-devel -f %{oreon_filedir}/kf5-kdewebkit-devel.list

%changelog

%autochangelog
