%global source1_hash 704b4e9988044ebcc1ca233943e682b3df37f74238eae77d2925dce03a6722bd
%global source0_hash 10fb8a0f7b874248ff60d9a8ee4e1f06a0efcf01b0d34d7635dfff86e848c352
%global framework kxmlgui
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
Name:    kf6-%{framework}
Version: 6.30.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 3 solution for user-configurable main windows
License: BSD-2-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
Requires:       kf6-filesystem
# oreon:deps
BuildRequires:  clang-devel
BuildRequires:  cmake
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(PySide6)
BuildRequires:  cmake(Qt6UiPlugin)
BuildRequires:  cmake(Shiboken6)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libX11-devel
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  python3-build
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
# /oreon:deps
%description
KDE Frameworks 6 Tier 3 solution for user-configurable main windows.

%package        -n python3-%{name}
Summary:        Qt for Python bindings for %{name}
%description    -n python3-%{name}
The package contains the pyside6 bindings library for %{name}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Config)
Requires:       cmake(KF6ConfigWidgets)
Requires:       cmake(KF6GuiAddons)
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
mkdir -p %{buildroot}%{_kf6_datadir}/kxmlgui5/
%find_lang %{name} --all-name
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n python3-kf6-kxmlgui -f %{oreon_filedir}/python3-kf6-kxmlgui.list
%files -n kf6-kxmlgui-devel -f %{oreon_filedir}/kf6-kxmlgui-devel.list

%changelog

%autochangelog
