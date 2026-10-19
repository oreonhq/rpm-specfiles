%global source0_hash 78ff018757c7b22137cf5d3526ef5e9388bc0cdead1f00daf2c898e2e274553f
Name:           xfontsel
Version:        1.1.2
Release:        1%{?dist}
Summary:        Tool to list X11 core protocol fonts
License:        X11
SourceLicense:  %{shrink:
                %{license} AND
                FSFAP-no-warranty-disclaimer AND
                FSFUL AND
                FSFULLR AND
                GPL-2.0-or-later WITH Autoconf-exception-generic AND
                GPL-3.0-or-later WITH Autoconf-exception-generic AND
                HPND-sell-variant
                }
URL:            https://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Source1:        %{url}/pub/individual/app/xfontsel-%{version}.tar.xz.sig
Source2:        xfontsel.gpg
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gpgverify
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xt)
# /oreon:deps
%description
The xfontsel application provides a simple way to display the X11 core protocol
fonts known to your X server, examine samples of each, and retrieve the X
Logical Font Description (“XLFD”) full name for a font.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%conf
autoreconf --force --install --verbose
%configure

%build

%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
