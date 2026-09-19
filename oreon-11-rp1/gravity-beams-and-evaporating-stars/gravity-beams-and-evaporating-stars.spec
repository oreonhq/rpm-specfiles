%global source0_hash 8952414d95d5892411086bf7a592cd79cdde63c896c40651a81b9173f9e4ff30

%global repo_owner  dextero
%global repo_name   LD30

Name: gravity-beams-and-evaporating-stars
%global shortname %(echo "%{name}" | sed -e 's:\\([a-z]\\)[a-z]*:\\1:g' -e 's:-::g')

Version: 1.0
Release: 23%{?dist}
Summary: A game about hurling asteroids into the sun
License: MIT

URL:     https://github.com/%{repo_owner}/%{repo_name}
Source0: %{URL}/archive/%{version}/%{repo_name}-%{version}.tar.gz

Patch0: %{shortname}--chdir-at-game-start.patch
Patch1: %{shortname}--store-hiscores-in-XDG_DATA_HOME.patch

BuildRequires: cmake > 3.1
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: make
BuildRequires: SFML-devel

Requires: hicolor-icon-theme

%global fontlist font(dejavusans)
BuildRequires: fontconfig
BuildRequires: %{fontlist}
Requires: %{fontlist}

%description
You are a lone planet whose star is dying. Use your gravity beams to hurl
nearby asteroids into the star, feeding it some extra matter.
While saving the star, be sure to avoid being hit by the asteroids yourself.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{repo_name}-%{version}

# Inject the RPM data dir
sed -e 's|__DATA_DIR__|"%{_datadir}/%{name}"|' -i src/main.cpp

%build
# TODO: Please submit an issue to upstream (rhbz#2380630)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build

%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 bin/game %{buildroot}%{_bindir}/%{name}

install -m 755 -d %{buildroot}%{_datadir}/%{name}
cp -a data %{buildroot}%{_datadir}/%{name}/data

# Replace the bundled DejaVuSans font
# with a symlink to the system-provided one
ln -sf \
  $(fc-match -f "%%{file}\n" "DejaVu Sans") \
  %{buildroot}%{_datadir}/%{name}/data/DejaVuSans.ttf

install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
install -m 644 -p \
  data/planet.png \
  %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

install -m 755 -d %{buildroot}%{_datadir}/applications/
install -m 644 \
  packaging/%{name}.desktop \
  %{buildroot}%{_datadir}/applications/

install -m 755 -d %{buildroot}%{_datadir}/metainfo/
install -m 644 -p \
  packaging/%{name}.appdata.xml \
  %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

install -m 755 -d %{buildroot}%{_mandir}/man1/
install -m 644 -p \
  packaging/%{name}.man \
  %{buildroot}%{_mandir}/man1/%{name}.1

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet packaging/%{name}.appdata.xml

%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man1/%{name}.*

%changelog
%autochangelog
