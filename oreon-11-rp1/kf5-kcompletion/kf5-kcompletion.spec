%global source0_hash 52badaaa51052470cc604ac32ccb3f993d17933ab0e7af17d2ab1613d77d09ea

%global framework kcompletion

Name:           kf5-%{framework}
Version: 5.116.0
Release: 7%{?dist}
Summary:        KDE Frameworks 5 Tier 2 addon with auto completion widgets and classes

License:        CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://invent.kde.org/frameworks/%{framework}

%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/stable/frameworks/5.116/%{framework}-%{version}.tar.xz

## upstream fixes

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-kconfig-devel >= %{majmin}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros

BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  cmake(Qt5UiPlugin)

%description
KCompletion provides widgets with advanced completion support as well as a
lower-level completion class which can be used with your own widgets.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt5Widgets)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf5

%cmake_build

%install
%cmake_install

%find_lang_kf5 kcompletion5_qt

%ldconfig_scriptlets

%files -f kcompletion5_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_libdir}/libKF5Completion.so.*

%files devel
%{_kf5_includedir}/KCompletion/
%{_kf5_libdir}/libKF5Completion.so
%{_kf5_libdir}/cmake/KF5Completion/
%{_kf5_archdatadir}/mkspecs/modules/qt_KCompletion.pri
%{_kf5_qtplugindir}/designer/kcompletion5widgets.so

%changelog
%autochangelog
