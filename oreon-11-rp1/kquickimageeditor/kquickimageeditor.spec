%global source0_hash none

Name:    kquickimageeditor
Version: 0.6.0
Release: 6%{?dist}
Summary: QtQuick components providing basic image editing capabilities
License: BSD-2-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only
URL:     https://invent.kde.org/libraries/%{name}
Source0: https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires: extra-cmake-modules

BuildRequires: kf6-rpm-macros
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)

BuildRequires: cmake(KF6Config)

BuildRequires: cmake(OpenCV)

%description
%{summary}

%package qt6
Summary: Qt6 QtQuick components providing basic image editing capabilities

%description qt6
%{summary}

%package qt6-devel
Summary: Development files for %{name}-qt6
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}

%description qt6-devel
The %{name}-qt6-devel package contains cmake and mkspecs for developing
applications that use %{name}-qt6.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%files qt6
%{_kf6_qmldir}/org/kde/kquickimageeditor
%{_kf6_libdir}/libKQuickImageEditor.so.%{version}
%{_kf6_libdir}/libKQuickImageEditor.so.1

%files qt6-devel
%{_kf6_libdir}/libKQuickImageEditor.so
%{_kf6_libdir}/cmake/KQuickImageEditor
%{_includedir}/KQuickImageEditor/
%{_includedir}/kquickimageeditor/
%{_kf6_archdatadir}/mkspecs/modules/qt_KQuickImageEditor.pri

%changelog
%autochangelog

