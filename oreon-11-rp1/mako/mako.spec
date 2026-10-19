%global source2_hash 42ad6b1bb877e1d8e3dffd101431468573e3678d0a89efff08da8383d6efa16f
%global source0_hash e97eb5bd0dc6a9159019949f48b3db4e8781b56bd6377bd65827e1cb440a7def
Name:       mako
Version:    1.11.0
Release:        1%{?dist}
Summary:        Lightweight Wayland notification daemon
Provides:   desktop-notification-daemon
License:    MIT
URL:        https://github.com/emersion/%{name}
Source0:        https://github.com/emersion/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:    %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
Source2:    https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/gpgkey-0FDE7BE0E88F5E48.gpg
Patch0: add-systemd-service-dbus.patch
Requires:       dbus
Recommends:     jq
%{?systemd_requires}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
mako is a lightweight notification daemon for Wayland compositors that support
the layer-shell protocol.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%meson \
    -Dwerror=false \
    -Dsd-bus-provider=libsystemd \
    -Dbash-completions=true \
    -Dfish-completions=true \
    -Dzsh-completions=true
%meson_build
%install
%meson_install
install -m0644 -Dt %{buildroot}%{_userunitdir}/ contrib/systemd/mako.service
%oreon_autofiles main

%post

%systemd_user_post %{name}.service
%preun

%systemd_user_preun %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
