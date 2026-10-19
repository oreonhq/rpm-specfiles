%global source0_hash 862d5363c5fdbb3cca60ce4d86cd352f88b3e8dad735cf79bad2b127657b6b16
%global commit 7fa23e746ce7dbb793fc6af9482304157479e5c4
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20250130
Name:           mankalaengine
Version:        1.1.%{commitdate}.%{shortcommit}
Release:        1%{?dist}
Summary:        A Mancala game engine with AI support
License:        GPL-3.0-or-later 
URL:            https://invent.kde.org/joaotgouveia/mankalaengine
Source0:        https://invent.kde.org/joaotgouveia/%{name}/-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0: 0000-Draft-MR-integrated-pallaguli-rules-and-tui.patch
Patch1: 0001-Removed-cppcheck-from-CMakeLists.txt.patch 
Patch2: 0002-Installing-Tui-binaries.patch 
Requires:       qt6-qtbase
Requires:       mesa-libGL
# oreon:deps
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  make
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
# /oreon:deps
%description
MankalaEngine is an engine used for 
creating computerized opponents for Mancala variants.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains 
libraries and header files for
developing  applications and plugins that use %{name}.

%package tui-games
Summary: TUI Binaries for Mancala Game Variants
%description tui-games
The %{name}-binaries package contains TUI binaries for different 
Mancala Variants supported by MankalaEngine.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit} -p1

%build

%cmake -DBUILD_EXAMPLES=ON -DBUILD_LINTING=OFF
%cmake_build
%check

%ctest
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mankalaengine-devel -f %{oreon_filedir}/mankalaengine-devel.list
%files -n mankalaengine-tui-games -f %{oreon_filedir}/mankalaengine-tui-games.list

%changelog

%autochangelog
