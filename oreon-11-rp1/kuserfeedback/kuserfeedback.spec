%global source0_hash 252308b822dd4690ea85ab1688c9b0da5512978ac6b435f77a5979fc1d2ffd13

%bcond kf6_compat %[0%{?fedora} >= 40 || 0%{?rhel} >= 10]

Name:    kuserfeedback
Summary: Framework for collecting user feedback for apps via telemetry and surveys
Version: 1.3.0
Release: 9%{?dist}

License: MIT
URL:     https://invent.kde.org/libraries/%{name}
Source0: https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz.sig
Source2: gpgkey-E0A3EB202F8E57528E13E72FD7574483BB57B18D.gpg

## upstream patches

BuildRequires: cmake
BuildRequires: gnupg2
BuildRequires: gcc-c++

BuildRequires: kf5-rpm-macros
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules

BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Charts)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5LinguistTools)

BuildRequires: bison
BuildRequires: flex

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt5Network)
Requires:       cmake(Qt5Widgets)

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        console
Summary:        Analytics and administration tool for UserFeedback servers
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  qt5-qtbase-private-devel
Requires:       qt5-qtcharts%{?_isa}

%description    console
Analytics and administration tool for UserFeedback servers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake_kf5 \
   -DENABLE_DOCS:BOOL=OFF \
   %{?with_kf6_compat:-DENABLE_CLI=OFF}

%cmake_build

%install
%cmake_install

%find_lang userfeedbackconsole5 --with-qt
%find_lang userfeedbackprovider5 --with-qt

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.kuserfeedback-console.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.kuserfeedback-console.desktop

%files -f userfeedbackprovider5.lang
%doc README.md
%license COPYING.LIB
%if %{without kf6_compat}
%{_bindir}/userfeedbackctl
%endif
%{_libdir}/libKUserFeedbackCore.so.1*
%{_libdir}/libKUserFeedbackWidgets.so.1*
%{_kf5_qmldir}/org/kde/userfeedback/
%{_kf5_datadir}/qlogging-categories5/org_kde_UserFeedback.categories

%files devel
%{_includedir}/KUserFeedback/
%{_libdir}/libKUserFeedbackCore.so
%{_libdir}/libKUserFeedbackWidgets.so
%{_kf5_libdir}/cmake/KUserFeedback/
%{_kf5_archdatadir}/mkspecs/modules/qt_KUserFeedback*.pri

%files console -f userfeedbackconsole5.lang
%{_bindir}/UserFeedbackConsole
%{_datadir}/applications/org.kde.kuserfeedback-console.desktop
%{_kf5_metainfodir}/org.kde.kuserfeedback-console.appdata.xml

%changelog
%autochangelog
