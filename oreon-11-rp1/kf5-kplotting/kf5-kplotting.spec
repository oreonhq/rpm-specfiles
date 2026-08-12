%global source0_hash bc3703f2ccd5d9d6a5e881a9476a6d21b2722aecbe5dfe48c03d1008772be579

%undefine __cmake_in_source_build
%global framework kplotting

Name:           kf5-%{framework}
Version: 5.116.0
Release: 7%{?dist}
Summary:        KDE Frameworks 5 Tier 1 addon for plotting

License:        CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}

%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/stable/frameworks/5.116/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros >= %{majmin}
BuildRequires:  pcre-devel
BuildRequires:  perl-interpreter

BuildRequires:  qt5-qtbase-devel
BuildRequires:  cmake(Qt5UiPlugin)

Requires:       kf5-filesystem >= %{majmin}

%description
KPlotting provides classes to do plotting.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
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

%ldconfig_scriptlets

%files
%doc README.md
%license LICENSES/*.txt
%{_kf5_libdir}/libKF5Plotting.so.*
%{_kf5_qtplugindir}/designer/kplotting5widgets.so

%files devel

%{_kf5_includedir}/KPlotting/
%{_kf5_libdir}/libKF5Plotting.so
%{_kf5_libdir}/cmake/KF5Plotting/
%{_kf5_archdatadir}/mkspecs/modules/qt_KPlotting.pri

%changelog
%autochangelog
