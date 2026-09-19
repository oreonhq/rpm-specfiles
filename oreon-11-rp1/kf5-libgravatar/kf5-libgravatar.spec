%global source0_hash ac25fa24444642d3c227e2a272d6f59b637896a051381c7344e0672aac5cd697

%global framework libgravatar

Name:    kf5-%{framework}
Version: 23.08.5
Release: 5%{?dist}
Summary: Gravatar support library

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/pim/%{framework}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}

BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)

%global kf5_ver 5.105.0
BuildRequires:  extra-cmake-modules >= %{kf5_ver}
BuildRequires:  kf5-rpm-macros >= %{kf5_ver}
BuildRequires:  cmake(KF5Config) >= %{kf5_ver}
BuildRequires:  cmake(KF5KIO) >= %{kf5_ver}
BuildRequires:  cmake(KF5I18n) >= %{kf5_ver}
BuildRequires:  cmake(KF5TextWidgets) >= %{kf5_ver}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{kf5_ver}

%global majmin_ver %{version}
BuildRequires:  cmake(KPim5PimCommon)
BuildRequires:  cmake(KPim5TextEdit)

Obsoletes:      kdepim-libs < 7:16.04.0
Conflicts:      kdepim-libs < 7:16.04.0

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

# Rename translation files to avoid conflict with KF6
find ./po -type f -execdir mv {} libgravatar5.po \;
sed -i "/TRANSLATION_DOMAIN/ s/libgravatar/libgravatar5/" CMakeLists.txt
sed -i "s/libgravatar/libgravatar5/" src/Messages.sh

%build
%cmake_kf5

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

%ldconfig_scriptlets

%files -f %{name}.lang
%license LICENSES/*
%{_kf5_datadir}/qlogging-categories5/*%{framework}.*
%{_kf5_libdir}/libKPim5Gravatar.so.5*

%files devel
%{_kf5_libdir}/libKPim5Gravatar.so
%{_kf5_libdir}/cmake/KPim5Gravatar/
%{_includedir}/KPim5/Gravatar/

%{_kf5_archdatadir}/mkspecs/modules/qt_Gravatar.pri

%changelog
%autochangelog
