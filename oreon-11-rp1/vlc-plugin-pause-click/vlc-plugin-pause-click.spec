%global source0_hash 2a2cd76bc0bc10cb5f7c2143ae8508008c5a100f9a9c19b4fbc2c517983ded4c

%global srcname vlc-pause-click-plugin

Name:           vlc-plugin-pause-click
Version:        2.2.0
Release:        %autorelease
Summary:        VLC plugin that pauses/plays video on mouse click 
License:        LGPL-2.1-or-later
URL:            https://github.com/nurupo/vlc-pause-click-plugin
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(vlc-plugin)

Requires:       vlc-plugins-video-out%{?_isa}

%description
VLC plugin that allows you to pause/play a video by clicking on the video
image. By default it pauses on every click, but it can be configured to
work nicely with double-click-to-fullscreen by enabling "Prevent pause/play
from triggering on double click" option in the settings.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build
%set_build_flags
%make_build CFLAGS="${CFLAGS}" LDFLAGS="${LDFLAGS}" OS=Linux

%install
%make_install OS=Linux

%files
%license LICENSE
%doc README.md
%{vlc_plugindir}/video_filter/libpause_click_plugin.so

%changelog
%autochangelog
