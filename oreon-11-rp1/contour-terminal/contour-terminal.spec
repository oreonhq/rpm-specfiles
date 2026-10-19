%global source0_hash 9afaaed7f705c56e413938f43d338c7700ca69122a531d94c10c8eb9f5a44c28
Name:           contour-terminal
Version:        0.7.0.8982
Release:        1%{?dist}
Summary:        Modern C++ Terminal Emulator
License:        Apache-2.0
URL:            https://github.com/contour-terminal/contour
Source0:        https://github.com/%{name}/contour/archive/v%{version}/contour-%{version}.tar.gz
Patch0:         https://github.com/contour-terminal/contour/pull/1855.patch
ExclusiveArch:  x86_64 aarch64
Requires:       qt6-qt5compat
Requires:       hicolor-icon-theme
Requires:       kf6-filesystem
Requires:       ncurses-term
# oreon:deps
BuildRequires:  catch-devel
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6CorePrivate)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6WaylandClientPrivate)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(boxed-cpp)
BuildRequires:  cmake(reflection-cpp)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  fmt-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  guidelines-support-library-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  libappstream-glib
BuildRequires:  libunicode-devel
BuildRequires:  libutempter-devel
BuildRequires:  libxcb-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  ncurses
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  range-v3-devel
BuildRequires:  wayland-devel
BuildRequires:  yaml-cpp-devel
# /oreon:deps
%description
Contour is a modern and actually fast, modal, virtual terminal emulator,
for everyday use. It is aiming for power users with a modern feature mindset.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir contour-%{version}
%oreon_prep
%build

%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCONTOUR_TESTING=ON
%cmake_build
%install
%cmake_install
rm %{buildroot}%{_datadir}/contour/LICENSE.txt
rm %{buildroot}%{_datadir}/contour/README.md
rm %{buildroot}%{_datadir}/terminfo/c/contour
%oreon_autofiles main

%check

%ctest
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
