%global source0_hash 22716d719654e8f887fe4d33654e252ddf3d3d818c44e15a8af0e6f2e7d6ccd7

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
# some known failures, ping upstream
#global tests 1
%endif

Name:    kreport
Summary: Framework for creation and generation of reports
Version: 3.2.0
Release: 21%{?dist}

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+

Url:     https://community.kde.org/KReport
Source0: http://download.kde.org/stable/%{name}/src/%{name}-%{version}.tar.xz

## upstream patches
Patch19: 0019-Fix-build-with-GCC-10-make-KReportGroupTracker-use-C.patch
Patch22: 0022-Find-also-Python3-with-find_package-PythonInterp.patch

## upstreamable patches
# fix/sanitize pkgconfig deps
Patch100: kreport-3.0.2-pkgconfig.patch

BuildRequires: gcc-c++

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5LinguistTools)

BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5Config)

BuildRequires: cmake(KPropertyWidgets) >= %{version}
BuildRequires: kproperty-devel >= %{version}
Requires:      kproperty%{?_isa} >= %{version}
# default python interpreter (ie, /usr/bin/python)
BuildRequires: python3

# autodeps
BuildRequires: cmake
BuildRequires: pkgconfig

# plugins
#BuildRequires: cmake(Marble)
#BuildRequires: cmake(Qt5WebKitWidgets)

%if 0%{?tests}
BuildRequires: cmake(Qt5Test)
BuildRequires: xorg-x11-server-Xvfb
%endif

%description
A framework for creation and generation of reports in multiple formats.

%package devel
Summary: Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(KPropertyWidgets) >= %{version}
Requires: cmake(KF5CoreAddons)
Requires: cmake(KF5WidgetsAddons)
Requires: cmake(KF5GuiAddons)
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf5 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{?!tests:OFF} \
  -DPYTHON_EXECUTABLE:PATH="%{__python3}"

%cmake_build

%install
%cmake_install

%find_lang_kf5 kreport_barcodeplugin_qt
%find_lang_kf5 kreport_mapsplugin_qt
%find_lang_kf5 kreport_qt
%find_lang_kf5 kreport_webplugin_qt
cat *_qt.lang > all.lang

%check
## tests have known failures, TODO: consult upstream
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
#xvfb-run -a \
make test ARGS="--output-on-failure --timeout 20" -C %{_target_platform} ||:
%endif

%ldconfig_scriptlets

%files -f all.lang
%license COPYING.LIB
%{_libdir}/libKReport3.so.4*
%dir %{_qt5_plugindir}/kreport3/
# TODO: consider splitting some into subpkgs (maps/marble in particular)
%{_qt5_plugindir}/kreport3/org.kde.kreport.barcode.so
#%%{_qt5_plugindir}/kreport3/org.kde.kreport.maps.so
#%%{_qt5_plugindir}/kreport3/org.kde.kreport.web.so
%{_kf5_datadir}/kservicetypes5/kreport_elementplugin.desktop
# .rcc icon resources
%{_datadir}/kreport3/

%files devel
%{_includedir}/KReport3/
%{_libdir}/libKReport3.so
%{_libdir}/cmake/KReport3/
%{_libdir}/pkgconfig/KReport3.pc
%{_kf5_archdatadir}/mkspecs/modules/qt_KReport3.pri

%changelog
%autochangelog
