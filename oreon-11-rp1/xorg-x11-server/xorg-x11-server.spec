%global source0_hash 1a4eb36ca65cc3b1b936566d677a9786e13c11cd5806e951ac55f3f5ce3984af
%undefine _hardened_build
%undefine _strict_symbol_defs_build
%global ansic_major 0
%global ansic_minor 4
%global videodrv_major 25
%global videodrv_minor 2
%global xinput_major 24
%global xinput_minor 4
%global extension_major 10
%global extension_minor 0
%global pkgname xorg-server
Summary:        X.Org X11 X server
Name:       xorg-x11-server
Version:    21.1.24
Release:        1%{?dist}
URL:        http://www.x.org
License:    Adobe-Display-PostScript AND BSD-3-Clause AND DEC-3-Clause AND HPND AND HPND-sell-MIT-disclaimer-xserver AND HPND-sell-variant AND ICU AND ISC AND MIT AND MIT-open-group AND NTP AND SGI-B-2.0 AND SMLNJ AND X11 AND X11-distribute-modifications-variant
Source0:        https://xorg.freedesktop.org/archive/individual/xserver/xorg-server-21.1.24.tar.xz
Source10:        xserver.pamd
Source20:   xvfb-run.sh
Source30:        xserver-sdk-abi-requires
Source40:        driver-abi-rebuild.sh
Patch0:     06_use-intel-only-on-pre-gen4.diff
Patch1:     0001-xfree86-use-modesetting-driver-by-default-on-GeForce.patch
Patch2:     0001-xf86-dri2-Use-va_gl-as-vdpau_driver-for-Intel-i965-G.patch
Patch3:     0001-Fedora-hack-Make-the-suid-root-wrapper-always-start-.patch
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  kernel-headers
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXres-devel
BuildRequires:  libXv-devel
BuildRequires:  make
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(audit)
BuildRequires:  pkgconfig(bigreqsproto)
BuildRequires:  pkgconfig(compositeproto)
BuildRequires:  pkgconfig(damageproto)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dri2proto)
BuildRequires:  pkgconfig(dri3proto)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(fixesproto)
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(kbproto)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(libxcvt)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(recordproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(resourceproto)
BuildRequires:  pkgconfig(scrnsaverproto)
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcmiscproto)
BuildRequires:  pkgconfig(xdmcp)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xf86bigfontproto)
BuildRequires:  pkgconfig(xf86vidmodeproto)
BuildRequires:  pkgconfig(xfont2)
BuildRequires:  pkgconfig(xineramaproto)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xshmfence)
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  systemtap-sdt-devel
BuildRequires:  xorg-x11-util-macros
BuildRequires:  xorg-x11-xtrans-devel
# /oreon:deps
%description
X.Org X11 X server.

%package        common
Summary:        Xorg server common files
Requires:       pixman
Requires:       xkbcomp
Requires:       xkeyboard-config
%description    common
Common files shared among all X servers.

%package        Xorg
Summary:        Xorg X server
Requires:       libEGL
Requires:       system-setup-keyboard
Requires:       xorg-x11-drv-libinput
Requires:       xorg-x11-server-common >= %{version}-%{release}
Provides:       Xorg = %{version}-%{release}
Provides:       Xserver
Provides:       xorg-x11-server-wrapper = %{version}-%{release}
Provides:       xserver-abi(ansic-%{ansic_major}) = %{ansic_minor}
Provides:       xserver-abi(videodrv-%{videodrv_major}) = %{videodrv_minor}
Provides:       xserver-abi(xinput-%{xinput_major}) = %{xinput_minor}
Provides:       xserver-abi(extension-%{extension_major}) = %{extension_minor}
Obsoletes:      xorg-x11-server-Xdmx < 1.20.15
Obsoletes:      xorg-x11-drv-fbdev < 0.5.0-19
Obsoletes:      xorg-x11-drv-vesa < 2.6.0-3
Obsoletes:      xorg-x11-drv-armsoc < 1.4.1-10
%description    Xorg
X.org X11 is an open source implementation of the X Window System. It provides
the basic low level functionality which full fledged graphical user interfaces
(GUIs) such as GNOME and KDE are designed upon.

