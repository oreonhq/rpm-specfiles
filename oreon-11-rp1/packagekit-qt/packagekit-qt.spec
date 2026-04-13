%undefine __cmake_in_source_build

Name:           packagekit-qt
Version:        1.1.4
Release:        1%{?dist}
Summary:        Qt 6 bindings for PackageKit
License:        LGPL-2.1-or-later
URL:            https://github.com/PackageKit/PackageKit-Qt

# Tag archive (consistent saved name for spectool)
Source0:        https://github.com/PackageKit/PackageKit-Qt/archive/refs/tags/v%{version}.tar.gz#/PackageKit-Qt-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-devel
BuildRequires:  PackageKit

%description
Qt6 library for talking to PackageKit over D-Bus.

%package -n packagekit-qt6
Summary:        Qt 6 PackageKit client library

%description -n packagekit-qt6
%{summary}.

%package -n packagekit-qt6-devel
Summary:        Development files for packagekit-qt6
Requires:       packagekit-qt6%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
Requires:       cmake(Qt6DBus)

%description -n packagekit-qt6-devel
Headers, pkg-config, and CMake files for building against packagekit-qt6.

%prep
%autosetup -n PackageKit-Qt-%{version} -p1

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files -n packagekit-qt6
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/libpackagekitqt6.so.2*

%files -n packagekit-qt6-devel
%{_libdir}/libpackagekitqt6.so
%{_includedir}/PackageKitQt/
%{_libdir}/pkgconfig/packagekitqt6.pc
%{_libdir}/cmake/packagekitqt6/

%changelog
* Sun Apr 12 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.4-1
- Add PackageKit-Qt for Plasma and Discover (Qt6 bindings)
