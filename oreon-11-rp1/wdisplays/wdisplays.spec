%global source0_hash 6b8674598d50cb56a3acb79bd563c1d7a7d7781a8ce8dcc83a240916024b7070
%global app_id network.cycles.wdisplays
Name:     wdisplays
Version:  1.1.3
Release:        1%{?dist}
Summary:        GUI display configurator for wlroots compositors
License:  GPL-3.0-or-later
URL:      https://github.com/artizirk/wdisplays
Source0:        https://github.com/artizirk/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Conflicts: wlroots < 0.7.0
Requires:  hicolor-icon-theme
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
# /oreon:deps
%description

wdisplays is a graphical application for configuring displays in
Wayland compositors. It borrows some code from kanshi. It should work
in any compositor that implements the
wlr-output-management-unstable-v1 protocol, including sway. The goal
of this project is to allow precise adjustment of display settings in
kiosks, digital signage, and other elaborate multi-monitor setups.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
find %{buildroot}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
