%global source0_hash 88fdddef806008aac2c7c0ebf8c9152e26cdb1b21fd70337069925723134dcc4

Name:           ballerburg
Version:        1.2.3
Release:        5%{?dist}
Summary:        Two players, two castles, and a hill in between

License:        GPL-3.0-or-later
URL:            https://baller.frama.io/
Source0:        https://framagit.org/baller/ballerburg/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:        https://baller.frama.io/king.png
Source2:        %{name}.desktop
Source3:        %{name}.appdata.xml

Patch:          ballerburg-1.2.3-Fix_depends.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  SDL2-devel
BuildRequires:  gettext
BuildRequires:  ImageMagick
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
Two castles, separated by a mountain, try to defeat each other with their
cannonballs, either by killing the opponent's king or by weakening the
opponent enough so that the king capitulates.

Ballerburg was originally written 1987 by Eckhard Kruse, for the Atari ST
machines (which were brand new computers at that point in time). Over 25
years later, here's finally the adaption of the original source code to
modern operating systems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-v%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

# Install additional docs
install -p -m 644 LIESMICH.txt README.txt doc/authors.txt \
  %{buildroot}%{_pkgdocdir}

# Install icons
for px in 32 48 64 256; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${px}x${px}/apps
  magick %{SOURCE1} \
    -gravity south \
    -resize ${px}x${px} \
    -extent ${px}x${px} \
    -background white \
    %{buildroot}%{_datadir}/icons/hicolor/${px}x${px}/apps/%{name}.png
done

# Install desktop file
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE2}

# Install appdata
install -d %{buildroot}%{_datadir}/metainfo
install -p -m 0644 %{SOURCE3} \
  %{buildroot}%{_datadir}/metainfo
appstream-util validate-relax --nonet \
  %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man6/ballerburg.6*
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%doc %{_pkgdocdir}
%license COPYING.txt

%changelog
%autochangelog
