%global source0_hash 1edcc41254bdc194beb0d33e267fae306556c4d24110a1d3d3f865717f25da23
Name:		chocolate-doom
Summary:        Historically compatible Doom engine
License:	GPL-2.0-or-later
%global rtld org.chocolate_doom
URL:		http://chocolate-doom.org/
Version:	3.1.1
Release:        1%{?dist}
%global git_tag %{name}-%{version}
Source0:        https://github.com/%{name}/%{name}/archive/%{git_tag}/%{git_tag}.tar.gz
Patch1:		0001-use-python3.patch
Provides:	bundled(sha1-gnupg)
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_net-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  fluidsynth-devel
BuildRequires:  gcc
BuildRequires:  libappstream-glib
BuildRequires:  libpng-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  python3dist(pillow)
# /oreon:deps
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
export CFLAGS="${CFLAGS} -std=gnu99"
%configure
%make_build
%install
export PYTHON=%{_bindir}/python3
%make_install DESTDIR=%{buildroot} \
     iconsdir="%{_datadir}/icons/hicolor/64x64/apps" \
     docdir="%{_pkgdocdir}"
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
%oreon_autofiles main

%check

for GAME in Doom Heretic Hexen Strife; do
	desktop-file-validate %{buildroot}/%{_datadir}/applications/%{rtld}.${GAME}.desktop
	desktop-file-validate %{buildroot}/%{_datadir}/applications/%{rtld}.${GAME}-Setup.desktop
	appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{rtld}.${GAME}.metainfo.xml
done
desktop-file-validate %{buildroot}/%{_datadir}/applications/screensavers/%{rtld}.Doom_Screensaver.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
