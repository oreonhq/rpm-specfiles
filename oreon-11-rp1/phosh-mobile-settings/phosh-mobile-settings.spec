%global source1_hash 25b9d153e9fb992a46d069e2bc2c4db6bc9fd33ef66169d8940be5c85ab4f009
%global source0_hash 10ad99eb5c80a2ed2d802fb23debc493e848a895f84e382a0d81d01a2a55aadc
%global gvc_commit 1cdc1cb2d622d64e9ad2781093bcc63719c5ea5b
Name:		phosh-mobile-settings
Version:	0.57.0
Release:        1%{?dist}
Summary:        Mobile Settings App for phosh and related components
License:	GPL-3.0-or-later AND LGPL-3.0-or-later
URL:		https://gitlab.gnome.org/World/Phosh/phosh-mobile-settings
Source0:        https://gitlab.gnome.org/World/Phosh/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:	https://gitlab.gnome.org/guidog/libgnome-volume-control/-/archive/%{gvc_commit}/libgnome-volume-control-%{gvc_commit}.tar.gz
ExcludeArch:	%{ix86}
ExcludeArch:	s390x
ExcludeArch:	ppc64le
Requires:	feedbackd >= 0.8.0
Requires:	phoc >= 0.34.0
Requires:	phosh >= 0.44.0
# oreon:deps
BuildRequires:  appstream-devel
BuildRequires:  dbus-daemon
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  lm_sensors-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmobile)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk4-wayland)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libcellbroadcast-0.0)
BuildRequires:  pkgconfig(libfeedback-0.0)
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(phosh-plugins)
BuildRequires:  pkgconfig(phosh-settings)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(yaml-0.1)
# /oreon:deps
%description
Mobile Settings App for phosh and related components

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -a1 -p1 -n %{name}-v%{version_no_tilde _}
mv libgnome-volume-control-%{gvc_commit} subprojects/gvc
mkdir -p /tmp/runtime-dir
chmod 0700 /tmp/runtime-dir

%conf
%meson -Dtweaks-data-dir=%{_datadir}/phosh-tweaks

%build

%meson_build
%install
%meson_install
install -d %{buildroot}%{_datadir}/phosh-tweaks
%find_lang %{name}
%oreon_autofiles main

%check

export XDG_RUNTIME_DIR=/tmp/runtime-dir
dbus-run-session sh <<'SH'
%meson_test
SH
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
