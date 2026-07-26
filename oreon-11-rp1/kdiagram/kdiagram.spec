%global source0_hash 4659b0c2cd9db18143f5abd9c806091c3aab6abc1a956bbf82815ab3d3189c6d

Name:    kdiagram
Summary: Powerful libraries (KChart, KGantt) for creating business diagrams
Version: 3.0.1
Release: 9%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
Url:     https://invent.kde.org/graphics/kdiagram

Source0: http://download.kde.org/stable/kdiagram/%{version}/kdiagram-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Help)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Svg)

# For AutoReq cmake-filesystem
BuildRequires: cmake

%description
Powerful libraries (KChart, KGantt) for creating business diagrams.

%package devel
Summary: Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(Qt6Svg)
Requires: cmake(Qt6Widgets)
Requires: cmake(Qt6PrintSupport)
%description devel
%{summary}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang_kf6 kchart6_qt
%find_lang_kf6 kgantt6_qt
cat kchart6_qt.lang kgantt6_qt.lang > %{name}.lang

%files -f %{name}.lang
%license LICENSE.GPL.txt
%{_kf6_libdir}/libKChart6.so.3*
%{_kf6_libdir}/libKGantt6.so.3*

%files devel
%{_includedir}/KChart6/
%{_includedir}/KGantt6/
%{_kf6_libdir}/libKChart6.so
%{_kf6_libdir}/libKGantt6.so
%{_kf6_libdir}/cmake/KChart6/
%{_kf6_libdir}/cmake/KGantt6/
%{_kf6_archdatadir}/mkspecs/modules/qt_KChart6.pri
%{_kf6_archdatadir}/mkspecs/modules/qt_KGantt6.pri
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch

%changelog
%autochangelog
