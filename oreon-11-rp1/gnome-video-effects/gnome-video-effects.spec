%global source0_hash d7aeaeb46b3f5a832fb2e0d90b42bf8c6160202ca52ac9add17afce192e3c8a8
Name:           gnome-video-effects
Version:        0.6.0
Release:        9%{?dist}
Summary:        Collection of GStreamer video effects
License:        GPL-2.0-only
URL:            https://wiki.gnome.org/Projects/GnomeVideoEffects
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.6/%{name}-%{version}.tar.xz
Buildarch:      noarch
# oreon:deps
BuildRequires:  gettext
BuildRequires:  meson
# /oreon:deps
%description
A collection of GStreamer effects to be used in different GNOME Modules.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.0-9
- Prepare for Oreon 11 (RP1)
