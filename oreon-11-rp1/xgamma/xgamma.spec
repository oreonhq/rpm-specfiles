%global source0_hash 98f9f69e53a11c354a6637ea5c3d7699ceb5c5b1f8ad6f0a14d9931e5a10d079
Name:       xgamma
Version:    1.0.8
Release:        2%{?dist}
Summary:        X utility to query and alter the gamma correction of a monitor
License:    X11 AND HPND-sell-variant
URL:        https://www.x.org/
Source0:        https://www.x.org/releases/individual/app/%{name}-%{version}.tar.xz
Source1:    %{url}releases/individual/app/%{name}-%{version}.tar.xz.sig
Source2:    gpgkey-3AB285232C46AE43D8E192F4DAB0F78EA6E7E2D2.gpg
Obsoletes:      xorg-x11-server-utils < 7.7-40
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xxf86vm)
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
