%global source0_hash 41fa6a54b0a88095ccdf7f8f3a96617e91fb15dcedae2aadaf2ee24677e9a88c
Name: ksnip
Version: 1.10.1
Release:        9%{?dist}
License: GPL-2.0-or-later
Summary:        Qt based cross-platform screenshot tool
URL: https://github.com/%{name}/%{name}
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch100: %{name}-wayland-workaround.patch
Requires: hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5XmlPatterns)
BuildRequires:  cmake(kColorPicker-Qt5)
BuildRequires:  cmake(kImageAnnotator-Qt5)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  ninja-build
# /oreon:deps
%description
Ksnip is a Qt based cross-platform screenshot tool that provides
many annotation features for your screenshots.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i 's/find_package(kImageAnnotator/find_package(kImageAnnotator-Qt5/g' CMakeLists.txt
sed -i 's/find_package(kColorPicker/find_package(kColorPicker-Qt5/g' CMakeLists.txt

%build

%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTS:BOOL=OFF
%cmake_build
%check

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%install
%cmake_install
%find_lang %{name} --with-qt
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
