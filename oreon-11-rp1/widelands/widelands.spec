%global source0_hash e6f3e8f4fcafd367962dbacde80e26fc63afad38cfe26fadba9c92d4a01bd687
%global fonts font(amiri) font(dejavusans) font(dejavusansmono) font(dejavuserif) font(widelands) font(gargi) font(wenquanyimicrohei) font(frankruehlclm)
Name:           widelands
Version:        1.3.1
Release:        1%{?dist}
Summary:        Open source realtime-strategy game
License:        GPL-2.0-or-later
URL:            http://www.widelands.org
Source0:        https://github.com/widelands/widelands/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         widelands-1.3-build19-ppc64le.patch
Patch1:         widelands-1.2-build20-gcc10.patch
Patch2:         widelands-1.3-make-sdl2-use-x11.patch
Patch3:         widelands-1.3-gcc13.patch
Patch4:         widelands-1.3-f37-sys-minizip-buildfix.patch
Patch5:         widelands-1.2.1-disable-some-tests.patch
Patch6:         widelands-1.3-gcc15.patch
Requires:      hicolor-icon-theme
Requires:      %{fonts}
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  asio-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  ctags
BuildRequires:  desktop-file-utils
BuildRequires:  font(amiri)
BuildRequires:  font(dejavusans)
BuildRequires:  font(dejavusansmono)
BuildRequires:  font(dejavuserif)
BuildRequires:  font(frankruehlclm)
BuildRequires:  font(gargi)
BuildRequires:  font(wenquanyimicrohei)
BuildRequires:  font(widelands)
BuildRequires:  fontconfig
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  libappstream-glib
BuildRequires:  libcurl-devel
BuildRequires:  libpng-devel
BuildRequires:  minizip-ng-compat-devel
BuildRequires:  python3
# /oreon:deps
%description
Widelands is an open source (GPLed), realtime-strategy game, using SDL and
other free libraries, which is still under development. Widelands is inspired
by Settlers II (Bluebyte) and is partly similar to it, so if you know it, you
perhaps will have a thought, what Widelands is all about.

%prep

%setup -q -n widelands
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%ifarch s390x
%patch -P5 -p1
%endif
%patch -P6 -p1

%build

%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DWL_INSTALL_BASEDIR=%{_prefix}/share/%{name} \
    -DWL_INSTALL_DATADIR=%{_prefix}/share/%{name} \
    -DOPTION_BUILD_WEBSITE_TOOLS=OFF \
    %{nil}
