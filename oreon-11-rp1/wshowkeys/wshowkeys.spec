%global source0_hash 9478950ec0ae4aceab3ad73229d97c1259ca81dcb2ff9dc0cc0a4ce5596efa14

# -*-Mode: rpm-spec -*-

%global commit e8bfc78f08ebdd1316daae59ecc77e62bba68b2b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global _hardened_build 1

Name:     wshowkeys
Version:  0
Release:  16.20200727git%{shortcommit}%{?dist}
Summary:  Displays key presses on screen on supported Wayland compositors
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:  GPL-3.0-only
#URL:      https://git.sr.ht/~sircmpwn/wshowkeys
URL:      https://github.com/ammgws/wshowkeys
#Source0:  %{url}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz
Source0:  %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: libinput-devel
BuildRequires: libudev-devel
BuildRequires: meson
BuildRequires: pango-devel
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: wayland-protocols-devel

%description
Displays key presses on screen on supported Wayland compositors
(requires wlr_layer_shell_v1 support eg sway).

Usage

wshowkeys [-b|-f|-s #RRGGBB[AA]] [-F font] [-t timeout]
    [-a top|left|right|bottom] [-m margin] [-o output]

    -b #RRGGBB[AA]: set background color
    -f #RRGGBB[AA]: set foreground color
    -s #RRGGBB[AA]: set color for special keys
    -F font: set font (Pango format, e.g. 'monospace 24')
    -t timeout: set timeout before clearing old keystrokes
    -a top|left|right|bottom: anchor the keystrokes to an edge.
       May be specified twice.
    -m margin: set a margin (in pixels) from the nearest edge
    -o output: request wshowkeys is shown on the specified
       output (unimplemented)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

%build
%meson
%meson_build

%install
%meson_install

%files
%attr (4711,root,root) %{_bindir}/%{name}

%doc README.md

%license LICENSE

%changelog
%autochangelog
