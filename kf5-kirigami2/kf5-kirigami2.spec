%global framework kirigami2

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: QtQuick plugins to build user interfaces based on the KDE UX guidelines

# templates/kirigami/src/contents/ui/About.qml: File is mislabeled as "GPL-2.1-or-later"
# in this version's source, but has been updated upstream to LGPL-2.1-or-later
License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND FSFAP AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT AND LGPL-2.1-or-later
URL:     https://techbase.kde.org/Kirigami

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

## upstream paches

# filter qml provides
%global __provides_exclude_from ^%{_kf5_qmldir}/.*\\.so$

BuildRequires: make
BuildRequires: extra-cmake-modules >= %{majmin}
BuildRequires: kf5-rpm-macros

BuildRequires: qt5-linguist
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-qtquickcontrols2-devel
BuildRequires: qt5-qtsvg-devel

BuildRequires: qt5-qtbase-private-devel


%if 0%{?tests}
%if 0%{?fedora}
BuildRequires: appstream
%endif
BuildRequires: xorg-x11-server-Xvfb
%endif

# workaround https://bugs.kde.org/show_bug.cgi?id=395156
%if 0%{?rhel}==7
BuildRequires: devtoolset-7-toolchain
BuildRequires: devtoolset-7-gcc-c++
%endif

Requires:      qt5-qtquickcontrols%{?_isa}
Requires:      qt5-qtquickcontrols2%{?_isa}

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
# strictly not required, but some consumers may assume/expect runtime bits to be present too
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
%if 0%{?rhel}==7
. /opt/rh/devtoolset-7/enable
%endif
%{cmake_kf5} \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}
%cmake_build


%install
%cmake_install

%find_lang_kf5 libkirigami2plugin_qt


%check
%if 0%{?tests}
## known failure(s), not sure if possible to enable opengl/glx using
## virtualized server (QT_XCB_FORCE_SOFTWARE_OPENGL doesn't seem to help)
#2/2 Test #2: qmltests .........................***Exception: Other  0.19 sec
#Could not initialize GLX
export QT_XCB_FORCE_SOFTWARE_OPENGL=1
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
  make test ARGS="--output-on-failure --timeout 30" -C %{_vpath_builddir} ||:
%endif


%files -f libkirigami2plugin_qt.lang
# README is currently only build instructions, omit for now
#doc README.md
%license LICENSES/*.txt
%{_kf5_libdir}/libKF5Kirigami2.so.5*
%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde/
%{_kf5_qmldir}/org/kde/kirigami.2/

%files devel
%{_kf5_libdir}/libKF5Kirigami2.so
%{_kf5_includedir}/Kirigami2/
%{_kf5_archdatadir}/mkspecs/modules/qt_Kirigami2.pri
%{_kf5_libdir}/cmake/KF5Kirigami2/
%dir %{_kf5_datadir}/kdevappwizard/
%dir %{_kf5_datadir}/kdevappwizard/templates/
%{_kf5_datadir}/kdevappwizard/templates/kirigami.tar.bz2


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
