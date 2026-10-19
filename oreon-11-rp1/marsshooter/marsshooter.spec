%global source0_hash c74a472bc905b2135a6524496d6e778f50ad1853fc49e2d1f394d14b6bf11b19
%global commit 84664cda094efe6e49d9b1550e4f4f98c33eefa2
%global commitdate 20211017
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global __cmake_in_source_build 1
Summary:        M.A.R.S. - A Ridiculous Shooter
Name:           marsshooter
Version:        0.7.6
Release:        1%{?dist}
License:        GPL-3.0-or-later
URL:            https://mars-game.sourceforge.net/
Source0:        https://github.com/thelaui/M.A.R.S./archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch1:         0001-Fix-BotController-toCover_-NULL-pointer-deref-crash.patch
Patch2:         0002-Replace-all-occurences-of-www.marsshooter.org-with-m.patch
Patch3:         0003-Add-a-NEWS.md-with-changes-since-0.7.5.patch
Patch4:         %{name}-waree-type.patch
%global fonts font(comfortaa) font(dejavusans) font(gargi) font(wenquanyimicrohei) font(waree)
Requires:       %{name}-data = %{version}-%{release}
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  SFML2-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  font(comfortaa)
BuildRequires:  font(dejavusans)
BuildRequires:  font(gargi)
BuildRequires:  font(waree)
BuildRequires:  font(wenquanyimicrohei)
BuildRequires:  fontconfig
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(taglib)
# /oreon:deps
%description
M.A.R.S. - a ridiculous shooter is a 2D space shooter with awesome visual
effects and attractive physics. Players can battle each other or computer
controlled enemies in exciting game modes:
    * awesome 2D-graphics with an unique style
    * a stunning amount of particles
    * single- and multi-player-support
    * an artificial intelligence using an aggro-system, which
      reacts differently upon varying situations
    * many impressive weapons
    * customizable ships
    * a very sexy GUI
    * several game modes: Space-ball, TeamDeathmatch, Cannonkeep,
      Deathmatch, Grave-Itation Pit

%package data
Summary:        Audio, icons and XML files for %{name}
License:        CC-BY-3.0 AND CC-BY-SA-3.0
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       %{fonts}
%description data
This package contains audio, icons and XML files for %{name}.

%prep

%autosetup -n M.A.R.S.-%{commit} -p1
rm -fr data_src ext_libs_for_windows

%build

export PKG_CONFIG_PATH=%{_libdir}/SFML2/pkgconfig
export CXXFLAGS="%{optflags} -I%{_includedir}/SFML2"
export LDFLAGS="%{?build_ldflags} -L%{_libdir}/SFML2"
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DSFML_DIR=%{_libdir}/cmake/SFML2 -DSFML_ROOT=%{_prefix} -Dmars_DATA_DEST_DIR=%{_datadir}/%{name} -Dmars_EXE_DEST_DIR=%{_bindir} .
%cmake_build
%install
%cmake_install
rm -r %{buildroot}%{_docdir}
ln -f -s $(fc-match -f "%{file}" "comfortaa") \
         %{buildroot}%{_datadir}/%{name}/fonts/Comfortaa-Regular.ttf
ln -f -s $(fc-match -f "%{file}" "dejavusans") \
         %{buildroot}%{_datadir}/%{name}/fonts/DejaVuSans.ttf
ln -f -s $(fc-match -f "%{file}" "gargi") \
         %{buildroot}%{_datadir}/%{name}/fonts/gargi.ttf
ln -f -s $(fc-match -f "%{file}" "waree") \
         %{buildroot}%{_datadir}/%{name}/fonts/Waree.ttf
mv %{buildroot}%{_datadir}/%{name}/fonts/Waree.ttf \
         %{buildroot}%{_datadir}/%{name}/fonts/Waree.otf
ln -f -s $(fc-match -f "%{file}" "wenquanyimicrohei") \
         %{buildroot}%{_datadir}/%{name}/fonts/wqy-microhei.ttc
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet \
  %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n marsshooter-data -f %{oreon_filedir}/marsshooter-data.list

%changelog

%autochangelog
