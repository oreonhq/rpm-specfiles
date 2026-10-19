%global source0_hash 9859ef16ba16069c3442283d76607712c0b7bc602b6fadf41b2c3d97a754d5f9
%define bcond_feature() %{lua:do
    local name = rpm.expand("%{1}")
    local value = rpm.expand("%{?with_" .. name:gsub('-', '_') .. "}")
    print(value ~= '' and "enabled" or "disabled")
end}
%bcond_without  backend_wayland
%bcond_without  backend_x11
Name:           yambar
Version:        1.11.0
Release:        1%{?dist}
Summary:        Modular status panel for X11 and Wayland
License:        MIT
URL:            https://codeberg.org/dnkl/%{name}
Source0:        https://codeberg.org/dnkl/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz.sig
Source2:        gpgkey-5BBD4992C116573F.asc
%if %{with backend_wayland}
%endif
%if %{with backend_x11}
%endif
# oreon:deps
BuildRequires:  bison
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fcft)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libmpdclient)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(tllist)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-errors)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  tllist-static
# /oreon:deps
%description
yambar is a lightweight and configurable status panel (bar, for short)
for X11 and Wayland, that goes to great lengths to be both CPU and
battery efficient - polling is only done when absolutely necessary.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains header files for developing
applications and plugins for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup
chmod -x examples/scripts/*

%build

%meson \
    -Dwerror=false \
    -Dbackend-wayland=%{bcond_feature backend-wayland} \
    -Dbackend-x11=%{bcond_feature backend-x11} \
    -Dplugin-xkb=%{bcond_feature backend-x11}
%meson_build
%install
%meson_install
rm %{buildroot}%{_docdir}/%{name}/LICENSE
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list
%files -n yambar-devel -f %{oreon_filedir}/yambar-devel.list

%changelog

%autochangelog
