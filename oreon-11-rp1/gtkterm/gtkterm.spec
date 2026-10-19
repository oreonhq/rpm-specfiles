%global source0_hash 47e39011067ccaa5e965308225d8f80ea4e1793ca884d7f32600fa1fb9ae6628
Name:           gtkterm
Version:        1.9.1
Release:        1%{?dist}
Summary:        Serial port terminal
License:        GPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://github.com/wvdakker/gtkterm
Source0:        https://github.com/wvdakker/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{url}/pull/82.patch
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(vte-2.91)
# /oreon:deps
%description
Simple GUI terminal used to communicate with the serial port.
Similar to minicom or hyperterminal.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
