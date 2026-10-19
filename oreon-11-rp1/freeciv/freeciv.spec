%global source0_hash b3ce15f54083b1fca146f62837a5f7d41d298537fa34940cca70eeb09c7a9c6e
Name:           freeciv
Version:        3.2.6
Release:        1%{?dist}
Summary:        A multi-player strategy game
License:        GPL-2.0-or-later
URL:            http://sourceforge.net/projects/freeciv/
Source0:        http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  SDL2_mixer-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gtk4-devel
BuildRequires:  libcurl-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  readline-devel
BuildRequires:  sqlite-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
find $RPM_BUILD_ROOT -name '*.la' -delete
find $RPM_BUILD_ROOT -name '*.a' -delete
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n freeciv-common -f %{oreon_filedir}/freeciv-common.list
%files -n freeciv-gtk -f %{oreon_filedir}/freeciv-gtk.list
%files -n freeciv-qt -f %{oreon_filedir}/freeciv-qt.list

%changelog

%autochangelog
