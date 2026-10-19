%global source0_hash ace1ee1ac0aa1b291c4c50c93fc3503b62318eeef0df0ee394a5a08da9691ff4
%global framework kauth
Name:    kf5-%{framework}
Version: 5.116.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 2 integration module to perform actions as privileged user
License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  polkit-qt5-1-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
# /oreon:deps
%description
KAuth is a framework to let applications perform actions as a privileged user.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kcoreaddons-devel >= %{majmin}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build

%cmake_kf5 \
  -DKDE_INSTALL_LIBEXECDIR=%{_kf5_libexecdir}
%cmake_build
%install
%cmake_install
%find_lang_kf5 kauth5_qt
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-kauth-devel -f %{oreon_filedir}/kf5-kauth-devel.list

%changelog

%autochangelog
