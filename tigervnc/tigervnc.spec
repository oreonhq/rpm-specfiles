#defining macros needed by SELinux
%global selinuxtype targeted
%global modulename vncsession

%bcond ffmpeg %[0%{?fedora} || 0%{?epel} || 0%{?eln}]
%bcond xserver %[!(0%{?rhel} >= 10)]

Name:           tigervnc
Version:        1.16.0
Release:        2%{?dist}
Summary:        A TigerVNC remote display system

%global _hardened_build 1

License:        GPL-2.0-or-later
URL:            https://www.tigervnc.com

Source0:        https://github.com/TigerVNC/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        xvnc.service
Source2:        xvnc.socket
Source3:        10-libvnc.conf
Source4:        HOWTO.md

# Backwards compatibility
Source5:        vncserver

# Downstream patches
Patch1:         tigervnc-vncsession-restore-script-systemd-service.patch

%if 0%{?fedora} >= 42 || 0%{?rhel} >= 11
# https://fedoraproject.org/wiki/Changes/Unify_bin_and_sbin
Patch2:         tigervnc-sbin-bin-merge.patch
%endif

# Upstream patches

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  cmake

BuildRequires:  gnutls-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  zlib-devel

# TigerVNC 1.4.x requires fltk 1.3.3 for keyboard handling support
# See https://github.com/TigerVNC/tigervnc/issues/8, also bug #1208814
%if 0%{?fedora} >= 44 || 0%{?rhel} >= 11
BuildRequires:  fltk1.3-devel
%else
BuildRequires:  fltk-devel
%endif
BuildRequires:  libxcvt-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  pixman-devel

%if 0%{?fedora} || 0%{?epel} || 0%{?eln}
# Icons
BuildRequires:  ImageMagick
%endif


%if %{with xserver}
# X11/graphics dependencies
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-autopoint
BuildRequires:  libXdamage-devel
BuildRequires:  libXdmcp-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXfont2-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXt-devel
BuildRequires:  libXtst-devel
BuildRequires:  libdrm-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  libtool
BuildRequires:  libxkbfile-devel
BuildRequires:  libxshmfence-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  pkgconfig(fontutil)
BuildRequires:  pkgconfig(xkbcomp)
BuildRequires:  xorg-x11-server-devel
BuildRequires:  xorg-x11-server-source
BuildRequires:  xorg-x11-util-macros
BuildRequires:  xorg-x11-xtrans-devel
%endif

%if %{with ffmpeg}
# Codecs
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
%endif

# SELinux
BuildRequires:  libselinux-devel
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd

# Wayland
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)

Requires(post): coreutils
Requires(postun):coreutils

Requires:       hicolor-icon-theme
Requires:       tigervnc-license
Requires:       tigervnc-icons
Requires:       which

%description
Virtual Network Computing (VNC) is a remote display system which
allows you to view a computing 'desktop' environment not only on the
machine where it is running, but from anywhere on the Internet and
from a wide variety of machine architectures.  This package contains a
client which will allow you to connect to other desktops running a VNC
server.

%package x11-server
Summary:        A TigerVNC server for X11
Requires:       perl-interpreter
Requires:       tigervnc-server-common = %{version}-%{release}
Requires:       (%{name}-selinux if selinux-policy-%{selinuxtype})
Requires:       xorg-x11-xauth
Requires:       xorg-x11-xinit
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Obsoletes:      tigervnc-server < %{version}-%{release}
Provides:       tigervnc-server = %{version}-%{release}
Obsoletes:      tigervnc-server-minimal < %{version}-%{release}
Provides:       tigervnc-server-minimal = %{version}-%{release}

%description x11-server
The VNC system allows you to access the same desktop from a wide
variety of platforms.  This package includes set of utilities
which make usage of TigerVNC X11 server more user friendly. It also
contains x0vncserver program which can export your active
X session.

%package wayland-server
Summary:        A TigerVNC server for Wayland compositors
Requires:       tigervnc-server-common = %{version}-%{release}
Requires:       (%{name}-selinux if selinux-policy-%{selinuxtype})

