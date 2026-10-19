%global source0_hash 67af0c2d74715957bd5373a6a30589ff0a996cb1d267dfd0538dccaa9a768dfa
%undefine __cmake_in_source_build
%if !0%{?bootstrap}
%endif
Name:    kproperty
Summary:        Property editing framework with editor widget
Version: 3.2.0
Release:        15%{?dist}
License: LicenseRef-Callaway-LGPLv2+
Url:     https://community.kde.org/KProperty
Source0:        http://download.kde.org/stable/%{name}/src/%{name}-%{version}.tar.xz
Patch100: kproperty-3.0.2-pkgconfig.patch
%if 0%{?tests}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf5-rpm-macros
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
A property editing framework with editor widget similar to what is
known from Qt Designer.

%package devel
Summary: Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(KF5GuiAddons)
Requires: cmake(KF5WidgetsAddons)
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{cmake_kf5} \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{?!tests:OFF}
%cmake_build
%install
%cmake_install
%find_lang_kf5 kpropertycore_qt
%find_lang_kf5 kpropertywidgets_qt
cat *_qt.lang  > all.lang
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
make test ARGS="--output-on-failure --timeout 20" -C %{_target_platform} ||:
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n kproperty-devel -f %{oreon_filedir}/kproperty-devel.list

%changelog

%autochangelog
