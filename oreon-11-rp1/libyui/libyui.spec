%global source0_hash 162933b33d05d0a5d7b97720fda85c625d6d5385d626813005db44e31c43ccb7
%define __cmake_builddir build
%global major_so_ver 15
%define libname    libyui
%define develname  libyui-devel
%global libsuffix yui
%define yui_ncurses_name libyui-ncurses
%define libncurses  libyui-ncurses
%define devncurses  libyui-ncurses-devel
%define yui_qt_name libyui-qt
%define libqt  libyui-qt
%define devqt  libyui-qt-devel
%define yui_qt_graph_name libyui-qt-graph
%define libqtgraph  libyui-qt-graph
%define devqtgraph  libyui-qt-graph-devel
Name:     %{libname}
Version:  4.6.2
Release:        1%{?dist}
Summary:        GUI-abstraction library
License:  (LGPLv2 or LGPLv3) and MIT
URL:      https://github.com/%{name}/%{name}
Source0:        https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  fontconfig-devel
BuildRequires:  gcc-c++
BuildRequires:  graphviz-devel
BuildRequires:  libtool
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libyui-mga)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(ruby)
BuildRequires:  rubygems
BuildRequires:  swig
# /oreon:deps
%description
This is the user interface engine that provides the abstraction
from graphical user interfaces (Qt, Gtk) and text based user
interfaces (ncurses).

Originally developed for YaST, %{name} can now be used
independently of YaST for generic (C++) applications.

%{name} has very few dependencies.

#----------------------------------------------------------
# libyui

%package -n %develname
Summary:      libYUI, YaST2 User Interface Engine - header files
Group:        Development/C++
Requires:     %{libname} >= %{version}
Requires:     boost-devel
Provides:     %{name}-devel = %{version}-%{release}
Provides:     yui-devel = %{version}-%{release}
%description -n %develname
This is the development package for libyui user interface engine that provides
the abstraction from graphical user interfaces (Qt, Gtk) and text based user
interfaces (ncurses).

%package -n %libqt
Summary:        Libyui - Qt (graphical) user interface
Group:          System/Libraries
Requires:       qt5-qtx11extras
Provides:       %{yui_qt_name} = %{version}-%{release}
%description -n %libqt
This package contains the Qt (graphical) user interface component for libyui.

%package -n %devqt
Summary:        Libyui - Qt (graphical) user interface header files
Group:          Development/KDE and Qt
Requires:       libyui-devel
Requires:       %{yui_qt_name} = %{version}-%{release}
Provides:       yui-qt-devel = %{version}-%{release}
%description -n %devqt
This package contains the header files for the Qt based user interface
component for libyui.

This package is not needed to develop libyui-based applications, only to
develop extensions for libyui-qt.

%package -n     %libqtgraph
Summary:        Libyui - Qt graph component for libyui.
Group:          System/Libraries
BuildRequires:  graphviz-devel
Requires:       qt5-qtx11extras
Provides:       %{yui_qt_graph_name} = %{version}-%{release}
%description -n %libqtgraph
This package contains the Qt graph component for libyui.

This is a special widget to visualize graphs such as the
storage device hierarchy (disks, partitions, subvolumes
etc.).  and similar graphviz-generated graphs.

%package -n     %devqtgraph
Summary:        Libyui - Qt (graphical) user interface header files
Group:          Development/KDE and Qt
Requires:       libyui-devel
Requires:       %{yui_qt_graph_name} = %{version}-%{release}
Provides:       yui-qt-devel = %{version}-%{release}
%description -n %devqtgraph
This package contains the header files for the Qt based user interface
component for libyui.

This package is not needed to develop libyui-based applications, only to
develop extensions for libyui-qt.

%package -n %libncurses
Summary:        Libyui - NCurses (text based) user interface
Group:          System/Libraries
Provides:       %{yui_ncurses_name} = %{version}-%{release}
%description -n %libncurses
This package contains the NCurses (text based) user interface component for
libyui.

