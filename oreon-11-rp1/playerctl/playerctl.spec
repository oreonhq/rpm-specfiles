%global source0_hash 75957ad5071956f563542c7557af16a57e40b4a7f66bc9b6373d022ec5eef548
Name:           playerctl
Version:        2.4.1
Release:        1%{?dist}
Summary:        Command-line MPRIS-compatible Media Player Controller
License:        LGPL-3.0-or-later
URL:            https://github.com/acrisci/playerctl
Source0:        https://github.com/acrisci/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      playerctl-static < 2.3.1-3
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
# /oreon:deps
%description
Playerctl is a command-line utility and library for controlling media players
that implement the MPRIS D-Bus Interface Specification. Playerctl makes it easy
to bind player actions, such as play and pause, to media keys. You can also get
metadata about the playing track such as the artist and title for integration
into statusline generators or other command-line tools.

For more advanced users, Playerctl provides an introspectable library available
in your favorite scripting language that allows more detailed control like the
ability to subscribe to media player events or get metadata such as artist and
title for the playing track.

Examples of players implementing the MPRIS D-Bus Interface Specification include
vlc, mpv, RhythmBox, web browsers, cmus, mpd, spotify and others.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package docs
Summary:        Documentation related to %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
BuildRequires:  gtk-doc
%description docs
%{summary}.

%package libs
Summary:        Libraries and shared code for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description libs
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dbash-completions=true -Dzsh-completions=true
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n playerctl-devel -f %{oreon_filedir}/playerctl-devel.list
%files -n playerctl-docs -f %{oreon_filedir}/playerctl-docs.list
%files -n playerctl-libs -f %{oreon_filedir}/playerctl-libs.list

%changelog

%autochangelog
