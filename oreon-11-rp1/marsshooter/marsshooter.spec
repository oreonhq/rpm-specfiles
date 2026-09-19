%global source0_hash none

%global commit 84664cda094efe6e49d9b1550e4f4f98c33eefa2
%global commitdate 20211017
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global __cmake_in_source_build 1

Summary:        M.A.R.S. - A Ridiculous Shooter
Name:           marsshooter
Version:        0.7.6
Release:        37%{?dist}
# Engine is GPLv3+, the libs under ext_libs_for_windows are LGPLv2+ / MPLv1.1
# but those are unused, so the resulting binary is pure GPLv3+
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://mars-game.sourceforge.net/
Source0:        https://github.com/thelaui/M.A.R.S./archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# Submitted upstream: https://github.com/thelaui/M.A.R.S./pull/41
Patch1:         0001-Fix-BotController-toCover_-NULL-pointer-deref-crash.patch
Patch2:         0002-Replace-all-occurences-of-www.marsshooter.org-with-m.patch
Patch3:         0003-Add-a-NEWS.md-with-changes-since-0.7.5.patch
# Fedora specific patch
Patch4:         %{name}-waree-type.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  SFML-devel
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(taglib)

# Automate finding font paths at build time
%global fonts font(comfortaa) font(dejavusans) font(gargi) font(wenquanyimicrohei) font(waree)
BuildRequires:  fontconfig %{fonts}

Requires:       %{name}-data = %{version}-%{release}
Requires:       hicolor-icon-theme

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
# TODO: Please submit an issue to upstream (rhbz#2380893)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -Dmars_DATA_DEST_DIR=%{_datadir}/%{name} -Dmars_EXE_DEST_DIR=%{_bindir} .
%cmake_build

%install
%cmake_install
# This includes license files, remove it and pick up with %%license in %%files
rm -r %{buildroot}%{_docdir}

# Replace bundled fonts with symlink to system fonts
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

%files
%doc README.md NEWS.md
%license license.txt
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man6/%{name}.6.gz

%files data
%license credits.txt music-license.eml
%{_datadir}/%{name}/

%changelog
%autochangelog
