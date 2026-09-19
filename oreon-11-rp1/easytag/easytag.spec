%global source0_hash fc51ee92a705e3c5979dff1655f7496effb68b98f1ada0547e8cbbc033b67dd5

Name:    easytag
Version: 2.4.3
Release: 29%{?dist}
Summary: Tag editor for MP3, Ogg, FLAC and other music files

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://wiki.gnome.org/Apps/EasyTAG
Source:  https://download.gnome.org/sources/%{name}/2.4/%{name}-%{version}.tar.xz

# Debian patches to port to taglib-2.x
Patch:   03_port-to-taglib-2.patch
Patch:   04_taglib-2-further-fix.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: desktop-file-utils
BuildRequires: docbook-dtds
BuildRequires: docbook-style-xsl
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: id3lib-devel >= 3.7.12
BuildRequires: intltool
BuildRequires: itstool
BuildRequires: libappstream-glib
BuildRequires: libappstream-glib-devel
BuildRequires: libtool
BuildRequires: libxslt
BuildRequires: pkgconfig(flac)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(id3tag)
BuildRequires: pkgconfig(opusfile)
BuildRequires: pkgconfig(speex)
BuildRequires: pkgconfig(taglib) >= 2.0
BuildRequires: pkgconfig(vorbisfile)
BuildRequires: pkgconfig(wavpack)
BuildRequires: make
BuildRequires: yelp-tools
Recommends:    yelp

# Obsoleted in F37
Obsoletes:     easytag-nautilus < 2.4.3-16

%description
EasyTAG is a utility for viewing, editing and writing the tags of MP4, MP3,
MP2, FLAC, Ogg Opus, Ogg Speex, Ogg Vorbis, MusePack and Monkey's Audio files.

%if 0
%package nautilus
Summary:  Nautilus extension for opening in EasyTAG
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:  GPL-3.0-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}

%description nautilus
Nautilus extension to add "Open with EasyTAG" to the Nautilus context menu, for
easier access to EasyTAG when opening directories and audio files.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%set_build_flags
autoreconf -fiv
# id3lib C interface uses int bool, not compatible with C23
CFLAGS="$CFLAGS -std=gnu11"
%configure --disable-appdata-validate
make V=1 %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} INSTALL="install -p" install
find %{buildroot} -type f -name "*.la" -delete
%find_lang %{name} --with-gnome

%check
make check

%files -f %{name}.lang
%doc ChangeLog HACKING README THANKS TODO
%license COPYING
%{_bindir}/easytag
%{_datadir}/applications/easytag.desktop
%{_datadir}/icons/hicolor/*/apps/easytag.*
%{_datadir}/icons/hicolor/symbolic/apps/easytag-symbolic.svg
%{_datadir}/glib-2.0/schemas/org.gnome.EasyTAG.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.EasyTAG.gschema.xml
%{_mandir}/man1/easytag.1*
%{_metainfodir}/easytag.appdata.xml

%if 0
%files nautilus
%license COPYING.GPL3
%{_datadir}/appdata/easytag-nautilus.metainfo.xml
%{_libdir}/nautilus/extensions-3.0/libnautilus-easytag.so
%endif

%changelog
%autochangelog
