%global source0_hash b422c92f15dde0432e1819001e9eb6167895b380aad44e55abff17e02daf6be4
Name:           zaz
Version:        1.0.1
Release:        12%{?dist}
Summary:        A puzzle game where the player has to arrange balls in triplets
License:        GPL-3.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:            http://zaz.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.png
Source2:        %{name}.appdata.xml
Source3:        %{name}.6
Patch0:         %{name}-1.0.0-jumpy_keyboard.patch
Patch1:         %{name}-1.0.1-libvorbis.patch
Requires:       hicolor-icon-theme
Requires:       gnu-free-mono-fonts
Requires:       gnu-free-sans-fonts
Requires:       oflb-dignas-handwriting-fonts
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  SDL_image-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ftgl-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  libtheora-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
# /oreon:deps
%description
Zaz is an arcade action puzzle game where the goal is to get rid of all 
incoming balls by rearranging their order and making triplets.

A 3D accelerator is needed for decent gameplay.

%prep

%autosetup -p1

# Fix permissions
chmod 644 src/*.{cpp,h}

%build

%configure
%make_build
%install
%make_install
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/FreeMonoBold.ttf
ln -s %{_datadir}/fonts/gnu-free/FreeMonoBold.ttf \
    $RPM_BUILD_ROOT%{_datadir}/%{name}/FreeMonoBold.ttf
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/FreeSans.ttf
ln -s %{_datadir}/fonts/gnu-free/FreeSans.ttf \
    $RPM_BUILD_ROOT%{_datadir}/%{name}/FreeSans.ttf
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/font1.ttf
ln -s %{_datadir}/fonts/oflb-dignas-handwriting/phranzysko_-_Digna_s_Handwriting.ttf \
    $RPM_BUILD_ROOT%{_datadir}/%{name}/font1.ttf
rm -r $RPM_BUILD_ROOT/usr/share/doc/
rm -rf $RPM_BUILD_ROOT%{_datadir}/pixmaps/
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
convert extra/%{name}.xpm \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 0644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
desktop-file-validate \
   $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -d $RPM_BUILD_ROOT%{_datadir}/metainfo
install -p -m 0644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/metainfo
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/metainfo/*.appdata.xml
install -d $RPM_BUILD_ROOT%{_mandir}/man6
install -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/man6/
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
