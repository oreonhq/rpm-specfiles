%global source0_hash aaaca02d36e54ec6ecf457dc266251946d895ac91521fbabb3470c3c09b3753c

# -*-Mode: rpm-spec -*-

%global nvnc_version 0.9.0

Name:     wayvnc
Version:  0.9.1
Release:  4%{?dist}
Summary:  A VNC server for wlroots based Wayland compositors
License:  ISC
URL:      https://github.com/any1/wayvnc
Source:   %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: meson
BuildRequires: pkgconfig(aml) >= 0.2.2
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(neatvnc) >= %{nvnc_version}
BuildRequires: pam-devel
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(xkbcommon) >= 1.0.0
BuildRequires: pkgconfig(jansson)
BuildRequires: pkgconfig(aml) >= 0.3.0
BuildRequires: scdoc

Requires: (sway >= 1.6 if sway)
Requires: aml >= 0.3.0
Requires: neatvnc >= %{nvnc_version}

%description

This is a VNC server for wlroots based Wayland compositors. It
attaches to a running Wayland session, creates virtual input devices
and exposes a single display via the RFB protocol. The Wayland session
may be a headless one, so it is also possible to run wayvnc without a
physical display attached.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%meson

%meson_build

%install
%meson_install

%files
%{_bindir}/%{name}
%{_bindir}/%{name}ctl

%doc README.md FAQ.md
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}ctl.1.*

%license COPYING

%changelog
%autochangelog
