Summary: Multimedia framework api
Name:    phonon
Version: 4.12.0
Release:	12%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     https://community.kde.org/Phonon

Source0: https://download.kde.org/stable/phonon/%{version}/phonon-%{version}.tar.xz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: kf5-rpm-macros
BuildRequires: pkgconfig
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libpulse-mainloop-glib) > 0.9.15
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(xkbcommon)
# Qt6
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Designer)
BuildRequires: cmake(Qt6OpenGL)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Core5Compat)

# Qt5
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Designer)
BuildRequires: cmake(Qt5OpenGL)
BuildRequires: cmake(Qt5Widgets)

BuildRequires: pkgconfig(xcb)

%description
%{summary}.

%package qt5
Summary: Multimedia framework api for Qt5
%{?_qt5:Requires: %{_qt5}%{?_isa} >= %{_qt5_version}}
Requires: %{name}-common = %{version}-%{release}
Recommends: phonon-qt5-backend%{?_isa}
Suggests: phonon-qt5-backend-vlc%{?_isa}
%description qt5
%{summary}.

%package qt5-devel
Summary: Developer files for %{name}-qt5
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-devel
%{summary}.

%package qt6
Summary: Multimedia framework api for Qt6
%{?_qt6:Requires: %{_qt6}%{?_isa} >= %{_qt6_version}}
Requires: %{name}-common = %{version}-%{release}
Recommends: phonon-qt6-backend%{?_isa}
Suggests: phonon-qt6-backend-vlc%{?_isa}
%description qt6
%{summary}.

%package qt6-devel
Summary: Developer files for %{name}-qt6
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
%description qt6-devel
%{summary}.

%package common
Summary: Translation files for %{name}
BuildArch: noarch
%description common
%{summary}.

%prep
%autosetup -n phonon-%{version} -p1

%build
mkdir -p phononqt6
pushd phononqt6
%cmake_kf6 -S .. \
  -DCMAKE_BUILD_TYPE:STRING="Release" \
  -DPHONON_BUILD_QT5:BOOL=OFF \
  -DPHONON_BUILD_QT6:BOOL=ON
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
popd

mkdir -p phononqt5
pushd phononqt5
%cmake_kf5 -S .. \
  -DCMAKE_BUILD_TYPE:STRING="Release" \
  -DPHONON_BUILD_QT5:BOOL=ON \
  -DPHONON_BUILD_QT6:BOOL=OFF \
  -DPHONON_BUILD_SETTINGS=OFF
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
popd


%install
pushd phononqt6
%cmake_install_kf6
popd

pushd phononqt5
%cmake_install_kf6
popd

%find_lang %{name} --with-qt --all-name
# own these dirs
mkdir -p %{buildroot}%{_qt5_plugindir}/phonon4qt5_backend
mkdir -p %{buildroot}%{_qt6_plugindir}/phonon4qt6_backend

%check
export PKG_CONFIG_PATH="%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig${PKG_CONFIG_PATH:+:}${PKG_CONFIG_PATH}"
test "$(pkg-config --modversion phonon4qt5)" = "%{version}"
test "$(pkg-config --modversion phonon4qt6)" = "%{version}"


%files qt5
%license COPYING.LIB
%{_libdir}/libphonon4qt5.so.4*
%{_libdir}/libphonon4qt5experimental.so.4*
# own backends dir
%dir %{_qt5_plugindir}/phonon4qt5_backend/

%files qt5-devel
%{_libdir}/cmake/phonon4qt5/
%{_includedir}/phonon4qt5/
%{_libdir}/libphonon4qt5.so
%{_libdir}/libphonon4qt5experimental.so
%{_libdir}/pkgconfig/phonon4qt5.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_phonon4qt5.pri
%{_qt5_plugindir}/designer/phonon4qt5widgets.so

%files qt6
%{_bindir}/phononsettings
%{_libdir}/libphonon4qt6.so.4*
%{_libdir}/libphonon4qt6experimental.so.4*
# own backends dir
%dir %{_qt6_plugindir}/phonon4qt6_backend/

%files qt6-devel
%{_libdir}/cmake/phonon4qt6/
%{_includedir}/phonon4qt6/
%{_libdir}/libphonon4qt6.so
%{_libdir}/libphonon4qt6experimental.so
%{_libdir}/pkgconfig/phonon4qt6.pc
%{_qt6_plugindir}/designer/phonon4qt6widgets.so

%files common -f %{name}.lang

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.12.0-11
- Prepare for Oreon 11 (RP1)
