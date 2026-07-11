%global source0_hash bbb8398d0f98c46e2ed7fd3ce526d4f7fc8476f5a449e89269f01b1bc751c4ad

%global gitcommit 42902ed51e02e78f13a002c5e81c240601b7445a
%global gitdate 20250914.113000
%global shortcommit %(c=%{gitcommit}; echo ${c:0:7})

Summary:   Qt support library for PackageKit
Name:      PackageKit-Qt
Version:   1.1.4
Release:   4%{?dist}

License:   LGPL-2.1-only
URL:       http://www.packagekit.org/

Source0:   https://github.com/hughsie/PackageKit-Qt/archive/v%{version}.tar.gz#/PackageKit-Qt-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Sql)
BuildRequires: gcc-c++
BuildRequires: PackageKit >= 0.9.1

Recommends: PackageKit

%description
PackageKit-Qt is a Qt support library for PackageKit

%package -n PackageKit-Qt6
Summary: Qt6 support library for PackageKit
Recommends: PackageKit
Obsoletes: packagekit-qt6 < %{version}-%{release}
Provides: packagekit-qt6 = %{version}-%{release}
Provides: packagekit-qt6%{?_isa} = %{version}-%{release}
%description -n PackageKit-Qt6
%{summary}.

%package -n PackageKit-Qt6-devel
Summary: Development files for PackageKit-Qt6
Requires: PackageKit-Qt6%{?_isa} = %{version}-%{release}
Obsoletes: packagekit-qt6-devel < %{version}-%{release}
Provides: packagekit-qt6-devel = %{version}-%{release}
Provides: packagekit-qt6-devel%{?_isa} = %{version}-%{release}
%description -n PackageKit-Qt6-devel
%{summary}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{version}


%build
%cmake -DBUILD_WITH_QT6=ON
%cmake_build


%install
%cmake_install

%files -n PackageKit-Qt6
%doc AUTHORS NEWS
%license COPYING
%{_libdir}/libpackagekitqt6.so.%{version}
%{_libdir}/libpackagekitqt6.so.2

%files -n PackageKit-Qt6-devel
%{_libdir}/libpackagekitqt6.so
%{_libdir}/pkgconfig/packagekitqt6.pc
%{_includedir}/PackageKitQt/
%{_libdir}/cmake/packagekitqt6/


%changelog
%autochangelog
