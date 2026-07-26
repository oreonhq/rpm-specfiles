%global source0_hash dd13768f35fd8bba9c4920b0f8269f39270e5a3cfed1a34c3b940a492286ece5

Summary:	Desktop Notification Daemon
Name:		notification-daemon

Version:	3.20.0
Release:	25%{?dist}

URL:		https://wiki.gnome.org/Projects/GnomeFlashback
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
Provides:	desktop-notification-daemon

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.19.5
BuildRequires:	pkgconfig(glib-2.0) >= 2.27.0
BuildRequires:	desktop-file-utils
BuildRequires:	intltool

%if 0%{?fedora} < 43
Obsoletes:		notify-daemon
Provides:		notify-daemon
Obsoletes:		notification-daemon-engine-slider < 0.2.0-3
Provides:		notification-daemon-engine-slider = %{version}-%{release}
%endif

Source0:		http://download.gnome.org/sources/notification-daemon/3.20/%{name}-%{version}.tar.xz

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

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%license	COPYING
%doc	AUTHORS
%doc	NEWS

%{_libexecdir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
%autochangelog
