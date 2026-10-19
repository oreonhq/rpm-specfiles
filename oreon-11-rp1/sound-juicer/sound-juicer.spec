%global source0_hash 2ee882744391beb4c6d64a0f6825fb765510b706ec2b704bfb42e42afaae1de6
Name:           sound-juicer
Version:        3.40.0
Release:        1%{?dist}
Summary:        Clean and lean CD ripper
License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Apps/SoundJuicer
Source0:        https://download.gnome.org/sources/%{name}/3.40/%{name}-%{version}.tar.xz
ExcludeArch:    s390 s390x
Requires:       gstreamer1-plugins-good
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gstreamer1-plugins-good
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(libbrasero-media3)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libdiscid)
BuildRequires:  pkgconfig(libmusicbrainz5)
# /oreon:deps
%description
GStreamer-based CD ripping tool. Saves audio CDs to Ogg/vorbis.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
rm $RPM_BUILD_ROOT%{_datadir}/doc/sound-juicer/AUTHORS
rm $RPM_BUILD_ROOT%{_datadir}/doc/sound-juicer/COPYING
rm $RPM_BUILD_ROOT%{_datadir}/doc/sound-juicer/NEWS
rm $RPM_BUILD_ROOT%{_datadir}/doc/sound-juicer/README.md
%find_lang sound-juicer --with-gnome
%oreon_autofiles main

%check

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/org.gnome.SoundJuicer.metainfo.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.SoundJuicer.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
