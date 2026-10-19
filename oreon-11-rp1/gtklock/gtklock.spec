%global source0_hash db20bf27bd5dd01901ea1753c89c170777dd7cf8fca19130cf90f5f4e3fb9633
Name: gtklock
Version: 4.0.0
Release:        1%{?dist}
Summary:        Lock screen based on gtkgreet
License: GPL-3.0-or-later
URL: https://github.com/jovanlanik/gtklock
Source0:        https://github.com/jovanlanik/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-session-lock-0)
BuildRequires:  pkgconfig(pam)
BuildRequires:  scdoc
# /oreon:deps
%description
%{name} is a lock screen based on gtkgreet. It uses the
ext-session-lock Wayland protocol. Works on sway and other
wlroots-based compositors.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dman-pages=enabled
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
