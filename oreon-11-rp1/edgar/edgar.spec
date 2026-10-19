%global source0_hash 23e57debc5e6995447bba3b64513e420e111ce24644a3a303237f4379ba3e710
Name:           edgar
Version:        1.38
Release:        1%{?dist}
Summary:        A platform game
License:        GPL-2.0-or-later AND CC-BY-3.0 AND CC-BY-SA-3.0 AND CC0-1.0
URL:            https://www.parallelrealities.co.uk/games/edgar/
Source0:        https://github.com/riksweeney/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:      hicolor-icon-theme
# oreon:deps
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
