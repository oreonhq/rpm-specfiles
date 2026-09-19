%global source0_hash 579dad3bd1ea44b5a20c0f133ebf47622e38960f9c7c8b3a316be30a369f431f

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kdiagram2
Summary: Powerful libraries (KChart, KGantt) for creating business diagrams
Version: 2.8.0
Release: 15%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Url:     https://invent.kde.org/graphics/kdiagram
Source0: http://download.kde.org/stable/kdiagram/%{version}/kdiagram-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Help)
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Svg)

%if 0%{?tests}
BuildRequires: cmake(Qt5Test)
BuildRequires: xorg-x11-server-Xvfb
%endif

# For AutoReq cmake-filesystem
BuildRequires: cmake

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

%autosetup -n kdiagram-%{version} -p1

%build
%cmake_kf5 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{?!tests:OFF}

%cmake_build

%install
%cmake_install

%find_lang_kf5 kchart_qt
%find_lang_kf5 kgantt_qt
cat kchart_qt.lang kgantt_qt.lang > %{name}.lang

%check
%if 0%{?tests}
# FIXME/TODO: make macros better to not have to do this when using xvfb-run
echo "%ctest" > ./rpm-check.sh
chmod +x ./rpm-check.sh
xvfb-run -a ./rpm-check.sh
%endif

%ldconfig_scriptlets

%files -f %{name}.lang
%license LICENSE.GPL.txt
%{_kf5_libdir}/libKChart.so.2*
%{_kf5_libdir}/libKGantt.so.2*

%files devel
%{_includedir}/KChart/
%{_includedir}/KGantt/
%{_includedir}/kchart_version.h
%{_includedir}/kgantt_version.h
%{_kf5_libdir}/libKChart.so
%{_kf5_libdir}/libKGantt.so
%{_kf5_libdir}/cmake/KChart/
%{_kf5_libdir}/cmake/KGantt/
%{_kf5_archdatadir}/mkspecs/modules/qt_KChart.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_KGantt.pri

%changelog
%autochangelog
