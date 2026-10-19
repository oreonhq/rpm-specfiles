%global stable_kf6 stable
%global source0_hash 615b7c244a5baee0be5214c53b8ce37d0a54e69a6fd6b8438c30d7fda45b0746
%if !0%{?bootstrap}
%global tests %[!(0%{?rhel} >= 10)]
%endif
Name:    analitza
Summary:        Library of mathematical features
Version: 26.04.3
Release:        1%{?dist}
License: GPL-2.0-or-later
URL:     https://invent.kde.org/education/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if 0%{?tests}
%endif
# oreon:deps
BuildRequires:  cmake(Eigen3)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
%{summary}.

%package devel
Summary: Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6 \
  %{?tests:-DBUILD_TESTING:BOOL=ON}
%cmake_build
%install
%cmake_install
%find_lang_kf6 analitza_qt
%oreon_autofiles analitza-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if 0%{?tests}
pushd "%{__cmake_builddir}"
xvfb-run -a \
ctest --output-on-failure --force-new-ctest-process %{?_smp_mflags} --timeout 300 ||:
popd
%endif
%files -f %{oreon_filedir}/main.list
%files -n analitza-devel -f %{oreon_filedir}/analitza-devel.list

%changelog

%autochangelog

