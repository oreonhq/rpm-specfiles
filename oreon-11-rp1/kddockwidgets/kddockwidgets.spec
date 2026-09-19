%global source0_hash 51dbf24fe72e43dd7cb9a289d3cab47112010f1a2ed69b6fc8ac0dff31991ed2

%bcond qt5 %[!(0%{?rhel} >= 10)]

%global sover 2.4

Name:           kddockwidgets
Version:        2.4.0
Release:        6%{?dist}
Summary:        Qt dock widget library

License:        GPL-3.0-only AND GPL-2.0-only AND BSD-3-Clause
URL:            https://github.com/KDAB/KDDockWidgets
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
%if %{with qt5}
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  qt5-qtbase-private-devel
%endif
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  cmake(spdlog)
BuildRequires:  cmake(fmt)
BuildRequires:  cmake(nlohmann_json)

# .qch generation
BuildRequires:  doxygen
BuildRequires:  cmake(Qt6ToolsTools)

%{?_qt5:Requires:       %{_qt5}%{?_isa} = %{_qt5_version}}

%description
Qt dock widget library written by KDAB, suitable for replacing QDockWidget
and implementing advanced functionalities missing in Qt.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        qt6
Summary:        Qt dock widget library for Qt 6

%{?_qt6:Requires:       %{_qt6}%{?_isa} = %{_qt6_version}}

%description    qt6
%{description}

%package        qt6-devel
Summary:        Development files for %{name}-qt6

Requires:       %{name}-qt6%{?_isa} = %{version}-%{release}
%description    qt6-devel
The %{name}-qt6-devel package contains libraries and header files for
developing applications that use %{name}-qt6.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n KDDockWidgets-%{version}

%build
%if %{with qt5}
%global _vpath_builddir %{_target_platform}-qt5
%cmake \
    -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DECM_MKSPECS_INSTALL_DIR=%{_qt5_archdatadir}/mkspecs/modules \
    -DKDDockWidgets_QT6=OFF
%cmake_build
%endif

%global _vpath_builddir %{_target_platform}-qt6
# qhelpgenerator needs to be in $PATH to be detected
export PATH=$(%{_qt6_qmake} -query QT_HOST_LIBEXECS):$PATH
%cmake \
    -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DECM_MKSPECS_INSTALL_DIR=%{_qt6_archdatadir}/mkspecs/modules \
    -DKDDockWidgets_QT6=ON \
    -DKDDockWidgets_DOCS=ON
%cmake_build

%install
%if %{with qt5}
%global _vpath_builddir %{_target_platform}-qt5
%cmake_install
rm -r %{buildroot}%{_datadir}/doc
%endif

%global _vpath_builddir %{_target_platform}-qt6
%cmake_install
mkdir -p %{buildroot}%{_qt6_docdir}
mv %{buildroot}%{_docdir}/KDDockWidgets-qt6/*.qch %{buildroot}%{_qt6_docdir}/
mv %{buildroot}%{_docdir}/KDDockWidgets-qt6/*.tags %{buildroot}%{_qt6_docdir}/
rm -r %{buildroot}%{_datadir}/doc/KDDockWidgets-qt6

%if %{with qt5}
%files
%license LICENSES/* LICENSE.txt
%doc CONTRIBUTORS.txt Changelog README.md
%{_libdir}/libkddockwidgets.so.%{sover}*
%{_libdir}/libkddockwidgets.so.3

%files devel
%{_includedir}/kddockwidgets
%{_libdir}/cmake/KDDockWidgets
%{_libdir}/libkddockwidgets.so
%{_qt5_archdatadir}/mkspecs/modules/qt_KDDockWidgets.pri
%endif

%files qt6
%license LICENSES/* LICENSE.txt
%doc CONTRIBUTORS.txt Changelog README.md
%{_libdir}/libkddockwidgets-qt6.so.%{sover}*
%{_libdir}/libkddockwidgets-qt6.so.3
%{_qt6_docdir}/kddockwidgets.tags

%files doc
%{_qt6_docdir}/kddockwidgets-api.qch

%files qt6-devel
%{_includedir}/kddockwidgets-qt6
%{_libdir}/cmake/KDDockWidgets-qt6
%{_libdir}/libkddockwidgets-qt6.so
%{_qt6_archdatadir}/mkspecs/modules/qt_KDDockWidgets.pri

%changelog
%autochangelog
