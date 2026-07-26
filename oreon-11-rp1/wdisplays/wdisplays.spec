%global source0_hash 6b8674598d50cb56a3acb79bd563c1d7a7d7781a8ce8dcc83a240916024b7070

# -*-Mode: rpm-spec -*-
%global app_id network.cycles.wdisplays

Name:     wdisplays
Version:  1.1.3
Release:  2%{?dist}
Summary:  GUI display configurator for wlroots compositors
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:  GPL-3.0-or-later
URL:      https://github.com/artizirk/wdisplays

Source:  %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: meson
BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.24
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols) >= 1.17

Conflicts: wlroots < 0.7.0
Requires:  hicolor-icon-theme

%description

wdisplays is a graphical application for configuring displays in
Wayland compositors. It borrows some code from kanshi. It should work
in any compositor that implements the
wlr-output-management-unstable-v1 protocol, including sway. The goal
of this project is to allow precise adjustment of display settings in
kiosks, digital signage, and other elaborate multi-monitor setups.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
find %{buildroot}

desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{app_id}.svg

%doc README.md

%license LICENSES/*

%clean

%changelog
%autochangelog
