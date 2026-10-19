%global source0_hash cd90514e16ad9d647791357aec9c4769cb096fb3cdfb910014f450c47613eb13
%undefine __cmake_in_source_build
%global framework kmediaplayer
Name:    kf5-%{framework}
Version: 5.116.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 3 module with interface for media player features
License: X11
URL:     https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kparts-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
%description
KDE Frameworks 5 Tier 3 module with plugin interfaces for media player features.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kparts-devel >= %{majmin}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

%build

%{cmake_kf5}
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-kmediaplayer-devel -f %{oreon_filedir}/kf5-kmediaplayer-devel.list

%changelog

%autochangelog
