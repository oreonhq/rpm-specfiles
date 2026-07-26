%global source0_hash 3ee85e5e2d211eca7bdb8b2fe0e3baf31998829af48198b5fa9bbee2aa0d24be

Name:       oclock
Version:    1.0.6
Release:    %autorelease
Summary:    A simple analog clock
License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Source1:    %{name}-%{version}.tar.xz.sig
# Keyring copied on 2023-02-26 from: xfontsel.gpg
Source2:        %{name}.gpg
BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  xorg-x11-util-macros
BuildRequires:  gnupg2

Obsoletes:  xorg-x11-apps < 7.7-31

%description
oclock is a simple analog clock using the SHAPE extension to make
a round (possibly transparent) window.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
autoreconf -v --install
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/X11/app-defaults/Clock-color

%changelog
%autochangelog
