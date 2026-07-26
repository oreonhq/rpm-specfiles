%global source0_hash none

%global fonts font(freesans) font(freeserif)

Name:           trackballs
Version:        1.3.5
Release:        1%{?dist}
Summary:        Steer a marble ball through a labyrinth
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://trackballs.github.io/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         trackballs-gcc15.patch

BuildRequires:  gcc-c++ cmake
BuildRequires:  guile30-devel SDL2-devel SDL2_image-devel SDL2_mixer-devel
BuildRequires:  SDL2_ttf-devel zlib-devel libglvnd-devel gettext
BuildRequires:  desktop-file-utils libappstream-glib
BuildRequires:  fontconfig %{fonts}
Requires:       %{fonts}

%description
Trackballs is a game in which you steer a marble ball through tracks of varying
difficulty. The game features 3D graphics, an integrated level editor and high
quality sound effects and background music.

%prep
%autosetup -p1
iconv -f ISO-8859-1 -t UTF8 share/%{name}.6 > share/%{name}.6.tmp
touch -r share/%{name}.6 share/%{name}.6.tmp
mv share/%{name}.6.tmp share/%{name}.6

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang %{name}

# Replace bundled fonts with symlinks to system fonts
ln -sf $(fc-match -f "%{file}" "freeserif:bold:italic") \
  $RPM_BUILD_ROOT%{_datadir}/trackballs/fonts/FreeSerifBoldItalic.ttf
ln -sf $(fc-match -f "%{file}" "freesans:bold") \
  $RPM_BUILD_ROOT%{_datadir}/trackballs/fonts/menuFont.ttf

mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
mv $RPM_BUILD_ROOT/%{_datadir}/metainfo/trackballs.appdata.xml \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
%ctest

%files -f %{name}.lang
%doc AUTHORS.md FAQ.md README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6.gz
%{_docdir}/%{name}/*.html
%{_docdir}/%{name}/*.css
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
%autochangelog
