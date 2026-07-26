%global source0_hash 93cd7c47ff83e00655605fcbec6a031f75d170d7eb467b85bcbe6c1733bcc213

Name:           xblast
Version:        2.10.4
Release:        44%{?dist}
Summary:        Lay bombs and Blast the other players of the field (SDL version)
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://xblast.sourceforge.net
Source0:        http://downloads.sourceforge.net/xblast/xblast-%{version}.tar.gz
Source1:        xblast.sh
Source2:        xblast.desktop
Source3:        xblast-32.png
Source4:        xblast-48.png
Source5:        xblast-128.png
Source6:        xblast.appdata.xml
Patch0:         xblast-2.10.4-sdl-fixes.patch
Patch1:         xblast-2.10.4-manpage.patch
Patch2:         xblast-2.10.4-fcommon-fix.patch
Patch3:         xblast-2.10.4-font-config-fix.patch
BuildRequires:  gcc make
BuildRequires:  libXt-devel gettext gawk desktop-file-utils SDL_gfx-devel
BuildRequires:  SDL_image-devel SDL_ttf-devel SDL_mixer-devel SDL_net-devel
BuildRequires:  libappstream-glib
Requires:       %{name}-data >= 2.10.0, %{name}-common = %{version}-%{release}
Requires:       font(dejavusans)
Provides:       %{name}-engine = %{version}-%{release}

%description
This is the new SDL version of XBlast, a multi-player game where the "purpose"
is to Blast the other players of the game-field by laying bombs close to them.
While at the same time you must avoid being blown up yourself.

%package x11
Summary:        Lay bombs and Blast the other players of the field (X11 version)
Requires:       %{name}-data >= 2.10.0, %{name}-common = %{version}-%{release}
Requires:       xorg-x11-fonts-ISO8859-1-75dpi
Provides:       %{name}-engine = %{version}-%{release}

%description x11
This is the original X11 version of XBlast, a multi-player game where the
"purpose" is to Blast the other players of the game-field by laying bombs close
to them. While at the same time you must avoid being blown up yourself.

%package common
Summary:        Files common to both the X11 and SDL version of XBlast
Requires:       %{name}-engine = %{version}-%{release}, hicolor-icon-theme

%description common
Files common to both the X11 and SDL version of XBlast, a multi-player game
where the "purpose" is to Blast the other players of the game-field by laying
bombs close to the other player.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i 's|$(game_datadir)/locale|%{_datadir}/locale|g' Makefile.in
# stop rpmlint from complaining about executable source files in the -debuginfo
chmod -x chat.* version.c
# stop autoxxx from rerunning because of strange timestamps in the tarbal
touch aclocal.m4 configure Makefile.in config.h.in

%build
# first build the SDL version
%configure --with-otherdatadir=%{_datadir}/%{name} --enable-admin --enable-sdl
make %{?_smp_mflags}
mv xblast xblast-sdl

# and then the X11 version
make distclean
%configure --with-otherdatadir=%{_datadir}/%{name} --enable-admin --enable-sound
make %{?_smp_mflags}

%install
make install localedir=%{_datadir}/locale DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

mv $RPM_BUILD_ROOT%{_bindir}/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}-x11
install -m 755 xblast-sdl $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
install -m 644 %{name}.man $RPM_BUILD_ROOT%{_mandir}/man6/%{name}.6

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -p -m 644 %{SOURCE4} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -p -m 644 %{SOURCE5} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%{_bindir}/%{name}-sdl

%files x11
%{_bindir}/%{name}-x11
%{_bindir}/xbsndsrv

%files -f %{name}.lang common
%doc AUTHORS README
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6.gz
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
%autochangelog
