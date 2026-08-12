%global source0_hash 34807e502cc0dbb984661c9569e9dfcfb1f005c451c9f3a5afdbb016de117552

%undefine __cmake_in_source_build
%global framework ktextwidgets

Name:    kf5-%{framework}
Version: 5.116.0
Release: 7%{?dist}
Summary: KDE Frameworks 5 Tier 3 addon with advanced text editing widgets

License: CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/stable/frameworks/5.116/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-kcompletion-devel >= %{majmin}
BuildRequires:  kf5-kconfig-devel >= %{majmin}
BuildRequires:  kf5-kconfigwidgets-devel >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
BuildRequires:  kf5-kiconthemes-devel >= %{majmin}
BuildRequires:  kf5-kservice-devel >= %{majmin}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{majmin}
BuildRequires:  kf5-kwindowsystem-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-sonnet-devel >= %{majmin}

BuildRequires:  qt5-qtbase-devel
BuildRequires:  cmake(Qt5UiPlugin)

%if !0%{?bootstrap}
%if 0%{?fedora}
BuildRequires:  pkgconfig(Qt5TextToSpeech)
%endif
%endif

%description
KDE Frameworks 5 Tier 3 addon with advanced text edting widgets.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-ki18n-devel >= %{majmin}
Requires:       kf5-sonnet-devel >= %{majmin}
Requires:       qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

%build
%{cmake_kf5}
%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_libdir}/libKF5TextWidgets.so.*

%files devel
%{_kf5_includedir}/KTextWidgets/
%{_kf5_libdir}/libKF5TextWidgets.so
%{_kf5_libdir}/cmake/KF5TextWidgets/
%{_kf5_archdatadir}/mkspecs/modules/qt_KTextWidgets.pri
%{_kf5_qtplugindir}/designer/ktextwidgets5widgets.so

%changelog
%autochangelog
