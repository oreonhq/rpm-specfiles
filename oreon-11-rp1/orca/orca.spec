%global source0_hash 8bc3e44bc5b7b66ec7e0cc5c82695c0075661922745d25724f5fc84a25602108
%global tarball_version %(echo %{version} | tr '~' '.')
%global major_version %(echo %{tarball_version} | cut -d "." -f 1)
Name:           orca
Version:        51.0
Release:        1%{?dist}
Summary:        Assistive technology for people with visual impairments
License:        LGPL-2.1-or-later AND CC-BY-SA-3.0
URL:            https://wiki.gnome.org/Projects/Orca
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-%{version}.tar.xz
BuildArch:      noarch
Requires:       python3-brlapi
Requires:       python3-dasbus
Requires:       python3-louis
Requires:       python3-pyatspi
Requires:       python3-speechd
Requires:       speech-dispatcher
Recommends:     python3-psutil
# oreon:deps
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  brlapi-devel
BuildRequires:  brltty
BuildRequires:  gettext
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(atk-bridge-2.0)
BuildRequires:  pkgconfig(atspi-2)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(liblouis)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3-brlapi
BuildRequires:  python3-dasbus
BuildRequires:  python3-devel
BuildRequires:  python3-louis
BuildRequires:  python3-pyatspi
BuildRequires:  python3-speechd
# /oreon:deps
%description
Orca is a screen reader that provides access to the graphical desktop via
user-customizable combinations of speech and/or braille. Orca works with
applications and toolkits that support the assistive technology service
provider interface (AT-SPI), e.g. the GNOME desktop.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/orca-autostart.desktop
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0.7-1
- Prepare for Oreon 11 (RP1)
