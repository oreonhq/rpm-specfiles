%global source0_hash 7a1c6d67a9ac39cbc800f3b4494c4f74c00c12e27f332b5fd73247f17982f06c

Name:           x11docker
Version:        7.6.0
Release:        %autorelease
Summary:        Run GUI applications and desktops in Linux containers

License:        MIT
URL:            https://github.com/mviereck/x11docker
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Default to the podman backend instead of docker
Patch0:         x11docker-podman-default.patch

BuildArch:      noarch

Requires:       bash
Requires:       (podman or /usr/bin/docker or /usr/bin/nerdctl)
Requires:       (xorg-x11-server-Xwayland or xorg-x11-server-Xorg)

Recommends:     nxagent
Recommends:     tini-static
Recommends:     xclip
Recommends:     xdotool
Recommends:     xdpyinfo
Recommends:     xhost
Recommends:     xorg-x11-server-Xephyr
Recommends:     xorg-x11-server-Xvfb
Recommends:     xorg-x11-xauth
Recommends:     xorg-x11-xinit
Recommends:     xpra
Recommends:     xrandr
Recommends:     (weston if libwayland-client)

%description
x11docker allows to run graphical desktop applications (and entire desktops) in
Linux containers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%install
install -Dpm0755 x11docker %{buildroot}%{_bindir}/x11docker
install -Dpm0644 x11docker.man %{buildroot}%{_mandir}/man1/x11docker.1

%files
%license LICENSE.txt
%doc README.md CHANGELOG.md TODO.md paper.bib paper.md x11docker.png
%{_bindir}/x11docker
%{_mandir}/man1/x11docker.1*

%changelog
%autochangelog
