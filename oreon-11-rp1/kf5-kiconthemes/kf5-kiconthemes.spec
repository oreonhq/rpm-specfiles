%global source0_hash 9e6efbe228739d799c5968e11c7bebecb8d84894e8d077b954f4682fd74f0561

%global framework kiconthemes

Name:    kf5-%{framework}
Version: 5.116.0
Release: 7%{?dist}
Summary: KDE Frameworks 5 Tier 3 integration module with icon themes

License: CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://api.kde.org/frameworks/kiconthemes/

%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/stable/frameworks/5.116/%{framework}-%{version}.tar.xz

## upstream patches

## upstreamable patches

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-karchive-devel >= %{majmin}
BuildRequires:  kf5-kconfigwidgets-devel >= %{majmin}
BuildRequires:  kf5-kconfigwidgets-devel >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
BuildRequires:  kf5-kitemviews-devel >= %{majmin}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  cmake(Qt5UiPlugin)

Requires:       hicolor-icon-theme

%description
KDE Frameworks 5 Tier 3 integration module with icon themes

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
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

%find_lang %{name} --all-name

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_bindir}/kiconfinder5
%{_kf5_libdir}/libKF5IconThemes.so.*
%{_kf5_qtplugindir}/iconengines/KIconEnginePlugin.so

%files devel
%{_kf5_includedir}/KIconThemes/
%{_kf5_libdir}/libKF5IconThemes.so
%{_kf5_libdir}/cmake/KF5IconThemes/
%{_kf5_archdatadir}/mkspecs/modules/qt_KIconThemes.pri
%{_kf5_qtplugindir}/designer/kiconthemes5widgets.so

%changelog
%autochangelog
