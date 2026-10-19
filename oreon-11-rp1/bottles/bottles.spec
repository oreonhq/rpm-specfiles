%global source0_hash b684e9b1699351f40f345312404870916502e75c168fcbca11310effff23bb90
Name:       bottles
Epoch:      2
Version:    52.0
Release:        1%{?dist}
Summary:        Run Windows in a Bottle
%global forgeurl https://github.com/bottlesdevs/Bottles
%global tag %{version}
%forgemeta
License:    GPL-3.0-or-later AND MIT
URL:        %{forgeurl}
Source0:        %{forgeurl}/archive/%{version}/Bottles-%{version}.tar.gz
Patch:      0001-Make-sure-Paths.bottles-exists.patch
Patch:      0002-Catch-AttributeError-in-set_manager.patch
Patch:      0003-Catch-AttributeError-when-window-is-closed.patch
Patch:      1001-Revert-meson-Add-check-for-Flatpak.patch
Patch:      1002-Change-issue-URL-to-Bugzilla.patch
Patch:      1003-Display-warning-regarding-issue-tracker.patch
Patch:      1004-Do-not-require-Xdp.patch
BuildArch:      noarch
Requires:       cabextract
Requires:       glibc(x86-32)           %dnl # https://github.com/bottlesdevs/Bottles/issues/601#issuecomment-936772762
Requires:       gtk4
Requires:       gtksourceview5
Requires:       hicolor-icon-theme
Requires:       libadwaita >= 1.1.99
Requires:       p7zip p7zip-plugins     %dnl # needed by the dependencies manager
Requires:       patool
Requires:       xdpyinfo                %dnl # needed by the display util
Requires:       ImageMagick             %dnl # https://bugzilla.redhat.com/show_bug.cgi?id=2227538
Requires:       python3dist(pyyaml)
Requires:       python3dist(pycurl)
Requires:       python3dist(chardet)
Requires:       python3dist(requests)
Requires:       python3dist(markdown)
Requires:       python3dist(icoextract)
Requires:       python3dist(patool)
Requires:       python3dist(pathvalidate)
Requires:       python3dist(fvs)
Requires:       python3dist(orjson)
Requires:       python3dist(pycairo)
Requires:       python3dist(pygobject)
Requires:       python3dist(charset-normalizer)
Requires:       python3dist(idna)
Requires:       python3dist(urllib3)
Requires:       python3dist(certifi)
Requires:       python3dist(pefile)
Requires:       python3dist(vkbasalt-cli)
Recommends:     freetype.i686
Recommends:     mesa-dri-drivers.i686
Recommends:     mesa-filesystem.i686
Recommends:     mesa-libEGL.i686
Recommends:     mesa-libgbm.i686
Recommends:     mesa-libglapi.i686
Recommends:     mesa-libGL.i686
Recommends:     mesa-libGLU.i686
Recommends:     mesa-va-drivers.i686
Recommends:     mesa-vulkan-drivers.i686 
Recommends:     SDL2.i686
Recommends:     vulkan-loader.i686
Recommends:     gamemode
Recommends:     gamescope
Recommends:     mangohud
Suggests:       obs-studio-plugin-vkcapture
Recommends:     vkBasalt
Recommends:     vmtouch
# oreon:deps
BuildRequires:  blueprint-compiler
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  python3-devel
# /oreon:deps
%description
Bottles lets you run Windows software on Linux, such as applications
and games. It introduces a workflow that helps you organize by
categorizing each software to your liking. Bottles provides several
tools and integrations to help you manage and optimize your
applications.

Features:

- Use pre-configured environments as a base
- Change runners for any bottle
- Various optimizations and options for gaming
- Repair in case software or bottle is broken
- Install various known dependencies
- Integrated task manager to manage and monitor processes
- Backup and restore

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

# F40 only has meson 1.4.1. Lower requirement.
sed -r -i 's/(meson_version.*)1\.[0-9]\.[0-9]/\11.4.1/' meson.build

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
