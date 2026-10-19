%global source0_hash bfc23919ac8b960243f85e8228ad7dfc28d557b52182a0b5a2a216a5c6a8057c
Name:          maliit-framework
Version:       2.3.0
Release:        11%{?dist}
Summary:        Input method framework
License:       LicenseRef-Callaway-LGPLv2
URL:           https://maliit.github.io/
Source0:        https://github.com/maliit/framework/archive/%{version}/%{name}-%{version}.tar.gz
Obsoletes: maliit-framework-gtk2 < 2.0.0
Obsoletes: maliit-framework-qt4 < 2.0.0
Obsoletes: maliit-framework-gtk3 < 2.0.0
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libX11-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXext-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtwayland-devel
BuildRequires:  systemd-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
# /oreon:deps
%description
Maliit provides a flexible and cross-platform input method framework. It has a
plugin-based client-server architecture where applications act as clients and
communicate with the Maliit server via input context plugins. The communication
link currently uses D-Bus.

%package qt5
Summary: Input method module for Qt 5 based on Maliit framework
BuildRequires: qt5-qtbase-private-devel
Obsoletes: maliit-plugins < 2.0.0
Requires: %{name}%{?_isa} = %{version}-%{release}
%description qt5
Input method module for Qt 4 based on Maliit framework.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
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
%global oreon_srcdir framework-%{version}
%oreon_prep
%build

%cmake -Denable-examples=ON \
       -Denable-tests=OFF \
       -Denable-dbus-activation=ON \
       -Denable-wayland-gtk=ON
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n maliit-framework-qt5 -f %{oreon_filedir}/maliit-framework-qt5.list
%files -n maliit-framework-devel -f %{oreon_filedir}/maliit-framework-devel.list
%files -n maliit-framework-docs -f %{oreon_filedir}/maliit-framework-docs.list
%files -n maliit-framework-examples -f %{oreon_filedir}/maliit-framework-examples.list

%changelog

%autochangelog
