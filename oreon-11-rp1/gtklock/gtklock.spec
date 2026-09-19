%global source0_hash db20bf27bd5dd01901ea1753c89c170777dd7cf8fca19130cf90f5f4e3fb9633

Name: gtklock
Version: 4.0.0
Release: %autorelease
Summary: Lock screen based on gtkgreet

License: GPL-3.0-or-later
URL: https://github.com/jovanlanik/gtklock
Source: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires: pkgconfig(gtk-session-lock-0) >= 0.2.0
BuildRequires: pkgconfig(pam)
BuildRequires: gcc
BuildRequires: meson
BuildRequires: scdoc

%description
%{name} is a lock screen based on gtkgreet. It uses the
ext-session-lock Wayland protocol. Works on sway and other
wlroots-based compositors.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%meson -Dman-pages=enabled
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license LICENSE
%{_sysconfdir}/pam.d/%{name}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
