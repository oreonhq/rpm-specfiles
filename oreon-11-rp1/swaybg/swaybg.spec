%global source2_hash b5e8dddd0148b4ed074803c85c5226eda1a9bb60d0e7aeeae7a787f7dfbb0245
%global source0_hash a6652a0060a0bea3c3318d9d03b6dddac34f6aeca01b883eef9e58281f5202a1
Name:       swaybg
Version:    1.2.2
Release:        1%{?dist}
Summary:        Wallpaper tool for Wayland compositors
License:    MIT
URL:        https://github.com/swaywm/swaybg
Source0:        https://github.com/swaywm/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:    %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
Source2:    https://keys.openpgp.org/vks/v1/by-fingerprint/34FF9526CFEF0E97A340E2E40FDE7BE0E88F5E48
Conflicts:  sway < 1.1
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  scdoc
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
