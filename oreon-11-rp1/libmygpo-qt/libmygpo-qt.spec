%global source0_hash 71d6461939be14c044d1688bd3381cb3a724c0acb292d34fe63b9c677a4d2247

Name:    libmygpo-qt
Version: 1.2.0
Release: 2%{?dist}
Summary: Qt Library that wraps the gpodder.net Web API

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     https://github.com/gpodder/libmygpo-qt/
Source0: https://github.com/gpodder/libmygpo-qt/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: qt5-rpm-macros
BuildRequires: qt6-rpm-macros

BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Network)

%description
libmygpo-qt is a Qt Library that wraps the gpodder.net Web API,

%package -n libmygpo-qt6
Summary: Qt Library that wraps the gpodder.net Web API

%description -n libmygpo-qt6
libmygpo-qt is a Qt Library that wraps the gpodder.net Web API,
http://wiki.gpodder.org/wiki/Web_Services/API_2

%package -n libmygpo-qt6-devel
Summary: Development files for %{name}
Requires: %{name}6%{?_isa} = %{version}-%{release}
%description -n libmygpo-qt6-devel
%{summary}.

%package -n libmygpo-qt5
Summary: Qt5 Library that wraps the gpodder.net Web API
%description -n libmygpo-qt5
libmygpo-qt5 is a Qt5 Library that wraps the gpodder.net Web API,
http://wiki.gpodder.org/wiki/Web_Services/API_2

%package -n libmygpo-qt5-devel
Summary: Development files for libmygpo-qt5
Requires: libmygpo-qt5%{?_isa} = %{version}-%{release}
%description -n libmygpo-qt5-devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%global _vpath_builddir %{_target_platform}
%cmake .. \
  -DBUILD_WITH_QT6:BOOL=ON \
  -DINCLUDE_INSTALL_DIR:PATH=%{_qt6_headerdir}/mygpo-qt \
  -DLIB_INSTALL_DIR:PATH=%{_qt6_libdir}/mygpo-qt

%cmake_build

%global _vpath_builddir %{_target_platform}-qt5
%cmake .. \
  -DBUILD_WITH_QT6:BOOL=OFF \
  -DINCLUDE_INSTALL_DIR:PATH=%{_qt5_headerdir}/mygpo-qt \
  -DLIB_INSTALL_DIR:PATH=%{_qt5_libdir}/mygpo-qt

%cmake_build

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

make install/fast DESTDIR=%{buildroot} -C %{_target_platform}-qt5

%check
export PKG_CONFIG_PATH=%{buildroot}%{_qt6_libdir}/pkgconfig
test "$(pkg-config --modversion libmygpo-qt6)" = "%{version}"
export CTEST_OUTPUT_ON_FAILURE=1
# test 2 currently fails on i686, poke upstream -- rex
make test -C %{_target_platform} ||:
export PKG_CONFIG_PATH=%{buildroot}%{_qt5_libdir}/pkgconfig
test "$(pkg-config --modversion libmygpo-qt5)" = "%{version}"
export CTEST_OUTPUT_ON_FAILURE=1
# test 2 currently fails on i686, poke upstream -- rex
make test -C %{_target_platform}-qt5 ||:

%ldconfig_scriptlets -n libmygpo-qt6

%files -n libmygpo-qt6
%doc AUTHORS LICENSE README
%{_qt6_libdir}/libmygpo-qt6.so.1*

%files -n libmygpo-qt6-devel
%{_qt6_headerdir}/mygpo-qt/
%{_qt6_libdir}/libmygpo-qt6.so
%{_qt6_libdir}/pkgconfig/libmygpo-qt6.pc
%{_qt6_libdir}/cmake/mygpo-qt6/

%ldconfig_scriptlets -n libmygpo-qt5

%files -n libmygpo-qt5
%doc AUTHORS LICENSE README
%{_qt5_libdir}/libmygpo-qt5.so.1*

%files -n libmygpo-qt5-devel
%{_qt5_headerdir}/mygpo-qt/
%{_qt5_libdir}/libmygpo-qt5.so
%{_qt5_libdir}/pkgconfig/libmygpo-qt5.pc
%{_qt5_libdir}/cmake/mygpo-qt5/

%changelog
%autochangelog
