%global source0_hash 7eb593d975b1590a184354ef68dbc3c26479d58eaea00de461d73695176f623c
%global appname kImageAnnotator
%global libname lib%{appname}
Name: kimageannotator
Version: 0.7.2
Release:        9%{?dist}
License: LGPL-3.0-or-later
Summary:        Library and a tool for annotating images
URL: https://github.com/ksnip/%{appname}
Source0:        https://github.com/ksnip/%{appname}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1: kimageannotator-0.7.2-libname.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(kColorPicker-Qt5)
BuildRequires:  cmake(kColorPicker-Qt6)
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# /oreon:deps
%description
Library and a tool for annotating images. Part of KSnip project.

%package qt5
Summary: Library and a tool for annotating images. Part of KSnip project. (Qt5)
Provides: kimageannotator = %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
Requires: %{name}-common%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description qt5
%{summary}.

%package qt5-devel
Summary: Qt5 Development files for %{name}
Provides: kimageannotator-devel = %{version}-%{release}
Obsoletes: %{name}-devel < %{version}-%{release}
Requires: %{name}-qt5%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: qt5-qtbase-devel
Requires: qt5-qtsvg-devel
%description qt5-devel
%{summary}.

%package qt6
Summary: Library and a tool for annotating images. Part of KSnip project. (Qt6)
Requires: %{name}-common%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description qt6
%{summary}.
	
%package qt6-devel
Summary: Qt6 Development files for %{name}
Requires: %{name}-qt6%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: qt6-qtbase-devel
Requires: qt6-qtsvg-devel
%description qt6-devel
%{summary}.

%package common
Summary: Common language translations for Qt5 and Qt6 builds
%description common
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{appname}-%{version} -p1

%build

mkdir qt5
pushd qt5
%cmake -G Ninja \
    -S'..' \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTS:BOOL=OFF \
    -DBUILD_EXAMPLE:BOOL=OFF
%cmake_build
popd
mkdir qt6
pushd qt6
%cmake -G Ninja \
    -S'..' \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTS:BOOL=OFF \
    -DBUILD_EXAMPLE:BOOL=OFF \
    -DBUILD_WITH_QT6:BOOL=ON
%cmake_build
popd
%install
pushd qt5
%cmake_install
popd
pushd qt6
%cmake_install
popd
%find_lang %{appname} --with-qt
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n kimageannotator-qt5 -f %{oreon_filedir}/kimageannotator-qt5.list
%files -n kimageannotator-qt5-devel -f %{oreon_filedir}/kimageannotator-qt5-devel.list
%files -n kimageannotator-qt6 -f %{oreon_filedir}/kimageannotator-qt6.list
%files -n kimageannotator-qt6-devel -f %{oreon_filedir}/kimageannotator-qt6-devel.list
%files -n kimageannotator-common -f %{oreon_filedir}/kimageannotator-common.list

%changelog

%autochangelog
