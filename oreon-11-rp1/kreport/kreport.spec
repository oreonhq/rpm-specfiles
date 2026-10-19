%global source0_hash 22716d719654e8f887fe4d33654e252ddf3d3d818c44e15a8af0e6f2e7d6ccd7
%if !0%{?bootstrap}
%endif
Name:    kreport
Summary:        Framework for creation and generation of reports
Version: 3.2.0
Release:        21%{?dist}
License: LicenseRef-Callaway-LGPLv2+
Url:     https://community.kde.org/KReport
Source0:        http://download.kde.org/stable/%{name}/src/%{name}-%{version}.tar.xz
Patch19: 0019-Fix-build-with-GCC-10-make-KReportGroupTracker-use-C.patch
Patch22: 0022-Find-also-Python3-with-find_package-PythonInterp.patch
Patch100: kreport-3.0.2-pkgconfig.patch
Requires:      kproperty%{?_isa} >= %{version}
%if 0%{?tests}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KPropertyWidgets)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf5-rpm-macros
BuildRequires:  kproperty-devel
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
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
%oreon_prep
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
make test ARGS="--output-on-failure --timeout 20" -C %{_target_platform} ||:
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n kreport-devel -f %{oreon_filedir}/kreport-devel.list

%changelog

%autochangelog
