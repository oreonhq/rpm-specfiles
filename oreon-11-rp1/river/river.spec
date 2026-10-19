%global source7_hash cc1f8835ad6e50d5cd4da82a5d1741203f3d7b47c744418167ba602e75b8b5c7
%global source6_hash 480fc90ddaf215ec0b66ffc7c2cae7d16a92c6579cc9a55da0ae03b469c28e5d
%global source5_hash 14173a7ee05a62f8531ebce8ddb33409ff5d08970cc6eadcbfbefd7360132a4c
%global source4_hash 4b0b57ce37f7bb3a2c2fc76eec93d060830d2c92155bf2a6baa43d61ad05499e
%global source2_hash b09f93a85ccb01e2eef8cf044e41308957e9acb7ccb419588a3df9fd975de9e8
%global source0_hash 6d4030526e307e40de357167b4d6daacb583aed353dd93e32e1314c2d34400fa
%global zig_pixman_ver 0.3.0
%global zig_wayland_ver 0.5.0
%global zig_wlroots_ver 0.19.4
%global zig_xkbcommon_ver 0.4.0
Name:           river
Version:        0.4.8
Release:        1%{?dist}
Summary:        Non-monolithic Wayland compositor
License:        GPL-3.0-only AND 0BSD AND CC-BY-SA-4.0 AND HPND-sell-variant AND MIT
URL:            https://codeberg.org/river/river
Source0:        https://codeberg.org/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
Source2:        https://isaacfreund.com/public_key.txt#/gpgkey-86DED400DDFD7A11.gpg
Source3:        %{name}.desktop
Source4:        https://codeberg.org/ifreund/zig-pixman/archive/v%{zig_pixman_ver}.tar.gz#/zig-pixman-%{zig_pixman_ver}.tar.gz
Source5:        https://codeberg.org/ifreund/zig-wayland/archive/v%{zig_wayland_ver}.tar.gz#/zig-wayland-%{zig_wayland_ver}.tar.gz
Source6:        https://codeberg.org/ifreund/zig-wlroots/archive/v%{zig_wlroots_ver}.tar.gz#/zig-wlroots-%{zig_wlroots_ver}.tar.gz
Source7:        https://codeberg.org/ifreund/zig-xkbcommon/archive/v%{zig_xkbcommon_ver}.tar.gz#/zig-xkbcommon-%{zig_xkbcommon_ver}.tar.gz
ExclusiveArch:  %{zig_arches}
Provides:       bundled(zig-pixman) = %{zig_pixman_ver}
Provides:       bundled(zig-wayland) = %{zig_wayland_ver}
Provides:       bundled(zig-wlroots) = %{zig_wlroots_ver}
Provides:       bundled(zig-xkbcommon) = %{zig_xkbcommon_ver}
Recommends:     mesa-dri-drivers
Recommends:     polkit
Recommends:     xorg-x11-server-Xwayland
# oreon:deps
BuildRequires:  (zig >= 0.15.2 with zig < 0.16)
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wlroots-0.19)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  scdoc
BuildRequires:  zig-rpm-macros
# /oreon:deps
%description
River is a non-monolithic Wayland compositor.
Unlike other Wayland compositors, river does not combine the compositor
and window manager into one program. Instead, river defers all window
management policy to a separate window manager implementing the
river-window-management-v1 protocol. This includes window position/size,
pointer/keyboard bindings, focus management, window decorations,
desktop shell graphics, and more.

River itself provides frame perfect rendering, good performance,
support for many Wayland protocol extensions, robust Xwayland support,
the ability to hot-swap window managers, and more.

%package        protocols-devel
Summary:        Protocol files for river, a non-monolithic Wayland compositor
License:        MIT
%description    protocols-devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q -a 4 -a 5 -a 6 -a 7

%zig_fetch zig-pixman
%zig_fetch zig-wayland
%zig_fetch zig-wlroots
%zig_fetch zig-xkbcommon

%build

%zig_build \
    -Dpie  \
    -Dxwayland
%install
%zig_install \
    -Dpie    \
    -Dxwayland
install -D -m644 -pv %{SOURCE3} %{buildroot}%{_datadir}/wayland-sessions/%{name}.desktop
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%zig_test
%files -f %{oreon_filedir}/main.list
%files -n river-protocols-devel -f %{oreon_filedir}/river-protocols-devel.list

%changelog

%autochangelog
