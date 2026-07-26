%global source0_hash d5dfdaa7fe65d7105fc0ea4b0d7b7bf6a28b4d39c664e31722000bc9afa61108

%global forgeurl https://git.sr.ht/~emersion/kanshi

Name:           kanshi
Version:        1.9.0
Release:        1%{?dist}
Summary:        Dynamic display configuration for Wayland

# Overall project license: MIT
#
# protocol/wlr-output-management-unstable-v1.xml:
# The file is licensed under HPND-sell-variant; it is processed to C-compilable
# files by the `wayland-scanner` binary during build and doesn't alter the main
# license of the binary.
License:        MIT
URL:            https://gitlab.freedesktop.org/emersion/kanshi
Source0:        %{url}/-/releases/v%{version}/downloads/%{name}-%{version}.tar.gz
Source1:        %{url}/-/releases/v%{version}/downloads/%{name}-%{version}.tar.gz.sig
# 0FDE7BE0E88F5E48: emersion <contact@emersion.fr>
Source2:        https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/gpgkey-0FDE7BE0E88F5E48.gpg
Source3:        %{name}.service

BuildRequires:  gcc
BuildRequires:  gpgverify
BuildRequires:  meson >= 0.59.0
BuildRequires:  systemd-rpm-macros

BuildRequires:  pkgconfig(scdoc) >= 1.9.2
BuildRequires:  pkgconfig(scfg)
BuildRequires:  pkgconfig(vali)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)

Enhances:       sway

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
# install systemd service
install -D -m 0644 -pv %{SOURCE3} %{buildroot}%{_userunitdir}/%{name}.service

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}*
%{_mandir}/man1/%{name}*.*
%{_mandir}/man5/%{name}.*
%{_userunitdir}/%{name}.service

%changelog
%autochangelog
