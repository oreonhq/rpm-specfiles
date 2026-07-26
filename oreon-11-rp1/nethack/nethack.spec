%global source0_hash 98cf67df6debf9668a61745aa84c09bcab362e5d33f5b944ec5155d44d2aacb2

%global nhgamedir /usr/games/nethack
%global nhdatadir /var/games/nethack

%global fontname nethack-bitmap

Name:           nethack
Version:        3.6.7
Release:        9%{?dist}
Summary:        A rogue-like single player dungeon exploration game

License:        NGPL
URL:            https://nethack.org
Source0:        https://www.nethack.org/download/3.6.7/nethack-367-src.tgz
Source1:        %{name}.desktop
Patch0:         %{name}-%{version}-makefile.patch
Patch1:         %{name}-%{version}-top.patch
Patch2:         %{name}-%{version}-config.patch
Patch3:         %{name}-%{version}-guidebook.patch
Patch4:         hackdir.patch
Patch5:         %{name}-%{version}-xpm.patch
Patch6:         modern_c.patch
Requires:       %{fontname}-fonts-core

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  bison, flex, desktop-file-utils
BuildRequires:  bdftopcf, mkfontdir, libX11-devel, libXaw-devel, libXext-devel
BuildRequires:  libXmu-devel, libXpm-devel, libXt-devel
BuildRequires:  fontpackages-devel
BuildRequires:  bdftopcf

%description
NetHack is a single player dungeon exploration game that runs on a
wide variety of computer systems, with a variety of graphical and text
interfaces all using the same game engine.

Unlike many other Dungeons & Dragons-inspired games, the emphasis in
NetHack is on discovering the detail of the dungeon and not simply
killing everything in sight - in fact, killing everything in sight is
a good way to die quickly.

Each game presents a different landscape - the random number generator
provides an essentially unlimited number of variations of the dungeon
and its denizens to be discovered by the player in one of a number of
characters: you can pick your race, your role, and your gender.

%package -n %{fontname}-fonts
Summary:        Bitmap fonts for Nethack
BuildArch:      noarch
Requires:       fontpackages-filesystem

%description -n %{fontname}-fonts
Bitmap fonts for Nethack.

%package -n %{fontname}-fonts-core
Summary:         X11 core fonts configuration for %{fontname}
BuildArch:      noarch
Requires:        %{fontname}-fonts
Requires(post):  %{fontname}-fonts
Requires(post):  mkfontdir
Requires(post):	 coreutils
Requires(preun): coreutils

%description -n %{fontname}-fonts-core
X11 core fonts configuration for %{fontname}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -n nethack-3.6.7
cd NetHack-3.6.7
mv * ..
cd ..
rm -rf NetHack-3.6.7
%dnl %patch0 -b .makefile
%patch -P0 -b .makefile
%patch -P1 -p0 
%patch -P2 -b .config
%patch -P3 -b .guidebook

# Extra patches
%patch -P4 -p1

%patch -P5 -b .xpm

%patch -P6 -p1

%{__sed} -i -e "s:PREFIX=\$(wildcard ~)/nh/install:PREFIX=/usr:" sys/unix/hints/linux
%{__sed} -i -e "s:^\(HACKDIR=\).*:\1%{nhgamedir}:" sys/unix/hints/linux
sh sys/unix/setup.sh sys/unix/hints/linux

# Set our paths
%{__sed} -i -e "s:^\(HACKDIR=\).*:\1%{nhgamedir}:" sys/unix/nethack.sh
%{__sed} -i -e "s:FEDORA_CONFDIR:%{nhgamedir}:" sys/unix/nethack.sh
%{__sed} -i -e "s:FEDORA_STATEDIR:%{nhdatadir}:" include/unixconf.h
%{__sed} -i -e "s:FEDORA_HACKDIR:%{nhgamedir}:" include/config.h
%{__sed} -i -e "s:/usr/games/lib/nethackdir:%{nhgamedir}:" \
        doc/nethack.6 doc/nethack.txt doc/recover.6 doc/recover.txt

# Point the linker in the right direction
%{__sed} -i -e "s:-L/usr/X11R6/lib:-L/usr/X11R6/%{_lib}:" \
        src/Makefile util/Makefile

%build
make all

%install
rm -rf $RPM_BUILD_ROOT
%make_install \
        PREFIX=$RPM_BUILD_ROOT \
        HACKDIR=$RPM_BUILD_ROOT%{nhgamedir} \
        GAMEDIR=$RPM_BUILD_ROOT%{nhgamedir} \
        VARDIR=$RPM_BUILD_ROOT%{nhdatadir} \
        SHELLDIR=$RPM_BUILD_ROOT%{_bindir} \
        CHOWN=/bin/true \
        CHGRP=/bin/true

install -d -m 0755 $RPM_BUILD_ROOT%{_mandir}/man6
make -C doc MANDIR=$RPM_BUILD_ROOT%{_mandir}/man6 manpages

install -D -p -m 0644 win/X11/nh_icon.xpm \
        $RPM_BUILD_ROOT%{_datadir}/pixmaps/nethack.xpm

desktop-file-install \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications \
        --add-category Game \
        --add-category RolePlaying \
        %{SOURCE1}

# Install the fonts for the X11 interface
cd win/X11
bdftopcf -o nh10.pcf nh10.bdf
bdftopcf -o ibm.pcf ibm.bdf
install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0644 -p *.pcf $RPM_BUILD_ROOT%{_fontdir}

%{__sed} -i -e 's:^!\(NetHack.tile_file.*\):\1:' \
        $RPM_BUILD_ROOT%{nhgamedir}/NetHack.ad

%post -n %{fontname}-fonts-core
mkfontdir %{_fontdir}
if [ ! -L /etc/X11/fontpath.d/nethack ] ; then
    ln -s %{_fontdir} /etc/X11/fontpath.d/nethack
fi

%preun -n %{fontname}-fonts-core
if [ $1 -eq 0 ] ; then 
    rm /etc/X11/fontpath.d/nethack
    rm %{_fontdir}/fonts.dir
fi;

%files
%doc doc/*.txt README dat/license dat/history
%doc dat/opthelp dat/wizhelp
%{_mandir}/man6/*
%{_datadir}/pixmaps/nethack.xpm
%{_datadir}/applications/nethack.desktop
%{_bindir}/nethack
%{nhgamedir}
%defattr(0664,root,games)
%config(noreplace) %{nhdatadir}/record
%config(noreplace) %{nhdatadir}/perm
%config(noreplace) %{nhdatadir}/logfile
%config(noreplace) %{nhdatadir}/xlogfile
%attr(0775,root,games) %dir %{nhdatadir}
%attr(0775,root,games) %dir %{nhdatadir}/save
%attr(2755,root,games) %{nhgamedir}/nethack
%config(noreplace) %{nhgamedir}/nhdat
%config(noreplace) %{nhgamedir}/sysconf
%config(noreplace) %{nhgamedir}/NetHack.ad
%config(noreplace) %{nhgamedir}/license
%config(noreplace) %{nhgamedir}/pet_mark.xbm
%config(noreplace) %attr(0555,root,games) %{nhgamedir}/recover
%config(noreplace) %{nhgamedir}/rip.xpm
%config(noreplace) %{nhgamedir}/pilemark.xbm
%config(noreplace) %{nhgamedir}/symbols
%config(noreplace) %{nhgamedir}/x11tiles

%_font_pkg -n bitmap *.pcf

%files -n %{fontname}-fonts-core

%changelog
%autochangelog