%description wayland-server
TigerVNC server which makes a Wayland compositor that is based on
wlroots, or has the RemoteDesktop portal implemented, remotely
accessible via VNC, TigerVNC or compatible viewers. It does not create
a virtual display, instead, it shares an existing display (typically,
that one connected to the physical screen).


%package server-common
Summary:        Common tools for TigerVNC servers
Requires:       dbus-x11
Requires:       mesa-dri-drivers
Requires:       tigervnc-license
Requires:       xkbcomp
Requires:       xkeyboard-config

%description server-common
Common tools used by both X11 and Wayland TigerVNC servers,
including vncpasswd for password management and vncconfig for
server configuration.

%package x11-server-module
Summary:        TigerVNC module to Xorg
Requires:       xorg-x11-server-Xorg %(xserver-sdk-abi-requires ansic) %(xserver-sdk-abi-requires videodrv)
Requires:       tigervnc-license
Obsoletes:      tigervnc-server-module < %{version}-%{release}
Provides:       tigervnc-server-module = %{version}-%{release}

%description x11-server-module
This package contains libvnc.so module to X server, allowing others
to access the desktop on your machine.

%package license
Summary:        License of TigerVNC suite
BuildArch:      noarch

%description license
This package contains license of the TigerVNC suite

%package icons
Summary:        Icons for TigerVNC viewer
BuildArch:      noarch

%description icons
This package contains icons for TigerVNC viewer

%package selinux
Summary:        SELinux module for TigerVNC
BuildArch:      noarch
BuildRequires:  selinux-policy-devel
Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
BuildRequires:  selinux-policy-devel
%{?selinux_requires}

%description selinux
This package provides the SELinux policy module to ensure TigerVNC
runs properly under an environment with SELinux enabled.

%prep
%setup -q

%patch -P1 -p1 -b .vncsession-restore-script-systemd-service

%if 0%{?fedora} >= 42 || 0%{?rhel} >= 11
%patch -P2 -p1 -b .sbin-bin-merge
%endif

# Upstream patches

