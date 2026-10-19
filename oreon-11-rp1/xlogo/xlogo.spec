%global source1_hash 3a3a96d0490462c27b5a244e271f61f874033913b20c2d87914fda1f0b9e5a62
%global source0_hash 8a3f67b20407a53286a7de1a04dbda12d272234d59ef35e68ecfaf7633d83624
Name:          xlogo
Version:       1.0.7
Release:        4%{?dist}
Summary:        Display the X11 logo
License:       MIT-open-group
URL:           https://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Source1:       https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz.sig
Source2:       gpgkey-CFDF148828C642A7.gpg
Obsoletes:     xorg-x11-apps < 7.7-31
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xt)
# /oreon:deps
%description
xlogo displays a magnified snapshot of a portion of an X11 screen.

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
