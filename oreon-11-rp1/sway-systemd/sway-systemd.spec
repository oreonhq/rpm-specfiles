%global source0_hash 3ce12188a91bc704019c87dd8b5eda01b387e904468c69b36468992c2d8ab347
Name:           sway-systemd
Version:        0.4.1
Release:        1%{?dist}
Summary:        Systemd integration for Sway session
License:        MIT
URL:            https://github.com/alebastr/sway-systemd
Source0:        https://github.com/alebastr/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       python3dist(dbus-next)
Requires:       python3dist(i3ipc)
Requires:       python3dist(psutil)
Requires:       python3dist(python-xlib)
Requires:       python3dist(tenacity)
Requires:       sway
Requires:       systemd
Recommends:     /usr/bin/dbus-update-activation-environment
# oreon:deps
BuildRequires:  meson
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
%{summary}.

The goal of this project is to provide a minimal set of configuration files
and scripts required for running Sway in a systemd environment.

This includes several areas of integration:
 - Propagate required variables to the systemd user session environment.
 - Define sway-session.target for starting user services.
 - Place GUI applications into a systemd scopes for systemd-oomd compatibility.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson \
    -Dautoload-configs='cgroups'
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
