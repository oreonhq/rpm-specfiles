%undefine __cmake_in_source_build
%global framework ktextwidgets

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 3 addon with advanced text editing widgets

License: CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
