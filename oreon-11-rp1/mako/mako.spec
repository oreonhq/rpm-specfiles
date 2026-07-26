%global source0_hash a72543f7b92568a0c3c45a5c0e3487ced65c18003eecd9b7d017a6464e7cef82

Name:       mako
Version:    1.10.0
Release:    3%{?dist}
Summary:    Lightweight Wayland notification daemon
Provides:   desktop-notification-daemon

License:    MIT
URL:        https://github.com/emersion/%{name}
Source0:    %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:    %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
# 0FDE7BE0E88F5E48: emersion <contact@emersion.fr>
Source2:    https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/gpgkey-0FDE7BE0E88F5E48.gpg

Patch0: add-systemd-service-dbus.patch

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson >= 0.60.0
BuildRequires:  systemd-rpm-macros
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
BuildRequires:  pkgconfig(wayland-protocols) >= 1.32
BuildRequires:  pkgconfig(wayland-scanner)

Requires:       dbus
Recommends:     jq
%{?systemd_requires}

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

# Install dbus-activated systemd unit
install -m0644 -Dt %{buildroot}%{_userunitdir}/ contrib/systemd/mako.service

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%files
%license LICENSE
%doc README.md
%{_bindir}/mako
%{_bindir}/makoctl
%{_mandir}/man1/mako.1*
%{_mandir}/man5/mako.5*
%{_mandir}/man1/makoctl.1*
%{_userunitdir}/%{name}.service
%{_datadir}/dbus-1/services/fr.emersion.mako.service
%{bash_completions_dir}/mako*
%{fish_completions_dir}/mako*.fish
%{zsh_completions_dir}/_mako*

%changelog
%autochangelog
