%global source0_hash 0c844eb5c9524f924495bd4145e5db575096de36f3ec87fb37e4c1ed6eacb897
%global alt_pkg_name swaync
Name:       SwayNotificationCenter
Version:    0.12.6
Release:        1%{?dist}
Summary:        Simple notification daemon with GTK GUI for SwayWM
License:    GPL-3.0-only
URL:        https://github.com/ErikReider/SwayNotificationCenter
Source0:        https://github.com/ErikReider/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       gvfs
Requires:       libnotify
Requires:       dbus
Requires:       dbus-common
Provides:   desktop-notification-daemon
Provides:   sway-notification-center = %{version}-%{release}
Provides:   %{alt_pkg_name} = %{version}-%{release}
# oreon:deps
BuildRequires:  blueprint-compiler
BuildRequires:  meson
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(fish)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk4-layer-shell-0)
BuildRequires:  pkgconfig(gtk4-wayland)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  sassc
BuildRequires:  scdoc
BuildRequires:  vala
# /oreon:deps
%description
%{summary}.

%package bash-completion
BuildArch:      noarch
Summary:        Bash completion files for %{name}
Provides:       %{alt_pkg_name}-bash-completion = %{version}-%{release}
Supplements:    (%{name} and bash-completion)
Requires:       bash-completion
Requires:       %{name} = %{version}-%{release}
%description bash-completion
This package installs Bash completion files for %{name}

%package zsh-completion
BuildArch:      noarch
Summary:        Zsh completion files for %{name}
Provides:       %{alt_pkg_name}-zsh-completion = %{version}-%{release}
Supplements:    (%{name} and zsh)
Requires:       zsh
Requires:       %{name} = %{version}-%{release}
%description zsh-completion
This package installs Zsh completion files for %{name}

%package fish-completion
BuildArch:      noarch
Summary:        Fish completion files for %{name}
Provides:       %{alt_pkg_name}-fish-completion = %{version}-%{release}
Supplements:    (%{name} and fish)
Requires:       fish
Requires:       %{name} = %{version}-%{release}
%description fish-completion
This package installs Fish completion files for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles SwayNotificationCenter-bash-completion usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles SwayNotificationCenter-zsh-completion usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles SwayNotificationCenter-fish-completion usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_user_post swaync.service
%preun

%systemd_user_preun swaync.service
%files -f %{oreon_filedir}/main.list
%files -n SwayNotificationCenter-bash-completion -f %{oreon_filedir}/SwayNotificationCenter-bash-completion.list
%files -n SwayNotificationCenter-zsh-completion -f %{oreon_filedir}/SwayNotificationCenter-zsh-completion.list
%files -n SwayNotificationCenter-fish-completion -f %{oreon_filedir}/SwayNotificationCenter-fish-completion.list

%changelog

%autochangelog
