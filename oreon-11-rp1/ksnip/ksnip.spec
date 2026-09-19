%global source0_hash 41fa6a54b0a88095ccdf7f8f3a96617e91fb15dcedae2aadaf2ee24677e9a88c

Name: ksnip
Version: 1.10.1
Release: 9%{?dist}

License: GPL-2.0-or-later
Summary: Qt based cross-platform screenshot tool
URL: https://github.com/%{name}/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Workaround to Wayland issues: https://github.com/ksnip/ksnip/pull/457
Patch100: %{name}-wayland-workaround.patch

BuildRequires: cmake(kColorPicker-Qt5)
BuildRequires: cmake(kImageAnnotator-Qt5)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5XmlPatterns)

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: ninja-build

Requires: hicolor-icon-theme

%description
Ksnip is a Qt based cross-platform screenshot tool that provides
many annotation features for your screenshots.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i 's/find_package(kImageAnnotator/find_package(kImageAnnotator-Qt5/g' CMakeLists.txt
sed -i 's/find_package(kColorPicker/find_package(kColorPicker-Qt5/g' CMakeLists.txt
sed -i 's/kColorPicker::kColorPicker/kColorPicker::kColorPicker-Qt5/g' src/CMakeLists.txt

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

%files -f %{name}.lang
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_metainfodir}/*.appdata.xml

%changelog
%autochangelog
