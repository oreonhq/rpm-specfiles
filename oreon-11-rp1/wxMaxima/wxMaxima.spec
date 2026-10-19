%global source0_hash 7524487ddf858eaba8d9e4d0fc2062bdb1d177b21183e5adfa78fc27929e57ce
%global app_id io.github.wxmaxima_developers.wxMaxima
Summary:        Graphical user interface for Maxima
Name:    wxMaxima
Version: 26.08.0
Release:        1%{?dist}
License: GPL-2.0-or-later
URL:     https://wxmaxima-developers.github.io/wxmaxima/
Source0:        https://github.com/wxMaxima-developers/wxmaxima/archive/Version-%{version}.tar.gz
ExcludeArch: %{ix86}
Provides: wxmaxima = %{version}-%{release}
Requires: jsmath-fonts
Requires: maxima >= 5.30
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  libxml2-devel
BuildRequires:  wxGTK-devel
# /oreon:deps
%description
A Graphical user interface for the computer algebra system
Maxima using wxWidgets.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n wxmaxima-Version-%{version} -p1

dos2unix data/%{app_id}.desktop

%build

%cmake
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{scalable,48x48,64x64,128x128}/apps/
cp -alf \
  %{buildroot}%{_datadir}/pixmaps/%{app_id}.svg \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
cp -alf \
  %{buildroot}%{_datadir}/pixmaps/%{app_id}.png \
  %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
convert -resize 64x64 \
  %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{app_id}.png \
  %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{app_id}.png
convert -resize 48x48 \
  %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{app_id}.png \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{app_id}.png
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes/
cp -alf  %{buildroot}%{_datadir}/pixmaps/text-x-wx*.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes/
%find_lang wxMaxima
%find_lang wxmaxima --with-man
rm -fv %{buildroot}%{_datadir}/wxmaxima/{COPYING,README,README.md}
rm -rfv %{buildroot}%{_datadir}/pixmaps/
rm -rfv %{buildroot}%{_datadir}/menu
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
