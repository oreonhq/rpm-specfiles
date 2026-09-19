%global source0_hash none

Name:		denemo
Version:	2.6.0
Release:	20%{?dist}
Summary:	Graphical music notation program
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later

Source:		https://ftp.gnu.org/gnu/denemo/denemo-%{version}.tar.gz
Source1:	%{name}-feta.metainfo.xml
Source2:	%{name}-emmentaler.metainfo.xml
Source3:	%{name}-music.metainfo.xml
Patch1:		%{name}-%{version}-configure.patch
# Upstream patch: https://savannah.gnu.org/bugs/index.php?63720
Patch2:		%{name}-%{version}-c99.patch
Patch3:		%{name}-guile-3.0.patch

URL: http://www.denemo.org/

BuildRequires: gcc libtool
BuildRequires: portaudio-devel aubio-devel guile30-devel
BuildRequires: gettext libxml2-devel fftw-devel desktop-file-utils
BuildRequires: libtool-ltdl-devel jack-audio-connection-kit-devel
BuildRequires: fontpackages-devel lash-devel libsamplerate-devel
BuildRequires: fluidsynth-devel librsvg2-devel gtk3-devel
BuildRequires: chrpath libsndfile-devel atril-devel gtksourceview3-devel
BuildRequires: portmidi-devel intltool rubberband-devel
BuildRequires: make autoconf automake gtk-doc

Requires: lilypond
Requires: denemo-music-fonts = %{version}-%{release}
Requires: denemo-emmentaler-fonts = %{version}-%{release}
Requires: denemo-feta-fonts = %{version}-%{release}

%description
Denemo is a free software (GPL) music notation editor for GNU/Linux that 
lets you rapidly enter notation for typesetting via the LilyPond music 
engraver.  You can compose, transcribe, arrange, listen to the music 
and much more. 

%package music-fonts
Summary:	Denemo Denemo fonts
BuildArch:	noarch
Requires:	fontpackages-filesystem
Requires:	denemo-fonts-common = %{version}-%{release}

%description music-fonts 
Denemo is a free software (GPL) music notation editor for GNU/Linux that 
lets you rapidly enter notation for typesetting via the LilyPond music 
engraver.  You can compose, transcribe, arrange, listen to the music 
and much more. 

These are the Denemo.ttf fonts derived from FreeSerif.ttf and FreeSans.ttf. 

%package emmentaler-fonts
Summary:	Denemo emmentaler fonts
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
BuildArch:	noarch
Requires:	fontpackages-filesystem
Requires:	denemo-fonts-common = %{version}-%{release}

%description emmentaler-fonts 
Denemo is a free software (GPL) music notation editor for GNU/Linux that 
lets you rapidly enter notation for typesetting via the LilyPond music 
engraver.  You can compose, transcribe, arrange, listen to the music 
and much more. 

These are the emmentaler.ttf fonts derived from lilypond's fonts.

%package feta-fonts
Summary:	Denemo feta fonts
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
BuildArch:	noarch
Requires:	fontpackages-filesystem
Requires:	denemo-fonts-common = %{version}-%{release}

%description feta-fonts 
Denemo is a free software (GPL) music notation editor for GNU/Linux that 
lets you rapidly enter notation for typesetting via the LilyPond music 
engraver.  You can compose, transcribe, arrange, listen to the music 
and much more. 

These are the feta.ttf fonts derived from lilypond's fonts.

%package fonts-common
Summary:	Denemo fonts common dir
BuildArch:	noarch
Requires:	fontpackages-filesystem

%description fonts-common
Denemo is a free software (GPL) music notation editor for GNU/Linux that 
lets you rapidly enter notation for typesetting via the LilyPond music 
engraver.  You can compose, transcribe, arrange, listen to the music 
and much more. 

This contains the directory common to all Denemo fonts.

%prep
%autosetup -p1

%build
export CFLAGS="$CFLAGS -std=gnu17"
autoupdate
autoreconf -if
%configure --enable-jack=yes --disable-binreloc --enable-guile_3_0=yes

%make_build
chrpath -d src/denemo
chmod 644 actions/*.scm

%install
%make_install

desktop-file-install --vendor=""\
	--dir=%{buildroot}/%{_datadir}/applications\
	--add-category=X-Notation\
	%{buildroot}/%{_datadir}/applications/org.denemo.Denemo.desktop

%find_lang %{name}
install -m 0755 -d %{buildroot}/%{_datadir}/denemo/fonts
install -m 0755 -d %{buildroot}%{_fontdir}
rm -f %{buildroot}/%{_bindir}/denemo-lilypond.bat

install -m 0644 -p fonts/*.ttf %{buildroot}%{_fontdir}
rm -rf %{buildroot}/%{_datadir}/fonts/truetype
rm -rf %{buildroot}/%{_includedir}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
	%{buildroot}%{_datadir}/appdata/%{name}-feta.metainfo.xml
install -Dm 0644 -p %{SOURCE2} \
	%{buildroot}%{_datadir}/appdata/%{name}-emmentaler.metainfo.xml
install -Dm 0644 -p %{SOURCE3} \
	%{buildroot}%{_datadir}/appdata/%{name}-music.metainfo.xml

%files -f %{name}.lang
%license COPYING
%doc ChangeLog
%dir %{_datadir}/denemo
%{_datadir}/denemo/*
%{_datadir}/pixmaps/org.denemo.Denemo.png
%{_datadir}/applications/org.denemo.Denemo.desktop
%{_bindir}/*
%{_datadir}/appdata/org.denemo.Denemo.appdata.xml

%_font_pkg -n feta feta.ttf
%{_datadir}/appdata/%{name}-feta.metainfo.xml

%_font_pkg -n emmentaler emmentaler.ttf
%{_datadir}/appdata/%{name}-emmentaler.metainfo.xml

%_font_pkg -n music Denemo.ttf
%{_datadir}/appdata/%{name}-music.metainfo.xml

%files fonts-common
%license COPYING
%doc AUTHORS
%defattr(0644,root,root,0755)

%changelog
%autochangelog
