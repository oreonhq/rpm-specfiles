%global source0_hash dd13768f35fd8bba9c4920b0f8269f39270e5a3cfed1a34c3b940a492286ece5
Summary:        Desktop Notification Daemon
Name:		notification-daemon
Version:	3.20.0
Release:        1%{?dist}
URL:		https://wiki.gnome.org/Projects/GnomeFlashback
License:	GPL-2.0-or-later
Provides:	desktop-notification-daemon
Source0:        http://download.gnome.org/sources/notification-daemon/3.20/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
# /oreon:deps
%description
notification-daemon is the server implementation of the freedesktop.org
desktop notification specification. Notifications can be used to inform
the user about an event or display some form of information without getting
in the user's way.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --disable-static
%make_build
%install
%make_install
%find_lang %{name}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
