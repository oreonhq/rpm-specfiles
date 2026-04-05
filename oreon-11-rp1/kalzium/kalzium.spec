# workaround for bz#1546230
# ocaml doesn't support relocation
%undefine _hardened_build

%if ! 0%{?bootstrap}
# The Kalzium solver needs OCaml with native compilation support (ocamlopt) and
# ocaml-facile.
%ifarch %{?ocaml_native_compiler}
%global with_facile 1
%endif

# pending fix for https://bugzilla.redhat.com/1544510
# disabled for Qt6, see CMakeLists.txt
%global avogadro 1
%endif


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kalzium
Summary: Periodic Table of Elements
Version: 25.12.3
Release:	2%{?dist}

License: GPL-2.0-or-later
URL:     https://invent.kde.org/education/kalzium
	
Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches

%if ! 0%{?bootstrap}
BuildRequires: libappstream-glib
BuildRequires: chemical-mime-data
BuildRequires: desktop-file-utils
%endif

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6Plotting)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6UnitConversion)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6Crash)

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: cmake(Qt6StateMachine)

BuildRequires: pkgconfig(openbabel-3)
%if 0%{?avogadro}
# Eigen is only used for the Avogadro-based compound viewer.
BuildRequires: pkgconfig(eigen3)
BuildRequires: cmake(AvogadroLibs)
# workaround missing dep in avogadro2-libs-devel for now
BuildRequires: glew-devel
BuildRequires: spglib-devel
%endif
%if 0%{?with_facile}
# OCaml is only used with the Facile library, in the equation balancer.
BuildRequires: ocaml(compiler)
BuildRequires: ocaml-facile-devel
%endif

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

# build.log wants this one, but it is really only used at runtime:
Requires: chemical-mime-data

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
%autosetup -p1


%build
%cmake_kf6 \
	-DQT_MAJOR_VERSION=6

%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-html --with-man


%check
%if !0%{?bootstrap}
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kalzium.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kalzium.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kalzium_cml.desktop
%endif


%files -f %{name}.lang
%dir %{_kf6_datadir}/libkdeedu/
%license LICENSES/*
%{_kf6_bindir}/kalzium
%{_kf6_datadir}/applications/org.kde.kalzium.desktop
%{_kf6_datadir}/applications/org.kde.kalzium_cml.desktop
%{_kf6_datadir}/config.kcfg/kalzium.kcfg
%{_kf6_datadir}/icons/hicolor/*/*/kalzium.*
%{_kf6_datadir}/kalzium/
%{_kf6_datadir}/libkdeedu/data/
%{_kf6_datadir}/qlogging-categories6/kalzium.categories
%{_kf6_metainfodir}/org.kde.kalzium.appdata.xml
%{_mandir}/man1/kalzium.*
%{_kf6_datadir}/knsrcfiles/kalzium.knsrc

%files libs
%if 0%{?avogadro}
%{_kf6_libdir}/libcompoundviewer.so.5*
%endif
%{_kf6_libdir}/libscience.so.5*

%files devel
%dir %{_includedir}/libkdeedu/
%{_includedir}/libkdeedu/*.h
%if 0%{?avogadro}
%{_kf6_libdir}/libcompoundviewer.so
%endif
%{_kf6_libdir}/libscience.so


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
