%global source0_hash 44780b7af02c0091be83efb9ccdb201588c1ec96fa382e22a70e681b95328ef2
Name:           x2gokdrive
Version:        0.0.0.3
Release:        5%{?dist}
Summary:        KDrive graphical server backend for X2GoServer
License:        GPL-3.0-or-later
URL:            https://www.x2go.org
Source0:        https://code.x2go.org/releases/source/%{name}/%{name}-%{version}.tar.gz
Source1:        copyright
Source2:        xorg.conf
ExcludeArch:    %{ix86}
%if 0%{?el8}
%endif
%if !(0%{?el8} && "%{_arch}" == "s390x")
%endif
# oreon:deps
BuildRequires:  Xvfb
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  font-util
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  imake
BuildRequires:  libgcrypt-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(audit)
BuildRequires:  pkgconfig(auparse)
BuildRequires:  pkgconfig(bigreqsproto)
BuildRequires:  pkgconfig(compositeproto)
BuildRequires:  pkgconfig(damageproto)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(fixesproto)
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(kbproto)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(presentproto)
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(recordproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(resourceproto)
BuildRequires:  pkgconfig(scrnsaverproto)
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-glx)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xf86dri)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xcb-xv)
BuildRequires:  pkgconfig(xcmiscproto)
BuildRequires:  pkgconfig(xdmcp)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xf86bigfontproto)
BuildRequires:  pkgconfig(xf86dgaproto)
BuildRequires:  pkgconfig(xf86vidmodeproto)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xfont2)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xineramaproto)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xmuu)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xres)
BuildRequires:  pkgconfig(xshmfence)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xv)
BuildRequires:  quilt
BuildRequires:  x2gokdriveclient
BuildRequires:  xauth
BuildRequires:  xkbcomp
BuildRequires:  xorg-x11-server-source
# /oreon:deps
%description
X2Go is a server based computing environment with
   - session resuming
   - low bandwidth support
   - session brokerage support
   - client-side mass storage mounting support
   - client-side printing support
   - audio support
   - authentication by smartcard and USB stick

X2Go KDrive is a KDrive-based Xserver for X2Go. It provides support for
running modern desktop environments like GNOME, KDE Plasma, Cinnamon, etc.
in X2Go Sessions.

The X2Go KDrive graphical backend is not suitable for low bandwidth WAN
connections between X2Go Client and X2Go Server. It is supposed for X2Go
being used on the local area network.

More information about X.Org can be found at:
<URL:https://www.x.org>

More information about X2Go can be found at:
<URL:https://wiki.x2go.org>

%package -n xorg-x11-server-x2gokdrive
Summary:        KDrive graphical server backend for X2GoServer
Requires:       xorg-x11-server-common >= 1.18.4
Requires:       mesa-dri-drivers
Requires:       x2goserver >= 4.1.0.4
%description -n xorg-x11-server-x2gokdrive
X2Go is a server based computing environment with
   - session resuming
   - low bandwidth support
   - session brokerage support
   - client-side mass storage mounting support
   - client-side printing support
   - audio support
   - authentication by smartcard and USB stick

This package is built from the X.org xserver module. X2Go KDrive is a
KDrive-based Xserver for X2Go. It provides support for running modern
desktop environments like GNOME, KDE Plasma, Cinnamon, etc. in X2Go
Sessions.

The X2Go KDrive graphical backend is not suitable for low bandwidth WAN
connections between X2Go Client and X2Go Server. It is supposed for X2Go
being used on the local area network.

More information about X.Org can be found at:
<URL:https://www.x.org>

More information about X2Go can be found at:
<URL:https://wiki.x2go.org>

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
cp -a %SOURCE1 .

# prepare xorg-server build tree
mkdir -p 'BUILD'
cp -av '/usr/share/xorg-x11-server-source/'* 'BUILD/'
# Precaution from:
# https://src.fedoraproject.org/rpms/tigervnc/blob/master/f/tigervnc.spec
find 'BUILD/' -type 'f' -perm '-001' -print0 | while read -r -d '' file; do
  chmod -x "${file}"
done
mkdir -p 'BUILD/hw/kdrive/x2gokdrive/'

# inject x2gokdrive into xorg-server build tree
cp 'Makefile.am' *'.c' *'.h' 'BUILD/hw/kdrive/x2gokdrive/'
cp -r 'man/' 'BUILD/hw/kdrive/x2gokdrive/'

