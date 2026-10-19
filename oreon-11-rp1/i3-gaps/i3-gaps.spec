%global source0_hash b85f2c58b89d40b330b7f7362bf5c9e63579f705d0f7f87a69aa1bac43ffdfb1
Name:           i3-gaps
Version:        4.21.1
Release:        1%{?dist}
Summary:        i3 with more features
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/Airblader/i3
Source0:        https://github.com/Airblader/i3/releases/download/%{version}/i3-%{version}.tar.xz
Source1:        i3-logo.svg
%ifnarch s390 s390x
%endif
Requires:       xorg-x11-fonts-misc
Recommends:     dex-autostart
Recommends:     xss-lock
Recommends:     network-manager-applet
Recommends:     pulseaudio-utils
Recommends:     dmenu
Requires:       perl(AnyEvent::I3) >= 0.12
Requires:       (i3-config or i3-config-fedora)
Conflicts:      i3
Recommends:     i3status
Recommends:     i3lock
Recommends:     i3-config
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libev-devel
BuildRequires:  meson
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(AnyEvent::Handle)
BuildRequires:  perl(AnyEvent::I3)
BuildRequires:  perl(AnyEvent::Util)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl-generators
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xinerama)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xcb-xrm)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(yajl)
BuildRequires:  xmlto
BuildRequires:  xorg-x11-drv-dummy
# /oreon:deps
%description
Key features of i3 are correct implementation of XrandR, horizontal and vertical
columns (think of a table) in tiling. Also, special focus is on writing clean,
readable and well documented code. i3 uses xcb for asynchronous communication
with X11, and has several measures to be very fast.

Please be aware that i3 is primarily targeted at advanced users and developers.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description    doc
Asciidoc generated documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n i3-%{version}

# Drop /usr/bin/env lines in those which will be installed to %%_bindir.
find . -maxdepth 1 -type f -name "i3*" -exec sed -i -e '1s;^#!/usr/bin/env perl;#!/usr/bin/perl;' {} + -print

%build

%meson
%meson_build
%install
%meson_install
mkdir -p %{buildroot}%{_mandir}/man1/
install -Dpm0644 man/*.1 \
        %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}%{_datadir}/pixmaps/
install -Dpm0644 %{SOURCE1} \
        %{buildroot}%{_datadir}/pixmaps/
rm -rf %{buildroot}%{_includedir}
rm -rf %{buildroot}%{_sysconfdir}/i3/config{,.keycodes}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/i3.desktop
%ifnarch s390 s390x
%endif
%files -f %{oreon_filedir}/main.list
%files -n i3-gaps-doc -f %{oreon_filedir}/i3-gaps-doc.list

%changelog

%autochangelog
