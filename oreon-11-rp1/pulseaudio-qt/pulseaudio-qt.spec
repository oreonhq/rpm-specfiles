%undefine __cmake_in_source_build

Name:           pulseaudio-qt
Version:        1.8.1
Release:        6%{?dist}
Summary:        Qt bindings to PulseAudio (Qt 6)
License:        LGPL-2.1-only
URL:            https://invent.kde.org/libraries/pulseaudio-qt
Source0:        https://invent.kde.org/libraries/pulseaudio-qt/-/archive/v%{version}/pulseaudio-qt-v%{version}.tar.bz2

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel

%description
Qt 6 library for talking to PulseAudio over D-Bus.


%package -n kf6-pulseaudio-qt
Summary:        Qt 6 PulseAudio client library

%description -n kf6-pulseaudio-qt
%{summary}.

%package -n kf6-pulseaudio-qt-devel
Summary:        Development files for kf6-pulseaudio-qt
Requires:       kf6-pulseaudio-qt%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
Requires:       cmake(Qt6DBus)

%description -n kf6-pulseaudio-qt-devel
Headers, pkg-config, and CMake files for kf6-pulseaudio-qt.


%prep
%autosetup -n pulseaudio-qt-v%{version} -p1


%build
%cmake \
  -DQT_MAJOR_VERSION=6 \
  -DCMAKE_BUILD_TYPE=Release \
  -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
%cmake_build


%install
%cmake_install


%files -n kf6-pulseaudio-qt
%license LICENSES/*
# Real name is .so.<upstream-version> (e.g. 1.8.1); SONAME is still .so.5
%{_libdir}/libKF6PulseAudioQt.so.*

%files -n kf6-pulseaudio-qt-devel
%{_includedir}/KF6/*
%{_libdir}/libKF6PulseAudioQt.so
%{_libdir}/pkgconfig/KF6PulseAudioQt.pc
%{_libdir}/cmake/KF6PulseAudioQt/


%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8.1-2
- Add pulseaudio-qt for Plasma audio applets
