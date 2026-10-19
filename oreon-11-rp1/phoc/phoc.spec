%global source1_hash da3680bd38314546a915df5ea265f8c963a42ff5ddc7d69dc1b339775f05dbd6
%global source0_hash 0a806146cd494b2bb10ca652025322b521923812d9fc965b94c4b2b115c51232
%global gvdb_commit 4758f6fb7f889e074e13df3f914328f3eecb1fd3
Name:     phoc
Version:  0.57.0
Release:        1%{?dist}
Summary:        Display compositor designed for phones
License:  GPL-3.0-or-later
URL:      https://gitlab.gnome.org/World/Phosh/phoc
Source0:        https://gitlab.gnome.org/World/Phosh/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:  https://gitlab.gnome.org/GNOME/gvdb/-/archive/%{gvdb_commit}/gvdb-%{gvdb_commit}.tar.gz
Requires:       gmobile >= 0.6.0
ExcludeArch:  %{ix86}
ExcludeArch:  s390x
ExcludeArch:  ppc64le
# oreon:deps
BuildRequires:  /usr/bin/rst2man
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  cmake
BuildRequires:  dbus-daemon
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  mutter-common
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmobile)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wlroots-0.19)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  xorg-x11-server-Xwayland
# /oreon:deps
%description
Phoc is a wlroots based Phone compositor as used on the Librem5. Phoc is
pronounced like the English word fog.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -a1 -q -n %{name}-v%{version_no_tilde _}
mv gvdb-%{gvdb_commit} subprojects/gvdb

%conf
%meson -Dembed-wlroots=disabled -Dman=true

%build

%meson_build
%install
%meson_install
%oreon_autofiles main

%check

%{shrink:xvfb-run -s -noreset %meson_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
