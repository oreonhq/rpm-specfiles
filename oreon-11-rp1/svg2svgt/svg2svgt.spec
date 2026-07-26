%global source0_hash 84b7a55b6b5024e433fc58ea26ee5bb37a00c911e82e03ec796b1ba415ba0c85

Name:           svg2svgt
Version:        0.9.6
Release:        25%{?commit:.git%shortcommit}%{?dist}
Summary:        SVG to SVG Tiny converter

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/manisandro/svg2svgt
Source0:        https://github.com/manisandro/svg2svgt/archive/v{%version}/%{name}-%{version}.tar.gz

# Add missing include
Patch0:         svg2svgt_includes.patch
# Raise minimum cmake version, use GNUInstallDirs
Patch1:         svg2svgt_cmake.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtxmlpatterns-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-qt5-qtbase
BuildRequires: mingw32-qt5-qttools
BuildRequires: mingw32-qt5-qttools-tools
BuildRequires: mingw32-qt5-qtsvg
BuildRequires: mingw32-qt5-qtxmlpatterns

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-qt5-qtbase
BuildRequires: mingw64-qt5-qttools
BuildRequires: mingw64-qt5-qttools-tools
BuildRequires: mingw64-qt5-qtsvg
BuildRequires: mingw64-qt5-qtxmlpatterns

Requires:       hicolor-icon-theme

%description
Library and tools to convert SVG images to SVG Tiny, the subset of SVG
implemented by QtSvg.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw32-%{name}
MinGW Windows %{name} library.

%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw64-%{name}
MinGW Windows %{name} library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{?commit:%commit}%{!?commit:%version}

%build
# Native build
%cmake
%cmake_build

# MinGW build
%mingw_cmake
%mingw_make_build

%install
%cmake_install

%mingw_make_install
rm -rf %{buildroot}%{mingw32_datadir}/{applications,icons,metainfo}/
rm -rf %{buildroot}%{mingw64_datadir}/{applications,icons,metainfo}/

%find_lang %{name} --with-qt

%mingw_debug_install_post

%check
%{_bindir}/desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%{_bindir}/appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
%ctest

%files -f %{name}.lang
%license LICENSE.LGPL
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-gui
%{_libdir}/lib%{name}.so.*
%dir %{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/%{name}.appdata.xml

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n mingw32-%{name}
%license LICENSE.LGPL
%{mingw32_bindir}/%{name}.exe
%{mingw32_bindir}/%{name}-gui.exe
%{mingw32_bindir}/lib%{name}-0.dll
%{mingw32_datadir}/%{name}/
%{mingw32_includedir}/%{name}/
%{mingw32_libdir}/lib%{name}.dll.a
%{mingw32_libdir}/pkgconfig/%{name}.pc

%files -n mingw64-%{name}
%license LICENSE.LGPL
%{mingw64_bindir}/%{name}.exe
%{mingw64_bindir}/%{name}-gui.exe
%{mingw64_bindir}/lib%{name}-0.dll
%{mingw64_datadir}/%{name}/
%{mingw64_includedir}/%{name}/
%{mingw64_libdir}/lib%{name}.dll.a
%{mingw64_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
