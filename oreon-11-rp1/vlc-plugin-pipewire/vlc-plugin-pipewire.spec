%global source0_hash dba410b7c11f295a6ea228bffeef31cf534f659ade75d15e7134308577124e7b

Name:           vlc-plugin-pipewire
Version:        3
Release:        %autorelease
Summary:        Pipewire plugin for VLC media player
License:        GPL-3.0-or-later
URL:            https://www.remlab.net/vlc-plugin-pipewire/
Source0:        https://www.remlab.net/files/%{name}/%{name}-v%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.50
BuildRequires:  pkgconfig(vlc-plugin) >= 3

Requires:       vlc-plugins-base%{?_isa}
Supplements:    (vlc-plugins-base%{?_isa} and pipewire%{?_isa})

%description
This plug-in for the VLC media player provides seamless integration with
PipeWire inside the VLC media player and LibVLC-based applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-v%{version}
# useless check, does not respect environment
sed -i -e '/ifeq/,+5d' Makefile

%build
%set_build_flags
%make_build CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS"

%install
%make_install

%files
%license COPYING
%doc README
%{vlc_plugindir}/audio_output/libaout_pipewire_plugin.so

%changelog
%autochangelog
