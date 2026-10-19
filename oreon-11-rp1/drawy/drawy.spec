%global source0_hash c1df7f3a9f113b00b1a77a3906a956dfbfa4d9c0c08d29f278a83ae782dd906a
%define rdnn        org.kde.drawy
%define commit      6387aa20ef967ee1a4f922009dfe1aaf13519574
%global shortcommit %{sub %{commit} 1 7}
Name:           drawy
Version:        1.0.0~^3.%{shortcommit}
Release:        1%{?dist}
Summary:        Your handy, infinite, brainstorming tool
License:        GPL-3.0-or-later AND OFL-1.1
URL:            https://invent.kde.org/graphics/drawy
Source0:        https://invent.kde.org/graphics/%{name}/-/archive/%{commit}/%{name}-6387aa2.tar.gz
ExcludeArch:    %{ix86}
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(libzstd)
# /oreon:deps
%description
Drawy is a work-in-progress infinite whiteboard tool written in Qt/C++, which
aims to be a native-desktop alternative to the amazing web-based Excalidraw.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n drawy-%{commit}

%conf
%cmake -DCMAKE_BUILD_TYPE=Release

%build

%cmake_build
%install
%cmake_install
%find_lang %{name} --with-qt
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{rdnn}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{rdnn}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
