%global source0_hash 5c10d56cb02cb60710c2412d4a3d02671cad74f25d1e9889c6c741f6e833fce6

%bcond kf6_compat %[0%{?fedora} >= 40 || 0%{?rhel} >= 10]

%global framework kguiaddons

Name:    kf5-%{framework}
Version: 5.116.0
Release: 6%{?dist}
Summary: KDE Frameworks 5 Tier 1 addon with various classes on top of QtGui

License: BSD-2-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin 5.116
%global stable stable
Source0: https://download.kde.org/stable/frameworks/5.116/%{framework}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros >= %{majmin}
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  plasma-wayland-protocols-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtwayland-devel pkgconfig(wayland-client)
BuildRequires:  qt5-qtx11extras-devel

Requires:       kf5-filesystem >= %{majmin}

%if %{with kf6_compat}
Recommends:     kf6-%{framework}%{?_isa}
%endif

%description
KDBusAddons provides convenience classes on top of QtGui.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

%build
%cmake_kf5 %{?with_kf6_compat:-DBUILD_GEO_SCHEME_HANDLER=OFF}

%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%doc README.md
%license LICENSES/*.txt
%if %{without kf6_compat}
%{_kf5_bindir}/kde-geo-uri-handler
%endif
%{_kf5_datadir}/qlogging-categories5/*categories
%{_kf5_libdir}/libKF5GuiAddons.so.*
%if %{without kf6_compat}
%{_kf5_datadir}/applications/*-handler.desktop
%endif

%files devel
%{_kf5_includedir}/KGuiAddons/
%{_kf5_libdir}/libKF5GuiAddons.so
%{_kf5_libdir}/cmake/KF5GuiAddons/
%{_kf5_archdatadir}/mkspecs/modules/qt_KGuiAddons.pri

%changelog
%autochangelog
