%global framework kconfig

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
#global python_bindings 1
%global tests 1
%endif

# use ninja instead of make
%global ninja 1

Name:    kf5-%{framework}
Version: 5.116.0
Release: 6%{?dist}
Summary: KDE Frameworks 5 Tier 1 addon with advanced configuration system

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

## upstream patches

## upstreamable patches

%if 0%{?ninja}
BuildRequires:  ninja-build
%endif

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros >= %{majmin}

BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Xml)

%if 0%{?python_bindings}
BuildRequires:  clang
BuildRequires:  clang-devel
BuildRequires:  python3-clang
BuildRequires:  python3-PyQt5-devel
%else
Obsoletes: python3-pykf5-%{framework} < %{version}-%{release}
Obsoletes: pykf5-%{framework}-devel < %{version}-%{release}
%endif
Obsoletes: python2-pykf5-%{framework} < %{version}

%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: time
BuildRequires: xorg-x11-server-Xvfb
%endif

Requires:       kf5-filesystem >= %{majmin}
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       %{name}-gui%{?_isa} = %{version}-%{release}

%description
KDE Frameworks 5 Tier 1 addon with advanced configuration system made of two
parts: KConfigCore and KConfigGui.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt5Xml)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        core
Summary:        Non-GUI part of KConfig framework
Requires:       (kde-settings if plasma-workspace)
%description    core
KConfigCore provides access to the configuration files themselves. It features
centralized definition and lock-down (kiosk) support.

%package        gui
Summary:        GUI part of KConfig framework
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
%description    gui
KConfigGui provides a way to hook widgets to the configuration so that they are
automatically initialized from the configuration and automatically propagate
their changes to their respective configuration files.

%if 0%{?python_bindings}
%package -n python3-pykf5-%{framework}
Summary: Python3 bindings for %{framework}
Requires: %{name} = %{version}-%{release}
%description -n python3-pykf5-%{framework}
%{summary}.

%package -n pykf5-%{framework}-devel
Summary: SIP files for %{framework} Python bindings
BuildArch: noarch
%description -n pykf5-%{framework}-devel
%{summary}.
%endif


%prep
%autosetup -n %{framework}-%{version} -p1


%build

%if 0%{?python_bindings:1}
PYTHONPATH=%{_datadir}/ECM/python
export PYTHONPATH
%endif

%cmake_kf5 \
  %{?ninja:-G Ninja} \
  %{?tests:-DBUILD_TESTING:BOOL=ON}

%cmake_build || \
cat %{__cmake_builddir}/autotests/kconfig_compiler/test5.cpp


%install
%cmake_install

%find_lang_kf5 kconfig5_qt


%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
## cant use %%ninja_test here for some reason, doesn't inherit env vars from xvfb or dbus -- rex
xvfb-run -a \
%if 0%{?ninja}
ninja test %{?_smp_mflags} -v -C redhat-linux-build ||:
%else
make test %{?_smp_mflags} -C redhat-linux-build ARGS="--output-on-failure --timeout 300" ||:
%endif
%endif


%files
%doc DESIGN README.md TODO
%license LICENSES/*.txt

%files core -f kconfig5_qt.lang
%{_kf5_bindir}/kreadconfig5
%{_kf5_bindir}/kwriteconfig5
%{_kf5_libexecdir}/kconfig_compiler_kf5
%{_kf5_libexecdir}/kconf_update
%{_kf5_libdir}/libKF5ConfigCore.so.5*
%{_kf5_libdir}/libKF5ConfigQml.so.5*
%{_kf5_datadir}/qlogging-categories5/%{framework}*

%files gui
%{_kf5_libdir}/libKF5ConfigGui.so.*

%files devel
%{_kf5_includedir}/KConfig/
%{_kf5_includedir}/KConfigCore/
%{_kf5_includedir}/KConfigGui/
%{_kf5_includedir}/KConfigQml/
%{_kf5_libdir}/libKF5ConfigCore.so
%{_kf5_libdir}/libKF5ConfigGui.so
%{_kf5_libdir}/libKF5ConfigQml.so
%{_kf5_libdir}/cmake/KF5Config/
%{_kf5_archdatadir}/mkspecs/modules/qt_KConfigCore.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_KConfigGui.pri

%if 0%{?python_bindings}
%files -n python3-pykf5-%{framework}
%{python3_sitearch}/PyKF5/

%files -n pykf5-%{framework}-devel
%{_datadir}/sip/PyKF5/
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-6
- Prepare for Oreon 11 (RP1)
