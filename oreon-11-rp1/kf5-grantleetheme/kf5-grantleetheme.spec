%global source0_hash 686381b3a0fb0d28e415f9fc9a66633d3c17e75fc2696bf486491bdb3ff242f5

%global framework grantleetheme

Name:    kf5-%{framework}
Version: 23.08.5
Release: 6%{?dist}
Summary: KDE PIM library for Grantlee template system

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     http://invent.kde.org/pim/%{framework}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= 5.32.0
BuildRequires:  kf5-rpm-macros

BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)

# when macros.grantlee5 was introduced
BuildRequires:  grantlee-qt5-devel >= 5.1.0-2
%{?grantlee5_requires}

BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5NewStuff)

Conflicts:      kdepim-libs < 7:16.04.0
Obsoletes:      kdepim-libs < 7:16.04.0

# translations moved here
Conflicts: kde-l10n < 17.03

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Grantlee5)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

# Rename translation files to avoid conflict with KF6
find ./po -type f -execdir mv {} libgrantleetheme5.po \;
sed -i "/TRANSLATION_DOMAIN/ s/libgrantleetheme/libgrantleetheme5/" src/CMakeLists.txt
sed -i "s/libgrantleetheme/libgrantleetheme5/" src/Messages.sh

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
%{_kf5_libdir}/libKPim5GrantleeTheme.so.*
%{grantlee5_plugindir}/kde_grantlee_plugin.so

%files devel
%{_includedir}/KPim5/GrantleeTheme/
%{_kf5_libdir}/libKPim5GrantleeTheme.so
%{_kf5_libdir}/cmake/KPim5GrantleeTheme/
%{_kf5_archdatadir}/mkspecs/modules/qt_GrantleeTheme.pri

%changelog
%autochangelog
