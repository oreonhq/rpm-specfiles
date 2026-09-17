%global source0_hash 7e2869d9769702afff49d3243b43f8cb7cc1dd5a79af85c8704e2d27ca1a777b

%global debug_package %{nil}

Name:           deepin-wayland-protocols
Epoch:          1
Version:        1.10.0.31
Release:        %autorelease
Summary:        Deepin Specific Protocols for Wayland
License:        LGPL-2.1-or-later AND MIT-CMU AND BSD-3-Clause
URL:            https://github.com/linuxdeepin/deepin-wayland-protocols
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules

%description
%{name} contains Deepin-specific Wayland protocols, which adds
functionality not available in the Wayland core protocol.

%package        devel
Summary:        Development files for %{name}

%description    devel
%{name} contains Deepin-specific Wayland protocols, which
adds functionality not available in the Wayland core protocol.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files devel
%license COPYING.LIB
%{_datadir}/deepin-wayland-protocols/
%{_libdir}/cmake/DeepinWaylandProtocols/

%changelog
%autochangelog
