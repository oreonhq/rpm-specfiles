%global source0_hash 6b563a4972b2888f75f500040e53228e662659d71cf8d2f67b7a59bc10811899
%define         srcurl          http://wallpapoz.akbarhome.com/
%define         icondir         %{_datadir}/icons/hicolor/128x128/apps
%define         mainver         0.6.2
%undefine         betaver
%define         baserelease		21
%define         rel             %{?betaver:0.}%{baserelease}%{?betaver:.%betaver}
Name:           wallpapoz
Version:        %{mainver}
Release:        21%{?dist}
Summary:        Gnome Multi Backgrounds and Wallpapers Configuration Tool
License:        GPL-2.0-or-later AND GFDL-1.1-or-later
URL:            http://vajrasky.wordpress.com/wallpapoz/
Source0:        https://github.com/downloads/vajrasky/%{name}/%{name}-%{version}.tar.bz2
Source11:       wallpapoz-autostart.desktop
Source12:       daemon_wallpapoz-wrapper
Source22:       wallpapoz-glade-builder-convert.sh
Patch0:         wallpapoz-0.6.1-workspace-num-respawn.patch
Patch2:         wallpapoz-0.6.1-dircheck.patch
Patch3:         wallpapoz-0.4.1-rev92-noitem_selected.patch
Patch4:         wallpapoz-0.4.1-rev92-paste-initialization.patch
Patch5:         wallpapoz-0.6.2-kill-daemon-without-x.patch
Patch6:         wallpapoz-0.6.1-kill-multiple-daemon.patch
Patch7:		wallpapoz-0.6.1-animated-image.patch
Patch8:		wallpapoz-0.6.1-nonutf8-directory.patch
Patch9:		wallpapoz-0.6.1-delete-one-wallpaper.patch
Patch10:	wallpapoz-0.6.1-delete-first-in-desktop-mode.patch
Patch12:	wallpapoz-0.5-startup-warn-about-workspace-name.patch
Patch13:	wallpapoz-0.6.1-switch-from-wallpaper-to-desktop-with-workspace-increase.patch
Patch14:	wallpapoz-0.6.2-wm-return-to-default.patch
Patch15:	wallpapoz-0.6.2-import-PIL-for-Image.patch
Patch16:	wallpapoz-0.6.2-LXDE.patch
Patch17:	wallpapoz-0.6.2-MATE.patch
Patch18:	wallpapoz-0.6.2-CINNAMON.patch
Patch31:	wallpapoz-0.6.2-python3.patch
Patch32:	wallpapoz-0.6.2-python3-desktop-type.patch
BuildArch:      noarch
Requires:       GConf2
Requires:       gtk3
Requires:       gobject-introspection
Requires:       python3-gobject
Requires:       python3-imaging
Requires:       xprop xwininfo
Requires:       /usr/bin/kill
Requires:       /usr/bin/pgrep
# oreon:deps
BuildRequires:  /usr/bin/gtk-builder-convert
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gobject-introspection
BuildRequires:  gtk3
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3-imaging
# /oreon:deps
%description
This tool enables your Gnome desktop to have different 
wallpapers for different workspaces or virtual desktops.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}%{?svnver:-%svnver}
%patch -P0 -p1 -b .respawn
%patch -P2 -p1 -b .dircheck
%patch -P3 -p1 -b .noitem
%patch -P4 -p1 -b .patch_init
%patch -P5 -p1 -b .kill_nox
%patch -P6 -p1 -b .kill_multi
%patch -P7 -p1 -b .anime
%patch -P8 -p1 -b .nonutf8
%patch -P9 -p1 -b .deletelastone
%patch -P10 -p1 -b .deletefirst
%patch -P12 -p1 -b .workspace_img
%patch -P13 -p1 -b .workspace_num_incr
%patch -P14 -p1 -b .default
%patch -P15 -p1 -b .pil
%patch -P16 -p1 -b .LXDE
%patch -P17 -p1 -b .MATE
%patch -P18 -p1 -b .CINNAMON

grep -rl --null '/usr/bin/env python$' . | \
	xargs --null sed -i -e 's|/usr/bin/env python|/usr/bin/python2|'

%patch -P31 -p1 -b .py3
%patch -P32 -p1 -b .py3.desktop

# For setup
mkdir TMPBINDIR
pushd TMPBINDIR
ln -sf /bin/true xwininfo
popd

# Install C gnome help documents (bug 651522)
ln -sf c share/gnome/help/wallpapoz/C

%build

bash %{SOURCE22}
find . -type f -print0 | xargs -0 chmod 0644
grep -rl --null '#!/usr/bin' . | xargs -0 chmod 0755
%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_prefix}
export PATH=$(pwd)/TMPBINDIR:$PATH
%{__python3} setup.py install --installdir=$RPM_BUILD_ROOT%{_prefix}
%{__sed} -i -e 's|%{name}\.png|%{name}|' \
   $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
desktop-file-install \
   --dir $RPM_BUILD_ROOT%{_datadir}/applications \
   --delete-original \
   $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_sysconfdir}/xdg/autostart
desktop-file-install \
	--dir ${RPM_BUILD_ROOT}%{_sysconfdir}/xdg/autostart \
	%{SOURCE11}
pushd ${RPM_BUILD_ROOT}
%{__mkdir_p} ./%{_libexecdir}
%{__mv} ./%{_bindir}/daemon_wallpapoz ./%{_libexecdir}
%{__install} -cp -m 0755 %{SOURCE12} ./%{_bindir}/daemon_wallpapoz
popd
rm -f ${RPM_BUILD_ROOT}%{_bindir}/launcher_wallpapoz.sh
install -cpm 0644  \
	wallpapoz-*/share/wallpapoz/glade/*builder*glade \
	%{buildroot}%{_datadir}/%{name}/glade/
%{find_lang} %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
