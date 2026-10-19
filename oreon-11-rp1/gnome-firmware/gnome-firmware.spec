%global source0_hash 3d52626d2a4fb19a11e8d07cb0cc07352751a9d6d4aacc2697be44cf4334ff35
%global app_id org.gnome.Firmware
Name:           gnome-firmware
Version:        49.0
Release:        1%{?dist}
Summary:        Install firmware on devices
License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/World/gnome-firmware
Source0:        https://gitlab.gnome.org/World/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  appstream
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(fwupd)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(xmlb)
BuildRequires:  python3
BuildRequires:  systemd-devel
# /oreon:deps
%description
This application can:

- Upgrade, downgrade and reinstall firmware on devices supported by fwupd.
- Unlock locked fwupd devices
- Verify firmware on supported devices
- Display all releases for a fwupd device

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n gnome-firmware-%{version}

%conf
%meson -Dconsolekit=true -Dsystemd=true -Dman=true

%build

%meson_build
%install
%meson_install
%find_lang gnome-firmware --with-gnome
%{python3} <<'EOF'
man = "%{buildroot}%{_mandir}/man1/gnome-firmware.1"
with open(man, "rb") as bad:
    text = bad.read()
text = text.replace(b"\xe2\x5c\x26\x2e\xa6", rb"\[u2026]")
with open(man, "wb") as good:
    good.write(text)
EOF
%oreon_autofiles main

%check

desktop-file-validate '%{buildroot}%{_datadir}/applications/%{app_id}.desktop'
appstream-util validate-relax --nonet \
    '%{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml'
appstreamcli validate --no-net --explain \
    '%{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
