%global source1_hash 7a32c4404c2106f9234c9b9cee3475694f1abac9d069f056b9fce6ef92729f06
%global source0_hash bf36e3619df1c6ad3d900bd36433d97ab295be41c1cc401ff0e766380788bbae
%global framework kjobwidgets
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
Name:           kf6-%{framework}
Version:        6.30.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 2 addon for KJobs
License:        CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
Requires:       kf6-filesystem
# oreon:deps
BuildRequires:  clang-devel
BuildRequires:  cmake
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libX11-devel
BuildRequires:  pkgconfig(pyside6)
BuildRequires:  pkgconfig(shiboken6)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  python3-build
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qttools-devel
# /oreon:deps
%description
%{summary}.

%package        -n python3-%{name}
Summary:        Qt for Python bindings for %{name}
%description    -n python3-%{name}
The package contains the pyside6 bindings library for %{name}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
Requires:       cmake(KF6CoreAddons)
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
%find_lang_kf6 kjobwidgets6_qt
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n python3-kf6-kjobwidgets -f %{oreon_filedir}/python3-kf6-kjobwidgets.list
%files -n kf6-kjobwidgets-devel -f %{oreon_filedir}/kf6-kjobwidgets-devel.list

%changelog

%autochangelog
