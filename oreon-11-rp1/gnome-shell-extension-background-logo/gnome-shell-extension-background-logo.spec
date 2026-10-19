%global source0_hash 7d677de67fc633416a2705f0b05344eeb6b4e882d613c6e3cbc6b16880c98115
%global tarball_version %(echo %{version} | tr '~' '.')
%global shell_version %%(cut -d "~" -f 1 <<<%{version})
Name:           gnome-shell-extension-background-logo
Version:        50.0
Release:        1%{?dist}
Summary:        Background logo extension for GNOME Shell
License:        GPL-2.0-or-later
URL:            https://forge.fedoraproject.org/workstation/background-logo-extension
Source0:        https://forge.fedoraproject.org/workstation/background-logo-extension/archive/50.beta.tar.gz#/background-logo-extension-%{version}.tar.gz
BuildArch:      noarch
Requires:       gnome-shell(api) = %{shell_version}
Requires:       system-logos
# oreon:deps
BuildRequires:  git
BuildRequires:  glib2-devel
BuildRequires:  meson
# /oreon:deps
%description
Show your pride! Display the Fedora logo (or any other graphic) in the corner of your desktop.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n background-logo-extension

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
