%global source0_hash 3ab47c042bc1c33f00c7e9273ab674665b85ab10592a8e0425589fe7f3eb1a69

Name:           x11vnc
Version:        0.9.17
Release:        3%{?dist}
Summary:        VNC server for the current X11 session
Summary(ru):    VNC-сервер для текущей сессии X11
# COPYING:                  GPL-2.0-or-later text
# misc/Xdummy.in:           GPL-2.0-or-later
# src/cleanup.c:            GPL-2.0-or-later WITH x11vnc-openssl-exception
# src/help.c:               GPL-2.0-or-later WITH x11vnc-openssl-exception AND GPL-2.0-or-later text
# src/help.h:               GPL-2.0-or-later WITH x11vnc-openssl-exception
# src/tkx11vnc.h:           GPL-2.0-or-later
# src/win_utils.c:          GPL-2.0-or-later WITH x11vnc-openssl-exception
# src/xi2_devices.c:        GPL-2.0-or-later
# src/xi2_devices.h:        GPL-2.0-or-later
# src/xkb_bell.h:           GPL-2.0-or-later WITH x11vnc-openssl-exception
## Not in any binary package
# m4/ax_type_socklen_t.m4:  GPL-2.0-or-later WITH Autoconf-exception-macro
## Not used at all
# misc/blockdpy.c:          GPL-2.0-or-later
# misc/connect_switch:      GPL-2.0-or-later
# misc/desktop.cgi:         GPL-2.0-or-later
# misc/deskshot:            GPL-2.0-or-later
# misc/enhanced_tightvnc_viewer/bin/util/ss_vncviewer:  GPL-2.0-or-later
# misc/enhanced_tightvnc_viewer/COPYING:    GPL-2.0-or-later text
# misc/enhanced_tightvnc_viewer/man/man1/ssvnc.1:       GPL-1.0-or-later
# misc/enhanced_tightvnc_viewer/man/man1/ssvncviewer.1: GPL-1.0-or-later
# misc/enhanced_tightvnc_viewer/README:     GPL-1.0-or-later
# misc/enhanced_tightvnc_viewer/src/patches/tight-vncviewer-full.patch:
#                           GPL-2.0-or-later AND GPL-1.0-or-later AND
#                           LGPL-2.0-or-later WITH WxWindows-exception-3.1 AND
#                           BSD-3-Clause
# misc/inet6to4:            GPL-2.0-or-later
# misc/LICENSE:             GPL-2.0-or-later
# misc/qt_tslib_inject.pl:  GPL-2.0-or-later
# misc/turbovnc/apply_turbovnc:     LicenseRef-Fedora-Public-Domain
#                                   This license has been approved
#                                   <https://gitlab.com/fedora/legal/fedora-license-data/-/issues/62>.
# misc/turbovnc/convert:            LicenseRef-Fedora-Public-Domain
# misc/turbovnc/convert_rfbserver:  LicenseRef-Fedora-Public-Domain
# misc/turbovnc/Makefile.am:        LicenseRef-Fedora-Public-Domain
# misc/turbovnc/README:             LicenseRef-Fedora-Public-Domain
# misc/turbovnc/tight.c:            GPL-2.0-or-later
# misc/turbovnc/turbojpeg.h:        LGPL-2.0-or-later WITH WxWindows-exception-3.1
# misc/turbovnc/undo_turbovnc:      LicenseRef-Fedora-Public-Domain
# misc/uinput.pl:           GPL-2.0-or-later
# misc/ultravnc_repeater.pl:    GPL-2.0-or-later
# misc/Xdummy.c:            GPL-2.0-or-later WITH x11vnc-openssl-exception
# src/nox11.h:              MIT-open-group
# tkx11vnc:     GPL-2.0-or-later
License:        GPL-2.0-or-later AND GPL-2.0-or-later WITH x11vnc-openssl-exception
SourceLicense:  %{license} AND GPL-2.0-or-later WITH Autoconf-exception-macro AND LGPL-2.0-or-later WITH WxWindows-exception-3.1 AND BSD-3-Clause AND LicenseRef-Fedora-Public-Domain AND LGPL-2.0-or-later WITH WxWindows-exception-3.1 AND MIT-open-group
URL:            https://github.com/LibVNC/x11vnc
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Enforce system crypto policy
# <https://fedoraproject.org/wiki/Packaging:CryptoPolicies#C.2FC.2B.2B_applications>
Patch0:         x11vnc-0.9.16-Respect-a-system-crypto-policy.patch
# Normalize changlog encoding
Patch1:         x11vnc-0.9.16-Convert-a-changelog-to-UTF-8.patch

BuildRequires:  autoconf
BuildRequires:  automake
# for autogen.sh script
BuildRequires:  bash
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXext-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXtst-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(avahi-client) >= 0.6.4
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(inputproto) >= 1.9.99.9
BuildRequires:  pkgconfig(libvncclient) >= 0.9.8
BuildRequires:  pkgconfig(libvncserver) >= 0.9.8
BuildRequires:  pkgconfig(xi) >= 1.2.99
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  sed
# Tests:
BuildRequires:  desktop-file-utils
# /usr/bin/wish is executed in do_gui() in src/gui.c.
Requires:       tk
# Default X11 server for "x11vnc --create" is Xvfb
Requires:       Xvfb
# Java viewers now are available on
# https://github.com/LibVNC/libvncserver/tree/master/webclients/java-applet
Obsoletes:      x11vnc-javaviewers < 0.9.14-14

%description
What WinVNC is to Windows x11vnc is to X Window System, i.e. a server which
serves the current X Window System desktop via RFB (VNC) protocol to the user.

Based on the ideas of x0rfbserver and on LibVNCServer it has evolved into
a versatile and productive while still easy to use program.

%description -l ru
Это подобно VNC-серверу под Windows - VNC-сервер, который предоставляет доступ
к текущей X-сессии пользователя по протоколу (VNC).  Таким образом, Вы всегда
можете вернуться к работе удаленно, даже если сессия была стандартно запущена
локально. Более того, доступ к Логин- менеджеру также может быть осуществлен
(GDM, KDM, XDM и т.п.)

Базируется на идее x0rfbserver и LibVNCServer x11vnc эволюционировал в гибкий
и производительный инструмент, который, однако, остаётся прост
в использовании.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%build
autoreconf -fi
%configure \
    --with-avahi \
    --with-colormultipointer \
    --with-crypto \
    --with-dpms \
    --with-fbdev \
    --without-fbpm \
    --without-macosx-native \
    --with-ssl \
    --with-uinput \
    --with-x \
    --without-xcomposite \
    --with-xdamage \
    --with-xfixes \
    --with-xinerama \
    --with-xkeyboard \
    --with-xrandr \
    --with-xrecord \
    --without-xtrap
%make_build

%install
%make_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/x11vnc.desktop

%files
%license COPYING
%doc ChangeLog doc/* NEWS README
%{_bindir}/x11vnc
%{_bindir}/Xdummy
%{_datadir}/applications/x11vnc.desktop
%{_mandir}/man1/x11vnc.1*

%changelog
%autochangelog