%package        Xnest
Summary:        A nested server
Requires:       xorg-x11-server-common >= %{version}-%{release}
Provides:       Xnest
%description    Xnest
Xnest is an X server which has been implemented as an ordinary X application. It
runs in a window just like other X applications, but it is an X server itself in
which you can run other software. It is a very useful tool for developers who
wish to test their applications without running them on their real X server.

%package        Xvfb
Summary:        A X Windows System virtual framebuffer X server
License:        MIT and GPL-2.0-only
Requires:       xorg-x11-server-common >= %{version}-%{release}
Requires:       xorg-x11-xauth
Provides:       Xvfb
Requires:       util-linux
%description    Xvfb
Xvfb (X Virtual Frame Buffer) is an X server that is able to run on machines
with no display hardware and no physical input devices. Xvfb simulates a dumb
framebuffer using virtual memory. Xvfb does not open any devices, but behaves
otherwise as an X display. Xvfb is normally used for testing servers.

%package        Xephyr
Summary:        A nested server
Requires:       xorg-x11-server-common >= %{version}-%{release}
Provides:       Xephyr
%description    Xephyr
Xephyr is an X server which has been implemented as an ordinary X application.
It runs in a window just like other X applications, but it is an X server itself
in which you can run other software. It is a very useful tool for developers who
wish to test their applications without running them on their real X server.
Unlike Xnest, Xephyr renders to an X image rather than relaying the X protocol,
and therefore supports the newer X extensions like Render and Composite.

%package        devel
Summary:        SDK for X server driver module development
Requires:       libpciaccess-devel
Requires:       libXfont2-devel
Requires:       xorg-x11-proto-devel
Requires:       xorg-x11-util-macros
Requires:       pixman-devel
Requires:       pkgconfig
Provides:       xorg-x11-server-static
%description devel
The SDK package provides the developmental files which are necessary for
developing X server driver modules, and for compiling driver modules outside of
the standard X11 source code tree. Developers writing video drivers, input
drivers, or other X modules should install this package.

%package        source
Summary:        Xserver source code required to build VNC server (Xvnc)
BuildArch:      noarch
%description        source
Xserver source code needed to build VNC server (Xvnc).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{pkgname}-%{version}

# check the ABI in the source against what we expect.
getmajor() {
    grep -i ^#define.ABI.$1_VERSION hw/xfree86/common/xf86Module.h |
    tr '(),' '   ' | awk '{ print $4 }'
}

getminor() {
    grep -i ^#define.ABI.$1_VERSION hw/xfree86/common/xf86Module.h |
    tr '(),' '   ' | awk '{ print $5 }'
}

test `getmajor ansic` == %{ansic_major}
test `getminor ansic` == %{ansic_minor}
test `getmajor videodrv` == %{videodrv_major}
test `getminor videodrv` == %{videodrv_minor}
test `getmajor xinput` == %{xinput_major}
test `getminor xinput` == %{xinput_minor}
test `getmajor extension` == %{extension_major}
test `getminor extension` == %{extension_minor}

%build

