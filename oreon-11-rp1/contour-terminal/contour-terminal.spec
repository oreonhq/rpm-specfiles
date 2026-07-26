%global source0_hash 0018f111530ffb5fc669fdd9e400f730156c4d8cfd03ec9e06da555d6bc921e5

Name:           contour-terminal
Version:        0.6.2.8008
Release:        %autorelease
Summary:        Modern C++ Terminal Emulator
License:        Apache-2.0
URL:            https://github.com/contour-terminal/contour
Source:         %{url}/archive/v%{version}/contour-%{version}.tar.gz
Patch0:         https://github.com/contour-terminal/contour/pull/1855.patch

ExclusiveArch:  x86_64 aarch64

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fmt-devel
BuildRequires:  guidelines-support-library-devel
BuildRequires:  range-v3-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  libxcb-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libutempter-devel
BuildRequires:  pkgconfig(libssh2)

BuildRequires:  libunicode-devel
BuildRequires:  cmake(boxed-cpp)
BuildRequires:  cmake(reflection-cpp)

# provides tic
BuildRequires:  ncurses

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  catch-devel

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6CorePrivate)
BuildRequires:  cmake(Qt6WaylandClientPrivate)
BuildRequires:  wayland-devel

Requires:       qt6-qt5compat
Requires:       hicolor-icon-theme
Requires:       kf6-filesystem
Requires:       ncurses-term

%description
Contour is a modern and actually fast, modal, virtual terminal emulator,
for everyday use. It is aiming for power users with a modern feature mindset.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -C

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCONTOUR_TESTING=ON
%cmake_build

%install
%cmake_install

rm %{buildroot}%{_datadir}/contour/LICENSE.txt
rm %{buildroot}%{_datadir}/contour/README.md
# already included in ncurses-term package
rm %{buildroot}%{_datadir}/terminfo/c/contour

%check
%ctest
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/contour
%{_datadir}/applications/*.desktop
%{_datadir}/kio/servicemenus/*.desktop
%dir %{_datadir}/contour
%dir %{_datadir}/contour/shell-integration
%{_datadir}/contour/shell-integration/shell-integration.bash
%{_datadir}/contour/shell-integration/shell-integration.fish
%{_datadir}/contour/shell-integration/shell-integration.tcsh
%{_datadir}/contour/shell-integration/shell-integration.zsh
%{_datadir}/icons/hicolor/*/apps/*.png
%{_metainfodir}/*.xml

%changelog
%autochangelog
