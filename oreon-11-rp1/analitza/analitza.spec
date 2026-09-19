%global source0_hash 615b7c244a5baee0be5214c53b8ce37d0a54e69a6fd6b8438c30d7fda45b0746


# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests %[!(0%{?rhel} >= 10)]
%endif

Name:    analitza
Summary: Library of mathematical features
Version: 26.04.3
Release: 1%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://invent.kde.org/education/%{name}
Source:  https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: cmake(Qt6OpenGLWidgets)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Eigen3)

%if 0%{?tests}
BuildRequires: xorg-x11-server-Xvfb
%endif

%description
%{summary}.

%package devel
Summary: Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup


%build
%cmake_kf6 \
  %{?tests:-DBUILD_TESTING:BOOL=ON}

%cmake_build


%install
%cmake_install

%find_lang_kf6 analitza_qt


%check
%if 0%{?tests}
pushd "%{__cmake_builddir}"
xvfb-run -a \
ctest --output-on-failure --force-new-ctest-process %{?_smp_mflags} --timeout 300 ||:
popd
%endif


%files -f analitza_qt.lang
#doc TODO
%license COPYING*
%dir %{_datadir}/libanalitza/
%{_datadir}/libanalitza/plots/
%{_kf6_libdir}/libAnalitza.so.9*
%{_kf6_libdir}/libAnalitzaGui.so.9*
%{_kf6_libdir}/libAnalitzaPlot.so.9*
%{_kf6_libdir}/libAnalitzaWidgets.so.9*
%{_kf6_qmldir}/org/kde/analitza/

%files devel
%{_includedir}/Analitza6/
%{_kf6_libdir}/libAnalitza.so
%{_kf6_libdir}/libAnalitzaGui.so
%{_kf6_libdir}/libAnalitzaPlot.so
%{_kf6_libdir}/libAnalitzaWidgets.so
%{_kf6_libdir}/cmake/Analitza6/


%changelog
%autochangelog

