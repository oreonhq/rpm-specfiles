%global source0_hash 9afc16e70e8bd8c8d5b13020387716f5e063e115b6599f0421a3846dc6ec312a
%global lib_ver 2.0.0
%bcond_without qt6
Name:           qcustomplot
Version:        2.1.1
Release:        1%{?dist}
Summary:        Qt widget for plotting and data visualization
License:        GPL-3.0-or-later
URL:            http://www.qcustomplot.com/
Source0:        http://www.%{name}.com/release/%{version}/QCustomPlot.tar.gz
Source1:        CMakeLists.txt
%if %{with qt6}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt6-qtbase-devel
# /oreon:deps
%description
QCustomPlot is a Qt C++ widget for plotting and data visualization.
This plotting library focuses on making good looking, publication quality 2D
plots, graphs and charts, as well as offering high performance for realtime
visualization applications.

This package contains the Qt4 version.

%package        qt5
Summary:        Qt widget for plotting and data visualization
%description    qt5
QCustomPlot is a Qt C++ widget for plotting and data visualization.
This plotting library focuses on making good looking, publication quality 2D
plots, graphs and charts, as well as offering high performance for realtime
visualization applications.

This package contains the Qt5 version.

%package        qt5-devel
Summary:        Development files for %{name} (Qt5)
Requires:       %{name}-qt5%{?_isa} = %{version}-%{release}
%description    qt5-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name} (Qt5).

%if %{with qt6}
%package        qt6
Summary:        Qt widget for plotting and data visualization
%description    qt6
QCustomPlot is a Qt C++ widget for plotting and data visualization.
This plotting library focuses on making good looking, publication quality 2D
plots, graphs and charts, as well as offering high performance for realtime
visualization applications.

This package contains the Qt6 version.

%package        qt6-devel
Summary:        Development files for %{name} (Qt6)
Requires:       %{name}-qt6%{?_isa} = %{version}-%{release}
%description    qt6-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name} (Qt6).
%endif

%package        doc
Summary:        Documentation and examples for %{name}
BuildArch:      noarch
%description    doc
The %{name}-doc package contains the documentation and examples for
%{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}
cp -a %{SOURCE1} .

%build

%define _vpath_builddir %{_target_platform}-qt5
%cmake -DQT_VER=5 -DLIB_VER=%{lib_ver}
%cmake_build
%if %{with qt6}
%define _vpath_builddir %{_target_platform}-qt6
%cmake -DQT_VER=6 -DLIB_VER=%{lib_ver}
%cmake_build
%endif
%install
%define _vpath_builddir %{_target_platform}-qt5
%cmake_install
install -d %{buildroot}%{_libdir}/pkgconfig/
cat > %{buildroot}%{_libdir}/pkgconfig/%{name}-qt5.pc <<EOF
libdir=%{_libdir}
includedir=%{_includedir}
Name: %{name}
Description: %{summary}
Version: %{version}
Cflags: -I\${includedir}
Libs: -L\${libdir} -lqcustomplot-qt5
EOF
%if %{with qt6}
%define _vpath_builddir %{_target_platform}-qt6
%cmake_install
cat > %{buildroot}%{_libdir}/pkgconfig/%{name}-qt6.pc <<EOF
libdir=%{_libdir}
includedir=%{_includedir}
Name: %{name}
Description: %{summary}
Version: %{version}
Cflags: -I\${includedir}
Libs: -L\${libdir} -lqcustomplot-qt6
EOF
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n qcustomplot-qt5 -f %{oreon_filedir}/qcustomplot-qt5.list
%files -n qcustomplot-qt5-devel -f %{oreon_filedir}/qcustomplot-qt5-devel.list
%files -n qcustomplot-qt6 -f %{oreon_filedir}/qcustomplot-qt6.list
%files -n qcustomplot-qt6-devel -f %{oreon_filedir}/qcustomplot-qt6-devel.list
%files -n qcustomplot-doc -f %{oreon_filedir}/qcustomplot-doc.list

%changelog

%autochangelog
