%global source0_hash fc51ee92a705e3c5979dff1655f7496effb68b98f1ada0547e8cbbc033b67dd5
Name:    easytag
Version: 2.4.3
Release:        1%{?dist}
Summary:        Tag editor for MP3, Ogg, FLAC and other music files
License: GPL-2.0-or-later
URL:     https://wiki.gnome.org/Apps/EasyTAG
Source0:        https://download.gnome.org/sources/%{name}/2.4/%{name}-%{version}.tar.xz
Patch:   03_port-to-taglib-2.patch
Patch:   04_taglib-2-further-fix.patch
Recommends:    yelp
Obsoletes:     easytag-nautilus < 2.4.3-16
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  id3lib-devel
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  libappstream-glib-devel
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(id3tag)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(wavpack)
BuildRequires:  yelp-tools
# /oreon:deps
%description
EasyTAG is a utility for viewing, editing and writing the tags of MP4, MP3,
MP2, FLAC, Ogg Opus, Ogg Speex, Ogg Vorbis, MusePack and Monkey's Audio files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%set_build_flags
autoreconf -fiv
CFLAGS="$CFLAGS -std=gnu11"
%configure --disable-appdata-validate
make V=1 %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} INSTALL="install -p" install
find %{buildroot} -type f -name "*.la" -delete
%find_lang %{name} --with-gnome
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
