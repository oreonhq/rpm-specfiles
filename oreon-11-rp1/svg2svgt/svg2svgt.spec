%global source0_hash 84b7a55b6b5024e433fc58ea26ee5bb37a00c911e82e03ec796b1ba415ba0c85
Name:           svg2svgt
Version:        0.9.6
Release:        1%{?dist}
Summary:        SVG to SVG Tiny converter
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/manisandro/svg2svgt
Source0:        https://github.com/manisandro/%{name}/archive/v{%{version}}/%{name}-%{version}.tar.gz
Patch0:         svg2svgt_includes.patch
Patch1:         svg2svgt_cmake.patch
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt5-qtbase
BuildRequires:  mingw32-qt5-qtsvg
BuildRequires:  mingw32-qt5-qttools
BuildRequires:  mingw32-qt5-qttools-tools
BuildRequires:  mingw32-qt5-qtxmlpatterns
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt5-qtbase
BuildRequires:  mingw64-qt5-qtsvg
BuildRequires:  mingw64-qt5-qttools
BuildRequires:  mingw64-qt5-qttools-tools
BuildRequires:  mingw64-qt5-qtxmlpatterns
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtxmlpatterns-devel
# /oreon:deps
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

%cmake
%cmake_build
%mingw_cmake
%mingw_make_build
%install
%cmake_install
%mingw_make_install
rm -rf %{buildroot}%{mingw32_datadir}/{applications,icons,metainfo}/
rm -rf %{buildroot}%{mingw64_datadir}/{applications,icons,metainfo}/
%find_lang %{name} --with-qt
%mingw_debug_install_post
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{_bindir}/desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%{_bindir}/appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
%ctest
%files -f %{oreon_filedir}/main.list
%files -n svg2svgt-devel -f %{oreon_filedir}/svg2svgt-devel.list
%files -n mingw32-svg2svgt -f %{oreon_filedir}/mingw32-svg2svgt.list
%files -n mingw64-svg2svgt -f %{oreon_filedir}/mingw64-svg2svgt.list

%changelog

%autochangelog
