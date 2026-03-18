# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global analitza 1
%global qalculate 1
%if 0%{?fedora}
# match julia.spec: ExclusiveArch:  x86_64
%ifarch x86_64
%global julia %%{undefined flatpak}
%endif
%global libr 1
%endif
%global libspectre 1
%ifarch %{arm} %{ix86} x86_64 aarch64
%global luajit 1
%endif
%global python3 1
%endif

# track libcantor soname, rebuild dependencies for changes, includes:
# LabPlot
%global soname 28

Name:    cantor
Summary: KDE Frontend to Mathematical Software
Version: 25.12.3
Release: 1%{?dist}

License: GPL-2.0-or-later
URL:     https://apps.kde.org/cantor/
Source:  https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

## upstream fixes
## upstreamable patches
# Kill using cantor internal API
Patch2:  cantor-21.04.3-no-julia-internal.patch

BuildRequires: openblas-devel

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6Pty)
BuildRequires: cmake(KF6SyntaxHighlighting)
BuildRequires: cmake(KF6TextEditor)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6XmlGui)

BuildRequires: cmake(Qt6Help)
BuildRequires: cmake(Qt6WebEngineCore)
BuildRequires: cmake(Qt6WebEngineWidgets)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Core5Compat)

BuildRequires: pkgconfig(libxslt)
BuildRequires: pkgconfig(poppler-qt6)

# optional deps/plugins

%if 0%{?analitza}
BuildRequires: cmake(Analitza6)
%endif
%if 0%{?qalculate}
BuildRequires: pkgconfig(libqalculate)
%endif
%if 0%{?libspectre}
BuildRequires: pkgconfig(libspectre)
%endif
%if 0%{?luajit}
BuildRequires: pkgconfig(luajit)
%endif
%if 0%{?python3}
BuildRequires: python3-devel
%endif
# no python3 subpkg anymore
Obsoletes: cantor-python3 < 20.04.1

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
%{summary}.

%package  libs
Summary:  Runtime files for %{name}
# when split occurred
Conflicts: kdeedu-math-libs < 4.7.0-10
Provides: %{name}-part = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
%if ! 0%{?julia}
Obsoletes: %{name}-julia < %{version}-%{release}
%endif
%if ! 0%{?libr}
Obsoletes: %{name}-R < %{version}-%{release}
%endif
%description libs
%{summary}.

%if 0%{?julia}
%package julia
Summary: julia backend for %{name}
BuildRequires: julia-devel
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Supplements: (%{name} and julia)
%description julia
%{summary}.
%endif

%if 0%{?libr}
%package R
Summary: R backend for %{name}
BuildRequires: pkgconfig(libR)
Obsoletes: kdeedu-math-cantor-R < 4.7.0-10
Provides:  kdeedu-math-cantor-R = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Supplements: (%{name} and R-core)
%description R 
%{summary}.
%endif

%package devel
Summary:  Development files for %{name}
# when split occurred
Conflicts: kdeedu-devel < 4.7.0-10
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
%{summary}.


%prep
%autosetup -p1


%build
# PYTHONLIBS_FOUND is used to find Python 2.7
# PYTHONLIBS3_FOUND is used to find Python 3.x
%cmake_kf6

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop


%files -f %{name}.lang
%doc README*
%license LICENSES/*
%{_kf6_bindir}/cantor
%{_kf6_bindir}/cantor_pythonserver
%{_kf6_bindir}/cantor_scripteditor
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/knsrcfiles/cantor.knsrc
%if 0%{?analitza}
%{_kf6_datadir}/knsrcfiles/cantor_kalgebra.knsrc
%endif
%if 0%{?luajit}
%{_kf6_datadir}/knsrcfiles/cantor_lua.knsrc
%endif
%{_kf6_datadir}/knsrcfiles/cantor_maxima.knsrc
%{_kf6_datadir}/knsrcfiles/cantor_octave.knsrc
%if 0%{?python3}
%{_kf6_datadir}/knsrcfiles/cantor_python.knsrc
%endif
%if 0%{?qalculate}
%{_kf6_datadir}/knsrcfiles/cantor_qalculate.knsrc
%endif
%{_kf6_datadir}/knsrcfiles/cantor_sage.knsrc
%{_kf6_datadir}/knsrcfiles/cantor_scilab.knsrc
%{_kf6_datadir}/knsrcfiles/cantor-documentation.knsrc
%{_datadir}/icons/hicolor/*/*/*
%dir %{_kf6_datadir}/cantor/
%{_kf6_datadir}/cantor/latex/
%{_kf6_datadir}/cantor/maximabackend/
%{_kf6_datadir}/cantor/octave/
%{_kf6_datadir}/cantor/octavebackend/
%{_kf6_datadir}/cantor/xslt/
%{_kf6_datadir}/config.kcfg/*
%{_kf6_datadir}/mime/packages/cantor.xml

%if 0%{?julia}
%files julia
%{_kf6_bindir}/cantor_juliaserver
# %{_kf6_datadir}/cantor/julia/
# %{_kf6_datadir}/cantor/juliabackend/
%{_kf6_qtplugindir}/cantor_plugins/backends/cantor_juliabackend.so
%{_kf6_datadir}/cantor/julia/graphic_packages.xml
%{_kf6_datadir}/cantor/juliabackend/scripts/variables_cleaner.jl
%{_kf6_datadir}/cantor/juliabackend/scripts/variables_loader.jl
%{_kf6_datadir}/cantor/juliabackend/scripts/variables_saver.jl
%endif

%if 0%{?libr}
%files R
%{_kf6_bindir}/cantor_rserver
%{_kf6_qtplugindir}/cantor_plugins/backends/cantor_rbackend.so
%{_kf6_datadir}/config.kcfg/rserver.kcfg
%{_kf6_datadir}/knsrcfiles/cantor_r.knsrc
%endif

%ldconfig_scriptlets libs

%files libs
%{_libdir}/libcantorlibs.so.%{soname}*
%{_libdir}/libcantorlibs.so.%{version}
%{_libdir}/libcantor_config.so
%{_kf6_plugindir}/parts/cantorpart.so
## backend/plugins
%if 0%{?python3}
%{_kf6_datadir}/cantor/python/
%{_kf6_libdir}/cantor_pythonbackend.so
%{_kf6_qtplugindir}/cantor_plugins/backends/cantor_pythonbackend.so
%endif
%dir %{_kf6_qtplugindir}/cantor_plugins/
%{_kf6_qtplugindir}/cantor_plugins/assistants/
%{_kf6_qtplugindir}/cantor_plugins/panels/
%dir %{_kf6_qtplugindir}/cantor_plugins/backends/
%if 0%{?analitza}
%{_kf6_qtplugindir}/cantor_plugins/backends/cantor_kalgebrabackend.so
%endif
%if 0%{?luajit}
%{_kf6_qtplugindir}/cantor_plugins/backends/cantor_luabackend.so
%endif
%{_kf6_qtplugindir}/cantor_plugins/backends/cantor_maximabackend.so
%{_kf6_qtplugindir}/cantor_plugins/backends/cantor_octavebackend.so
%if 0%{?qalculate}
%{_kf6_qtplugindir}/cantor_plugins/backends/cantor_qalculatebackend.so
%endif
%{_kf6_qtplugindir}/cantor_plugins/backends/cantor_sagebackend.so
%{_kf6_qtplugindir}/cantor_plugins/backends/cantor_scilabbackend.so
%files devel
%{_includedir}/cantor/
%{_libdir}/libcantorlibs.so
%{_libdir}/cmake/Cantor/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
