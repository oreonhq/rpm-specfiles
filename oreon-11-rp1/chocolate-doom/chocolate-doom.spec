%global source0_hash 1edcc41254bdc194beb0d33e267fae306556c4d24110a1d3d3f865717f25da23

Name:		chocolate-doom
Summary:	Historically compatible Doom engine
License:	GPL-2.0-or-later

%global rtld org.chocolate_doom
URL:		http://chocolate-doom.org/

Version:	3.1.1
Release:	1%{?dist}

%global git_tag %{name}-%{version}
Source0:	https://github.com/chocolate-doom/chocolate-doom/archive/%{git_tag}/%{git_tag}.tar.gz

# Always use the system python3 instead of asking /usr/bin/env first.
Patch1:		0001-use-python3.patch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	fluidsynth-devel
BuildRequires:	libpng-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	make
BuildRequires:	SDL2-devel
BuildRequires:	SDL2_mixer-devel
BuildRequires:	SDL2_net-devel

BuildRequires:	python3
BuildRequires:	python3dist(pillow)

BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib

#Provides:	bundled(md5-plumb)
Provides:	bundled(sha1-gnupg)

%description
Chocolate Doom is a game engine that aims to accurately reproduce the experience 
of playing vanilla Doom. It is a conservative, historically accurate Doom source 
port, which is compatible with the thousands of mods and levels that were made 
before the Doom source code was released. Rather than flashy new graphics, 
Chocolate Doom's main features are its accurate reproduction of the game as it
was played in the 1990s. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{git_tag}
autoreconf -vif

%build
export PYTHON=%{_bindir}/python3

# Despite AC_PROC_CC_C99 inside configure.ac,
# -std= does not seem to be set when building
export CFLAGS="${CFLAGS} -std=gnu99"

%configure
%make_build

%install
export PYTHON=%{_bindir}/python3
%make_install DESTDIR=%{buildroot} \
     iconsdir="%{_datadir}/icons/hicolor/64x64/apps" \
     docdir="%{_pkgdocdir}"

# The program installs a .desktop file for a generic "chocolate-setup"
# executable, even though each game ships with its own setup executable.
# Create separate desktop files for each of those.
for GAME in Doom Heretic Hexen Strife; do
	EXEC="chocolate-$(echo "${GAME}" | tr '[A-Z]' '[a-z]')-setup"
	FILE="%{buildroot}%{_datadir}/applications/%{rtld}.${GAME}-Setup.desktop"

	cp -p %{buildroot}%{_datadir}/applications/%{rtld}.Setup.desktop "${FILE}"
	desktop-file-edit \
		--set-key=Exec --set-value="${EXEC}" \
		--set-name="Chocolate ${GAME} setup" \
		--set-comment="Setup tool for Chocolate ${GAME}" \
		"${FILE}"
done
rm %{buildroot}%{_datadir}/applications/%{rtld}.Setup.desktop

%check
for GAME in Doom Heretic Hexen Strife; do
	desktop-file-validate %{buildroot}/%{_datadir}/applications/%{rtld}.${GAME}.desktop
	desktop-file-validate %{buildroot}/%{_datadir}/applications/%{rtld}.${GAME}-Setup.desktop
	appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{rtld}.${GAME}.metainfo.xml
done
desktop-file-validate %{buildroot}/%{_datadir}/applications/screensavers/%{rtld}.Doom_Screensaver.desktop

%files
%doc %{_docdir}/chocolate*
%{_datadir}/bash-completion
%{_bindir}/chocolate-doom
%{_bindir}/chocolate-doom-setup
%{_bindir}/chocolate-heretic
%{_bindir}/chocolate-heretic-setup
%{_bindir}/chocolate-hexen
%{_bindir}/chocolate-hexen-setup
%{_bindir}/chocolate-server
%{_bindir}/chocolate-strife
%{_bindir}/chocolate-strife-setup
%{_datadir}/applications/%{rtld}.Doom.desktop
%{_datadir}/applications/%{rtld}.Doom-Setup.desktop
%{_datadir}/applications/%{rtld}.Heretic.desktop
%{_datadir}/applications/%{rtld}.Heretic-Setup.desktop
%{_datadir}/applications/%{rtld}.Hexen.desktop
%{_datadir}/applications/%{rtld}.Hexen-Setup.desktop
%{_datadir}/applications/%{rtld}.Strife.desktop
%{_datadir}/applications/%{rtld}.Strife-Setup.desktop
%{_datadir}/applications/screensavers/%{rtld}.Doom_Screensaver.desktop
%{_datadir}/icons/hicolor/64x64/apps/chocolate-doom.png
%{_datadir}/icons/hicolor/64x64/apps/chocolate-heretic.png
%{_datadir}/icons/hicolor/64x64/apps/chocolate-hexen.png
%{_datadir}/icons/hicolor/64x64/apps/chocolate-setup.png
%{_datadir}/icons/hicolor/64x64/apps/chocolate-strife.png
%{_metainfodir}/%{rtld}.Doom.metainfo.xml
%{_metainfodir}/%{rtld}.Heretic.metainfo.xml
%{_metainfodir}/%{rtld}.Hexen.metainfo.xml
%{_metainfodir}/%{rtld}.Strife.metainfo.xml
%{_mandir}/man5/chocolate-doom.cfg.5*
%{_mandir}/man5/chocolate-heretic.cfg.5*
%{_mandir}/man5/chocolate-hexen.cfg.5*
%{_mandir}/man5/chocolate-strife.cfg.5*
%{_mandir}/man5/default.cfg.5*
%{_mandir}/man5/heretic.cfg.5*
%{_mandir}/man5/hexen.cfg.5*
%{_mandir}/man5/strife.cfg.5*
%{_mandir}/man6/chocolate-doom.6*
%{_mandir}/man6/chocolate-doom-setup.6*
%{_mandir}/man6/chocolate-heretic-setup.6*
%{_mandir}/man6/chocolate-heretic.6*
%{_mandir}/man6/chocolate-hexen-setup.6*
%{_mandir}/man6/chocolate-hexen.6*
%{_mandir}/man6/chocolate-server.6*
%{_mandir}/man6/chocolate-strife-setup.6*
%{_mandir}/man6/chocolate-strife.6*

%changelog
%autochangelog
