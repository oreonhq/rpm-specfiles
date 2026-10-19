%global source0_hash 7b5773311010665ed1da7f8782a14baed95dec11484115c420b84edb699803c3
%global stable_kf6 stable
%undefine _hardened_build
%if ! 0%{?bootstrap}
%ifarch %{?ocaml_native_compiler}
%global with_facile 1
%endif
%global avogadro 1
%endif
ExcludeArch: %{ix86}
Name:    kalzium
Summary:        Periodic Table of Elements
Version: 26.08.1
Release:        1%{?dist}
License: GPL-2.0-or-later
URL:     https://invent.kde.org/education/kalzium
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if ! 0%{?bootstrap}
%endif
%if 0%{?avogadro}
%endif
%if 0%{?with_facile}
%endif
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: chemical-mime-data
# oreon:deps
BuildRequires:  chemical-mime-data
BuildRequires:  cmake
BuildRequires:  cmake(AvogadroLibs)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Plotting)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6UnitConversion)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6StateMachine)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(openbabel-3)
BuildRequires:  spglib-devel
# /oreon:deps
%description
%{summary}.

%package  libs
Summary:  Runtime files for %{name}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.

%package devel
Summary:  Development files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6 \
	-DQT_MAJOR_VERSION=6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html --with-man
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if !0%{?bootstrap}
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kalzium.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kalzium.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kalzium_cml.desktop
%endif
%files -f %{oreon_filedir}/main.list
%files -n kalzium-libs -f %{oreon_filedir}/kalzium-libs.list
%files -n kalzium-devel -f %{oreon_filedir}/kalzium-devel.list

%changelog

%autochangelog
