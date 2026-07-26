%global source0_hash none

%global		ver	0771

Name:		ultimatestunts
Version:	0.7.7
Release:	30%{?dist}
Summary:	Remake of the famous DOS-game Stunts

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.ultimatestunts.nl
Source0:	http://downloads.sf.net/%{name}/%{name}-srcdata-%{ver}.tar.gz
Source1:	%{name}.desktop
Patch0:		ultimatestunts-0761-make.patch
Patch1:		ultimatestunts-0751-locale.patch
Patch2:		ultimatestunts-0761-unistd.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:	dos2unix
BuildRequires:	freealut-devel
BuildRequires:	SDL_image-devel
BuildRequires:	freeglut-devel
BuildRequires:	libXi-devel
BuildRequires:	libvorbis-devel
BuildRequires:	desktop-file-utils

%description
UltimateStunts is a remake of the famous DOS-game Stunts. It was a 3D racing
game, with simple CGA/EGA/VGA graphics and no texture or smooth shading, but
because of the spectacular stunts (loopings, bridges to jump over, etc.)
it was really fun to play. One of the best aspects of this game is that it
had a track editor. Because of the tile-based tracks, every gamer was able
to make it's own tracks. This remake works on UNIX-compatible systems (like
Linux), and on windows. It also provides more modern features, like openGL
graphics, 3D sound and internet multiplaying.

%prep
%setup -q -n %{name}-srcdata-%{ver}
%patch -P0 -p0 -b .make
%patch -P1 -p0 -b .locale
%patch -P2 -p1 -b .unistd

# remove SVN control files
find . -name .svn -type d -print0 | xargs -0 rm -rf

# fixup access
find ./data -type d -print0 | xargs -0 chmod a+rx
find ./data -type f -print0 | xargs -0 chmod a+r
find ./doc -type f -print0 | xargs -0 chmod a+r
chmod a-x simulation/metaserver.cpp
chmod a-x shared/usmisc.cpp

# fixup EOL
pushd "doc/nolanguage/Original Stunts Track-Format_files"
dos2unix -q style.css
dos2unix -q stunts.htm
touch -r tree.png style.css stunts.htm
popd

# fixup encoding
pushd "doc/nolanguage/Original Stunts Track-Format_files"
f=stunts.htm
iconv -f ISO8859-1 -t UTF-8 -o $f.new $f
touch -r tree.png $f.new
mv $f.new $f
popd

pushd doc/nl
for f in *.htm
do
	iconv -f ISO8859-1 -t UTF-8 -o $f.new $f
	touch -r $f $f.new
	mv $f.new $f
done
popd

# ensure the config gets regenerated with correct $datadir
rm -f %{name}.conf

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT \
	usdatadir=$RPM_BUILD_ROOT%{_datadir}/%{name} \
	localedir=%{_datadir}/locale

rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/lang

%find_lang %{name}

desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	%{SOURCE1}

%files -f %{name}.lang
%doc COPYING doc/*
%{_bindir}/ustunts*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}

%changelog
%autochangelog
