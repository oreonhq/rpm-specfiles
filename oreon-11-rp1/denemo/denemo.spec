%global source0_hash 4be5970c69847f97f1f876275c9744e5034e7c983b12a1045fb20c236494b55d
Name:		denemo
Version:	2.6.0
Release:        20%{?dist}
Summary:        Graphical music notation program
License:	GPL-3.0-or-later
Source0:        https://ftp.gnu.org/gnu/denemo/denemo-%{version}.tar.gz
Source1:	%{name}-feta.metainfo.xml
Source2:	%{name}-emmentaler.metainfo.xml
Source3:	%{name}-music.metainfo.xml
Patch1:		%{name}-%{version}-configure.patch
Patch2:		%{name}-%{version}-c99.patch
Patch3:		%{name}-guile-3.0.patch
URL: http://www.denemo.org/
Requires: lilypond
Requires: denemo-music-fonts = %{version}-%{release}
Requires: denemo-emmentaler-fonts = %{version}-%{release}
Requires: denemo-feta-fonts = %{version}-%{release}
# oreon:deps
BuildRequires:  atril-devel
BuildRequires:  aubio-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  fftw-devel
BuildRequires:  fluidsynth-devel
BuildRequires:  fontpackages-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  gtksourceview3-devel
BuildRequires:  guile30-devel
BuildRequires:  intltool
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  lash-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  portaudio-devel
BuildRequires:  portmidi-devel
BuildRequires:  rubberband-devel
# /oreon:deps
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
%oreon_prep
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
install -Dm 0644 -p %{SOURCE1} \
	%{buildroot}%{_datadir}/appdata/%{name}-feta.metainfo.xml
install -Dm 0644 -p %{SOURCE2} \
	%{buildroot}%{_datadir}/appdata/%{name}-emmentaler.metainfo.xml
install -Dm 0644 -p %{SOURCE3} \
	%{buildroot}%{_datadir}/appdata/%{name}-music.metainfo.xml
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n denemo-music-fonts -f %{oreon_filedir}/denemo-music-fonts.list
%files -n denemo-emmentaler-fonts -f %{oreon_filedir}/denemo-emmentaler-fonts.list
%files -n denemo-feta-fonts -f %{oreon_filedir}/denemo-feta-fonts.list
%files -n denemo-fonts-common -f %{oreon_filedir}/denemo-fonts-common.list

%changelog

%autochangelog
