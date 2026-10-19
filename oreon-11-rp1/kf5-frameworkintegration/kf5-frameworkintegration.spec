%global source0_hash 2f70ee4b34d70645a647a5fe0ffe0b6efd468e79a01d6de3978c8509f55de2c3
%global framework frameworkintegration
Name:    kf5-%{framework}
Version: 5.116.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 4 workspace and cross-framework integration plugins
License: CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
%global __provides_exclude_from ^(%{_kf5_plugindir}/.*\\.so)$
Obsoletes:      %{name} < 5.11.0-3
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-knewstuff-devel
BuildRequires:  kf5-knotifications-devel
BuildRequires:  kf5-kpackage-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  libXcursor-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtx11extras-devel
# /oreon:deps
%description
Framework Integration is a set of plugins responsible for better integration of
Qt applications when running on a KDE Plasma workspace.

Applications do not need to link to this directly.

%package        libs
Summary:        Runtime libraries for %{name}.
Requires:       %{name} = %{version}-%{release}
%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       kf5-kiconthemes-devel >= %{majmin}
Requires:       kf5-kconfigwidgets-devel >= %{majmin}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{framework}-%{version}

%build

%cmake_kf5
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-frameworkintegration-libs -f %{oreon_filedir}/kf5-frameworkintegration-libs.list
%files -n kf5-frameworkintegration-devel -f %{oreon_filedir}/kf5-frameworkintegration-devel.list

%changelog

%autochangelog
