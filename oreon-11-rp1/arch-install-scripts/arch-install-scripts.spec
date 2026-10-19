%global source0_hash 7d506875460ffeda1db8c3cc062f09b31859977177ace7a3b5fdbf98025da5f2
Name:           arch-install-scripts
Version:        31
Release:        1%{?dist}
Summary:        Scripts to bootstrap Arch Linux distribution
License:        GPL-2.0-only
URL:            https://gitlab.archlinux.org/archlinux/arch-install-scripts
%global forgeurl %url
%global tag v%version
%forgemeta
Source0:        https://gitlab.archlinux.org/archlinux/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildArch:      noarch
Requires:       archlinux-keyring
Requires:       pacman
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  m4
BuildRequires:  make
# /oreon:deps
%description
A small suite of scripts aimed at automating some menial tasks when installing
Arch Linux, most notably including actually performing the installation.

To install and launch Arch in a container:
  pacman-key --init
  pacman-key --populate archlinux
  mkdir -p /var/lib/machines/arch
  pacstrap -G -M -i -c /var/lib/machines/arch base
  systemd-nspawn -bD /var/lib/machines/arch

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tag}

%build

%make_build PREFIX=%{_prefix}
%install
%make_install PREFIX=%{_prefix}
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
