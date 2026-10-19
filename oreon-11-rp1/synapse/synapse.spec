%global source0_hash 324c22d56415690979f23aae78cf080315a6defc506afd3e6ac14bb2ec4cddbc
Name:		synapse
Version:	0.2.99.4
Release:        1%{?dist}
Summary:        A semantic launcher written in Vala
License:	LGPL-2.0-or-later AND GPL-2.0-or-later AND GPL-3.0-or-later
URL:		https://launchpad.net/synapse-project
Source0:        https://launchpad.net/synapse-project/0.3/%{version}/+download/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  /usr/bin/valac
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(keybinder-3.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(rest-0.7)
BuildRequires:  pkgconfig(zeitgeist-2.0)
# /oreon:deps
%description
Synapse is a semantic launcher written in Vala that you can use to start
applications as well as find and access relevant documents and files by making
use of the Zeitgeist engine.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --disable-static --enable-zeitgeist=yes --disable-silent-rules
%make_build
%install
%make_install
%find_lang %{name}
desktop-file-install \
  --delete-original \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/synapse.desktop
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/synapse.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
