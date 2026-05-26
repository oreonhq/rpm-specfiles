# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 bbb8398d0f98c46e2ed7fd3ce526d4f7fc8476f5a449e89269f01b1bc751c4ad
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%undefine __cmake_in_source_build

Name:           packagekit-qt
Version:        1.1.4
Release:        2%{?dist}
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
%oreon_verify_sources
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
# Real soname from CMake is libpackagekitqt6.so.1.1.4 (plus symlinks), not only .so.2*
%{_libdir}/libpackagekitqt6.so.*

%files -n packagekit-qt6-devel
%{_libdir}/libpackagekitqt6.so
%{_includedir}/PackageKitQt/
%{_libdir}/pkgconfig/packagekitqt6.pc
%{_libdir}/cmake/packagekitqt6/

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.4-2
- Import
