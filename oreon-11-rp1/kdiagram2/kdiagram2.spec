%global source0_hash 579dad3bd1ea44b5a20c0f133ebf47622e38960f9c7c8b3a316be30a369f431f
%if !0%{?bootstrap}
%global tests 1
%endif
Name:    kdiagram2
Summary:        Powerful libraries (KChart, KGantt) for creating business diagrams
Version: 2.8.0
Release:        1%{?dist}
License: GPL-2.0-or-later
Url:     https://invent.kde.org/graphics/kdiagram
Source0:        http://download.kde.org/stable/kdiagram/%{version}/kdiagram-%{version}.tar.xz
Patch0: kdiagram2-ecm-pri-version.patch
%if 0%{?tests}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Help)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
Powerful libraries (KChart, KGantt) for creating business diagrams.

%package devel
Summary: Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(Qt5Svg)
Requires: cmake(Qt5Widgets)
Requires: cmake(Qt5PrintSupport)
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir kdiagram-%{version}
%oreon_prep
%build

%cmake_kf5 \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{?!tests:OFF}
%cmake_build
%install
%cmake_install
%find_lang_kf5 kchart_qt
%find_lang_kf5 kgantt_qt
cat kchart_qt.lang kgantt_qt.lang > %{name}.lang
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if 0%{?tests}
echo "%ctest" > ./rpm-check.sh
chmod +x ./rpm-check.sh
xvfb-run -a ./rpm-check.sh
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n kdiagram2-devel -f %{oreon_filedir}/kdiagram2-devel.list

%changelog

%autochangelog
