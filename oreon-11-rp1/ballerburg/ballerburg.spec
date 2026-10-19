%global source1_hash 1e82f4db17785e489e805fc2b9e043578a696d1fba8943e5951c11a30f8202f7
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
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  SDL2-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
# /oreon:deps
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
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
install -p -m 644 LIESMICH.txt README.txt doc/authors.txt \
  %{buildroot}%{_pkgdocdir}
for px in 32 48 64 256; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${px}x${px}/apps
  magick %{SOURCE1} \
    -gravity south \
    -resize ${px}x${px} \
    -extent ${px}x${px} \
    -background white \
    %{buildroot}%{_datadir}/icons/hicolor/${px}x${px}/apps/%{name}.png
done
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE2}
install -d %{buildroot}%{_datadir}/metainfo
install -p -m 0644 %{SOURCE3} \
  %{buildroot}%{_datadir}/metainfo
appstream-util validate-relax --nonet \
  %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
