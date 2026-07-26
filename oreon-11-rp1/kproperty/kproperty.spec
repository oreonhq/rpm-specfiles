%global source0_hash 67af0c2d74715957bd5373a6a30589ff0a996cb1d267dfd0538dccaa9a768dfa

%undefine __cmake_in_source_build

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
# some tests known to fail, ping upstream
#global tests 1
%endif

Name:    kproperty
Summary: Property editing framework with editor widget
Version: 3.2.0
Release: 15%{?dist}

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
Url:     https://community.kde.org/KProperty
Source0: http://download.kde.org/stable/%{name}/src/%{name}-%{version}.tar.xz

## upstreamable patches
# fix/sanitize pkgconfig deps
Patch100: kproperty-3.0.2-pkgconfig.patch

BuildRequires: make
BuildRequires: gcc-c++

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros

BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5LinguistTools)

BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5WidgetsAddons)

# autodeps
BuildRequires: cmake
BuildRequires: pkgconfig

%if 0%{?tests}
BuildRequires: cmake(Qt5Test)
BuildRequires: xorg-x11-server-Xvfb
%endif

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

%autosetup -p1

%build
%{cmake_kf5} \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{?!tests:OFF}
%cmake_build

%install
%cmake_install

%find_lang_kf5 kpropertycore_qt
%find_lang_kf5 kpropertywidgets_qt
cat *_qt.lang  > all.lang

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
%{_libdir}/libKPropertyCore3.so.4*
%{_libdir}/libKPropertyWidgets3.so.4*
# .rcc icon resources
# not sure if this is needed at runtime for sure or not, but it's relatively
# small currently, so can't hurt -- rex
%{_datadir}/kproperty3/

%files devel
%{_includedir}/KPropertyCore3/
%{_libdir}/libKPropertyCore3.so
%{_libdir}/cmake/KPropertyCore3/
%{_libdir}/pkgconfig/KPropertyCore3.pc

%{_includedir}/KPropertyWidgets3/
%{_libdir}/libKPropertyWidgets3.so
%{_libdir}/cmake/KPropertyWidgets3/
%{_libdir}/pkgconfig/KPropertyWidgets3.pc

%changelog
%autochangelog
