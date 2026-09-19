%global source0_hash b7c8495771139f549752db59f8f52f019d10a2db1e4fa361b4e5c5903df06298

# -*-Mode: rpm-spec-mode; -*-

Name:     wob
Version:  0.15.1
Release:  9%{?dist}
Summary:  A lightweight overlay volume/backlight/progress/anything bar for Wayland
License:  ISC
URL:      https://github.com/francma/wob

Source0: %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1: %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz.sig
# francma publishes their public keys on github as
# wget https://keys.openpgp.org/vks/v1/by-fingerprint/5C6DA024DDE27178073EA103F4B432D5D67990E3
# gpg --import ~/tmp/5C6DA024DDE27178073EA103F4B432D5D67990E3.asc
# gpg2 --export --export-options export-minimal 5C6DA024DDE27178073EA103F4B432D5D67990E3 > 5C6DA024DDE27178073EA103F4B432D5D67990E3.gpg
Source2: 5C6DA024DDE27178073EA103F4B432D5D67990E3.gpg

BuildRequires: gcc
BuildRequires: gnupg2
BuildRequires: meson
BuildRequires: pkgconfig(libseccomp)
BuildRequires: scdoc
BuildRequires: libcmocka-devel
BuildRequires: wayland-devel
BuildRequires: wayland-protocols-devel
BuildRequires: inih-devel

Requires: inih

%description
A lightweight overlay volume/backlight/progress/anything bar for
Wayland.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%gpgverify -k 2 -s 1 -d 0
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/%{name}

%doc README.md
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man5/%{name}.ini.5.*

%license LICENSE

%changelog
%autochangelog
