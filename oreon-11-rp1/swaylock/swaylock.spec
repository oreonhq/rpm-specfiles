%global source0_hash a15154348fef852fdb224112d137c393c826478b777f63479beb15e8d3812eaf
Name:       swaylock
Version:    1.8.6
Release:        1%{?dist}
Summary:        Screen locker for Wayland
License:    MIT
URL:        https://github.com/swaywm/swaylock
Source0:        https://github.com/swaywm/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:    %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
Source2:    gpgkey-E88F5E48.asc
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  scdoc
# /oreon:deps
%description
swaylock is a screen locking utility for Wayland compositors.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
