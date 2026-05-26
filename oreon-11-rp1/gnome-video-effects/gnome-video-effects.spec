Name:           gnome-video-effects
Version:        0.6.0
Release:        9%{?dist}
Summary:        Collection of GStreamer video effects

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://wiki.gnome.org/Projects/GnomeVideoEffects
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.6/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 d7aeaeb46b3f5a832fb2e0d90b42bf8c6160202ca52ac9add17afce192e3c8a8
%global source0_file gnome-video-effects-0.6.0.tar.xz
# oreon url source checksums end
Buildarch:      noarch

BuildRequires:  gettext
BuildRequires:  meson

%if 0%{?fedora}
Requires:       frei0r-plugins
%endif

%description
A collection of GStreamer effects to be used in different GNOME Modules.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/gnome-video-effects-0.6.0.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d7aeaeb46b3f5a832fb2e0d90b42bf8c6160202ca52ac9add17afce192e3c8a8" || { echo "oreon: Source0 SHA256 mismatch for gnome-video-effects-0.6.0.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q


%build
%meson
%meson_build


%install
%meson_install


%files
%doc AUTHORS NEWS README
%license COPYING
%{_datadir}/pkgconfig/gnome-video-effects.pc
%{_datadir}/gnome-video-effects


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.0-9
- Prepare for Oreon 11 (RP1)
