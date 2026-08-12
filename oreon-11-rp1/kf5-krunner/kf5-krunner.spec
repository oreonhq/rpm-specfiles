%global source0_hash b87fb29e4354acb21f085b7978c7f1f49f41766a1d4f98fc86781fb9884a0841

%global framework krunner

Name:    kf5-%{framework}
Version: 5.116.0
Release: 7%{?dist}
Summary: KDE Frameworks 5 Tier 3 solution with parallelized query system

License: BSD-2-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/stable/frameworks/5.116/%{framework}-%{version}.tar.xz

## upstream patches

# filter qml provides
%global __provides_exclude_from ^%{_kf5_qmldir}/.*\\.so$

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros

BuildRequires:  kf5-kactivities-devel >= %{majmin}
BuildRequires:  kf5-kconfig-devel >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
BuildRequires:  kf5-kio-devel >= %{majmin}
BuildRequires:  kf5-kservice-devel >= %{majmin}
BuildRequires:  kf5-plasma-devel >= %{majmin}
BuildRequires:  kf5-solid-devel >= %{majmin}
BuildRequires:  kf5-threadweaver-devel >= %{majmin}

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel

%description
KRunner provides a parallelized query system extendable via plugins.

%package        devel
Summary:        Development files for %{name}
# krunner template moved here
Conflicts:      kapptemplate < 16.03.80
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-plasma-devel >= %{majmin}
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

%ldconfig_scriptlets

%files
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}*
%{_kf5_libdir}/libKF5Runner.so.*
%{_kf5_qmldir}/org/kde/runnermodel/
%{_kf5_datadir}/kservicetypes5/plasma-runner.desktop

%files devel
%{_kf5_includedir}/KRunner/
%{_kf5_libdir}/libKF5Runner.so
%{_kf5_libdir}/cmake/KF5Runner/
%{_kf5_archdatadir}/mkspecs/modules/qt_KRunner.pri
%{_kf5_datadir}/kdevappwizard/templates/*.tar.bz2
%{_kf5_datadir}/dbus-1/interfaces/*

%changelog
%autochangelog
