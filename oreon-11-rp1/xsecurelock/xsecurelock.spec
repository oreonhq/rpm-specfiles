%global source0_hash 6e8df4d804e388499e7a9116161a0355034d2ebb61471291383875be515e8025
Name:           xsecurelock
Version:        1.9.0
Release:        1%{?dist}
Summary:        X11 screen lock utility with security in mind
License:        Apache-2.0
URL:            https://github.com/google/xsecurelock
Source0:        https://github.com/google/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Requires: libXft
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  httpd-tools
BuildRequires:  libXft-devel
BuildRequires:  make
BuildRequires:  mpv
BuildRequires:  pam-devel
BuildRequires:  pamtester
BuildRequires:  pandoc
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  xscreensaver
# /oreon:deps
%description
XSecureLock is an X11 screen lock utility designed with the primary goal of
security.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --with-pam-service-name=system-auth --with-xft --with-xscreensaver=/usr/bin/xscreensaver --with-mpv=/usr/bin/mpv --with-htpasswd=/usr/bin/htpasswd
%make_build
%install
%make_install
rm %{buildroot}%{_pkgdocdir}/LICENSE
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
