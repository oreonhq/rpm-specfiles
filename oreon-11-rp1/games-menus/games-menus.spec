%global source0_hash e444284445d224ae09b50da6f5d8aabd972e1d0947ab241637c2f2c64da7bf60

Name:           games-menus
Version:        0.3.2
Release:        36%{?dist}
Summary:        Catagorized submenus for the MATE/KDE Games menu
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.redhat.com/archives/fedora-games-list/2007-March/msg00003.html
# No URL as we are upstream
Source0:        %{name}-%{version}.tar.gz
Patch0:         games-menus-0.3.2-it-spellfix.patch
BuildArch:      noarch
Requires:       redhat-menus hicolor-icon-theme
Provides:       dribble-menus = 1.2
Obsoletes:      dribble-menus <= 1.2

%description
Catagorized submenus for the MATE/KDE Games menu, for better usuability of the
games menu with lots of games installed

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build
# nothing to build data only

%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/xdg/menus/applications-merged
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor
install -p -m 644 games-categories.menu \
  $RPM_BUILD_ROOT%{_sysconfdir}/xdg/menus/applications-merged
cp -a desktop-directories $RPM_BUILD_ROOT%{_datadir}
cp -a icons/* $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/

%files
%doc copyright-info.txt COPYING* README
%config(noreplace) %{_sysconfdir}/xdg/menus/applications-merged/games-categories.menu
%{_datadir}/desktop-directories/*.directory
%{_datadir}/icons/hicolor/*/apps/package_games_*.png

%changelog
%autochangelog
