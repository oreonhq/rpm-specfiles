%global source0_hash 431587933e8f01d92a976933fe415aa0b000e5e7ec053b53efac0d8004311acc
%global fonts font(freesans) font(freeserif)
Name:           trackballs
Version:        1.3.5
Release:        1%{?dist}
Summary:        Steer a marble ball through a labyrinth
License:        GPL-2.0-or-later
URL:            https://trackballs.github.io/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         trackballs-gcc15.patch
Requires:       %{fonts}
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  font(freesans)
BuildRequires:  font(freeserif)
BuildRequires:  fontconfig
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  guile30-devel
BuildRequires:  libappstream-glib
BuildRequires:  libglvnd-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
%oreon_autofiles main

%check

%ctest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
