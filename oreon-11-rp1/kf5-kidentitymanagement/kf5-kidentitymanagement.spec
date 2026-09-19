%global source0_hash bcd7f7ef26a24b2d198a7739bdc8b4f3868d42e05355173fbc91a95220d77201

%global framework kidentitymanagement

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Version: 23.08.5
Release: 5%{?dist}
Summary: The KIdentityManagement Library

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  cmake(KF5TextEditTextToSpeech)
BuildRequires:  cmake(KPim5TextEdit)
BuildRequires:  kf5-kdelibs4support-devel >= 5.15
BuildRequires:  kf5-kcoreaddons-devel >= 5.15
BuildRequires:  kf5-kcompletion-devel >= 5.15
BuildRequires:  kf5-ktextwidgets-devel >= 5.15
BuildRequires:  kf5-kxmlgui-devel >= 5.15
BuildRequires:  kf5-kio-devel >= 5.15
BuildRequires:  kf5-kconfig-devel >= 5.15
BuildRequires:  kf5-kemoticons-devel >= 5.15
BuildRequires:  kf5-kcodecs-devel >= 5.15
#global majmin_ver %(echo %{version} | cut -d. -f1,2)
%global majmin_ver %{version}
BuildRequires:  qt5-qtbase-devel
%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: xorg-x11-server-Xvfb
%endif

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kcoreaddons-devel
Requires:       kf5-kpimtextedit-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf5 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name

%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
make test ARGS="--output-on-failure --timeout 10" -C %{_target_platform} ||:
%endif

%ldconfig_scriptlets

%files -f %{name}.lang
%license LICENSES/*
%{_kf5_datadir}/qlogging-categories5/*%{framework}.*
%{_kf5_libdir}/libKPim5IdentityManagement.so.*
%{_kf5_libdir}/libKPim5IdentityManagementWidgets.so.*
%{_kf5_archdatadir}/mkspecs/modules/qt_KIdentityManagementWidgets.pri

%files devel
%{_datadir}/dbus-1/interfaces/kf5_org.kde.pim.IdentityManager.xml
%{_kf5_archdatadir}/mkspecs/modules/qt_KIdentityManagement.pri
%{_includedir}/KPim5/KIdentityManagement/
%{_includedir}/KPim5/KIdentityManagementWidgets/
%{_kf5_libdir}/cmake/KF5IdentityManagement/
%{_kf5_libdir}/cmake/KPim5IdentityManagement/
%{_kf5_libdir}/libKPim5IdentityManagement.so
%{_kf5_libdir}/libKPim5IdentityManagementWidgets.so

%changelog
%autochangelog
