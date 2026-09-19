%global source0_hash 8a3f67b20407a53286a7de1a04dbda12d272234d59ef35e68ecfaf7633d83624

Name:          xlogo
Version:       1.0.7
Release:       4%{?dist}
Summary:       Display the X11 logo

License:       MIT-open-group
URL:           https://www.x.org
Source0:       https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Source1:       https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz.sig
# Upstream does not publish a GPG keyring, so create one for inclusion in
# the source RPM.  First import the public key then export it:
#
# gpg2 --keyserver hkp://keyserver.ubuntu.com --recv-keys CFDF148828C642A7
# gpg2 --export --export-options export-minimal CFDF148828C642A7 > gpgkey-CFDF148828C642A7.gpg
Source2:       gpgkey-CFDF148828C642A7.gpg

BuildRequires: automake
BuildRequires: libtool
BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xmu)
BuildRequires: pkgconfig(xt)
BuildRequires: pkgconfig(xft)
BuildRequires: pkgconfig(xaw7)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xorg-macros) >= 1.8
BuildRequires: gnupg2

Obsoletes:     xorg-x11-apps < 7.7-31

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

%files
%license COPYING
%doc README.md ChangeLog
%{_bindir}/xlogo
%{_mandir}/man1/xlogo.1*
%{_datadir}/X11/app-defaults/XLogo
%{_datadir}/X11/app-defaults/XLogo-color

%changelog
%autochangelog
