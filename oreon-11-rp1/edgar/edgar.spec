%global source0_hash none

Name:           edgar
Version:        1.38
Release:        2%{?dist}
Summary:        A platform game

# edgar now contains sounds licensed under a "good" Fedora license:
# http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=653813#80
License:        GPL-2.0-or-later AND CC-BY-3.0 AND CC-BY-SA-3.0 AND CC0-1.0
URL:            https://www.parallelrealities.co.uk/games/edgar/
Source0:        https://github.com/riksweeney/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: SDL2_image-devel
BuildRequires: SDL2_mixer-devel
BuildRequires: SDL2_ttf-devel
BuildRequires: zlib-devel
BuildRequires: libpng-devel
BuildRequires: gettext
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils
Requires:      hicolor-icon-theme

%description
When his father fails to return home after venturing out one dark and stormy 
night, Edgar fears the worst: he has been captured by the evil sorcerer who 
lives in a fortress beyond the forbidden swamp.

Donning his armor, Edgar sets off to rescue him, but his quest will not be 
easy...

%prep
%setup -q

# Fix Makefile
sed -i 's/LDFLAGS += -s/:/' makefile
sed -i 's:$(PREFIX)/games/:$(PREFIX)/bin/:' makefile
sed -i 's:$(PREFIX)/share/games/edgar/:$(PREFIX)/share/edgar/:' \
  makefile

%build
%set_build_flags
%make_build NO_PAK=1

%install
%make_install NO_PAK=1

desktop-file-validate \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man6/%{name}.6*
%doc %{_pkgdocdir}
%license doc/license

%changelog
%autochangelog
