%global source0_hash 7c21b594b872f8497d5f854e034c40fd70aa4fd4888255cbc409051c3b6b0dee

Summary:   Qt5 support library for PackageKit
Name:      PackageKit-Qt5
Version:   1.1.2
Release:   5%{?dist}

License:   LGPL-2.1-only
URL:       http://www.packagekit.org/

Source0:   https://github.com/hughsie/PackageKit-Qt/archive/v%{version}.tar.gz

# Upstream patches

BuildRequires: cmake
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Sql)
BuildRequires: gcc-c++
# required for /usr/share/dbus-1/interfaces/*.xml
BuildRequires: PackageKit >= 0.9.1

Recommends: PackageKit

%description
PackageKit-Qt is a Qt support library for PackageKit

%package devel
Summary: Development files for PackageKit-Qt5
Requires: PackageKit-Qt5%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n PackageKit-Qt-%{version}

%build
%cmake -DBUILD_WITH_QT6=OFF
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS NEWS
%license COPYING
%{_libdir}/libpackagekitqt5.so.%{version}
%{_libdir}/libpackagekitqt5.so.1

%files devel
%{_libdir}/libpackagekitqt5.so
%{_libdir}/pkgconfig/packagekitqt5.pc
%{_includedir}/packagekitqt5/
%{_libdir}/cmake/packagekitqt5/

%changelog
%autochangelog
