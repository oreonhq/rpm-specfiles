%global source2_hash 42ad6b1bb877e1d8e3dffd101431468573e3678d0a89efff08da8383d6efa16f
%global source0_hash d5dfdaa7fe65d7105fc0ea4b0d7b7bf6a28b4d39c664e31722000bc9afa61108
%global forgeurl https://git.sr.ht/~emersion/kanshi
Name:           kanshi
Version:        1.9.0
Release:        1%{?dist}
Summary:        Dynamic display configuration for Wayland
License:        MIT
URL:            https://gitlab.freedesktop.org/emersion/kanshi
Source0:        https://gitlab.freedesktop.org/emersion/%{name}/-/releases/v%{version}/downloads/%{name}-%{version}.tar.gz
Source1:        %{url}/-/releases/v%{version}/downloads/%{name}-%{version}.tar.gz.sig
Source2:        https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/gpgkey-0FDE7BE0E88F5E48.gpg
Source3:        %{name}.service
Enhances:       sway
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gpgverify
BuildRequires:  meson
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(scfg)
BuildRequires:  pkgconfig(vali)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
kanshi allows you to define output profiles that are automatically enabled
and disabled on hotplug. For instance, this can be used to turn a laptop's
internal screen off when docked.

This is a Wayland equivalent for tools like autorandr. kanshi can be used
on Wayland compositors supporting the wlr-output-management protocol.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%meson
%meson_build
%install
%meson_install
install -D -m 0644 -pv %{SOURCE3} %{buildroot}%{_userunitdir}/%{name}.service
%oreon_autofiles main

%post

%systemd_user_post %{name}.service
%preun

%systemd_user_preun %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
