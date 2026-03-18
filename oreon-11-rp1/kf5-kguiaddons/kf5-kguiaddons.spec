%bcond kf6_compat %[0%{?fedora} >= 40 || 0%{?rhel} >= 10]

%global framework kguiaddons

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 1 addon with various classes on top of QtGui

License: BSD-2-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
