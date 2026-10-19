%global source0_hash 3ee85e5e2d211eca7bdb8b2fe0e3baf31998829af48198b5fa9bbee2aa0d24be
Name:       oclock
Version:    1.0.6
Release:        1%{?dist}
Summary:        A simple analog clock
License:    MIT
URL:        https://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Source1:    %{name}-%{version}.tar.xz.sig
Source2:        %{name}.gpg
Obsoletes:  xorg-x11-apps < 7.7-31
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
BuildRequires:  xorg-x11-util-macros
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
