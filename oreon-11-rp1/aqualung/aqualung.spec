%global source0_hash a6ae09e25a7c6711fabbb504372089a9306e7ce28c1b34d6d565bccd6ef96e9a

%global forgeurl https://github.com/jeremyevans/aqualung

Name:           aqualung
Version:        2.0
Release:        6%{?dist}
Summary:        Music Player for GNU/Linux
License:        GPL-2.0-or-later
URL:            https://aqualung.jeremyevans.net
Source:         %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz
Source:         %{name}.desktop
# https://github.com/jeremyevans/aqualung/pull/48
Patch:          %{name}-ffmpeg8.patch

# autogen.sh
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  gettext-devel
# GUI
BuildRequires:  atk-devel
BuildRequires:  cairo-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  glib2-devel
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  libpng-devel
BuildRequires:  libxml2-devel
BuildRequires:  pango-devel
BuildRequires:  pixman-devel
BuildRequires:  zlib-devel
# Desktop
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
# Output
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(samplerate)
# Encode/Decode
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(oggz)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  libmpcdec-devel
BuildRequires:  mac-devel
BuildRequires:  ffmpeg-free-devel
BuildRequires:  lame-devel
BuildRequires:  pkgconfig(wavpack)
BuildRequires:  pkgconfig(lrdf)
# CD
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  libcdio-paranoia-devel
BuildRequires:  pkgconfig(libcddb)
# Others
BuildRequires:  pkgconfig(libusb)
BuildRequires:  libifp-devel
BuildRequires:  pkgconfig(lua)
BuildRequires:  sed

Requires:       hicolor-icon-theme

%description
Aqualung is an advanced music player originally targeted at the GNU/Linux
operating system. It plays audio CDs, internet radio streams and pod casts as
well as sound files in just about any audio format and has the feature of
inserting no gaps between adjacent tracks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

# Fix lib64 path
sed -i 's@/usr/lib/@%{_libdir}/@g' src/plugin.c

# Regenerate autotools
./autogen.sh

%build
%set_build_flags
# pipewire-jack is not in the default search path, and configure does not use pkg-config
export LDFLAGS="$LDFLAGS $(pkg-config --libs-only-L jack)"
%configure \
    --without-sndio \
    --with-oss \
    --with-alsa \
    --with-jack \
    --with-pulse \
    --with-src \
    --with-sndfile \
    --with-flac \
    --with-vorbisenc \
    --with-speex \
    --with-mpeg \
    --with-mod \
    --with-mpc \
    --with-mac \
    --with-lavc \
    --with-lame \
    --with-wavpack \
    --with-ladspa \
    --with-cdda \
    --with-cddb \
    --with-ifp \
    --with-lua

%make_build

%install
%make_install

desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

for i in 16 24 32 48 64; do
  install -Dpm0644 src/img/icon_${i}.png \
    %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done

cat <<EOF > %{name}.appdata.xml
<?xml version="1.0" encoding="UTF-8"?>
<component type="desktop-application">
    <id>net.jeremyevans.aqualung</id>
    <name>Aqualung</name>
    <summary>Advanced music player</summary>
    <metadata_license>FSFAP</metadata_license>
    <project_license>GPL-2.0-or-later</project_license>
    <description>
        <p>
            Aqualung is an advanced music player originally targeted at the GNU/Linux
            operating system. It plays audio CDs, internet radio streams and pod casts as
            well as sound files in just about any audio format and has the feature of
            inserting no gaps between adjacent tracks.
        </p>
    </description>
    <launchable type="desktop-id">%{name}.desktop</launchable>
    <provides>
        <binary>aqualung</binary>
    </provides>
    <content_rating type="oars-1.1"/>
    <developer_name>Jeremy Evans</developer_name>
    <releases>
        <release version="%{version}" date="%(date +%F -r %{SOURCE0})" />
    </releases>
    <screenshots>
      <screenshot type="default">
        <caption>Default skin (Music Store builder)</caption>
        <image>https://aqualung.jeremyevans.net/images/default.png</image>
      </screenshot>
      <screenshot>
        <caption>Woody skin (File Info and volume calculation)</caption>
        <image>https://aqualung.jeremyevans.net/images/woody.png</image>
      </screenshot>
      <screenshot>
        <caption>Metal skin (Playlist featuring Album mode)</caption>
        <image>https://aqualung.jeremyevans.net/images/metal.png</image>
      </screenshot>
      <screenshot>
        <caption>Dark skin (LADSPA plugin support)</caption>
        <image>https://aqualung.jeremyevans.net/images/dark.png</image>
      </screenshot>
      <screenshot>
        <caption>Plain skin (Settings dialog and album cover)</caption>
        <image>https://aqualung.jeremyevans.net/images/plain.png</image>
      </screenshot>
      <screenshot>
        <caption>Ocean skin (Search in Music Store)</caption>
        <image>https://aqualung.jeremyevans.net/images/ocean.png</image>
      </screenshot>
    </screenshots>
    <url type="homepage">%{url}</url>
</component>
EOF
install -D -p -m 644 %{name}.appdata.xml %{buildroot}%{_metainfodir}/%{name}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog
%doc %{_pkgdocdir}/*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_metainfodir}/%{name}.appdata.xml

%changelog
%autochangelog
