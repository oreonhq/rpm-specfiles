%global source0_hash d7cb6449f66e3e2312925a0ebec9d3d75378ff5bd021f4e9d041b06e391cc3b8
%global uuid netspeed@hedayaty.gmail.com
Name:           gnome-shell-extension-netspeed
Version:        49
Release:        1%{?dist}
Summary:        A gnome-shell extension to show speed of the internet
BuildArch:      noarch
License:        GPL-3.0-or-later
URL:            https://github.com/martinkg/NetSpeed
Source0:        https://github.com/martinkg/NetSpeed/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires: gnome-shell >= 3.14.0
# oreon:deps
BuildRequires:  gettext
BuildRequires:  glib2
BuildRequires:  jq
BuildRequires:  meson
# /oreon:deps
%description
Add an Internet speed indicator to status area.

You can use gnome-tweaks (additional package) or run in terminal:

  $ gnome-extensions enable %uuid

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%meson \
    -Dlocal_install=disabled
%meson_build
%install
%meson_install
%find_lang %{name} --all-name
rm %{buildroot}%{_datadir}/glib-2.0/schemas/gschemas.compiled
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
