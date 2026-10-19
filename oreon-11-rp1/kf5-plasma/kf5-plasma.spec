%global source0_hash 7e932c4da5f527206ce07d3b145231ef396a3d22441edcd24deeaf9dac509f4f
%bcond kf6_compat %[0%{?fedora} >= 40 || 0%{?rhel} >= 10]
%global framework plasma-framework
Name:    kf5-plasma
Version: 5.116.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 3 framework is foundation to build a primary user interface
License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/plasma
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
Source10: fedora-plasma-cache.sh.in
%global __provides_exclude_from ^%{_kf5_qmldir}/.*\\.so$
Requires:       qt5-qtquickcontrols%{?_isa}
Requires:       qt5-qtquickcontrols2%{?_isa}
Conflicts:      kdeplasma-addons < 5.5.0-3
%if %{without kf6_compat}
Provides: plasma-framework = %{version}-%{release}
%endif
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kactivities-devel
BuildRequires:  kf5-karchive-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kdeclarative-devel
BuildRequires:  kf5-kdesu-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-kglobalaccel-devel
BuildRequires:  kf5-kguiaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kirigami2-devel
BuildRequires:  kf5-knotifications-devel
BuildRequires:  kf5-kpackage-devel
BuildRequires:  kf5-kparts-devel
BuildRequires:  kf5-kservice-devel
BuildRequires:  kf5-kwayland-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-solid-devel
BuildRequires:  libGL-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXext-devel
BuildRequires:  libXrender-devel
BuildRequires:  libxcb-devel
BuildRequires:  openssl-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtquickcontrols2-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtx11extras-devel
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Conflicts:      kapptemplates < 15.12.0-1
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kpackage-devel >= %{majmin}
Requires:       kf5-kservice-devel >= %{majmin}
Requires:       kf5-kwindowsystem-devel >= %{majmin}
Requires:       qt5-qtbase-devel
%if %{without kf6_compat}
Provides: plasma-framework-devel = %{version}-%{release}
%endif
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

install -m644 -p %{SOURCE10} .

%build

%cmake_kf5 %{?with_kf6_compat:-DBUILD_DESKTOPTHEMES=OFF}
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-man --all-name
mkdir -p %{buildroot}%{_kf5_datadir}/plasma/plasmoids
mkdir -p %{buildroot}%{_kf5_qmldir}/org/kde/private
mkdir -p %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/env
sed -e "s|@@VERSION@@|%{version}|g" fedora-plasma-cache.sh.in > \
  %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/env/fedora-plasma-cache.sh
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-plasma-devel -f %{oreon_filedir}/kf5-plasma-devel.list

%changelog

%autochangelog
