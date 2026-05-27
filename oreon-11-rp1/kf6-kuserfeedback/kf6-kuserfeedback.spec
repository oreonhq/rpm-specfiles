%global source0_hash 3004be541acf03b6e2203b5eafede7f9d9a8fe41d77cdd2aee35e03f13929a30

%global framework kuserfeedback

%global stable_kf6 stable
%global majmin_ver_kf6 6.24


Name:    kf6-%{framework}
Summary: Framework for collecting user feedback for apps via telemetry and surveys
Version: 6.24.0
Release:	6%{?dist}

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n %{framework}-%{version}


%build
%cmake_kf6 \
   -DENABLE_DOCS:BOOL=OFF \
   -DENABLE_CONSOLE=ON

%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
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
- inline cmake --build (no qt6 prepare_docs pass)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop Qt6 qdoc -html packaging (kf6 macros skip qt6 prepare_docs pass)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Qt6 qdoc: -html file list via find, tags/index in -devel

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop -DQDOC_BIN=/bin/true now that qt6-qttools qdoc is patched (QTBUG-142742)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)

