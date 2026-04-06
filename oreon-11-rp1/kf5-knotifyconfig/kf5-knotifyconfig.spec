%undefine __cmake_in_source_build
%global framework knotifyconfig

## uncomment to enable bootstrap mode
#global bootstrap 1

## currently includes no tests
#if !0%%{?bootstrap}
#global tests 1
#endif

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 3 module for KNotify configuration

License: CC0-1.0 AND LGPL-2.0-only
URL:     https://invent.kde.org/frameworks/%{framework}

%global kf5_dl_bug %(echo %{version} | cut -d. -f3)
%if 0%{?kf5_dl_bug} >= 50
%global kf5_dl_stable unstable
%global kf5_dl_majmin %(echo %{version} | cut -d. -f1,2).50
%else
%global kf5_dl_stable stable
%global kf5_dl_majmin %(echo %{version} | cut -d. -f1,2)
%endif
Source0: http://download.kde.org/%{kf5_dl_stable}/frameworks/%{kf5_dl_majmin}/%{framework}-%{version}.tar.xz

## upstream patches

BuildRequires:  make
BuildRequires:  extra-cmake-modules >= %{kf5_dl_majmin}
BuildRequires:  kf5-kcompletion-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kconfig-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kconfigwidgets-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-ki18n-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kio-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-knotifications-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kxmlgui-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-rpm-macros
BuildRequires:  libcanberra-devel
BuildRequires:  phonon-qt5-devel
BuildRequires:  qt5-qtbase-devel

%if !0%{?bootstrap}
%if 0%{?fedora}
BuildRequires:  cmake(Qt5TextToSpeech)
%endif
%endif

%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: time
BuildRequires: xorg-x11-server-Xvfb
%endif

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
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
time \
make test ARGS="--output-on-failure --timeout 10" -C %{_target_platform} ||:
%endif


%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/*%{framework}.*
%{_kf5_libdir}/libKF5NotifyConfig.so.*

%files devel

%{_kf5_includedir}/KNotifyConfig/
%{_kf5_libdir}/libKF5NotifyConfig.so
%{_kf5_libdir}/cmake/KF5NotifyConfig/
%{_kf5_archdatadir}/mkspecs/modules/qt_KNotifyConfig.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