%meson \
    -D agp=auto \
    -D builder_string="Build ID: %{name} %{version}-%{release}" \
    -D default_font_path="catalogue:/etc/X11/fontpath.d,built-ins" \
    -D devel-docs=false \
    -D dga=true \
    -D docs-pdf=false \
    -D docs=false \
    -D dpms=true \
    -D dri1=false \
    -D dri2=true \
    -D dri3=true \
    -D drm=true \
    -D dtrace=false \
    -D fallback_input_driver=libinput \
    -D glamor=true \
    -D glx=true \
    -D hal=false \
    -D input_thread=true \
    -D int10=false \
    -D ipv6=true \
    -D libunwind=true \
    -D linux_acpi=false \
    -D linux_apm=false \
    -D listen_local=true \
    -D listen_tcp=false \
    -D listen_unix=true \
    -D log_dir="%{_localstatedir}/log" \
    -D mitshm=auto \
    -D module_dir="%{_libdir}/xorg/modules" \
    -D pciaccess=true \
    -D screensaver=true \
    -D secure-rpc=false \
    -D sha1=libcrypto \
    -D suid_wrapper=true \
    -D systemd_logind=true \
    -D udev_kms=true \
    -D udev=true \
    -D vgahw=true \
    -D xace=true \
    -D xcsecurity=true \
    -D xdm-auth-1=true \
    -D xdmcp=true \
    -D xephyr=true \
    -D xf86bigfont=false \
    -D xf86-input-inputtest=true \
    -D xinerama=true \
    -D xkb_output_dir="%{_localstatedir}/lib/xkb" \
    -D xnest=true \
    -D xorg=true \
    -D xpbproxy=false \
    -D xquartz=false \
    -D xres=true \
    -D xselinux=true \
    -D xvfb=true \
    -D xvmc=true \
    -D xv=true \
    -D xwin=false
%meson_build
%install
%meson_install
install -D -m 0644 -p xkb/README.compiled %{buildroot}%{_localstatedir}/lib/xkb/README.compiled
install -D -m 0644 %{SOURCE10} %{buildroot}%{_sysconfdir}/pam.d/xserver
mkdir -p %{buildroot}%{_sysconfdir}/X11/xorg.conf.d
install -D -m 0755 %{SOURCE30} %{buildroot}%{_bindir}/xserver-sdk-abi-requires
install -D -m 0755 %{SOURCE20} %{buildroot}%{_bindir}/xvfb-run
%global xserver_source_dir %{_datadir}/xorg-x11-server-source
%global inst_srcdir %{buildroot}/%{xserver_source_dir}
mkdir -p %{inst_srcdir}/{Xext,xkb,GL,hw/{xquartz/bundle,xfree86/common}}
mkdir -p %{inst_srcdir}/{hw/dmx/doc,man,doc,hw/dmx/doxygen}
cp {,%{inst_srcdir}/}hw/xquartz/bundle/cpprules.in
cp {,%{inst_srcdir}/}man/Xserver.man
cp {,%{inst_srcdir}/}doc/smartsched
cp {,%{inst_srcdir}/}xserver.ent.in
cp {,%{inst_srcdir}/}hw/xfree86/Xorg.sh.in
cp xkb/README.compiled %{inst_srcdir}/xkb
cp hw/xfree86/xorgconf.cpp %{inst_srcdir}/hw/xfree86
find . -type f -not -path "./%{_vpath_builddir}/*" | egrep '.*\.(c|h|am|ac|inc|m4|h.in|pc.in|man.pre|pl|txt)$' |
xargs tar cf - | (cd %{inst_srcdir} && tar xf -)
find %{inst_srcdir}/hw/xfree86 -name \*.c -delete
find %{buildroot} -type f -name '*.la' -delete
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n xorg-x11-server-common -f %{oreon_filedir}/xorg-x11-server-common.list
%files -n xorg-x11-server-Xorg -f %{oreon_filedir}/xorg-x11-server-Xorg.list
%files -n xorg-x11-server-Xnest -f %{oreon_filedir}/xorg-x11-server-Xnest.list
%files -n xorg-x11-server-Xvfb -f %{oreon_filedir}/xorg-x11-server-Xvfb.list
%files -n xorg-x11-server-Xephyr -f %{oreon_filedir}/xorg-x11-server-Xephyr.list
%files -n xorg-x11-server-devel -f %{oreon_filedir}/xorg-x11-server-devel.list
%files -n xorg-x11-server-source -f %{oreon_filedir}/xorg-x11-server-source.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 21.1.22-1
- Import
