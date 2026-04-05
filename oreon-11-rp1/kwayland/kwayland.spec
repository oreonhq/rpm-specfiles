Name:       kwayland
Version:    6.6.2
Release:	2%{?dist}
Summary:    Qt-style API to interact with the wayland-client API

License:    BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND MIT-CMU AND MIT
URL:        https://invent.kde.org/plasma/%{name}

Source0:    https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:    https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

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

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -p1


%build
%cmake_kf6
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
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
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
