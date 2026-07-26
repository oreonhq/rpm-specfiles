%global source0_hash a311206a67719b0ec764694d1a827e12cc745600a5ed12549e25e7a8fd87fbc4

Name:           xsecurelock
Version:        1.8.0
Release:        10%{?dist}
Summary:        X11 screen lock utility with security in mind
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/google/xsecurelock

Source0:        https://github.com/google/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

Requires: libXft
BuildRequires: make
BuildRequires: gcc
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xmu)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pam-devel
BuildRequires: pamtester
BuildRequires: pkgconfig(libbsd)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(xrandr)
BuildRequires: httpd-tools
BuildRequires: pandoc
BuildRequires: doxygen
BuildRequires: libXft-devel
BuildRequires: xscreensaver
BuildRequires: mpv

%description
XSecureLock is an X11 screen lock utility designed with the primary goal of
security.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure --with-pam-service-name=system-auth --with-xft --with-xscreensaver=/usr/bin/xscreensaver --with-mpv=/usr/bin/mpv --with-htpasswd=/usr/bin/htpasswd
%make_build

%install
%make_install
rm %{buildroot}%{_pkgdocdir}/LICENSE

%files
%license LICENSE
%doc README.md
%doc CONTRIBUTING
%doc /usr/share/doc/xsecurelock/examples/saver_livestreams
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%{_libexecdir}/%{name}/auth_x11
%{_libexecdir}/%{name}/authproto_pam
%{_libexecdir}/%{name}/authproto_pamtester
%{_libexecdir}/%{name}/authproto_htpasswd
%{_libexecdir}/%{name}/dimmer
%{_libexecdir}/%{name}/pgrp_placeholder
%{_libexecdir}/%{name}/saver_blank
%{_libexecdir}/%{name}/saver_multiplex
%{_libexecdir}/%{name}/until_nonidle
%{_libexecdir}/%{name}/saver_xscreensaver
%{_libexecdir}/%{name}/saver_mpv

%changelog
%autochangelog