%if %{with xserver}
cp -r /usr/share/xorg-x11-server-source/* unix/xserver
pushd unix/xserver
for all in `find . -type f -perm -001`; do
        chmod -x "$all"
done
# EPEL 10 possibly too in the future
%if 0%{?fedora} && 0%{?fedora} > 40
cat ../xserver21.patch | patch -p1
%else
cat ../xserver120.patch | patch -p1
%endif
popd
%else
sed -i -r '/add_subdirectory.(|x0)vncserver/d' unix/CMakeLists.txt
%endif

# Downstream patches

%build
# TODO: Please submit an issue to upstream (rhbz#2381485)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%ifarch sparcv9 sparc64 s390 s390x
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%else
export CFLAGS="$RPM_OPT_FLAGS -fpic"
%endif
export CXXFLAGS="$CFLAGS -std=c++11"

%if 0%{?fedora} >= 35 || 0%{?rhel} >= 10
%define __cmake_builddir %{_target_platform}

mkdir -p %{__cmake_builddir}
%endif

%cmake -DCMAKE_INSTALL_UNITDIR=%{_unitdir}

%cmake_build

%if %{with xserver}
pushd unix/xserver

autoreconf -fiv
%configure \
        --disable-xorg --disable-xnest --disable-xvfb --disable-dmx \
        --disable-xwin --disable-xephyr --disable-kdrive --disable-xwayland \
        --with-pic --disable-static \
        --with-default-font-path="catalogue:/etc/X11/fontpath.d,built-ins" \
        --with-xkb-output=%{_localstatedir}/lib/xkb \
        --enable-glx --disable-dri --enable-dri2 --enable-dri3 \
        --disable-unit-tests \
        --disable-config-hal \
        --disable-config-udev \
        --without-dtrace \
        --disable-devel-docs \
        --disable-selective-werror

make TIGERVNC_BUILDDIR="`pwd`/../../%{__cmake_builddir}" %{?_smp_mflags}
popd
%endif

# SELinux
pushd unix/vncserver/selinux
make
popd

%if 0%{?rhel}
# Build icons
%if 0%{?rhel} >= 9
pushd %{_target_platform}/media
%else
pushd media
%endif
make
popd
%endif



%install
%cmake_install
rm -f %{buildroot}%{_docdir}/%{name}-%{version}/{README.rst,LICENCE.TXT}

%if %{with xserver}
pushd unix/xserver/hw/vnc
%make_install TIGERVNC_BUILDDIR="`pwd`/../../../../%{__cmake_builddir}"
popd

# Install systemd unit file
install -m644 %{SOURCE1} %{buildroot}%{_unitdir}/xvnc@.service
install -m644 %{SOURCE2} %{buildroot}%{_unitdir}/xvnc.socket
install -m755 %{SOURCE5} %{buildroot}/%{_bindir}/vncserver
%endif

# Install selinux policy file
pushd unix/vncserver/selinux
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}
popd

# Install desktop stuff
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{16x16,24x24,48x48}/apps

pushd media/icons
for s in 16 22 24 32 48 64 128; do
install -m644 tigervnc_$s.png %{buildroot}%{_datadir}/icons/hicolor/${s}x$s/apps/tigervnc.png
done
popd

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.tigervnc.vncviewer.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/vncviewer.desktop

%find_lang %{name} %{name}.lang

%if %{with xserver}
# remove unwanted files
rm -f  %{buildroot}%{_libdir}/xorg/modules/extensions/libvnc.la

mkdir -p %{buildroot}%{_sysconfdir}/X11/xorg.conf.d/
install -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/X11/xorg.conf.d/10-libvnc.conf

install -m 644 %{SOURCE4} %{buildroot}/%{_docdir}/tigervnc/HOWTO.md

%post x11-server
%systemd_post xvnc@.service
%systemd_post xvnc.socket

%preun x11-server
%systemd_preun xvnc@.service
%systemd_preun xvnc.socket

%postun x11-server
%systemd_postun xvnc@.service
%systemd_postun xvnc.socket
%endif

%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
%selinux_relabel_post -s %{selinuxtype}

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
    %selinux_relabel_post -s %{selinuxtype}
fi


%files -f %{name}.lang
%doc README.rst
%{_bindir}/vncviewer
%{_datadir}/applications/*
%{_mandir}/man1/vncviewer.1*
%{_datadir}/metainfo/org.tigervnc.vncviewer.metainfo.xml

%if %{with xserver}
%files x11-server
%config(noreplace) %{_sysconfdir}/pam.d/tigervnc
%config(noreplace) %{_sysconfdir}/tigervnc/vncserver-config-defaults
%config(noreplace) %{_sysconfdir}/tigervnc/vncserver-config-mandatory
%config(noreplace) %{_sysconfdir}/tigervnc/vncserver.users
%{_unitdir}/vncserver@.service
%{_unitdir}/xvnc@.service
%{_unitdir}/xvnc.socket
%{_bindir}/vncserver
%{_bindir}/x0vncserver
%{_bindir}/Xvnc
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 11
%{_bindir}/vncsession
%else
%{_sbindir}/vncsession
%endif
%{_libexecdir}/vncserver
%{_libexecdir}/vncsession-start
%{_libexecdir}/vncsession-restore
%{_mandir}/man1/x0vncserver.1*
%{_mandir}/man1/Xvnc.1*
%{_mandir}/man8/vncserver.8*
%{_mandir}/man8/vncsession.8*
%{_docdir}/tigervnc/HOWTO.md

%files x11-server-module
%{_libdir}/xorg/modules/extensions/libvnc.so
%config(noreplace) %{_sysconfdir}/X11/xorg.conf.d/10-libvnc.conf
%endif

%files server-common
%{_bindir}/vncconfig
%{_bindir}/vncpasswd
%{_mandir}/man1/vncpasswd.1*
%{_mandir}/man1/vncconfig.1*

%files wayland-server
%{_bindir}/w0vncserver
%{_bindir}/w0vncserver-forget
%{_mandir}/man1/w0vncserver.1*
%{_mandir}/man1/w0vncserver-forget.1*

%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.*
%ghost %verify(not md5 size mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{modulename}

%files license
%{_docdir}/tigervnc/LICENCE.TXT

%files icons
%{_datadir}/icons/hicolor/*/apps/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.16.0-2
- Prepare for Oreon 11 (RP1)
