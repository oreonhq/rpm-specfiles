%global source0_hash e78c785ec4a8a22a48a91835c97601f5704b5076b154415353b0d2697dc0b4f7
%global appname kColorPicker
%global libname lib%{appname}

Name: kcolorpicker
Version: 0.3.1
Release: 8%{?dist}

License: LGPL-3.0-or-later
Summary: QToolButton control with color popup menu
URL: https://github.com/ksnip/%{appname}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:  kcolorpicker-cmake-libname.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build

BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)

%description
QToolButton with color popup menu which lets you select a color.

The popup features a color dialog button which can be used to add
custom colors to the popup menu.

%package qt5
Summary: QToolButton control with color popup menu (Qt5)
Provides: kcolorpicker = %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}
%description qt5
%{summary}.

%package qt5-devel
Summary: Qt5 Development files for %{name}
Provides: kcolorpicker-devel = %{version}-%{release}	
Obsoletes: %{name}-devel < %{version}-%{release}
Requires: %{name}-qt5%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: qt5-qtbase-devel
%description qt5-devel
%{summary}.

%package qt6
Summary: QToolButton control with color popup menu (Qt6)
%description qt6
%{summary}.

%package qt6-devel
Summary: Qt6 Development files for %{name}
Requires: %{name}-qt6%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: qt6-qtbase-devel
%description qt6-devel
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

%files qt5
%doc README.md
%license LICENSE
%{_libdir}/%{libname}-Qt5.so.0*

%files qt5-devel
%{_includedir}/%{appname}-Qt5/
%{_libdir}/cmake/%{appname}-Qt5/
%{_libdir}/%{libname}-Qt5.so

%files qt6
%doc README.md
%license LICENSE
%{_libdir}/%{libname}-Qt6.so.0*

%files qt6-devel
%{_includedir}/%{appname}-Qt6/
%{_libdir}/cmake/%{appname}-Qt6/
%{_libdir}/%{libname}-Qt6.so

%changelog
%autochangelog
