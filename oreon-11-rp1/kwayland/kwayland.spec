%global source0_hash 8d4c83524919dc87b5dec546d0fb14c591c03957888cb7b240a4a9d1bbdc8269

%global stable_kf6 stable


Name:       kwayland
Version:        6.7.5
Release: 1%{?dist}
Summary:    Qt-style API to interact with the wayland-client API

License:    BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND MIT-CMU AND MIT
URL:        https://invent.kde.org/plasma/%{name}

Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  appstream
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  make
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-static
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel

BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt6WaylandClient)

Requires:   kf6-filesystem

# Renamed from kf6-kwayland
Obsoletes:      kf6-kwayland < 1:%{version}-%{release}
Provides:       kf6-kwayland = 1:%{version}-%{release}
Obsoletes:      kwayland-doc < 1:%{version}-%{release}

%description
%{summary}.

%package    devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}
Requires:   qt6-qtbase-devel
Obsoletes:  kf6-kwayland-devel < 1:%{version}-%{release}
Provides:   kf6-kwayland-devel = 1:%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1


%build
%cmake_kf6 -DBUILD_QCH=OFF
%cmake_build


%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*categories
%{_libdir}/libKWaylandClient.so.6
%{_libdir}/libKWaylandClient.so.%{version}

%files devel
%doc README.md
%license LICENSES/*.txt
%{_includedir}/KWayland/
%{_libdir}/cmake/KWayland/
%{_libdir}/libKWaylandClient.so
%{_libdir}/pkgconfig/KWaylandClient.pc

%changelog
%autochangelog
