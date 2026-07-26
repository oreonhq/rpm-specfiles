%global source0_hash 1d804599dc4d908aae81916f141a708538dde4888fef20e612c6d19c562ba84e

Name: anarch
License: CC0-1.0

%global summ_text Suckless, anarcho-pacifist Doom clone that runs everywhere
Summary: %{summ_text}

%global git_date 20230123
%global git_commit eeb04a079784ccd9c4b37909795ae781902712eb
%global git_commit_short %(c='%{git_commit}'; echo "${c:0:8}")

Version: 1.1^%{git_date}git%{git_commit_short}
Release: 6%{?dist}

URL: https://drummyfish.gitlab.io/anarch/
Source0: https://gitlab.com/drummyfish/%{name}/-/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz

Source100: %{name}.desktop
Source101: %{name}.metainfo.xml

# The game stores its save file in the current running directory.
# This patch makes it use XDG_DATA_HOME instead.
Patch0: 0000-store-savefile-in-XDG_DATA_HOME.patch

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: gcc
BuildRequires: CSFML-devel
BuildRequires: SDL2-devel

%global desc_text Anarch is an extremely small, completely Public Domain, no-dependency, \
no-file, portable suckless anarcho-pacifist from-scratch 90s-style Doom clone \
that runs everywhere, made for the benefit of all living beings. \

%description
%{desc_text}

%package SDL2
Summary: %{summ_text} (SDL2 version)
Requires: hicolor-icon-theme

%description SDL2
%{desc_text}

This version of the game runs using the SDL2 library.

%package CSFML
Summary: %{summ_text} (CSFML version)
Requires: hicolor-icon-theme

%description CSFML
%{desc_text}

This version of the game runs using the CSFML library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{git_commit}

%build
# The game can be built in many versions.
# The Linux ones are: terminal, SDL2, CSFML.
#
# The terminal version is experimental and needs to be ran as root,
# as it uses /dev/input and /dev/tty for IO.
#
# This leaves us with the CSFML and the SDL2 versions.
for LIBRARY in \
	'CSFML:csfml:main_csfml.c:-lcsfml-graphics -lcsfml-window -lcsfml-system -lcsfml-audio' \
	'SDL2:sdl2:main_sdl.c:-lSDL2'
do
	LIB_NAME="$(echo "${LIBRARY}" | cut -d: -f1)"
	LIB_SUFFIX="$(echo "${LIBRARY}" | cut -d: -f2)"
	LIB_SOURCE="$(echo "${LIBRARY}" | cut -d: -f3)"
	LIB_LDFLAGS="$(echo "${LIBRARY}" | cut -d: -f4)"

	gcc -D_DEFAULT_SOURCE \
		%{optflags} -std=c99 -Wall -Wextra -Wpedantic \
		${LIB_LDFLAGS} %{build_ldflags} \
		-o "%{name}-${LIB_SUFFIX}" "${LIB_SOURCE}"

	sed -e "s|LIB_NAME|${LIB_NAME}|g" -e "s|LIB_SUFFIX|${LIB_SUFFIX}|g" \
		< "%{SOURCE100}" > "%{name}-${LIB_SUFFIX}.desktop"

	sed -e "s|LIB_NAME|${LIB_NAME}|g" -e "s|LIB_SUFFIX|${LIB_SUFFIX}|g" \
		< "%{SOURCE101}" > "%{name}-${LIB_SUFFIX}.metainfo.xml"
done

# Also build the test executable.
gcc %{optflags} -std=c99 %{build_ldflags} -o %{name}-test main_test.c

%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 -d %{buildroot}%{_datadir}/applications
install -m 755 -d %{buildroot}%{_metainfodir}

ICON_DIR='%{buildroot}%{_datadir}/icons/hicolor/128x128/apps'
install -m 755 -d "${ICON_DIR}"

for LIBRARY in csfml sdl2; do
	install -m 755 -p "%{name}-${LIBRARY}" -t %{buildroot}%{_bindir}
	install -m 644 -p "%{name}-${LIBRARY}.desktop" -t %{buildroot}%{_datadir}/applications
	install -m 644 -p "%{name}-${LIBRARY}.metainfo.xml" -t %{buildroot}%{_metainfodir}
	install -m 644 -p media/logo_big.png "${ICON_DIR}/%{name}-${LIBRARY}.png"
done

%check
./%{name}-test

for LIBRARY in csfml sdl2; do
	desktop-file-validate "%{buildroot}%{_datadir}/applications/%{name}-${LIBRARY}.desktop"
	appstream-util validate-relax --nonet "%{buildroot}%{_metainfodir}/%{name}-${LIBRARY}.metainfo.xml"
done

%files CSFML
%doc README.md
%license LICENSE
%{_bindir}/%{name}-csfml
%{_datadir}/applications/%{name}-csfml.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}-csfml.png
%{_metainfodir}/%{name}-csfml.metainfo.xml

%files SDL2
%doc README.md
%license LICENSE
%{_bindir}/%{name}-sdl2
%{_datadir}/applications/%{name}-sdl2.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}-sdl2.png
%{_metainfodir}/%{name}-sdl2.metainfo.xml

%changelog
%autochangelog
