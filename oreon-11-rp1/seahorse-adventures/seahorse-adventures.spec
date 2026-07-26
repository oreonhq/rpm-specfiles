%global source0_hash 203ccbe572942653385a2a51079b8aa815321b49a3ea344fea172abd43973798

Name: seahorse-adventures
Summary: Help barbie the seahorse float on bubbles to the moon
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later

Version: 1.4
Release: 10%{?dist}

URL: http://www.imitationpickles.org/barbie/

%global git_tag Release-%{version}
Source0: https://github.com/dulsi/seahorse-adventures/archive/%{git_tag}/%{name}-%{git_tag}.tar.gz

BuildArch: noarch

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

Requires: hicolor-icon-theme
Requires: python3-pygame

# Game can work without Gamerzilla, so let's not make it a hard requirement
Recommends: pylibgamerzilla

%global fontlist font(bitstreamverasans)
BuildRequires: fontconfig
BuildRequires: %{fontlist}
Requires: %{fontlist}

%description
Help barbie the seahorse float on bubbles to the moon. This is a retro-side
scroller game. It won the teams category in pyweek 4. Includes original
soundtrack, graphics, and 15 levels!

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{git_tag}
sed \
	-e 's|#![ ]*/usr/bin/python|#!%{_bindir}/python3|' \
	-e 's|#![ ]*/usr/bin/env python|#!%{_bindir}/python3|' \
	-i create-upload.py leveledit.py run_game.py tileedit.py

%build
# nothing to build, pure python code only

%install
install -m 755 -d %{buildroot}%{_datadir}/%{name}
install -m 755 -p leveledit.py run_game.py tileedit.py %{buildroot}%{_datadir}/%{name}/
cp -a data/ lib/ %{buildroot}%{_datadir}/%{name}

VERA_PATH="$(fc-match -f "%%{file}" "Bitstream Vera Sans")"
find %{buildroot}%{_datadir}/%{name}/ -name 'Vera.ttf' \
	-exec ln -sf "${VERA_PATH}" '{}' ';'

install -m 755 -d %{buildroot}%{_bindir}
ln -s %{_datadir}/%{name}/run_game.py %{buildroot}%{_bindir}/%{name}

install -m 755 -d %{buildroot}%{_datadir}/applications
install -m 644 -p ./%{name}.desktop %{buildroot}%{_datadir}/applications/

install -m 755 -d %{buildroot}%{_metainfodir}
install -m 644 -p ./%{name}.metainfo.xml %{buildroot}%{_metainfodir}/

for ICON_SIZE in 32 64 128; do
	ICON_DIR="%{buildroot}%{_datadir}/icons/hicolor/${ICON_SIZE}x${ICON_SIZE}/apps"
	install -m 755 -d "${ICON_DIR}"
	install -m 644 -p "./icon${ICON_SIZE}.png" "${ICON_DIR}/%{name}.png"
done

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files
%doc CHANGES.txt LEVELS.txt NOTES.txt README.txt TODO.txt
%license LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_metainfodir}/%{name}.metainfo.xml

%changelog
%autochangelog
