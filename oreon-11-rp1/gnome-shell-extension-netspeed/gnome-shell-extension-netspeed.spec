%global source0_hash 23c4a0408ada0f0fe530d4b187e6471fdf2b474420d19fae5d19b98bf5e79baa

%global uuid netspeed@hedayaty.gmail.com

Name:           gnome-shell-extension-netspeed
Version:        49
Release:        %autorelease.1
Summary:        A gnome-shell extension to show speed of the internet
BuildArch:      noarch
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/martinkg/NetSpeed
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/gnome-shell-extension-netspeed-49.tar.gz

BuildRequires: gettext
BuildRequires: glib2
BuildRequires: jq
BuildRequires: meson

Requires: gnome-shell >= 3.14.0
# Requires: libappindicator-gtk3

%description
Add an Internet speed indicator to status area.

You can use gnome-tweaks (additional package) or run in terminal:

  $ gnome-extensions enable %uuid

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%build
%meson \
    -Dlocal_install=disabled
%meson_build

%install
%meson_install
%find_lang %{name} --all-name
rm %{buildroot}%{_datadir}/glib-2.0/schemas/gschemas.compiled

%files -f %{name}.lang
%license gpl-2.0.md
%doc CHANGELOG README.md
%{_datadir}/gnome-shell/extensions/%{uuid}/
%{_datadir}/glib-2.0/schemas/*.gschema.xml

%changelog
%autochangelog
