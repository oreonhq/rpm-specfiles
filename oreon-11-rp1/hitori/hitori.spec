%global source0_hash 42270bd4f9525d180d3151bd7245335dc5cf248a984e02f68ff930da799e583b

Name:		hitori
Version:	44.0
Release:	8%{?dist}
Summary:	Logic puzzle game for GNOME
Summary(de):	Logikpuzzle für GNOME

# The executable is licensed under GPLv3+, while the user manual is CC-BY-SA.
License:	GPL-3.0-or-later and CC-BY-SA-3.0
URL:		https://wiki.gnome.org/Apps/Hitori
Source0:	https://download.gnome.org/sources/hitori/3.38/hitori-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	itstool
BuildRequires:	meson
BuildRequires:	/usr/bin/appstream-util
BuildRequires:	/usr/bin/xmllint

%description
A small application written to allow one to play the Hitori puzzle game,
which is similar in theme to more popular puzzles such as Sudoku.

It has full support for playing the game (i.e. it checks all three rules are
satisfied). It has undo/redo support, can give hints, and allows for cells
to be tagged with one of two different tags, to aid in solving the puzzle.
It has support for anything from 5×5 to 10×10 grids.

%description -l de
Ein kleines Programm zum Spielen des Hitori-Puzzles, das thematisch
populäreren Puzzlespielen wie beispielsweise Sudoku ähnelt.

Das Programm unterstützt die Spielregeln vollständig. Es wird in
jedem Fall überprüft, ob die drei Ausschlussregeln angewendet sind.
Das Zurücknehmen und Wiederholen von Zügen ist ebenso möglich wie das
Kennzeichnen von Feldern mit einer oder mehreren Markierungen, um den Weg zur
Lösung zu erleichtern. Mögliche Spielfeldgrößen reichen von 5x5 bis hin zu
10x10 Feldern. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Hitori.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Hitori.desktop

%files -f %{name}.lang
%license COPYING COPYING-DOCS
%doc AUTHORS MAINTAINERS NEWS README.md
%{_bindir}/hitori
%{_datadir}/applications/org.gnome.Hitori.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.hitori.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Hitori.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Hitori-symbolic.svg
%{_metainfodir}/org.gnome.Hitori.appdata.xml

%changelog
%autochangelog
