%global source1_hash 8414309bcd84085eb0c70d8fdb6a69a56534c6d64c7b8f1969a8222eb19cd79d
%global source0_hash e8bf60e398e2f8098a4db7db44c5475d70540ad8f8948a123c8bc109dc4db776
%global		framework kcalendarcore
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
Name:		kf6-%{framework}
Version:	6.30.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 1 KCalendarCore Library
License:	BSD-3-Clause AND LGPL-2.0-or-later AND LGPL-3.0-or-later
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
Requires:       kf6-filesystem
# oreon:deps
BuildRequires:  bison
BuildRequires:  clang-devel
BuildRequires:  cmake
BuildRequires:  cmake(PySide6)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Shiboken6)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libical-devel
BuildRequires:  make
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  python3-build
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  qt6-qtbase-devel
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n python3-kf6-kcalendarcore -f %{oreon_filedir}/python3-kf6-kcalendarcore.list
%files -n kf6-kcalendarcore-devel -f %{oreon_filedir}/kf6-kcalendarcore-devel.list

%changelog

%autochangelog
