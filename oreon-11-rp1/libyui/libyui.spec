%global source0_hash 368da511227fe6538d8392b864a99116729d1cc89df95fa1015ac08f0bfb6661

%define __cmake_builddir build

%global major_so_ver 15

%define libname    libyui
%define develname  libyui-devel

# Define libsuffix.
%global libsuffix yui

#--------------------------------------------------------
# Package libyui-ncurses
%define yui_ncurses_name libyui-ncurses

%define libncurses  libyui-ncurses
%define devncurses  libyui-ncurses-devel
#--------------------------------------------------------
# Package libyui-qt
%define yui_qt_name libyui-qt

%define libqt  libyui-qt
%define devqt  libyui-qt-devel

#--------------------------------------------------------
# Package libyui-qt-graph
%define yui_qt_graph_name libyui-qt-graph

%define libqtgraph  libyui-qt-graph
%define devqtgraph  libyui-qt-graph-devel

Name:     %{libname}
Version:  4.2.16
Release:  28%{?dist}
Summary:  GUI-abstraction library

License:  (LGPLv2 or LGPLv3) and MIT
URL:      https://github.com/%{name}/%{name}
Source0:  %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  libtool
BuildRequires:  perl-devel
BuildRequires:  rubygems
BuildRequires:  swig
BuildRequires:  fontconfig-devel
BuildRequires:  perl-generators

BuildRequires:  pkgconfig(ruby)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(libpng)

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)

BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(libyui-mga)

%description
This is the user interface engine that provides the abstraction
from graphical user interfaces (Qt, Gtk) and text based user
interfaces (ncurses).

Originally developed for YaST, %{name} can now be used
independently of YaST for generic (C++) applications.

%{name} has very few dependencies.

#----------------------------------------------------------
# libyui

%files
%dir %{_datadir}/%{name}
%license COPYING*
%{_libdir}/%{name}.so.%{major_so_ver}*

#----------------------------------------------------------
# libyui-devel

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

%files -n %develname
%{_libdir}/libyui.so
%{_libdir}/pkgconfig/libyui.pc
%{_includedir}/yui/*.h
%{_datadir}/libyui/buildtools

#-----------------------------------------------------------------------
# libyui-qt

%package -n %libqt
Summary:        Libyui - Qt (graphical) user interface
Group:          System/Libraries
Requires:       qt5-qtx11extras
Provides:       %{yui_qt_name} = %{version}-%{release}

%description -n %libqt
This package contains the Qt (graphical) user interface component for libyui.

%files -n %libqt
%doc COPYING*
%{_libdir}/yui/libyui-qt.so.%{major_so_ver}*

#-----------------------------------------------------------------------
# libyui-qt-devel

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

%files -n %devqt
%{_includedir}/yui/qt
%{_libdir}/yui/libyui-qt*.so
%{_libdir}/pkgconfig/libyui-qt.pc

#-----------------------------------------------------------------------
# libyui-qt-graph

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

%files -n %libqtgraph
%doc COPYING*
%dir %{_libdir}/yui
%{_libdir}/yui/%libqtgraph.so.*

#-----------------------------------------------------------------------
# libyui-qt-graph-devel

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

%files -n %devqtgraph
%{_includedir}/yui/qt-graph/*

#-----------------------------------------------------------------------
# libyui-ncurses

%package -n %libncurses
Summary:        Libyui - NCurses (text based) user interface
Group:          System/Libraries
Provides:       %{yui_ncurses_name} = %{version}-%{release}

%description -n %libncurses
This package contains the NCurses (text based) user interface component for
libyui.

%files -n %libncurses
%doc COPYING*
%{_libdir}/yui/libyui-ncurses.so.%{major_so_ver}*

#-----------------------------------------------------------------------
# libyui-ncurses-devel

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

%files -n %devncurses
%{_libdir}/yui/libyui-ncurses*.so
%{_includedir}/yui/ncurses
%{_libdir}/pkgconfig/libyui-ncurses.pc

#----------------------------------------------------------
# libyui-ncurses-tools

%package -n %{yui_ncurses_name}-tools

Summary:        Libyui - tools for the NCurses (text based) user interface
Group:          System/Libraries
Requires:       screen

%description -n %{yui_ncurses_name}-tools
This package contains tools for the NCurses (text based) user interface
component for libyui:

libyui-terminal - useful for testing on headless machines

%files -n %{yui_ncurses_name}-tools
%{_bindir}/libyui-terminal

#----------------------------------------------------------
# ruby-yui

%package -n ruby-yui
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Summary:        Ruby bindings for libyui
Group:          Development/Ruby

%description -n ruby-yui
This package provides Ruby language bindings to access functions of libyui, the
YaST User Interface engine that provides the abstraction from graphical user
interfaces (Qt, Gtk) and text based user interfaces (ncurses).

%files -n ruby-yui
%doc libyui-bindings/swig/ruby/examples/*.rb
%{ruby_vendorarchdir}/_yui.so

#----------------------------------------------------------
# python3-yui

%package -n python3-yui
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Summary:        Python 3 bindings for libyui
Group:          Development/Python

%description -n python3-yui
This package provides Python 3 language bindings to access functions of libyui,
the YaST User Interface engine that provides the abstraction from graphical
user interfaces (Qt, Gtk) and text based user interfaces (ncurses).

%files -n python3-yui
%doc libyui-bindings/swig/python/examples/*.py
%{python3_sitearch}/_yui.so
%{python3_sitearch}/yui.*
%{python3_sitearch}/__pycache__/*

#----------------------------------------------------------
# perl-yui

%package -n perl-yui
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Summary:        Perl bindings for libyui
Group:          Development/Perl

%description -n perl-yui
This package provides Perl language bindings to access functions of libyui, the
YaST User Interface engine that provides the abstraction from graphical user
interfaces (Qt, Gtk) and text based user interfaces (ncurses).

%files -n perl-yui
%doc libyui-bindings/swig/perl/examples/*.pl
%{perl_vendorarch}/yui.so
%{perl_vendorlib}/yui.pm

#----------------------------------------------------------

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

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

%changelog
%autochangelog
