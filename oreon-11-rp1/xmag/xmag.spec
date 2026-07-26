%global source0_hash 326d3c583d795bb53ac609d144e7f7fb1499baba7eaec14b8e6cd232ea069532

Name:       xmag
Version:    1.0.8
Release:    5%{?dist}
Summary:    Display a magnified snapshot of an X11 screen
# COPYING:      MIT-open-group AND X11 texts
# CutPaste.c:   MIT-open-group
# CutPaste.h:   X11
# man/xmag.man: MIT-open-group
# RootWin.c:    MIT-open-group
# RootWin.h:    MIT-open-group
# RootWinP.h:   MIT-open-group
# Scale.c:      MIT-open-group
# Scale.h:      MIT-open-group
# ScaleP.h:     MIT-open-group
# xmag.c:       MIT-open-group
## Not in any binary package
# aclocal.m4:   FSFULLR AND FSFULLRWD AND
#               GPL-2.0-or-later WITH Autoconf-exception-generic AND MIT AND
#               GPL-3.0-or-later WITH Autoconf-exception-macro AND MIT-open-group
# compile:      GPL-2.0-or-later WITH Autoconf-exception-generic
# config.guess: GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# config.sub:   GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# configure:    FSFUL
# configure.ac: MIT-CMU
# depcomp:      GPL-2.0-or-later WITH Autoconf-exception-generic
# INSTALL:      FSFAP
# install-sh:   X11
# Makefile.am:  MIT-CMU
# Makefile.in:  FSFULLRWD
# man/Makefile.in:  FSFULLRWD
# missing:      GPL-2.0-or-later WITH Autoconf-exception-generic
License:    MIT-open-group AND X11
SourceLicense:  FSFAP AND FSFUL AND FSFULLR AND FSFULLRWD AND GPL-2.0-or-later WITH Autoconf-exception-generic AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-3.0-or-later WITH Autoconf-exception-macro AND MIT AND MIT-CMU AND MIT-open-group AND X11
URL:        https://gitlab.freedesktop.org/xorg/app/xmag
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Source1:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz.sig
# Retrieved from http://keyserver.ubuntu.com:11371 key server.
Source2:    gpgkey-4A193C06D35E7C670FA4EF0BA2FB9E081F2D130E.gpg
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.22
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(x11)
Obsoletes:      xorg-x11-apps < 7.7-31

%description
xmag displays a magnified snapshot of a portion of an X11 screen.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
rm aclocal.m4 compile config.guess config.sub configure depcomp install-sh \
    Makefile.in man/Makefile.in missing

%build
autoreconf --force --install
%configure --enable-selective-werror --disable-silent-rules --disable-strict-compilation
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog README.md Scale.txt
%{_bindir}/xmag
%{_mandir}/man1/xmag.1*
%{_datadir}/X11/app-defaults/Xmag

%changelog
%autochangelog
