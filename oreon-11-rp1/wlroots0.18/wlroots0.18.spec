%global source2_hash 42ad6b1bb877e1d8e3dffd101431468573e3678d0a89efff08da8383d6efa16f
%global source0_hash 164a7c8bf9f8ae2c1fb00e7bddb6f08cad7e81b3eb35577b48483b1ac265a087
%global abi_ver 0.18
%global compat_ver %{abi_ver}
%global liftoff_ver 0.5.0
Name:           wlroots%{compat_ver}
Version:        %{compat_ver}.3
Release:        1%{?dist}
Summary:        A modular Wayland compositor library
License:        MIT
URL:            https://gitlab.freedesktop.org/wlroots/wlroots
Source0:        https://gitlab.freedesktop.org/wlroots/wlroots/-/releases/%{version}/downloads/wlroots-%{version}.tar.gz
Source1:        %{url}/-/releases/%{version}/downloads/wlroots-%{version}.tar.gz.sig
Source2:        https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/gpgkey-0FDE7BE0E88F5E48.gpg
Patch:          Fix-discarded-const-qualifier.patch
Patch:          %{url}/-/commit/c1452d88.patch#/backend-libinput-fix-build-with-libinput-1.31.patch
Patch:          Revert-layer-shell-error-on-0-dimension-without-anch.patch
Requires:       libliftoff%{?_isa} >= %{liftoff_ver}
# oreon:deps
BuildRequires:  (pkgconfig(libliftoff) >= 0.5.0 with pkgconfig(libliftoff) < 0.6)
BuildRequires:  gcc
BuildRequires:  glslang
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-errors)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-present)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-res)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xinput)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xwayland)
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} == %{version}-%{release}
Recommends:     pkgconfig(xcb-icccm)
Conflicts:      pkgconfig(wlroots)
%description    devel
Development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -N -n wlroots-%{version}
# apply unconditional patches (0..99)
%autopatch -p1 -M99
# apply conditional patches (100..)

%build

MESON_OPTIONS=(
    -Dexamples=false
)
%{meson} "${MESON_OPTIONS[@]}"
%{meson_build}
%install
%{meson_install}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%{meson_test}
%files -f %{oreon_filedir}/main.list
%files -n wlroots0.18-devel -f %{oreon_filedir}/wlroots0.18-devel.list

%changelog

%autochangelog
