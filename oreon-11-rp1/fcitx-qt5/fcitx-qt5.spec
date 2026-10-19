%global source0_hash 951fcf8f1db23ed22ad91094eb4c6c906f92005a3643b52f666bd8a331163147
%global project_name FcitxQt5
Name:           fcitx-qt5
Version:        1.2.7
Release:        1%{?dist}
Summary:        Fcitx IM module for Qt5
License:        GPL-2.0-or-later AND LicenseRef-Callaway-BSD
URL:            https://github.com/fcitx/fcitx-qt5
Source0:        https://download.fcitx-im.org/%{name}/%{name}-%{version}.tar.xz
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
%filter_provides_in %{_qt5_plugindir}/platforminputcontexts/libfcitxplatforminputcontextplugin.so
%filter_provides_in %{_libdir}/fcitx/qt/libfcitx-quickphrase-editor5.so
%filter_setup
# oreon:deps
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx-devel
BuildRequires:  gettext-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
# /oreon:deps
%description
This package provides Fcitx Qt5 input context.

%package devel
Summary:        Development files for fcitx-qt5
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake
%description devel
The %{name}-devel package contains libraries and header files necessary for
developing programs using fcitx-qt5 libraries.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%cmake
%cmake_build
%install
%cmake_install
%find_lang %{name}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n fcitx-qt5-devel -f %{oreon_filedir}/fcitx-qt5-devel.list

%changelog

%autochangelog
