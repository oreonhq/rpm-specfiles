%global source0_hash 933250628090e240141c23acc40f796da1ff5a658987b60a0c7cc182701e6bcd

%global framework ki18n

Name:    kf5-%{framework}
Version: 5.116.0
Release: 7%{?dist}
Summary: KDE Frameworks 5 Tier 1 addon for localization

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only) AND ODbL-1.0
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin 5.116
%global stable stable
Source0: https://download.kde.org/stable/frameworks/5.116/%{framework}-%{version}.tar.xz
## upstream patches

# filter plugin provides
%global __provides_exclude_from ^(%{_kf5_plugindir}/.*\\.so)$

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  gettext
BuildRequires:  kf5-rpm-macros >= %{majmin}
BuildRequires:  perl-interpreter
BuildRequires:  python3
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtscript-devel

Requires:       kf5-filesystem >= %{majmin}

%description
KDE Frameworks 5 Tier 1 addon for localization.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gettext
Requires:       python3
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf5 \
   -DPYTHON_EXECUTABLE:PATH=%__python3

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name

%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_libdir}/libKF5I18n.so.*
%{_kf5_libdir}/libKF5I18nLocaleData.so.*
%{_kf5_datadir}/qlogging-categories5/*%{framework}*
%{_kf5_qmldir}/org/kde/i18n/
%{_kf5_qtplugindir}/kf5/ktranscript.so
%lang(ca) %{_datadir}/locale/ca/LC_SCRIPTS/ki18n5/
%lang(ca@valencia) %{_datadir}/locale/ca@valencia/LC_SCRIPTS/ki18n5/
%lang(fi) %{_datadir}/locale/fi/LC_SCRIPTS/ki18n5/
%lang(gd) %{_datadir}/locale/gd/LC_SCRIPTS/ki18n5/
%lang(ja) %{_datadir}/locale/ja/LC_SCRIPTS/ki18n5/
%lang(ko) %{_datadir}/locale/ko/LC_SCRIPTS/ki18n5/
%lang(nb) %{_datadir}/locale/nb/LC_SCRIPTS/ki18n5/
%lang(nn) %{_datadir}/locale/nn/LC_SCRIPTS/ki18n5/
%lang(ru) %{_datadir}/locale/ru/LC_SCRIPTS/ki18n5/
%lang(sr) %{_datadir}/locale/sr/LC_SCRIPTS/ki18n5/
%lang(sr@ijekavian) %{_datadir}/locale/sr@ijekavian/LC_SCRIPTS/ki18n5/
%lang(sr@ijekavianlatin) %{_datadir}/locale/sr@ijekavianlatin/LC_SCRIPTS/ki18n5/
%lang(sr@latin) %{_datadir}/locale/sr@latin/LC_SCRIPTS/ki18n5/
%lang(sr) %{_datadir}/locale/uk/LC_SCRIPTS/ki18n5/

%files devel
%{_kf5_includedir}/KI18n/
%{_kf5_includedir}/KI18nLocaleData/
%{_kf5_libdir}/libKF5I18n.so
%{_kf5_libdir}/libKF5I18nLocaleData.so
%{_kf5_libdir}/cmake/KF5I18n/
%{_kf5_archdatadir}/mkspecs/modules/qt_KI18n.pri

%changelog
%autochangelog
