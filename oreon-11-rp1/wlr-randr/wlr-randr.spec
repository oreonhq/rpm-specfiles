%global source0_hash a64b6eb296d1c75af098fa2d229f9aaf3ceae45eeff24056930bd4bc613c6a5e

Name:           wlr-randr
Version:        0.5.0
Release:        3%{?dist}
Summary:        An xrandr clone for wlroots compositors

# Overall project license: MIT
#
# protocol/wlr-output-management-unstable-v1.xml:
# The file is licensed under HPND-sell-variant; it is processed to C-compilable
# files by the `wayland-scanner` binary during build and doesn't alter the main
# license of the binary.
License:        MIT
URL:            https://gitlab.freedesktop.org/emersion/wlr-randr
Source0:        %{url}/-/releases/v%{version}/downloads/%{name}-%{version}.tar.gz
Source1:        %{url}/-/releases/v%{version}/downloads/%{name}-%{version}.tar.gz.sig
# 0FDE7BE0E88F5E48: emersion <contact@emersion.fr>
Source2:        https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/gpgkey-0FDE7BE0E88F5E48.gpg

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)

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

%files
%license LICENSE
%doc README.md
%{_bindir}/wlr-randr
%{_mandir}/man1/wlr-randr.1*

%changelog
%autochangelog
