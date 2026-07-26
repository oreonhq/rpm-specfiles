%global source0_hash 540a5ae54b7325218798af79f73a97d6ffcbcc683156de33b3a964e934368f05

%global framework kbookmarks

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 3 addon for bookmarks manipulation

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0:        http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

## upstream patches

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-kcodecs-devel >= %{majmin}
BuildRequires:  kf5-kconfig-devel >= %{majmin}
BuildRequires:  kf5-kconfigwidgets-devel >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{majmin}
BuildRequires:  kf5-kxmlgui-devel >= %{majmin}

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel

%description
KBookmarks lets you access and manipulate bookmarks stored using the
XBEL format.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
Requires:       kf5-kwidgetsaddons-devel >= %{majmin}
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

%find_lang_kf5 kbookmarks5_qt

%ldconfig_scriptlets

%files -f kbookmarks5_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_libdir}/libKF5Bookmarks.so.*

%files devel

%{_kf5_includedir}/KBookmarks/
%{_kf5_libdir}/libKF5Bookmarks.so
%{_kf5_libdir}/cmake/KF5Bookmarks/
%{_kf5_archdatadir}/mkspecs/modules/qt_KBookmarks.pri

%changelog
%autochangelog
