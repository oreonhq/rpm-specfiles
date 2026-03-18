Name:    baloo-widgets
Summary: Widgets for Baloo
Version: 25.12.3
Release: 1%{?dist}

# # KDE e.V. may determine that future LGPL versions are accepted
License: LGPL-2.0-only OR LGPL-3.0-only
URL:     https://invent.kde.org/libraries/%{name}
Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Test)

BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6FileMetaData)
BuildRequires:  cmake(KF6Baloo)

%description
%{summary}.

%package devel
Summary:  Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel
Requires: kf6-kcoreaddons-devel
Requires: kf6-kio-devel
%description devel
%{summary}.


%prep
%autosetup


%build
%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name


%files -f %{name}.lang
%doc LICENSES/*
%{_kf6_libdir}/libKF6BalooWidgets.so.*
%{_kf6_bindir}/baloo_filemetadata_temp_extractor
%{_kf6_datadir}/qlogging-categories6/%{name}*
%{_kf6_plugindir}/propertiesdialog/
%{_kf6_plugindir}/kfileitemaction/

%files devel
%{_kf6_libdir}/cmake/KF6BalooWidgets/
%{_kf6_includedir}/BalooWidgets/
%{_kf6_libdir}/libKF6BalooWidgets.so


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
