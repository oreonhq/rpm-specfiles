%global source0_hash 0c5801f9c50d4fea4a183876a887068a4b73d9f5545453dbcd1cd17ec46e2300

%global		framework kcalendarcore

%global stable_kf6 stable
%global majmin_ver_kf6 6.29


Name:		kf6-%{framework}
Version:	6.29.0
Release:        1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 KCalendarCore Library
License:	BSD-3-Clause AND LGPL-2.0-or-later AND LGPL-3.0-or-later
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	kf6-rpm-macros
BuildRequires:	bison
BuildRequires:	libical-devel
BuildRequires:	qt6-qtbase-devel
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:  cmake(Qt6Qml)

BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  clang-devel
BuildRequires:  cmake(Shiboken6)
BuildRequires:  cmake(PySide6)

Requires:       kf6-filesystem

%description
%{summary}.

%package -n python3-%{name}
Summary:        Qt for Python bindings for %{name}
%description -n python3-%{name}
The package contains the pyside6 bindings library for %{name}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libical-devel
Requires:       qt6-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%files
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*kcalendarcore.*
%{_kf6_libdir}/libKF6CalendarCore.so.*
%{_kf6_qmldir}/org/kde/calendarcore/

%files -n python3-%{name}
%{python3_sitearch}/KCalendarCore.cpython-%{python3_version_nodots}*.so

%files devel
%{_kf6_includedir}/KCalendarCore/
%dir %{_includedir}/PySide6/KCalendarCore/
%{_includedir}/PySide6/KCalendarCore/kcalendarcore_python.h
%dir %{_kf6_datadir}/PySide6/typesystems/
%{_kf6_datadir}/PySide6/typesystems/typesystem_kcalendarcore.xml
%{_kf6_libdir}/libKF6CalendarCore.so
%{_kf6_libdir}/cmake/KF6CalendarCore/
%{_kf6_libdir}/pkgconfig/KF6CalendarCore.pc


%changelog
%autochangelog
