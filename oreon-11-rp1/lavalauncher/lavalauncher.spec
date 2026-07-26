%global source0_hash 951edb0e00a118cd57d54349349d4898cfc18c6208a7c4d7f6e892eec1497c3b

# -*-Mode: rpm-spec -*-

Name:     lavalauncher
Version:  2.1.1
Release:  13%{?dist}
Summary:  %{name} is a simple launcher for Wayland
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:  GPL-3.0-only
URL:      https://git.sr.ht/~leon_plickat/%{name}
Source0:  %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: cmake
BuildRequires: cairo-devel
BuildRequires: meson
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: scdoc
BuildRequires: wayland-devel
BuildRequires: wayland-protocols-devel

%description
LavaLauncher is a simple launcher for Wayland.

It displays a dynamically sized bar with user defined buttons. Buttons
consist of an image, which is displayed as the button icon on the bar,
and at least one shell command, which is executed when the user
activates the button.

Buttons can be activated with pointer and touch events.

A single LavaLauncher instance can provide multiple such bars, across
multiple outputs.

The Wayland compositor must implement the Layer-Shell and XDG-Output
for LavaLauncher to work.

Beware: Unlike applications launchers which are similar in visual
design to LavaLauncher, which are often called "docks", LavaLauncher
does not care about .desktop files or icon themes nor does it keep
track running applications. Instead, LavaLaunchers approach of
manually defined buttons is considerably more flexible: You could have
buttons not just for launching applications, but for practically
anything you could do in your shell, like for ejecting your optical
drive, rotating your screen, sending your cat an email, playing a
funny sound, muting all audio, toggling your lamps and a lot more. Be
creative!

LavaLauncher is opinionated, yet remains configurable. The
configuration syntax is documented in the man page.

LavaLauncher has been successfully tested on sway, wayfire (Wayfire
currently does not respect subsurfaces ordering used by LavaLauncher),
river and hikari.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -n %{name}-v%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/%{name}

%doc README.md
%{_mandir}/man1/%{name}.1.*

%license LICENSE

%changelog
%autochangelog
