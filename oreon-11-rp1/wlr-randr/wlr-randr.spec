%global source2_hash 42ad6b1bb877e1d8e3dffd101431468573e3678d0a89efff08da8383d6efa16f
%global source0_hash a64b6eb296d1c75af098fa2d229f9aaf3ceae45eeff24056930bd4bc613c6a5e
Name:           wlr-randr
Version:        0.5.0
Release:        3%{?dist}
Summary:        An xrandr clone for wlroots compositors
License:        MIT
URL:            https://gitlab.freedesktop.org/emersion/wlr-randr
Source0:        https://gitlab.freedesktop.org/emersion/%{name}/-/releases/v%{version}/downloads/%{name}-%{version}.tar.gz
Source1:        %{url}/-/releases/v%{version}/downloads/%{name}-%{version}.tar.gz.sig
Source2:        https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/gpgkey-0FDE7BE0E88F5E48.gpg
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)
# /oreon:deps
%description
wlr-randr is an xrandr clone for wlroots compositors

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
