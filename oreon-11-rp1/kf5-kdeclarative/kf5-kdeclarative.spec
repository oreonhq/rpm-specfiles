%global source0_hash 9e7f9c2ac3d22dec3baa0a0fc17a9366ffb442c41cdb81c37cf65ca462eac55f
%global framework kdeclarative
%global bootstrap 1
%if !0%{?bootstrap}
%global tests 1
%endif
Name:    kf5-%{framework}
Version: 5.116.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 3 addon for Qt declarative
License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND LGPL-2.1-only OR LGPL-3.0-only AND MIT
URL:     https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
%global __provides_exclude_from ^%{_kf5_qmldir}/.*\\.so$
%if 0%{?tests}
%endif
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kglobalaccel-devel
BuildRequires:  kf5-kguiaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-knotifications-devel
BuildRequires:  kf5-kpackage-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  libepoxy-devel
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtdeclarative-devel
# /oreon:deps
%description
KDE Frameworks 5 Tier 3 addon for Qt declarative

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kconfig-devel >= %{majmin}
Requires:       kf5-kpackage-devel >= %{majmin}
Requires:       qt5-qtdeclarative-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{framework}-%{version}

%build

%cmake_kf5 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
time \
make test ARGS="--output-on-failure --timeout 10 --verbose" -C %{_target_platform} ||:
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n kf5-kdeclarative-devel -f %{oreon_filedir}/kf5-kdeclarative-devel.list

%changelog

%autochangelog
