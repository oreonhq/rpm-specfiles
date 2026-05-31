%global source0_hash dc65f1ea97dd0b2155c2281a79e87d27183c0737fb96377744091a3c8460ae1e

Name:           vulkan-tools
Version:        1.4.341.0
Release:        %autorelease
Summary:        Vulkan tools

License:        Apache-2.0
URL:            https://github.com/KhronosGroup/Vulkan-Tools
Source0:        https://github.com/KhronosGroup/Vulkan-Tools/archive/vulkan-sdk-1.4.341.0.tar.gz#/Vulkan-Tools-sdk-1.4.341.0.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  glslang
BuildRequires:  ninja-build
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  vulkan-loader-devel
BuildRequires:  vulkan-volk-devel
BuildRequires:  vulkan-volk-static
BuildRequires:  wayland-protocols-devel
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xcb)

Provides:       vulkan-demos%{?_isa} = %{version}-%{release}
Obsoletes:      vulkan-demos < %{version}-%{release}

%description
Vulkan tools

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n Vulkan-Tools-vulkan-sdk-%{version} -p1


%build
%cmake -GNinja -DCMAKE_BUILD_TYPE=Release -DGLSLANG_INSTALL_DIR=%{_prefix}
%cmake_build


%install
%cmake_install

%files
%license LICENSE.txt
%doc README.md CONTRIBUTING.md
%{_bindir}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.341.0-1
- Prepare for Oreon 11 (RP1)
