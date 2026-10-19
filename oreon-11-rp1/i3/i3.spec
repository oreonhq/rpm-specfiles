%global source0_hash 4a742bbe81b9e5ee6057f42a8e3c691d88894e93f1a5d81fe239128512ac05c0
Name:           i3
Version:        4.25.1
Release:        1%{?dist}
Summary:        Improved tiling window manager
License:        BSD-3-Clause
URL:            https://i3wm.org
Source0:        https://%{name}wm.org/downloads/%{name}-%{version}.tar.xz
Source1:        %{URL}/downloads/%{name}-%{version}.tar.xz.asc
Source2:        gpgkey-424E14D703E7C6D43D9D6F364E7160ED4AC8EE1D.gpg
Source3:        %{name}-logo.svg
Source4:        fedora-i3-config
Source5:        fedora-i3-keycodes
Patch0:         0001-Correct-dex-binary-name-dex-dex-autostart.patch
Provides:       i3-gaps = %{version}-%{release}
Obsoletes:      i3-gaps < 4.22-1
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
Recommends:     i3status
Recommends:     i3lock
Recommends:     i3-config
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gnupg2
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

%package        config
Summary:        Upstream configuration for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Recommends:     rxvt-unicode
Conflicts:      %{name}-config-fedora
%description    config
This is the upstream/vanilla configuration file of i3.

%package        config-fedora
RemovePathPostfixes: .fedora
Summary:        Configuration of %{name} for the Fedora i3 Spin
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Recommends:     xfce4-terminal
Requires:       xdg-user-dirs
Requires:       xss-lock
Conflicts:      %{name}-config
%description    config-fedora
This is the configuration file of i3 used for the Fedora i3 Spin.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-devel-doc = %{version}-%{release}
Obsoletes:      %{name}-devel-doc < 4.25
%description    doc
Asciidoc generated documentation for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
Header files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

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
install -Dpm0644 %{SOURCE3} \
        %{buildroot}%{_datadir}/pixmaps/
install -Dpm0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/%{name}/config.fedora
install -Dpm0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/%{name}/config.keycodes.fedora
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/i3.desktop
%ifnarch s390 s390x
%endif
%files -f %{oreon_filedir}/main.list
%files -n i3-config -f %{oreon_filedir}/i3-config.list
%files -n i3-config-fedora -f %{oreon_filedir}/i3-config-fedora.list
%files -n i3-doc -f %{oreon_filedir}/i3-doc.list
%files -n i3-devel -f %{oreon_filedir}/i3-devel.list

%changelog

%autochangelog
