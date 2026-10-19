%global source0_hash 1416d1d0c5abb9b96fde52f55e6db92eb552e4275f751ad536a38a4265654e91
Name:           rcssmonitor
Version:        19.0.1
Release:        1%{?dist}
Summary:        RoboCup 2D Soccer Simulator Monitor
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://sourceforge.net/projects/sserver/
Source0:        http://downloads.sourceforge.net/sserver/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Patch0:         rcssmonitor-19.0.0-simdjson-pr2187-no-member-in-template-class.patch
Provides:       rcsslogplayer = %{version}-%{release}
Obsoletes:      rcsslogplayer <= 15.1.1-30
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
The RoboCup Soccer Simulator Monitor is a viewer for moved 2d vector graphics.
You can use it to watch 2D soccer games running on rcssserver. However, The
architecture of The RoboCup Soccer Simulator Monitor was from the beginning
kept as general and modular as possible and not just hacked to fit the  needs
of the robocup soccer server (rcssserver). So by now The RoboCup Soccer
Simulator Monitor is also used to visualize many other two dimensional system.

You can use UDP/IP communication sockets to send commands to The RoboCup Soccer
Simulator Monitor. A generic communication device is also included. It
understands a very easy description language to build and move 2d objects.

%package        devel
Summary:        Header files and libraries for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
This package contains the header files and libraries
for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
sed -i.flagfix "/CMAKE_CXX_FLAGS/d" CMakeLists.txt

%build

%cmake
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}/%{_datadir}/pixmaps/
cp -p icons/rcss.xpm %{buildroot}/%{_datadir}/pixmaps/
desktop-file-install \
  --dir=%{buildroot}/%{_datadir}/applications %{SOURCE1}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n rcssmonitor-devel -f %{oreon_filedir}/rcssmonitor-devel.list

%changelog

%autochangelog
