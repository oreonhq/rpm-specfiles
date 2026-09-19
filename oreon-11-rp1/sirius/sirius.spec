%global source0_hash 6e512fccaf276a818f96072898576fb9bdd8905de95e6d23aa3277e2b04332ae

Name:		sirius
Version:	0.8.0
Release:	51%{?dist}

Summary:	Reversi game for Gnome
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
# The upstream website for sirius has disappeared and a search hasn't
# turned up a new one.
#URL:		http://sirius.bitvis.nu/
#Source0:	http://sirius.bitvis.nu/files/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
Patch0:         sirius-desktop.patch
Patch1:         sirius-libm.patch
# Don't use message as a format string
Patch2:         format-fix.patch

BuildRequires: make
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	libgnomeui-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	libtool intltool autoconf automake

%description
Sirius is a program for playing the game of reversi. The program includes an AI
(Artificial Intelligence) opponent which plays at a very challenging level and
is actually quite hard to beat. The AI opponent's strength can therefore be
adjusted in several ways to give you a suitable opponent.

The AI opponent uses a plain alpha-beta search with hashing to figure out which
move to make. To be able to tell a good position from a bad one, it uses a
pattern based evaluation function. The pattern used is the 9 discs surrounding
each corner and the 8 discs creating the edge of the board. The evaluation
function also takes mobility, potential mobility and parity into count. For the
initial 9 moves the AI opponent optionally uses a simple opening book. During
midgame it searches and evaluates about 200.000 nodes per second on a PIII
750 MHz, in the endgame this number is significantly higher due to more
transpositions and a less expensive evaluation function.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0
%patch -P1
%patch -P2 -b .format-fix

%build
# Upstream hasn't updated their autotools output in a while and it needs
# to be rebuilt.
intltoolize --force
autoreconf -vif
%configure
make %{?_smp_mflags} CFLAGS="%{optflags}"
iconv -f iso8859-1 -t utf-8 AUTHORS > AUTHORS.conv && mv -f AUTHORS.conv AUTHORS
iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv && mv -f ChangeLog.conv ChangeLog
iconv -f iso8859-1 -t utf-8 README > README.conv && mv -f README.conv README

%install
make install DESTDIR=%{buildroot} INSTALL="%{__install} -p"
%find_lang %{name}

desktop-file-install                 --delete-original	\
	--dir %{buildroot}%{_datadir}/applications	\
	--add-category Game				\
	%{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
%{_datadir}/applications/sirius.desktop

%changelog
%autochangelog
