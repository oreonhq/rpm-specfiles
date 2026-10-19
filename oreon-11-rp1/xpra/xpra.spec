%global source0_hash 87ac8dbf38fa162402ab95f4591d9906d3695e26958943f6d833dc105bce905c
%bcond_with debug
%bcond_with openh264
%global __provides_exclude_from ^%{python3_sitearch}/.*\\.so$
%if 0%{?_cups_serverbin:1}
%global cupslibdir %_cups_serverbin
%else
%global cupslibdir %(cups-config --serverbin 2> /dev/null || echo "/usr/lib/cups")
%endif
%global gnome_shell_extension input-source-manager@xpra_org
%global build_opts -C--global-option=--without-nvidia -C--global-option=--without-pandoc_lua -C--global-option=--with-verbose -C--global-option=--with-Xdummy -C--global-option=--with-Xdummy_wrapper -C--global-option=--without-strict -C--global-option=--with-vpx %{?with_debug:-C--global-option=--with-debug} %{?with_openh264:-C--global-option=--with-openh264} -C--global-option=--without-cuda_rebuild -C--global-option=--with-client -C--global-option=--without-qt6_client -C--global-option=--without-pyglet_client -C--global-option=--without-enc_x264
Name:           xpra
Version:        6.5.3
Release:        1%{?dist}
Epoch:          1
Summary:        Remote display server for applications and desktops
License:        GPL-2.0-or-later AND BSD-2-Clause AND LGPL-3.0-or-later AND BSD-3-Clause
URL:            https://www.xpra.org/
Source0:        https://github.com/Xpra-org/xpra/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml
Patch0:         %{name}-fix_audio.patch
Patch1:         %{name}-bug4724.patch
%if %{with debug}
%endif
%if %{with openh264}
%endif
Requires: python3-pillow
Requires: python3-lz4
Requires: dbus-x11
Requires: xmodmap
Requires: xrandr
Requires: xorg-x11-drv-dummy%{?_isa}
Requires: xorg-x11-xauth%{?_isa}
Requires: xorg-x11-server-Xorg%{?_isa}
Requires: gstreamer1%{?_isa}
Requires: gstreamer1-plugins-base%{?_isa}
Requires: gstreamer1-plugins-good%{?_isa}
Requires: pulseaudio%{?_isa}
Requires: pulseaudio-utils%{?_isa}
Requires: cups-filesystem
Requires: shared-mime-info%{?_isa}
Requires: systemd-udev%{?_isa}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-xpra = %{version}-%{release}
# /oreon:deps
%package -n       python3-xpra+gui
Summary:        Metapackage for python3-xpra gui extras
Requires:       python3-xpra = %{version}-%{release}
Provides:       python3dist(xpra[gui]) = %{version}-%{release}

%description -n python3-xpra+gui
Metapackage for python3-xpra gui extras.

%package -n       python3-xpra+cli
Summary:        Metapackage for python3-xpra cli extras
Requires:       python3-xpra = %{version}-%{release}
Provides:       python3dist(xpra[cli]) = %{version}-%{release}

%description -n python3-xpra+cli
Metapackage for python3-xpra cli extras.

%description
Xpra is "screen for X": it allows you to run X programs, usually on a remote
host, direct their display to your local machine, and then to disconnect from
these programs and reconnect from the same or another machine, without losing
any state. It gives you remote access to individual applications.

Xpra is "rootless" or "seamless": programs you run under it show up on your
desktop as regular programs, managed by your regular window manager.
Sessions can be accessed over SSH, or password protected over plain TCP sockets.
Xpra is usable over reasonably slow links and does its best to adapt to changing
network bandwidth constraints.

%package -n %{name}-client-gnome
Summary:			Gnome integration for the xpra client
Requires:			%{name}-client-gtk3%{?_isa} = 1:%{version}-%{release}
Requires:			gnome-shell-extension-appindicator
%description -n %{name}-client-gnome
This package installs the GNOME Shell extensions
that can help in restoring the system tray functionality.
It also includes the gnome_shell_extension extension which
is required for querying and activating keyboard input sources.

%package -n %{name}-client-gtk3
Summary:			GTK3 xpra client
BuildRequires:		xclip
Requires:			%{name}%{?_isa} = 1:%{version}-%{release}
%description -n %{name}-client-gtk3
This package contains the GTK3 xpra client.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -N

%patch -P 1 -p1

rm -rf *.egg-info

# cc1: error: unrecognized compiler option ‘-mfpmath=387’
%ifarch %{arm}
sed -i 's|-mfpmath=387|-mfloat-abi=hard|' setup.py
%endif

# Create a sysusers.d config file
cat >xpra.sysusers.conf <<EOF
g xpra -
EOF

%build

export CFLAGS="%{optflags} -I%{_includedir}/security %(pkgconf --cflags pygobject-3.0)"
%pyproject_wheel %{build_opts}
%install
%pyproject_install
mv %{buildroot}%{_prefix}/etc  %{buildroot}/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
mv %{buildroot}%{_datadir}/icons/xpra.png \
    %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/
rm -f %{buildroot}%{_datadir}/icons/xpra-mdns.png
install -pm 644 fs/share/icons/xpra-mdns.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
rm -f %{buildroot}%{_datadir}/icons/xpra-shadow.png
install -pm 644 fs/share/icons/xpra-shadow.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
rm -rf %{buildroot}%{_datadir}/appdata
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE1} %{buildroot}%{_metainfodir}/
mkdir -p %{buildroot}%{_sysconfdir}/xpra
install -pm 644 fs/etc/xpra/nvenc.keys %{buildroot}%{_sysconfdir}/xpra
rm %{buildroot}%{_datadir}/xpra/COPYING
for i in `ack -rl '^#!/.*python' %{buildroot}%{python3_sitearch}/xpra`; do
    %py3_shebang_fix $i
    chmod 0755 $i
done
find %{buildroot}%{python3_sitearch}/xpra -name '*.so' \
    -exec chmod 0755 {} \;
find %{buildroot}%{_datadir}/xpra -name '*.swf' -exec rm {} \;
mkdir -p %{buildroot}%{_rundir}/xpra
%py3_shebang_fix %{buildroot}%{cupslibdir}/backend/xpraforwarder
%py3_shebang_fix %{buildroot}%{_libexecdir}/xpra/auth_dialog
%py3_shebang_fix %{buildroot}%{_libexecdir}/xpra/xdg-open
for i in `find %{buildroot}%{_bindir} -perm /644 -type f \( -name "*" \)`; do
    chmod 0755 $i
done
rm -rf %{buildroot}%{_docdir}/xpra/Build
install -pm 644 README.md %{buildroot}%{_docdir}/xpra/
install -m0644 -D xpra.sysusers.conf %{buildroot}%{_sysusersdir}/xpra.conf
sed -e 's|build/bdist.linux-%{?_arch}/wheel/xpra-%{version}.data/data||g' -i %{buildroot}%{_sysconfdir}/xpra/conf.d/55_server_x11.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post xpra-encoder.service
%systemd_post xpra.service
%tmpfiles_create %{_tmpfilesdir}/xpra.conf
%preun

%systemd_preun xpra-encoder.service
%systemd_preun xpra.service
%postun

%systemd_postun_with_restart xpra-encoder.service
%systemd_postun_with_restart xpra.service
%check

%{?fedora:appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/xpra.appdata.xml}
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files
%files -n xpra-client-gnome -f %{oreon_filedir}/xpra-client-gnome.list
%files -n xpra-client-gtk3 -f %{oreon_filedir}/xpra-client-gtk3.list

%changelog

%autochangelog