# patch xorg-server build tree, so that it will build x2gokdrive
export XORG_UPSTREAM_VERSION="$(grep 'AC_INIT' 'BUILD/configure.ac' | sed -r 's/^AC_INIT[^,]*, ([^,]+),.*/\1/')"
# Just use the latest version present
[ ! -d "patches.xorg/${XORG_UPSTREAM_VERSION}" ] && cp -a patches.xorg/1.20.13 patches.xorg/${XORG_UPSTREAM_VERSION}
pushd 'BUILD'
QUILT_PATCHES="../patches.xorg/${XORG_UPSTREAM_VERSION}/" quilt push -a
if [ -d "../patches.xorg/${XORG_UPSTREAM_VERSION}/missing" ]; then
  # Hack used to install missing files.
  # This is actually working around problems in the upstream
  # xorg-server-source packages, which will have to be reported upstream.
  cp -av "../patches.xorg/${XORG_UPSTREAM_VERSION}/missing/"* 'BUILD/'
fi

%build

export CFLAGS="$RPM_OPT_FLAGS -fPIC"
export CXXFLAGS="$CFLAGS"
pushd 'BUILD'
rm -f 'configure' 'config.'{sub,guess} 'depcomp' 'install-sh' 'compile' 'ltmain.sh' 'missing' 'ylwrap'
autoreconf -fvi
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro}
%configure \
        --libexecdir='%{_prefix}/lib/xorg' \
        --with-module-dir='%{_prefix}/lib/xorg/modules' \
        --with-serverconfig-path='%{_libexecdir}' \
        --disable-silent-rules \
        --disable-static \
        --disable-devel-docs \
        --disable-docs \
        --without-dtrace \
        --disable-strict-compilation \
        --disable-debug \
        --with-int10=x86emu \
        --with-vendor-name="Fedora Project" \
        --with-builderstring="%{name} %{version} (https://wiki.x2go.org)" \
        --with-xkb-path=%{_datadir}/X11/xkb \
        --with-xkb-output=%{_localstatedir}/lib/xkb \
        --with-shared-memory-dir=/dev/shm \
        --enable-mitshm \
        --enable-xres \
        --disable-xcsecurity \
        --disable-tslib \
        --enable-dbe \
        --disable-xf86bigfont \
        --enable-dpms \
        --disable-xorg \
        --disable-linux-acpi \
        --disable-linux-apm \
        --disable-xquartz \
        --disable-xwin \
        --disable-xnest \
        --disable-xfake \
        --disable-xfbdev \
        --disable-install-setuid \
        --disable-xshmfence \
        --disable-config-hal \
        --disable-config-udev \
        --with-default-font-path="catalogue:%{_sysconfdir}/X11/fontpath.d,built-ins" \
        --enable-composite \
        --enable-record \
        --enable-xv \
        --disable-xvmc \
        --disable-dga \
        --enable-screensaver \
        --disable-xdmcp \
        --disable-xdm-auth-1 \
        --enable-glx \
        --enable-present \
        --enable-xinerama \
        --enable-xf86vidmode \
        --enable-xace \
        --disable-xfree86-utils \
        --disable-suid-wrapper \
        --disable-dmx \
        --disable-xvfb \
        --enable-kdrive \
        --enable-x2gokdrive \
        --disable-xephyr \
        --disable-xwayland \
        --with-sha1=libgcrypt \
        --enable-xcsecurity \
        --disable-dri3 \
        --disable-xselinux \
        --disable-systemd-logind \
        --without-systemd-daemon \
        --disable-dri \
        --disable-dri2 \
        --disable-glamor \
%if !(0%{?el8} && "%{_arch}" == "s390x")
        --enable-libunwind \
%else
        --disable-libunwind \
%endif
        --disable-libdrm \
        --enable-unit-tests \
        CPPFLAGS="${CPPFLAGS} %{?__global_cppflags} -DPRE_RELEASE=0" \
        LDFLAGS='%{__global_ldflags}'
%make_build
popd
%install
pushd 'BUILD'
%make_install
popd
%oreon_autofiles xorg-x11-server-x2gokdrive usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export PATH=%{buildroot}%{_bindir}:$PATH
export QT_DEBUG_PLUGINS=1
xvfb-run -f ~/.Xauthority testscripts/run-x2gokdriveclient-to-x2gokdrive-on-localhost
sleep 5
cat $HOME/.x2go/S-9/session
cat $HOME/.x2go/C-9/session
for pid in $HOME/.x2go/[CS]-9/pid
do
  [ -f $pid ] && kill $(cat $pid)
done
exit 0
%files -f %{oreon_filedir}/main.list
%files -n xorg-x11-server-x2gokdrive -f %{oreon_filedir}/xorg-x11-server-x2gokdrive.list

%changelog

%autochangelog
