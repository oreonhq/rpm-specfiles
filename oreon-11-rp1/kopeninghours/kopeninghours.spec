%global source0_hash 674f7dd168679eecbc85d7e68052a0a979f4243a432958a698ba5bbd82178589

Name:    kopeninghours
Version: 25.12.3
Release: 2%{?dist}
Summary: Library for parsing and evaluating OSM opening hours expressions

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/libraries/%{name}

Source0: https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake
BuildRequires:  cmake(KF6Holidays)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  python3-devel
BuildRequires:  boost-devel
Requires:       kf6-filesystem

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6 -DBUILD_QCH=OFF -DQT_MAJOR_VERSION=6
%cmake_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSES/*.txt
%doc README.md
%{_kf6_libdir}/libKOpeningHours.so.*
%{_qt6_qmldir}/org/kde/kopeninghours
%{_datadir}/qlogging-categories6/org_kde_kopeninghours.categories
%{python3_sitelib}/PyKOpeningHours/

%files devel
%{_includedir}/KOpeningHours
%{_kf6_libdir}/cmake/KOpeningHours
%{_kf6_libdir}/libKOpeningHours.so
%{_includedir}/kopeninghours
%{_includedir}/kopeninghours_version.h

%files doc

%changelog
%autochangelog
