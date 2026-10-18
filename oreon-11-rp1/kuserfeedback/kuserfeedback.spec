%global source0_hash c8a463c8e570f6d532cbe150732220575c6385df97c91399b6c84450691771ca

Name:    kuserfeedback
Summary: Framework for collecting user feedback for apps via telemetry and surveys
Version: 6.30.0
Release: 1%{?dist}

License: MIT
URL:     https://invent.kde.org/libraries/%{name}
Source0: https://download.kde.org/stable/frameworks/6.30/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/stable/frameworks/6.30/%{name}-%{version}.tar.xz.sig
Source2: gpgkey-E0A3EB202F8E57528E13E72FD7574483BB57B18D.gpg

## upstream patches

BuildRequires: cmake
BuildRequires: gnupg2
BuildRequires: gcc-c++

BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Charts)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Qml)

BuildRequires: bison
BuildRequires: flex

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Network)
Requires:       cmake(Qt6Widgets)

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        console
Summary:        Analytics and administration tool for UserFeedback servers
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtcharts%{?_isa}

%description    console
Analytics and administration tool for UserFeedback servers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake_kf6 \
   -DENABLE_DOCS:BOOL=OFF \
   -DENABLE_CONSOLE:BOOL=ON \
   -DENABLE_PHP:BOOL=OFF \
   -DENABLE_PHP_UNIT:BOOL=OFF

%cmake_build

%install
%cmake_install

%find_lang userfeedbackconsole6 --with-qt
%find_lang userfeedbackprovider6 --with-qt

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.kde.kuserfeedback-console.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.kuserfeedback-console.desktop

%files -f userfeedbackprovider6.lang
%doc README.md
%license COPYING.LIB
%{_bindir}/userfeedbackctl
%{_libdir}/libKF6UserFeedbackCore.so.6*
%{_libdir}/libKF6UserFeedbackWidgets.so.6*
%{_kf6_qmldir}/org/kde/userfeedback/
%{_libdir}/qt6/mkspecs/modules/qt_KF6UserFeedbackCore.pri
%{_libdir}/qt6/mkspecs/modules/qt_KF6UserFeedbackWidgets.pri

%files devel
%{_includedir}/KF6/KUserFeedback/
%{_includedir}/KF6/KUserFeedbackCore/
%{_includedir}/KF6/KUserFeedbackWidgets/
%{_libdir}/libKF6UserFeedbackCore.so
%{_libdir}/libKF6UserFeedbackWidgets.so
%{_libdir}/cmake/KF6UserFeedback/

%files console -f userfeedbackconsole6.lang
%{_bindir}/UserFeedbackConsole
%{_datadir}/applications/org.kde.kuserfeedback-console.desktop
%{_datadir}/metainfo/org.kde.kuserfeedback-console.appdata.xml
%{_datadir}/qlogging-categories6/org_kde_UserFeedback.categories

%changelog
%autochangelog
