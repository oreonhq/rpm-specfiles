%global source1_hash af006aa9475df5ed02864be5c10dd84877d9debb49dbb0f3680272c4bb8c5c96
%global source0_hash 326d3c583d795bb53ac609d144e7f7fb1499baba7eaec14b8e6cd232ea069532
Name:       xmag
Version:    1.0.8
Release:        5%{?dist}
Summary:        Display a magnified snapshot of an X11 screen
License:    MIT-open-group AND X11
SourceLicense:  FSFAP AND FSFUL AND FSFULLR AND FSFULLRWD AND GPL-2.0-or-later WITH Autoconf-exception-generic AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-3.0-or-later WITH Autoconf-exception-macro AND MIT AND MIT-CMU AND MIT-open-group AND X11
URL:        https://gitlab.freedesktop.org/xorg/app/xmag
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Source1:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz.sig
Source2:    gpgkey-4A193C06D35E7C670FA4EF0BA2FB9E081F2D130E.gpg
Obsoletes:      xorg-x11-apps < 7.7-31
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xt)
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
