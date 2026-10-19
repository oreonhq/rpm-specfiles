%global source0_hash 019186a996096ef4fc356e21577b5673f5baa3a29ac8e3d608b753371c18018d
Name:          zenity
Version:       4.2.2
Release:        1%{?dist}
Summary:        Display dialog boxes from shell scripts
License:       LGPL-2.1-or-later
URL:           https://wiki.gnome.org/Projects/Zenity
Source0:        https://download.gnome.org/sources/%{name}/4.2/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  /usr/bin/help2man
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  mesa-dri-drivers
BuildRequires:  mesa-libEGL
BuildRequires:  meson
BuildRequires:  mutter
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  which
BuildRequires:  xwayland-run
# /oreon:deps
%description
Zenity lets you display Gtk+ dialog boxes from the command line and through
shell scripts. It is similar to gdialog, but is intended to be saner. It comes
from the same family as dialog, Xdialog, and cdialog.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%{shrink:xwfb-run -c mutter -w 10 -- %meson_build}
%install
%meson_install
rm -f %{buildroot}/%{_bindir}/gdialog
%find_lang zenity --with-gnome
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Zenity.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
