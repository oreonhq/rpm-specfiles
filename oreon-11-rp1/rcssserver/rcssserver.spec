%global source0_hash 08abeef0bf94816a9886647fd578da0dc58d40b08bb6a27ed85cddc2acce2aea
Name:           rcssserver
Version:        19.0.0
Release:        6%{?dist}
Summary:        Robocup 2D Soccer Simulation Server
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://sourceforge.net/projects/sserver/
Source0:        http://downloads.sourceforge.net/sserver/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
# oreon:deps
BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  zlib-devel
# /oreon:deps
%description
The RoboCup Soccer Simulator Server (rcssserver) is a research and educational
tool for mutli-agent systems and artificial intelligence. It allows 11
simulated autonomous robotic players to play soccer (football).

This package includes the simulation server. If you want to view the games 
you should install and run a monitor (rcssmonitor or rcssmonitor_classic).

%package        devel
Summary:        Header files and libraries for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       boost-devel
%description    devel
This package contains the header files and libraries
for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package        gui
Summary:        A simple way to run 2D Soccer Simulation on a single machine
Requires:       %{name} = %{version}-%{release}
Requires:       rcssmonitor
%description    gui
This package contains rcsoccersim script as simple way for
running 2D Soccer Simulation on a single machine. It'll also
provide a menu entry for this script.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git
sed -i.flagfix "/CMAKE_CXX_FLAGS/d" CMakeLists.txt

%build

%cmake
%cmake_build
%install
%cmake_install
desktop-file-install \
  --dir=%{buildroot}/%{_datadir}/applications %{SOURCE1}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rcssserver-devel -f %{oreon_filedir}/rcssserver-devel.list
%files -n rcssserver-gui -f %{oreon_filedir}/rcssserver-gui.list

%changelog

%autochangelog