%package -n %devncurses
Summary:        Libyui - Header fles for the NCurses (text based) user interface
Group:          Development/Other
Requires:       libyui-devel
Requires:       %{yui_ncurses_name} = %{version}-%{release}
Provides:       yui-ncurses-devel = %{version}-%{release}
%description -n %devncurses
This package contains the header files for the NCurses (text based) user
interface component for libyui.

This package is not needed to develop libyui-based applications, only to
develop extensions for libyui-ncurses.

%package -n %{yui_ncurses_name}-tools
Summary:        Libyui - tools for the NCurses (text based) user interface
Group:          System/Libraries
Requires:       screen
%description -n %{yui_ncurses_name}-tools
This package contains tools for the NCurses (text based) user interface
component for libyui:

libyui-terminal - useful for testing on headless machines

%package -n ruby-yui
License:        GPL-2.0-or-later
Summary:        Ruby bindings for libyui
Group:          Development/Ruby
%description -n ruby-yui
This package provides Ruby language bindings to access functions of libyui, the
YaST User Interface engine that provides the abstraction from graphical user
interfaces (Qt, Gtk) and text based user interfaces (ncurses).

%package -n python3-yui
License:        GPL-2.0-or-later
Summary:        Python 3 bindings for libyui
Group:          Development/Python
%description -n python3-yui
This package provides Python 3 language bindings to access functions of libyui,
the YaST User Interface engine that provides the abstraction from graphical
user interfaces (Qt, Gtk) and text based user interfaces (ncurses).

%package -n perl-yui
License:        GPL-2.0-or-later
Summary:        Perl bindings for libyui
Group:          Development/Perl
%description -n perl-yui
This package provides Perl language bindings to access functions of libyui, the
YaST User Interface engine that provides the abstraction from graphical user
interfaces (Qt, Gtk) and text based user interfaces (ncurses).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

  for pkgname in libyui libyui-qt libyui-qt-graph libyui-ncurses libyui-bindings ;do
    pushd $pkgname
    %cmake \
        -DWERROR=FALSE \
        -DBUILD_EXAMPLES=OFF \
        -DWITH_MGA=ON \
        -DWITH_MONO=OFF \
        -DPYTHON_EXECUTABLE=%{python3} \
        -DPYTHON_INCLUDE_DIR=%{_includedir}/python%{python3_version} \
        -DPYTHON_SITEDIR=%{python3_sitearch} \
        -DPYTHON_LIB_DIR=%{python3_sitelib}
    %cmake_build
    popd
  done
%install
for pkgname in libyui libyui-qt libyui-qt-graph libyui-ncurses libyui-bindings ;do
  pushd $pkgname
  %cmake_install
  popd
done
install -m0755 -d %{buildroot}%{_libdir}/yui
%oreon_autofiles ruby-yui usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-yui usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles perl-yui usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libyui-devel -f %{oreon_filedir}/libyui-devel.list
%files -n libyui-qt -f %{oreon_filedir}/libyui-qt.list
%files -n libyui-qt-devel -f %{oreon_filedir}/libyui-qt-devel.list
%files -n libyui-qt-graph -f %{oreon_filedir}/libyui-qt-graph.list
%files -n libyui-qt-graph-devel -f %{oreon_filedir}/libyui-qt-graph-devel.list
%files -n libyui-ncurses -f %{oreon_filedir}/libyui-ncurses.list
%files -n libyui-ncurses-devel -f %{oreon_filedir}/libyui-ncurses-devel.list
%files -n libyui-ncurses-tools -f %{oreon_filedir}/libyui-ncurses-tools.list
%files -n ruby-yui -f %{oreon_filedir}/ruby-yui.list
%files -n python3-yui -f %{oreon_filedir}/python3-yui.list
%files -n perl-yui -f %{oreon_filedir}/perl-yui.list

%changelog

%autochangelog
