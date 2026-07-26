%global source0_hash none

Name:           freeciv
Version:        3.2.4
Release:        1%{?dist}
Summary:        A multi-player strategy game

License:        GPL-2.0-or-later
URL:            http://sourceforge.net/projects/freeciv/
Source0:        http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.xz

# If a local build fails unable to find Qt5, remove qt-devel.
BuildRequires:  gcc gcc-c++
BuildRequires:	gtk4-devel
BuildRequires:	readline-devel
BuildRequires:	zlib-devel
BuildRequires:	SDL2_mixer-devel
BuildRequires:	ncurses-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	libcurl-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  sqlite-devel
BuildRequires:  make

%description
Freeciv is a turn-based, multi-player, X based strategy game. Freeciv
is generally comparable to, and has compatible rules with, the
Civilization II(R) game by Microprose(R). In Freeciv, each player is
the leader of a civilization, and is competing with the other players
in order to become the leader of the greatest civilization.

%package common
Summary:  %{summary}

%description common
Freeciv common files

%package gtk
Summary:  %{summary}
Requires:  %{name}-common = %{version}-%{release}
Provides: freeciv = %{version}-%{release}
Obsoletes: freeciv < 0:3.0.3-2

%description gtk
Freeciv gtk client

%package qt
Summary:  %{summary}
Requires:  %{name}-common = %{version}-%{release}

%description qt
Freeciv qt client

%prep
%setup -q -n %{name}-%{version}

%build
export MOCCMD="$(%{_qt6_qmake} -query QT_HOST_LIBEXECS)/moc"
%configure --enable-client=gtk4,qt --disable-static --enable-ruledit \
	--with-qtver=qt6 --enable-fcmp=gtk4,qt
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}-core
%find_lang %{name}-nations
%find_lang %{name}-ruledit

desktop-file-install --delete-original \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications  	\
	$RPM_BUILD_ROOT%{_datadir}/applications/org.%{name}.server.desktop

desktop-file-install --delete-original	\
	--dir $RPM_BUILD_ROOT%{_datadir}/applications	\
	$RPM_BUILD_ROOT%{_datadir}/applications/org.%{name}.gtk4.desktop

desktop-file-install --delete-original	\
	--dir $RPM_BUILD_ROOT%{_datadir}/applications	\
	$RPM_BUILD_ROOT%{_datadir}/applications/org.%{name}.qt.desktop

%if 0%{?rhel}
# On RHEL 7, the doc macro puts docs in a versioned subdir
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/freeciv/
%endif

# Remove civmanual
#rm $RPM_BUILD_ROOT%{_bindir}/civmanual
find $RPM_BUILD_ROOT -name '*.la' -delete
find $RPM_BUILD_ROOT -name '*.a' -delete

%files common -f %{name}-core.lang -f %{name}-nations.lang -f %{name}-ruledit.lang
%doc %{_docdir}/freeciv/*

%license COPYING
%{_bindir}/freeciv-server
%{_bindir}/freeciv-manual
%{_bindir}/freeciv-ruledit
%{_bindir}/freeciv-ruleup
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/pixmaps/%{name}-*.png
%{_datadir}/metainfo/*
%{_mandir}/man6/freeciv*6*
%{_sysconfdir}/freeciv/database.lua

%files gtk
%{_bindir}/freeciv-mp-gtk4
%{_bindir}/freeciv-gtk4

%files qt
%{_bindir}/freeciv-mp-qt
%{_bindir}/freeciv-qt

%changelog
%autochangelog
