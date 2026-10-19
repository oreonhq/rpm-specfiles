%global source0_hash 72dfbedf5ac7e341639cd9628173baffea84559f40a6453f504eb0f91cdf39ff
Name:     stevia
Version:  0.57.0
Release:        1%{?dist}
Summary:        On screen keyboard (OSK) Phosh
License:  GPL-3.0-or-later
URL:      https://gitlab.gnome.org/World/Phosh/stevia
Source0:        https://gitlab.gnome.org/World/Phosh/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
ExcludeArch:  %{ix86}
ExcludeArch:  s390x
# oreon:deps
BuildRequires:  /usr/bin/fzf
BuildRequires:  /usr/bin/rst2man
BuildRequires:  /usr/bin/xwfb-run
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  mutter
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-wayland-3.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmobile)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk+-wayland-3.0)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libfeedback-0.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  systemd-rpm-macros
BuildRequires:  words
# /oreon:deps
%description
Stevia is an on screen keyboard (OSK) for Phosh.

The purpose of Stevia is:
* to make typing pleasant and fast on touch screens
* be helpful when debugging input-method related issues
* be quick and easy to (cross)compile
* to be easy to extend (hence the API documentation)

%package phosh-osk-provider
Summary:   Use Stevia as Phosh's default OSK
BuildArch: noarch
Requires:  %{name}
Provides:  phosh-osk = 1.0
Conflicts: phosh-osk
Conflicts: squeekboard-phosh-osk-provider
%description phosh-osk-provider
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-v%{version_no_tilde _}

%conf
%meson -Dman=true

%build

%meson_build
%install
%meson_install
%find_lang phosh-osk-%{name} --with-man
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/sm.puri.OSK0.desktop
LC_ALL=C.UTF-8 xwfb-run -c mutter -- sh <<'SH'
%meson_test
SH
%files -f %{oreon_filedir}/main.list
%files -n stevia-phosh-osk-provider -f %{oreon_filedir}/stevia-phosh-osk-provider.list

%changelog

%autochangelog
