%global source0_hash 98f9f69e53a11c354a6637ea5c3d7699ceb5c5b1f8ad6f0a14d9931e5a10d079

Name:       xgamma
Version:    1.0.8
Release:    2%{?dist}
Summary:    X utility to query and alter the gamma correction of a monitor
# COPYING:      X11 AND HPND-sell-variant
# man/xgamma.man:   X11 without the permision grant, probably a copy-and-paste
#                   mistake
#                   <https://gitlab.freedesktop.org/xorg/app/xgamma/-/issues/2>
# xgamma.c:     X11
## Not in any binary package
# configure.ac: HPND-sell-variant
# INSTALL:      FSFAP
# Makefile.am:  HPND-sell-variant
# meson.build:  MIT
## Unbundled
# aclocal.m4:   FSFULLRWD AND FSFULLR AND
#               GPL-2.0-or-later WITH Autoconf-exception-generic AND
#               GPL-3.0-or-later WITH Autoconf-exception-macro AND X11
# compile:      GPL-2.0-ro-later WITH Autoconf-exception-generic
# config.guess: GPL-3.0-or-later WITH Autoconf-exception-generic
# config.sub:   GPL-3.0-or-later WITH Autoconf-exception-generic
# configure:    FSFUL
# depcomp:      GPL-2.0-or-later WITH Autoconf-exception-generic
# install-sh:   X11 AND LicenseRef-Fedora-Public-Domain
# Makefile.in:  FSFULLRWD AND HPND-sell-variant
# man/Makefile.in:  FSFULLRWD
# missing:      GPL-2.0-or-later WITH Autoconf-exception-generic
License:    X11 AND HPND-sell-variant
URL:        https://www.x.org/
Source0:    %{url}releases/individual/app/%{name}-%{version}.tar.xz
Source1:    %{url}releases/individual/app/%{name}-%{version}.tar.xz.sig
# Key imported from hkp://keyserver.ubuntu.com server and verified using the
# previous 4A193C06D35E7C670FA4EF0BA2FB9E081F2D130E key.
Source2:    gpgkey-3AB285232C46AE43D8E192F4DAB0F78EA6E7E2D2.gpg
BuildRequires:  autoconf >= 2.60
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17
# xorg-x11-server-utils-7.7-39.fc35 splitted into many packages
Obsoletes:      xorg-x11-server-utils < 7.7-40

%description
xgamma allows X users to query and alter the gamma correction of a
monitor via the X video mode extension (XFree86-VidModeExtension).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup
rm aclocal.m4 compile config.guess config.sub configure depcomp install-sh \
     Makefile.in man/Makefile.in missing

%build
autoreconf -v --force --install
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
