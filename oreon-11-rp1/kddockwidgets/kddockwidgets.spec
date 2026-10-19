%global source0_hash 51dbf24fe72e43dd7cb9a289d3cab47112010f1a2ed69b6fc8ac0dff31991ed2
%bcond qt5 %[!(0%{?rhel} >= 10)]
%global sover 2.4
Name:           kddockwidgets
Version:        2.4.0
Release:        1%{?dist}
Summary:        Qt dock widget library
License:        GPL-3.0-only AND GPL-2.0-only AND BSD-3-Clause
URL:            https://github.com/KDAB/KDDockWidgets
Source0:        https://github.com/KDAB/KDDockWidgets/archive/v%{version}/%{name}-%{version}.tar.gz
%if %{with qt5}
%endif
%{?_qt5:Requires:       %{_qt5}%{?_isa} = %{_qt5_version}}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6ToolsTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(fmt)
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  cmake(spdlog)
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libxkbcommon-devel
BuildRequires:  ninja-build
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt6-qtbase-private-devel
# /oreon:deps
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
%global oreon_srcdir KDDockWidgets-%{version}
%oreon_prep
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with qt5}
%files -f %{oreon_filedir}/main.list
%files -n kddockwidgets-doc -f %{oreon_filedir}/kddockwidgets-doc.list
%files -n kddockwidgets-devel -f %{oreon_filedir}/kddockwidgets-devel.list
%files -n kddockwidgets-qt6 -f %{oreon_filedir}/kddockwidgets-qt6.list
%files -n kddockwidgets-qt6-devel -f %{oreon_filedir}/kddockwidgets-qt6-devel.list

%changelog

%autochangelog
%endif
