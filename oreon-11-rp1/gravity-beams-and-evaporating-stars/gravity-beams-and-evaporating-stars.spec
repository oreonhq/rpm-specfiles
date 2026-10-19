%global source0_hash 8952414d95d5892411086bf7a592cd79cdde63c896c40651a81b9173f9e4ff30
%global repo_owner  dextero
%global repo_name   LD30
Name: gravity-beams-and-evaporating-stars
%global shortname %(echo "%{name}" | sed -e 's:\\([a-z]\\)[a-z]*:\\1:g' -e 's:-::g')
Version: 1.0
Release:        1%{?dist}
Summary:        A game about hurling asteroids into the sun
License: MIT
URL:     https://github.com/%{repo_owner}/%{repo_name}
Source0:        https://github.com/%{repo_owner}/%{repo_name}/archive/%{version}/%{repo_name}-%{version}.tar.gz
Patch0: %{shortname}--chdir-at-game-start.patch
Patch1: %{shortname}--store-hiscores-in-XDG_DATA_HOME.patch
Requires: hicolor-icon-theme
%global fontlist font(dejavusans)
Requires: %{fontlist}
# oreon:deps
BuildRequires:  SFML2-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  font(dejavusans)
BuildRequires:  fontconfig
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
# /oreon:deps
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

export PKG_CONFIG_PATH=%{_libdir}/SFML2/pkgconfig
export CXXFLAGS="%{optflags} -I%{_includedir}/SFML2"
export LDFLAGS="%{?build_ldflags} -L%{_libdir}/SFML2"
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DSFML_DIR=%{_libdir}/cmake/SFML2 -DSFML_ROOT=%{_prefix}
%cmake_build
%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 bin/game %{buildroot}%{_bindir}/%{name}
install -m 755 -d %{buildroot}%{_datadir}/%{name}
cp -a data %{buildroot}%{_datadir}/%{name}/data
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
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet packaging/%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
