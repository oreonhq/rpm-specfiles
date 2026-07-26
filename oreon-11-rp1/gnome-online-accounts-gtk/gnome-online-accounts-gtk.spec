%global source0_hash 1335240713781c7f88d3d0a179cd275d309fd010cbd9d9048518560a75d774ac

Name:           gnome-online-accounts-gtk
Version:        3.50.10
Release:        2%{?dist}
Summary:        GUI Utility for logging into online accounts
License:        GPL-3.0-or-later
URL:            https://github.com/xapp-project/%{name}
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(goa-1.0) >= 3.50
BuildRequires:  pkgconfig(goa-backend-1.0) >= 3.50
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)

Requires:       gnome-online-accounts%{?_isa}

%description
GUI Utility for logging into online accounts for the
purpose of syncing mail, contacts and remote filesystems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/gnome-online-accounts-gtk
%{_datadir}/applications/gnome-online-accounts-gtk.desktop
%{_datadir}/icons/hicolor/scalable/apps/gnome-online-accounts-gtk.svg

%changelog
%autochangelog
