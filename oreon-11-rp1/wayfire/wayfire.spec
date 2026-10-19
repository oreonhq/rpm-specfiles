%global source2_hash d497bb95b625e84a81e0cd9dacb875a82ffe9011f05ecd2633eb08b9fd5d2f95
%global source1_hash c4f8d8118fcb5798cc6cad26ee867bf9a8c0ea0219601d878e19bbece83dbe1e
%global source0_hash d497bb95b625e84a81e0cd9dacb875a82ffe9011f05ecd2633eb08b9fd5d2f95
%global forgeurl https://github.com/WayfireWM/wayfire
%global commit1 3ef27d1f76b5f3d1f34305bff12b3174e81727c2
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})
%global commit2 093d8943df03cc8a2667990a065513c1bf2b57e0
%global shortcommit2 %(c=%{commit2}; echo ${c:0:7})
Name:           wayfire
Version:        0.11.0
%forgemeta
Release:        1%{?dist}
Summary:        A modular and extensible wayland compositor
License:        MIT
URL:            https://wayfire.org
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/WayfireWM/wf-utils/archive/%{commit1}/wf-utils-%{shortcommit1}.tar.gz
Source2:        https://github.com/WayfireWM/wf-touch/archive/%{commit2}/wf-touch-%{shortcommit2}.tar.gz
Recommends:     wayfire-config-manager
Recommends:     wf-shell
Provides:       bundled(wf-touch) = 0.0~git%{commit2}
Provides:       bundled(wf-utils) = 0.0~git%{commit1}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(doctest)
BuildRequires:  cmake(glm)
BuildRequires:  gcc-c++
BuildRequires:  inotify-tools-devel
BuildRequires:  libevdev-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wf-config)
BuildRequires:  pkgconfig(wlroots-0.19)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(yyjson)
# /oreon:deps
%description
Wayfire is a 3D Wayland compositor, inspired by Compiz and based on wlroots.

It aims to create a customizable, extendable and lightweight environment without
sacrificing its appearance.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1
%autosetup -D -T -a1
%autosetup -D -T -a2
mv wf-utils-%{commit1}/* subprojects/wf-utils/
mv wf-touch-%{commit2}/* subprojects/wf-touch/

%build

%meson                            \
    -Duse_system_wfconfig=enabled \
    -Duse_system_wlroots=enabled  \
    -Dxwayland=enabled            \
    %{nil}
%meson_build
%install
%meson_install
install -D -p -m 0644 %{name}.desktop %{buildroot}%{_datadir}/wayland-sessions/%{name}.desktop
rm -f %{buildroot}%{_libdir}/libwftouch.a
rm -f %{buildroot}%{_prefix}/man/%{name}.1
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n wayfire-devel -f %{oreon_filedir}/wayfire-devel.list

%changelog

%autochangelog
