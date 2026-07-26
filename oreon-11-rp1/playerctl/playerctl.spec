%global source0_hash 75957ad5071956f563542c7557af16a57e40b4a7f66bc9b6373d022ec5eef548

Name:           playerctl
Version:        2.4.1
Release:        12%{?dist}
Summary:        Command-line MPRIS-compatible Media Player Controller

License:        LGPL-3.0-or-later
URL:            https://github.com/acrisci/playerctl
Source:         %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

Obsoletes:      playerctl-static < 2.3.1-3

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

%autosetup

%build
%meson -Dbash-completions=true -Dzsh-completions=true
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}d
%{_datadir}/bash-completion/
%{_datadir}/dbus-1/services/org.mpris.MediaPlayer2.playerctld.service
%{_datadir}/man/man1/%{name}.*
%{_datadir}/zsh/

%files devel
%license COPYING
%{_datadir}/gir-1.0/Playerctl-2.0.gir
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files docs
%license COPYING
%{_datadir}/gtk-doc/

%files libs
%license COPYING
%{_libdir}/girepository-1.0/
%{_libdir}/lib%{name}.so.2*

%changelog
%autochangelog