%cmake_build
%install
%cmake_install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mv $RPM_BUILD_ROOT%{_prefix}/games/%{name} \
   $RPM_BUILD_ROOT%{_bindir}/%{name}
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/*.metainfo.xml
pushd $RPM_BUILD_ROOT
rm -r usr/share/%{name}/i18n/fonts/amiri
mkdir usr/share/%{name}/i18n/fonts/amiri-fonts
ln -s amiri-fonts usr/share/%{name}/i18n/fonts/amiri
ln -s $(fc-match -f "%{file}" "amiri") \
  usr/share/%{name}/i18n/fonts/amiri-fonts/amiri-regular.ttf
ln -s $(fc-match -f "%{file}" "amiri:bold") \
  usr/share/%{name}/i18n/fonts/amiri-fonts/amiri-bold.ttf
ln -s $(fc-match -f "%{file}" "amiri:italic") \
  usr/share/%{name}/i18n/fonts/amiri-fonts/amiri-slanted.ttf
ln -s $(fc-match -f "%{file}" "amiri:bold:italic") \
  usr/share/%{name}/i18n/fonts/amiri-fonts/amiri-boldslanted.ttf
rm -r usr/share/%{name}/i18n/fonts/DejaVu
mkdir usr/share/%{name}/i18n/fonts/dejavu-fonts
ln -s dejavu-fonts usr/share/%{name}/i18n/fonts/DejaVu
ln -s $(fc-match -f "%{file}" "sans") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSans.ttf
ln -s $(fc-match -f "%{file}" "sans:bold") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSans-Bold.ttf
ln -s $(fc-match -f "%{file}" "sans:italic") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSans-Oblique.ttf
ln -s $(fc-match -f "%{file}" "sans:bold:italic") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSans-BoldOblique.ttf
ln -s $(fc-match -f "%{file}" "serif") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSerif.ttf
ln -s $(fc-match -f "%{file}" "serif:bold") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSerif-Bold.ttf
ln -s $(fc-match -f "%{file}" "serif:italic") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSerif-Italic.ttf
ln -s $(fc-match -f "%{file}" "serif:bold:italic") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSerif-BoldItalic.ttf
ln -s $(fc-match -f "%{file}" "monospace") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSansMono.ttf
ln -s $(fc-match -f "%{file}" "monospace:bold") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSansMono-Bold.ttf
ln -s $(fc-match -f "%{file}" "monospace:italic") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSansMono-Oblique.ttf
ln -s $(fc-match -f "%{file}" "monospace:bold:italic") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSansMono-BoldOblique.ttf
ln -s $(fc-match -f "%{file}" "DejaVuSansCondensed") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSansCondensed.ttf
ln -s $(fc-match -f "%{file}" "DejaVuSansCondensed:bold") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSansCondensed-Bold.ttf
ln -s $(fc-match -f "%{file}" "DejaVuSansCondensed:italic") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSansCondensed-Oblique.ttf
ln -s $(fc-match -f "%{file}" "DejaVuSansCondensed:bold:italic") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSansCondensed-BoldOblique.ttf
rm -r usr/share/%{name}/i18n/fonts/MicroHei
mkdir usr/share/%{name}/i18n/fonts/wqy-microhei-fonts
ln -s wqy-microhei-fonts usr/share/%{name}/i18n/fonts/MicroHei
ln -s $(fc-match -f "%{file}" "wenquanyimicrohei") \
   usr/share/%{name}/i18n/fonts/wqy-microhei-fonts/wqy-microhei.ttc
rm -r usr/share/%{name}/i18n/fonts/Nakula/*
ln -s $(fc-match -f "%{file}" "gargi") \
   usr/share/%{name}/i18n/fonts/Nakula/nakula.ttf
rm -r usr/share/%{name}/i18n/fonts/Culmus/*
ln -s $(fc-match -f "%{file}" "frankruehlclm:bold") \
  usr/share/%{name}/i18n/fonts/Culmus/TaameyFrankCLM-Bold.ttf
ln -s $(fc-match -f "%{file}" "frankruehlclm:bold:italic") \
  usr/share/%{name}/i18n/fonts/Culmus/TaameyFrankCLM-BoldOblique.ttf
ln -s $(fc-match -f "%{file}" "frankruehlclm:medium") \
  usr/share/%{name}/i18n/fonts/Culmus/TaameyFrankCLM-Medium.ttf
ln -s $(fc-match -f "%{file}" "frankruehlclm:medium:italic") \
  usr/share/%{name}/i18n/fonts/Culmus/TaameyFrankCLM-MediumOblique.ttf
rm -r usr/share/%{name}/i18n/fonts/Widelands/*
ln -s $(fc-match -f "%{file}" "widelands") \
   usr/share/%{name}/i18n/fonts/Widelands/Widelands.ttf
find usr/share/widelands/i18n/translations/ -maxdepth 2 -type f -name \*_\*.po | sed -n 's#\(usr/share/widelands/i18n/translations/.*/\([^/]*\)_[^/]*\.po\)#%lang(\2) /\1#p' > %{_builddir}/%{?buildsubdir}/%{name}.files
find usr/share/widelands/i18n/translations/ -maxdepth 2 -type f -name \*.po -and ! -name "*_*.po" | sed -n -e 's#\(usr/share/widelands/i18n/translations/.*/\([^/]\+\)\.po\)#%lang(\2) /\1#p' >> %{_builddir}/%{?buildsubdir}/%{name}.files
find usr/share/widelands/ -mindepth 1 -maxdepth 1 -not -name i18n | sed -n 's#\(usr/share/widelands/*\)#/\1#p' >> %{_builddir}/%{?buildsubdir}/%{name}.files
popd
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
