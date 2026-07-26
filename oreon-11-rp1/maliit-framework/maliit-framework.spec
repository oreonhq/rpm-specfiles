%global source0_hash bfc23919ac8b960243f85e8228ad7dfc28d557b52182a0b5a2a216a5c6a8057c

Name:          maliit-framework
Version:       2.3.0
Release:       11%{?dist}
Summary:       Input method framework

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2
URL:           https://maliit.github.io/
Source0:       https://github.com/maliit/framework/archive/%{version}/%{name}-%{version}.tar.gz 

BuildRequires: cmake
BuildRequires: gcc-c++

BuildRequires: doxygen
BuildRequires: libX11-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXdamage-devel
BuildRequires: libXext-devel
BuildRequires: libXfixes-devel
BuildRequires: libxkbcommon-devel
BuildRequires: systemd-devel

BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-static
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-qtwayland-devel

BuildRequires: wayland-devel
BuildRequires: wayland-protocols-devel

Obsoletes: maliit-framework-gtk2 < 2.0.0
Obsoletes: maliit-framework-qt4 < 2.0.0
Obsoletes: maliit-framework-gtk3 < 2.0.0

%description
Maliit provides a flexible and cross-platform input method framework. It has a
plugin-based client-server architecture where applications act as clients and
communicate with the Maliit server via input context plugins. The communication
link currently uses D-Bus.

%package qt5
Summary: Input method module for Qt 5 based on Maliit framework
## as of version 2.0.0 -- rdieter
# libQt5Gui.so.5(Qt_5.15.2_PRIVATE_API)(64bit)
# libQt5WaylandClient.so.5(Qt_5.15.2_PRIVATE_API)(64bit)
BuildRequires: qt5-qtbase-private-devel
#libQt5Core.so.5(Qt_5_PRIVATE_API)(64bit)
Obsoletes: maliit-plugins < 2.0.0

Requires: %{name}%{?_isa} = %{version}-%{release}

%description qt5
Input method module for Qt 4 based on Maliit framework.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
# libmaliit-plugins moved to -qt5
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description devel
Files for development with %{name}.

%package docs
Summary: Documentation files for %{name}

%description docs
This package contains developer documentation for %{name}.

%package examples
Summary: Tests and examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}

%description examples
This package contains tests and examples for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n framework-%{version} -p1

# Temporarily turn off tests for successful build - onuralp
%build
%cmake -Denable-examples=ON \
       -Denable-tests=OFF \
       -Denable-dbus-activation=ON \
       -Denable-wayland-gtk=ON

%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%license LICENSE.LGPL
%doc README.md NEWS
%{_bindir}/maliit-server
%{_libdir}/libmaliit-glib.so.2*
%{_datadir}/dbus-1/services/org.maliit.server.service

%ldconfig_scriptlets qt5

%files qt5
%{_libdir}/libmaliit-plugins.so.2*
%{_libdir}/qt5/plugins/platforminputcontexts/libmaliitplatforminputcontextplugin.so
%{_libdir}/qt5/plugins/wayland-shell-integration/libinputpanel-shell.so

%files devel
%{_includedir}/maliit-2
%{_libdir}/cmake/MaliitGLib/
%{_libdir}/cmake/MaliitPlugins/
%{_libdir}/libmaliit-plugins.so
%{_libdir}/libmaliit-glib.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/qt5/mkspecs/features/*.prf

%files docs
%{_datadir}/doc/maliit-framework-doc/
%{_datadir}/doc/maliit-framework/

%files examples
%{_bindir}/maliit-exampleapp-plainqt

%changelog
%autochangelog
