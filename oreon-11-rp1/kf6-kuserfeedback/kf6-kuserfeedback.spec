%global framework kuserfeedback

%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:    kf6-%{framework}
Summary: Framework for collecting user feedback for apps via telemetry and surveys
Version: 6.24.0
Release:	3%{?dist}

License: MIT AND CC0-1.0 AND BSD-3-Clause
URL:     https://invent.kde.org/frameworks/%{framework}
Source0: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

## upstream patches

BuildRequires: cmake
BuildRequires: gnupg2
BuildRequires: gcc-c++

BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules

BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Charts)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6LinguistTools)

BuildRequires: bison
BuildRequires: flex

%description
%{summary}.

%package        console
Summary:        Analytics and administration tool for UserFeedback servers
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtcharts%{?_isa}
# Obsolete the qt5 version
Obsoletes:      kuserfeedback-console < %{version}-%{release}
Provides:       kuserfeedback-console = %{version}-%{release}
Provides:       kuserfeedback-console%{?_isa} = %{version}-%{release}

%description    console
Analytics and administration tool for UserFeedback servers.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Network)
Requires:       cmake(Qt6Widgets)

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n %{framework}-%{version}


%build
%cmake_kf6 \
   -DENABLE_DOCS:BOOL=OFF \
   -DENABLE_CONSOLE=ON

%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang userfeedbackconsole6 --with-qt
%find_lang userfeedbackprovider6 --with-qt


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kuserfeedback-console.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.kuserfeedback-console.desktop


%files -f userfeedbackprovider6.lang
%doc README.md
%license LICENSES/*
%{_bindir}/userfeedbackctl
%{_libdir}/libKF6UserFeedbackCore.so.*
%{_libdir}/libKF6UserFeedbackWidgets.so.*
%{_kf6_qmldir}/org/kde/userfeedback/
%{_kf6_datadir}/qlogging-categories6/org_kde_UserFeedback.categories

%files console -f userfeedbackconsole6.lang
%{_bindir}/UserFeedbackConsole
%{_datadir}/applications/org.kde.kuserfeedback-console.desktop
%{_kf6_metainfodir}/org.kde.kuserfeedback-console.appdata.xml

%files devel
%{_kf6_includedir}/KUserFeedback/
%{_kf6_includedir}/KUserFeedbackCore/
%{_kf6_includedir}/KUserFeedbackWidgets/
%{_libdir}/libKF6UserFeedbackCore.so
%{_libdir}/libKF6UserFeedbackWidgets.so
%{_kf6_libdir}/cmake/KF6UserFeedback/
%{_kf6_archdatadir}/mkspecs/modules/qt_KF6UserFeedback*.pri

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop -DQDOC_BIN=/bin/true now that qt6-qttools qdoc is patched (QTBUG-142742)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)
